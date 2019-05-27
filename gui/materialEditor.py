# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 00:55:36 2019

@author: AsteriskAmpersand
"""
# -*- coding: utf-8 -*-
"""
Created on Sat May 11 21:14:21 2019

@author: AsteriskAmpersand
"""
import sys
import os
import tempfile
from mrl3.MaterialMrl3 import MRL3
from gui.ui.FileTab import Ui_Form
from gui.HeaderView import HeaderWidget
from gui.ResourceView import ResourceWidget
from gui.PropertiesViewFactory import ParameterWidget
#from ParameterView import ParameterWidget
from gui.Popups import ReplaceDialog, RepointDialog
from common.FileLike import FileLike
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog

def RestoreData(restoreData, *args, **kwargs):
    tempFileName, path, Resolver = restoreData
    tab = EditorTab(tempFileName, Resolver)
    tab.path = path
    tab.restorePoint = restoreData
    return tab
    

class EditorTab(QtWidgets.QWidget):
    def __init__(self, materialPath = None, resolver = lambda x: hex(x)):
        super().__init__()
        self.path = materialPath if materialPath else ""
        self.material = MRL3(resolver)
        self.restorePoint = None
        if materialPath:
            with open(materialPath,"rb") as matFile:
                self.material.marshall(FileLike(matFile.read()))
        else:
            self.material.create()
        self.oldHash = self.material.generateHash()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
        self.setupMaterialList()
        
        self.createPages(self.ui.MaterialHeaderView, self.material.Materials,HeaderWidget)
        self.createPages(self.ui.ResourceBinding, self.material.Materials,ResourceWidget)
        self.createPages(self.ui.ParameterView, self.material.Materials,ParameterWidget)
        self.setupResourceList()
        
        self.ui.MaterialSelectorView.selectionModel().currentChanged.connect(self.pageSyncro)
        
        #self.show()
    def createPages(self, stackedView, materials, widgetClass):
        for widget in (widgetClass(material) for material in materials):
            stackedView.addWidget(widget)
    def pageSyncro(self, ix, ex):
        ix = ix.row()
        for view in [self.ui.MaterialHeaderView,self.ui.ResourceBinding,self.ui.ParameterView]:
            view.setCurrentIndex(ix)
            
    def setupMaterialList (self):
        self.ui.MaterialSelectorView.setModel(self.material.Materials)  
        self.ui.MaterialSelectorView.setMovement(QtWidgets.QListView.Snap)
        self.ui.MaterialSelectorView.setAcceptDrops(True)
        self.ui.MaterialSelectorView.setDragDropMode(QtWidgets.QListView.DragDrop)
        self.ui.MaterialSelectorView.setDragDropOverwriteMode(False)
        self.ui.MaterialSelectorView.setDropIndicatorShown(True)
        
        self.ui.MaterialSelectorView.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.ui.MaterialSelectorView.model().swapOcurred.connect(self.swapMaterial)
        delMat = QtWidgets.QAction("Delete Material", self)
        delMat.triggered.connect(lambda: self.delMaterial(self.ui.MaterialSelectorView.currentIndex()))
        self.ui.MaterialSelectorView.addAction(delMat)
        
        self.ui.MaterialSelectorView.model().dropOcurred.connect(self.newMaterials)
        
    def setupResourceList(self):
        self.ui.ResourceList.setModel(self.material.Textures)
        
        self.ui.ResourceList.setMovement(QtWidgets.QListView.Snap)
        self.ui.ResourceList.setDragDropMode(QtWidgets.QListView.InternalMove)
        self.ui.ResourceList.setDragDropOverwriteMode(False)
        self.ui.ResourceList.setDropIndicatorShown(True)
        self.ui.ResourceList.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked)
        self.ui.ResourceList.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        
        self.ui.ResourceList.model().dataChanged.connect(self.texRename)
        
        createTexture = QtWidgets.QAction("New",self.ui.ResourceList)
        createTexture.triggered.connect(self.newTex)
        self.ui.ResourceList.addAction(createTexture)
        
        delTexture = QtWidgets.QAction("Delete",self.ui.ResourceList)
        delTexture.triggered.connect(self.delTex)
        self.ui.ResourceList.addAction(delTexture)
        
        repointTexture = QtWidgets.QAction("Repoint", self.ui.ResourceList)
        repointTexture.triggered.connect(self.repointTex)
        self.ui.ResourceList.addAction(repointTexture)
        
        replaceTexture = QtWidgets.QAction("Global Replace", self.ui.ResourceList)
        replaceTexture.triggered.connect(self.globalReplaceTex)
        self.ui.ResourceList.addAction(replaceTexture)
        
        self.ui.ResourceList.model().swapOcurred.connect(self.swapTex)
    
    def resourceWidgets(self):
        return (self.ui.ResourceBinding.widget(ix) for ix in range(self.ui.ResourceBinding.count()))
    
    def newMaterials(self, materialIx, count):
        for widgetClass, listingView in zip([HeaderWidget, ResourceWidget,ParameterWidget],
                                            [self.ui.MaterialHeaderView,self.ui.ResourceBinding,self.ui.ParameterView]):
            for ix in range(count):
                widget = widgetClass(self.material.Materials[materialIx+ix])
                listingView.insertWidget(materialIx+ix, widget)
            
    def delMaterial(self, ix):
        self.material.Materials.removeRow(ix.row())
        for listingView in [self.ui.MaterialHeaderView,self.ui.ResourceBinding,self.ui.ParameterView]:
            widget = listingView.widget(ix.row())
            listingView.removeWidget(widget)

    def swapMaterial(self, ixFro, ixTo):
        #Materials have already been swapped, what's missing is swapping the widgets
        for listingView in [self.ui.MaterialHeaderView,self.ui.ResourceBinding,self.ui.ParameterView]:
            widget = listingView.widget(ixFro)
            listingView.removeWidget(widget)  
            listingView.insertWidget(ixTo if ixTo<ixFro else ixTo-1, widget)
    def texRename(self, *args):
        for resourceWidget in self.resourceWidgets():
           resourceWidget.resync()
    def newTex(self, *args):
        self.material.newTexture()
        for resourceWidget in self.resourceWidgets():
           resourceWidget.resync()
    def delTex(self, *args):
        self.material.delTexture(self.ui.ResourceList.selectedIndexes()[0].row())
        for resourceWidget in self.resourceWidgets():
           resourceWidget.resync()
    def swapTex(self, ixFro, ixTo):
        self.material.swapTex(ixFro, ixTo)
        for resourceWidget in self.resourceWidgets():
           resourceWidget.resync()
    def globalReplaceTex(self, *args):
        dialog = ReplaceDialog([str(tex) for tex in self.material.Textures])
        if dialog.exec():
            self.material.Textures.globalReplace(dialog.Find.text(),dialog.Replace.text(),dialog.Regexp.isChecked())
            for resourceWidget in self.resourceWidgets():
               resourceWidget.resync()
    def repointTex(self):
        texture=self.ui.ResourceList.currentIndex().row()
        dialog = RepointDialog(self.material.Textures,texture)
        if dialog.exec():
            self.material.repointTexture(dialog.From.currentIndex()+1,dialog.To.currentIndex()+1)
            for resourceWidget in self.resourceWidgets():
               resourceWidget.resync()
               
    def Save(self):
        if self.path:
            return self.save(self.path)
        else:
            path = QFileDialog.getSaveFileName()[0]
            if not path:
                return False
            return self.save(path)
               
    def save(self, path):
        try:
            self.material.updateCountsAndOffsets()
            fileContent = self.material.serialize()
            with open(path,"wb") as outf:
                outf.write(fileContent)
            self.path = path
            self.oldHash = self.material.generateHash()
            return True
        except Exception as e:
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('Failed to save material file. %s'%e)
            error_dialog.exec()
            return False
    
    def unsavedChanges(self):
        return self.oldHash != self.material.generateHash()
        
    def promptSave(self):
        try:
            if self.restorePoint:
                os.remove(self.tempFileName)
        except: print("Exception should not be possible")#pass
        savePath = self.path if self.path is not None else "New File"
        if self.unsavedChanges():
            choice = QtWidgets.QMessageBox.question(self, 'Unsaved Changes on %s'%savePath,
                                    "Save Changes to %s?"%savePath,
                                    QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No | QtWidgets.QMessageBox.Cancel)
            if choice == QtWidgets.QMessageBox.Cancel:
                return False
            if choice == QtWidgets.QMessageBox.Yes:
                return self.Save()
            if choice == QtWidgets.QMessageBox.No:
                return True
        else:
            return True
        
    def createRestorePoint(self):
        _,tempfileName = tempfile.mkstemp()
        with open(tempfileName,"wb") as tempFile:
            tempFile.write(self.material.serialize())
            tempFile.seek(0)
            tempFile.close()
            self.restorePoint = (tempfileName, self.path, self.material.Resolver)
        
    def loadRestorePoint(self):
        if self.restorePoint == None:
            raise ValueError("No restore point.")
        return self.restorePoint
    
if "__main__" in __name__:
    app = QtWidgets.QApplication(sys.argv)
    window = EditorTab(r"E:\MHW\Merged\Master_MtList.mrl3")
    sys.exit(app.exec_())