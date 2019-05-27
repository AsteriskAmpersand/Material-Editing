# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 21:28:28 2019

@author: AsteriskAmpersand
"""
        
import sys
from PyQt5 import QtWidgets, QtGui, QtCore
import materialLibrary as MatLib
import materialCompendium as MatComp
import materialEditor as MatEdit
import configuration as Config

class Window(QtWidgets.QMainWindow):
    menuTools = [
                 ("New","Ctrl+N","Create an empty Mrl3","self.Mrl3Editor.New","Mrl3"),
                 ("Open","Ctrl+O","Open an Mrl3","self.Mrl3Editor.Open","Mrl3"),
                 ("Save","Ctrl+S","Save current Mrl3","self.Mrl3Editor.Save","Mrl3"),
                 ("SaveAs","Ctrl+Shift+S","Save current Mrl3 as","self.Mrl3Editor.SaveAs","Mrl3"),
                 ("Save All","Ctrl+Alt+S","Save all opened Mrl3","self.Mrl3Editor.SaveAll","Mrl3"),
                 ("Add Resource Path","Ctrl+R","Save all opened Mrl3","self.Mrl3Editor.CreateResource","Mrl3"),
                 
                 ("New","Ctrl+Shift+M","Create an empty Mrl3","self.Mrl3Editor.New","Mrl3"),
                 ("Open Library","Ctrl+U","Open a Material Library","self.Library.Open","Library"),
                 ("Save Library","Ctrl+D","Save the Material Library","self.Library.Save","Library"),
                 ("Save Library As","Ctrl+Shift+D","Save the Material Library as","self.Library.SaveAs","Library"),
                 ("Add Material","Ctrl+Shift+A","Add a material or a complete file to the Material Library","self.Library.AddMaterial","Library"),  
                 
                 ("Generate Compendium","Ctrl+K","Generates the Compendium","self.Compendium.Generate","Compendium"),
                 ("Expand Compendium","Ctrl+E","Expands the Compendium","self.Compendium.Expand","Compendium"),
                 ("Save Compendium","Ctrl+G","Saves changes to the Compendium","self.Compendium.Save","Compendium"),
                 
                 ("Copy","Ctrl+C","Copy the active selection","self.Copy","Edit"),
                 ("Paste","Ctrl+V","Paste from the clipboard to the active selection","self.Paste","Edit"),
                 ("Delete","Del","Delete Active Selection","self.Delete","Edit"),                 
                ]
    
    def __init__(self):
        super().__init__()
        self.setGeometry(50,50,500,300)
        self.setWindowTitle("CrAs-T Mrl3 Editor")
        self.setWindowIcon(QtGui.QIcon(r"G:\Tools\MaterialEditor\Material-Editing\gui\resources\DodoSama.png"))
        self.statusBar()  
        self.home() 
        self.selected = None
        self.show()
        
    def home(self):
        self.Settings = Config.Configuration()
        self.Library = MatLib.MaterialLibrary(self.Settings)
        self.Compendium = MatComp.MaterialCompendium(self.Settings)
        self.Mrl3Editor = MatEdit.MaterialEditor(self.Settings)
        mainMenu = self.menuBar()
        menuList = {}
        for action,shortcut,statusTip,trigger,subMenu in self.menuTools:
            qtAction = QtWidgets.QAction(action, self)
            if shortcut: qtAction.setShortcut(shortcut)
            qtAction.setStatusTip(statusTip)
            qtAction.triggered.connect(eval(trigger))
            if subMenu not in menuList:
                newMenu = mainMenu.addMenu(subMenu)
                menuList[subMenu] = newMenu
            menuList[subMenu].addAction(qtAction)
        
    def Copy(self):
        pass
    def Paste(self):
        pass
    def Delete(self):
        pass
    def close_event(self, event):
        self.Settings.save(self.Library.path, self.Mrl3Editor.path)
        for container in [self.Library, self.Compendium, self.Mrl3Editor]:
            if not container.unsavedChanges():
                response = container.promptSave()
                if not response:
                    event.ignore()
                    return
        sys.exit()
        
def run():
    app = QtWidgets.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

run()