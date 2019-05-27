# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 17:57:13 2019

@author: AsteriskAmpersand
"""
import sys
from PyQt5 import QtWidgets, QtGui, QtCore

def run():
    app = QtWidgets.QApplication(sys.argv)
    model = QtCore.QStringListModel(["path1","path2","path3"])
    view = QtWidgets.QListView()
    view.setModel(model)
    view.show()
    sys.exit(app.exec_())
    
run()