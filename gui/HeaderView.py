# -*- coding: utf-8 -*-
"""
Created on Sun May 12 03:52:57 2019

@author: AsteriskAmpersand
"""
import sys
from gui.ui.MaterialHeader import Ui_Form

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, pyqtSignal

class HeaderWidget(QtWidgets.QWidget):
    materialAdded = pyqtSignal(object)
    hashChanged = pyqtSignal(int)
    def __init__(self, material, **kwargs):
        self.header = material.Header
        super().__init__(**kwargs)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.linkWidgets(self.header, self.ui)        
        #self.show()
        
    def linkWidgets(self,header,ui):
        ui.MaterialLinkName.setText(header.resolver(header.materialNameHash))
        ui.MaterialLinkName.textChanged.connect(self.matNameHashChange)
        ui.MaterialHash.setText(hex(header.materialNameHash))
        
        ui.ShaderHash.setText(hex(header.shaderHash)[2:])
        ui.ShaderHash.textChanged.connect(lambda x: self.header.__setattr__("shaderHash", int(x,base=16)))        
        
        ui.SkinId.setText(hex(header.skinid)[2:])
        ui.SkinId.textChanged.connect(lambda x: self.header.__setattr__("skinid", int(x,base=16))) 
        
        self.blindLink(ui.SurfaceDirection, header, "unkn4")
        self.blindLink(ui.UnknownOffset, header, "unkn6")
        self.blindLink(ui.StrayUnknown, header, "unkn8")        
        for i in range(24):
            ui.__getattribute__("unk%d"%i).setValue(header.getUnkn(i))
            ui.__getattribute__("unk%d"%i).valueChanged.connect(header.metaSetUnkn(i))
    
    def matNameHashChange(self, newValue):
        self.header.setNameHash(newValue)
        self.ui.MaterialHash.setText(hex(self.header.materialNameHash))    

    def blindLink(self, uiObj, baseObj, prop):
        uiObj.setValue(baseObj.__getattribute__(prop))
        uiObj.valueChanged.connect(lambda x: baseObj.__setattr__(prop, x))
        
        
if "__main__" in __name__:
    from common.FileLike import FileLike
    from mrl3.MaterialMrl3 import MRL3
    app = QtWidgets.QApplication(sys.argv)
    material = MRL3()
    with open(r"E:\MHW\Merged\Master_MtList.mrl3","rb") as matFile:
            material.marshall(FileLike(matFile.read()))
    window = HeaderWidget(material.Materials[0])
    sys.exit(app.exec_())