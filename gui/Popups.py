# -*- coding: utf-8 -*-
"""
Created on Tue May 14 18:55:19 2019

@author: AsteriskAmpersand
"""
from PyQt5 import QtCore, QtGui, QtWidgets
from gui.ui.PopUpGlobalReplace import Ui_Dialog as ui_replace
from gui.ui.PopUpRepoint import Ui_Dialog as ui_repoint
import re

class ReplaceDialog(QtWidgets.QDialog, ui_replace):
    def __init__(self, stringList=[], parent=None):
        super().__init__(parent)
        self.previewTargets = stringList
        self.setupUi(self)
        preview = self.buttonBox.addButton("Preview", QtWidgets.QDialogButtonBox.ActionRole)
        preview.clicked.connect(self.preview)
        
    def preview(self):
        find = self.Find.text()
        replace = self.Replace.text()
        regexp = self.Regexp.isChecked()
        operation = re.sub if regexp else lambda f, r, x: x.replace(f,r)
        candidates = []
        for string in self.previewTargets:
            prev = string
            try:
                new = operation(find,replace,string)
            except Exception as e:
                candidates=["Error in regular expression. %s"%e]
                break
            if new != prev:
                candidates.append((prev+" > "+new))
        if candidates:
            message = "\n".join(candidates)
        else:
            message = "No matches found."
        messageBox = QtWidgets.QMessageBox()
        messageBox.setWindowTitle("Preview Matches")
        messageBox.setText(message)
        messageBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        messageBox.setContentsMargins(9,9,9,9)
        messageBox.adjustSize()
        messageBox.exec()
        
class RepointDialog(QtWidgets.QDialog, ui_repoint):
    def __init__(self, choices=[], default=0, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        self.From.addItems(map(str,choices))
        self.To.addItems(map(str,choices))
        self.From.setCurrentIndex(default)

if __name__ == '__main__':
    import sys            
    app = QtWidgets.QApplication(sys.argv)
    w = RepointDialog([1,2,3])
    if w.exec():
        print(w.From.currentIndex())
        print(w.To.currentIndex())
    sys.exit(app.exec_())
    