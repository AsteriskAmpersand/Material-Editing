# -*- coding: utf-8 -*-
"""
Created on Thu May 16 19:03:20 2019

@author: AsteriskAmpersand
"""
import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from gui.ui.MaterialResources import Ui_Form

class ResourceWidget(QtWidgets.QWidget):
    def __init__(self, material, **kwargs):
        self.material = material
        super().__init__(**kwargs)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.linkWidgets(self.material.resourceBindings, self.ui)       
        self.currentlySelected = -1
        #self.show()
        
    def linkWidgets(self, resources, ui):
        self.ui.ResourceListView.setModel(resources)
        self.ui.ResourceListView.selectionModel().currentChanged.connect(self.resourceChanged)
        
    def blindLink(self, uiObj, baseObj, prop):
        uiObj.setValue(baseObj.__getattribute__(prop))
        uiObj.valueChanged.connect(lambda x: baseObj.__setattr__(prop, x))        
        
    def resourceChanged(self, ix):
        selection = ix
        selectedIx = selection.row()
        self.ui.ResourceType.setText("Resource Type: "+self.material.resourceBindings[selectedIx].getRole(QtCore.Qt.DisplayRole))
        for ix in range(3):
            try:self.ui.__getattribute__("resourceUnk%d"%ix).valueChanged.disconnect()
            except:pass
            self.ui.__getattribute__("resourceUnk%d"%ix).setValue(self.material.resourceBindings[selectedIx].unknArr[ix])
            self.ui.__getattribute__("resourceUnk%d"%ix).valueChanged.connect(lambda x: self.material.resourceBindings[selectedIx].unknArr.__setitem__(ix, x))      
        self.ui.ResourceIx.setValue(self.material.resourceBindings[selectedIx].texIdx)
        self.syncIx(selectedIx)
        try:self.ui.ResourceIx.valueChanged.disconnect()
        except:pass
        self.ui.ResourceIx.valueChanged.connect(self.idxChange())
        try:self.ui.resourceUnk3.valueChanged.disconnect()
        except:pass
        self.blindLink(self.ui.resourceUnk3, self.material.resourceBindings[selectedIx],"unkn")
        
    def currentSelection(self):
        return self.ui.ResourceListView.currentIndex().row()
    
    def idxChange(self):
        def __idxChange__(ix):
            currentIx = self.currentSelection()
            self.material.resourceBindings[currentIx].texIdx = ix
            self.syncIx(currentIx)
        return __idxChange__
    
    def resync(self):
        currentIx = self.currentSelection()
        if currentIx == -1:
            return
        self.ui.ResourceIx.setValue(self.material.resourceBindings[currentIx].texIdx)
        self.syncIx(currentIx)
    
    def sync(self):
        currentIx = self.currentSelection()
        self.syncIx(currentIx)

    def syncIx(self,currentIx):
        currentTexIx = self.material.resourceBindings[currentIx].texIdx
        resourcePaths = self.material.ResourceData
        materialPath = str(resourcePaths[currentTexIx-1]).replace("\x00","") if 0<currentTexIx<=len(resourcePaths) else ""
        self.ui.ResourceLabel.setText(materialPath)
        
if "__main__" in __name__:
    from common.FileLike import FileLike
    from mrl3.MaterialMrl3 import MRL3
    app = QtWidgets.QApplication(sys.argv)
    material = MRL3()
    with open(r"E:\MHW\Merged\Master_MtList.mrl3","rb") as matFile:
            material.marshall(FileLike(matFile.read()))
    window = ResourceWidget(material.Materials[0])
    sys.exit(app.exec_())