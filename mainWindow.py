# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 23:00:05 2019

@author: AsteriskAmpersand
"""

import sys
import os
from PyQt5 import uic, QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QFileDialog
import gui.materialLibrary as ml
import gui.materialCompendium as mc
import gui.materialEditor as me
import gui.configuration as config
from gui.ui.MainWindow import Ui_MainWindow
from PyQt5.QtCore import QFile, QTextStream

def functionChain(functionList):
    for function in functionList:
        function()

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, arguments):
        super().__init__()
        self.setAcceptDrops(True)
        
        self.Config = config.Configuration()
        self.Compendium = mc.MaterialCompendium(self.Config)
        self.Library = ml.MaterialLibrary(self.Config, self.Compendium.resolveHashToName)
        
        if getattr(sys, 'frozen', False):
            application_path = sys._MEIPASS
        elif __file__:
            application_path = os.path.dirname(__file__)
        self.setWindowIcon(QtGui.QIcon(application_path+r"\gui\resources\DodoSama.png"))
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("CrAs-T Mrl3 Editor")
        
        self.ui.LibraryView.setModel(self.Library.model())
        self.ui.LibraryView.setHeaderHidden(True)
        self.ui.LibraryView.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.ui.LibraryView.setDragEnabled(True)
        self.ui.LibraryView.setAcceptDrops(True)
        self.ui.LibraryView.setDragDropOverwriteMode(False)
        self.ui.LibraryView.setDropIndicatorShown(True)
        
        self.ui.CompendiumView.setDragEnabled(True)
        self.compendiumLoad()
        self.Compendium.sender.compendiumRebased.connect(self.compendiumLoad)
        
        self.ui.Mrl3EditorView.setTabsClosable(True)
        self.ui.Mrl3EditorView.tabCloseRequested.connect(self.closeTab)
        self.ui.Mrl3EditorView.setMovable(True)
        
        self.connectToolbar()
        self.connectButtons()
        
        self.ui.splitter.setSizes([10,90])
        self.loadRecentFiles(self.Config.filepaths+arguments)
        self.show()
        
    def loadRecentFiles(self, fileList):
        for file in fileList:
            try:
                tab = me.EditorTab(file, resolver = self.Compendium.resolveHashToName)
                self.ui.Mrl3EditorView.addTab(tab,file.split("\\")[-1].replace(".mrl3",""))
            except Exception as e:
                error_dialog = QtWidgets.QErrorMessage()
                error_dialog.showMessage('Failed to Load Previously Open File %s. Error: %s'%(file, str(e)))
                error_dialog.exec()
    
    def connectButtons(self):
        self.ui.libraryAdd.clicked.connect(self.Library.AddMaterial)
        self.ui.libraryRemove.clicked.connect(lambda : self.Library.RemoveMaterial(self.ui.LibraryView.selectedIndexes()))

    def connectToolbar(self):
        self.ui.actionNew.triggered.connect(self.newTab)
        self.ui.actionOpen.triggered.connect(self.openTab)
        self.ui.actionSave.triggered.connect(self.saveTab)
        self.ui.actionSave_As.triggered.connect(self.saveAsTab)
        self.ui.actionSave_All.triggered.connect(self.saveAllTab)
        self.ui.actionCreate_Restore_Point.triggered.connect(self.createRestorePoint)
        self.ui.actionLoad_Restore_Point.triggered.connect(self.loadRestorePoint)
        
        self.ui.actionNew_Library.triggered.connect(self.Library.New)
        self.ui.actionOpen_Library.triggered.connect(self.Library.Open)
        self.ui.actionSave_Library.triggered.connect(self.Library.Save)
        self.ui.actionSave_Library_As.triggered.connect(self.Library.SaveAs)
        
        self.ui.actionExpand_Compendium.triggered.connect(lambda: functionChain([self.Compendium.Expand, self.compendiumSort]))
        self.ui.actionRebase_Compendium.triggered.connect(lambda: functionChain([self.Compendium.Rebase, self.compendiumSort]))
        self.ui.actionSave_Compendium.triggered.connect(self.Compendium.Save)

    def compendiumLoad(self):
        self.ui.CompendiumView.setModel(self.Compendium.model(self.ui.CompendiumView))
        self.compendiumSort()

    def compendiumSort(self):
        self.ui.CompendiumView.setHeaderHidden(True)
        self.ui.CompendiumView.setSortingEnabled(True)
        self.ui.CompendiumView.sortByColumn(0, QtCore.Qt.AscendingOrder)
        
    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls:
            event.accept()
        else:
            event.ignore()
    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls:
            event.setDropAction(QtCore.Qt.CopyAction)
            event.accept()
        else:
            event.ignore()
    def dropEvent(self, event):
        if event.mimeData().hasUrls:
            event.setDropAction(QtCore.Qt.CopyAction)
            event.accept()
            for url in event.mimeData().urls():
                self._openTab(str(url.toLocalFile()))
        else:
            event.ignore()

        
    def newTab(self):
        tab = me.EditorTab(resolver = self.Compendium.resolveHashToName)
        self.ui.Mrl3EditorView.addTab(tab,"New Mrl3")
    def openTab(self):
        path = QFileDialog.getOpenFileName(None,"Open Mrl3 File",filter = "MHW Mrl3 Material File (*.mrl3)")[0]
        self._openTab(path)
    def _openTab(self, path):
        if not path:
            return False
        tab = me.EditorTab(path, resolver = self.Compendium.resolveHashToName)
        self.ui.Mrl3EditorView.addTab(tab,path.split("\\")[-1].replace(".mrl3",""))
        return True
    def closeTab(self, ix):
        if self.ui.Mrl3EditorView.widget(ix).promptSave():
            self.ui.Mrl3EditorView.removeTab(ix)
    def saveTab(self):
        current = self.ui.Mrl3EditorView.currentWidget()
        currentIx = self.ui.Mrl3EditorView.currentIndex()
        current.Save()    
        self.ui.Mrl3EditorView.setTabText(currentIx,current.path.split("\\")[-1].replace(".mrl3",""))          
    def saveAsTab(self):
        current = self.ui.Mrl3EditorView.currentWidget()
        startingDir = current.path if current.path else ""
        path = QFileDialog.getSaveFileName(directory = startingDir, filter = "MHW Material File (*.mrl3)")[0]
        if not path:
            return False
        currentIx = self.ui.Mrl3EditorView.currentIndex()
        current.save(path)
        self.ui.Mrl3EditorView.setTabText(currentIx,current.path.split("\\")[-1].replace(".mrl3",""))   
    def saveAllTab(self):
        for ix,tab in enumerate([self.ui.Mrl3EditorView.widget(i) for i in range(self.ui.Mrl3EditorView.count())]):
            tab.Save()
            self.ui.Mrl3EditorView.setTabText(ix,tab.path.split("\\")[-1].replace(".mrl3",""))
    def createRestorePoint(self):
        self.ui.Mrl3EditorView.currentWidget().createRestorePoint()
    def loadRestorePoint(self):
        currentIx = self.ui.Mrl3EditorView.currentIndex()
        try:
            restoreData = self.ui.Mrl3EditorView.widget(currentIx).loadRestorePoint()
            self.ui.Mrl3EditorView.removeTab(currentIx)
            tab = me.RestoreData(restoreData)
            self.ui.Mrl3EditorView.insertTab(currentIx,tab,tab.path.split("\\")[-1].replace(".mrl3",""))
        except Exception as e:
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('Failed to Load Restore Point. %s'%e)
            error_dialog.exec()
        
    def closeEvent(self, *events):
        for tab in [self.ui.Mrl3EditorView.widget(i) for i in range(self.ui.Mrl3EditorView.count())]+[
                self.Library,self.Compendium]:
            if not tab.promptSave():
                for e in events:
                    e.ignore()
                return
        filePaths = [self.ui.Mrl3EditorView.widget(i).path for i in range(self.ui.Mrl3EditorView.count())]
        self.Config.save(self.Library.path, filePaths)

if __name__ == '__main__':
    from pathlib import Path
    app = QtWidgets.QApplication(sys.argv)
    args = app.arguments()[1:]
    window = MainWindow(args)
    sys.exit(app.exec_())