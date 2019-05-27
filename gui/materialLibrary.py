# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 00:58:57 2019

@author: AsteriskAmpersand
"""
#soft library vs hard library when opening and saving
from gui.mrl3Models.Mrl3MaterialLibrary import Mrl3MaterialLibrary
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QFileDialog
from collections import OrderedDict

class MaterialLibrary():
    def __init__(self, config, resolver):
        self.path = config.libpath
        self.resolver = resolver
        self.Mrl3Library = Mrl3MaterialLibrary(self.resolver, self.path)
        self.Mrl3Library.changesMade.connect(lambda: self.__setattr__("changes",True))
        self.changes = False
        
    def New(self):
        self.path = None
        self.Mrl3Library.reset()
        self.changes = True
        
    def model(self):
        return self.Mrl3Library
    
    def Open(self):
        try:
            path,_ = QFileDialog.getOpenFileName(None,"Open Library File",filter = "MHW Mrl3 Library File (*.czt)")
            if path:
                self.Mrl3Library.reset()
                self.Mrl3Library.loadJson(path)
                #self.Mrl3Library = Mrl3MaterialLibrary(self.resolver, self.path)
                self.path = path
                self.changes = True
        except Exception as e:
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('Failed to open library file. %s'%e)
            error_dialog.exec()

    def unsavedChanges(self):
        return self.changes

    def promptSave(self):
        if self.unsavedChanges():
            choice = QtWidgets.QMessageBox.question(None, 'Unsaved Changes on the Library',
                                    "Save Changes to the Library?",
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
        return self.SaveAs(self.path)
    
    def SaveAs(self, path = None):
        if not path:
            path = QFileDialog.getSaveFileName(filter = "Library file (*.lib)")[0]
            if not path:
                return False
        self.path = path
        try:
            self.Mrl3Library.save(path)
            self.changes = False
            return True
        except Exception as e:
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('Failed to Save Library to File. %s'%str(e))
            return self.promptSave()
    
    def AddMaterial(self):
        path = QFileDialog.getOpenFileName()[0]
        try:
            self.Mrl3Library.add(path)
            self.changes = True
        except Exception as e:
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('Failed to Load Material File. %s'%e)
            error_dialog.exec()
            
    def RemoveMaterial(self, selection):
        if not selection:
            return
        else:
            for index in selection:
                self.Mrl3Library.remove(index)
            self.changes = True