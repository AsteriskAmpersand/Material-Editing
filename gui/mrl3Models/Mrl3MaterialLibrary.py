# -*- coding: utf-8 -*-
"""
Created on Sat May  4 13:43:35 2019

@author: AsteriskAmpersand
"""
import os
import sys
import pickle
import json
import time
from collections import OrderedDict
from pathlib import Path

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSignal

from gui.materialMime import packMatHash, packAllMatHash, unpackMatHashes, safeCastHash
from mrl3.MaterialMrl3 import MRL3
from common.crc import CrcJamcrc
from common.FileLike import FileLike

generalhash =  lambda x:  CrcJamcrc.calc(x.encode())
       

class Mrl3MaterialLibrary(QtGui.QStandardItemModel):
    changesMade = pyqtSignal()
    def __init__(self, resolver=lambda x: "0x"+str(x), path=None, parent=None):
        super().__init__(parent)
        self.resolver = resolver
        try: self.loadJson(path)
        except Exception as e: pass
            
    def loadJson(self, lib):
        with open(lib,"r") as libFile:
            lib = json.load(libFile, object_pairs_hook=OrderedDict)
            if lib:
                lib = OrderedDict([(key,val) for key, val in lib.items()])
        self.expand(lib)
        return

    def save(self, path):
        with open(path, "w") as libFile:
                libFile.write(json.dumps(self.serializeDict()))
        return True
        
    def add(self, path):
        path = Path(path)
        with open(path,"rb") as matf:
            mat = MRL3()
            mat.marshall(FileLike(matf.read()))
            hashes = mat.getMaterialHashes()
        self.expand(OrderedDict([(path.resolve().as_posix(), hashes)]))
        
    def reset(self):
        for row in range(self.rowCount(QtCore.QModelIndex())):
            self.remove(self.index(row,0,QtCore.QModelIndex()))
        
    def remove(self, index):
        if not index.parent().isValid():
            self.removeRows(index.row(), 1, index.parent())
        self.changesMade.emit()
    
    def expand(self, resDict):
        for path, materials in resDict.items():
            item = QtGui.QStandardItem(path)
            item.setFlags(item.flags() & (~Qt.ItemIsEditable) | (Qt.ItemIsDragEnabled) | (Qt.ItemIsDropEnabled))
            self.appendRow(item)
            for material in materials:
                subitem = QtGui.QStandardItem(self.resolver(material))
                subitem.setFlags(subitem.flags() & (~Qt.ItemIsEditable) | (Qt.ItemIsDragEnabled) & (~Qt.ItemIsDropEnabled))
                item.appendRow(subitem)
        self.changesMade.emit()
        #self.dataChanged.emit(self.index(0,0,QtCore.QModelIndex()),self.index(0,0,QtCore.QModelIndex()))
    
    def serializeDict(self):
        keyCount = self.rowCount(QtCore.QModelIndex())
        result = {}
        for keyIx in range(keyCount):
            mix = self.index(keyIx,0,QtCore.QModelIndex())
            key = self.data(mix)
            values = [safeCastHash(self.data(self.index(valueIx,0,mix))) for valueIx in range(self.rowCount(mix))]
            result[key] = values
        return result

    def flags(self, index):
        if not index.isValid():
            return Qt.ItemIsSelectable | Qt.ItemIsDropEnabled | Qt.ItemIsDragEnabled | Qt.ItemIsEnabled
        else:
            return Qt.ItemIsSelectable | Qt.ItemIsDragEnabled | Qt.ItemIsEnabled
        
    @staticmethod
    def mimeTypes():
        return ["custom/mrl3Path"]
    
    def mimeData(self, indexes):
        if len(indexes)>1:
            raise ValueError
        index = indexes[0]
        return (packMatHash if index.parent().isValid() else packAllMatHash)(self, index)      
        
    def supportedDragActions(self):
        return QtCore.Qt.CopyAction | QtCore.Qt.MoveAction | QtCore.Qt.TargetMoveAction

    def dropMimeData(self, qMimeData, action, row, column, parent):
        if (action == Qt.IgnoreAction):
            return True
        if qMimeData.hasFormat("custom/mrl3Path"):
            path, hashes = unpackMatHashes(qMimeData.data("custom/mrl3Path"))
            self.add(path)
            return True   
        return False            
        
if __name__ == '__main__':
    from Mrl3Compendium import Mrl3Compendium
    import sys
    app = QtWidgets.QApplication(sys.argv)
    m = Mrl3Compendium()
    resolver = m.resolveHashToName
    model = Mrl3MaterialLibrary(resolver)
    model.add(r"E:\MHW\Merged\Master_MtList.mrl3")

    view = QtWidgets.QTreeView()
    view.setHeaderHidden(True)
    #view.setSortingEnabled(True)
    #view.sortByColumn(0, QtCore.Qt.AscendingOrder)
    view.setModel(model)
    view.setWindowTitle("Simple Tree Model")
    view.show()
    model.add(r"E:\MHW\Merged\template.mrl3")
    sys.exit(app.exec_())