# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 00:52:38 2019

@author: AsteriskAmpersand
"""
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QFileDialog 
from PyQt5.QtCore import pyqtSignal

import sys
from gui.mrl3Models.Mrl3Compendium import Mrl3Compendium
from pathlib import Path

class SenderObject(QtCore.QObject):
    compendiumRebased = pyqtSignal()

class MaterialCompendium():
    sender = SenderObject()
    def __init__(self, config):
        self.path = config.ibcompendiumpath
        self.Mrl3Compendium = Mrl3Compendium(self.path)
        self.views = []
        self.changes = False
        
    def model(self, view):
        self.views.append(view)
        return self.Mrl3Compendium.model()

    def resolveHashToName(self, matHash):
        return self.Mrl3Compendium.resolveHashToName(matHash)    
        
    def Rebase(self):
        operation = self.Modify(self.Mrl3Compendium.rebase,'Rebase operation failed.')
        if operation:
            self.sender.compendiumRebased.emit()
            return True
        else:
            return False
        
    def UpdateViews(self):
        self.changes = True
        for view in self.views:
            view.setModel(self.Mrl3Compendium.model())
        
    def Expand(self):
        operation = self.Modify(self.Mrl3Compendium.expand,'Expansion operation failed.')
        if operation:
            return True
        else:
            return False
        
    def Modify(self, operator, errMessage):
        folder = QFileDialog.getExistingDirectory(None, ("Select Root of Chunk"), QtCore.QDir.currentPath());
        if not folder:
            return False
        try:
            files = list(Path(folder).rglob("*.mrl3"))#getMaterialHashes
            operator(files)
        except Exception as e:
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage(errMessage)
            error_dialog.exec()
            return False
        self.changes = True
        return True
    
    def unsavedChanges(self):
        return self.changes
    
    def promptSave(self):
        if self.unsavedChanges():
            choice = QtWidgets.QMessageBox.question(None, 'Unsaved Changes on the Compendium',
                                    "Save Changes to the Compendium?",
                                    QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No | QtWidgets.QMessageBox.Cancel)
            if choice == QtWidgets.QMessageBox.Cancel:
                return False
            if choice == QtWidgets.QMessageBox.Yes:
                return self.Save()
            if choice == QtWidgets.QMessageBox.No:
                return True
        else:
            return True
        
    def Save(self):
        try:
            self.Mrl3Compendium.save(self.path)
            self.changes = False
            return True
        except Exception as e:
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('Failed to Save Compendium back to File. %s'%str(e))
            error_dialog.exec()
            return self.promptSave()
        