# -*- coding: utf-8 -*-
"""
Created on Sat May 11 23:46:30 2019

@author: AsteriskAmpersand
"""

from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal
from common.FileLike import FileLike

class DefaultType():
    pass

class QList (QtCore.QAbstractListModel):
    default_type = DefaultType
    swapOcurred = pyqtSignal(int,int)
    dropOcurred = pyqtSignal(int,int)
    def __init__(self, pythonlist = [], parent = None):
        self.list = pythonlist
        self.pendingRemoveRowsAfterDrop = False
        self.parent = parent
        super().__init__()
        
    def rowCount(self, parent = QtCore.QModelIndex()):
        if parent.isValid():
            return 0
        return len(self.list)
    
    def data(self, ix, role):
        try:
            return self.list[ix.row()].getRole(role)
            #if role == QtCore.Qt.DisplayRole:
            #    return str(self.list[ix.row()])
        except:
            pass
        return None
        
    #def headerData(self, orientation, role = QtCore.Qt.DisplayRole()):
    #    return QtCore.QVariant()

    def supportedDropActions(self):
        return QtCore.Qt.MoveAction
    
    def setData(self, index, value, role):
        if not index.isValid():
            return False
        if index.row()<0 or index.row() >= len(self.list):
            return False
        self.list[index.row()] = value
        self.dataChanged.emit(index, index)
        return True
    
    def insertRows(self, row, count, parent=QtCore.QModelIndex()):
        if parent.isValid() or count <= 0: return False
        startingRow = max(0,row)
        endRow = min(row+count-1, len(self.list))
        self.beginInsertRows(parent, startingRow, endRow)
        defaultClass = self.list[0].__class__ if self.default_type is DefaultType and len(self.list)>0 else self.default_type
        self.list[startingRow:startingRow] = [defaultClass() for i in range(count)]
        self.endInsertRows()
        return True
    
    def removeRows(self, row, count, index=QtCore.QModelIndex()):
        if self.pendingRemoveRowsAfterDrop:
            self.pendingRemoveRowsAfterDrop = False
            lipos = self.lastInsert
            lilen = self.lastInsertLength
            if row > lipos:
                row = row+lilen
            self.removeRows(row,count,index)
            return True
        if index.isValid() or count <= 0:
            return False
        self.beginRemoveRows(QtCore.QModelIndex(), row, row + count - 1)
        self.list[row : row+count] = []
        self.endRemoveRows()
        return True
    
    def mimeTypes(self):
        return ["custom/MaterialResource"]
    
    def mimeData(self, indices):
        mime = QtCore.QMimeData()
        bytestr = b''
        for index in indices:
            data = self.list[index.row()].serialize()
            bytestr+=data
            self.lastSource = index.row()
        if not bytestr:
            return 0
        mime.setData("custom/MaterialResource", bytestr)
        return mime
    
    def dropMimeData(self, data, action, row, column, parent):
        if action == QtCore.Qt.IgnoreAction:
            return True
        if column > 0:
            return False
        num_rows = self.rowCount(QtCore.QModelIndex())
        if num_rows <= 0:
            return False

        if row < 0:
            if parent.isValid():
                row = parent.row()
            else:
                return False
        encoded_data = FileLike(data.data("custom/MaterialResource"))
        new_items = []
        while (encoded_data):
            cObj = self.default_type()
            cObj = self.list[0].__class__() if type(cObj) is DefaultType else cObj
            cObj.marshall(encoded_data)
            new_items.append(cObj)
        self.list[row:row]=new_items
        self.lastInsert = row
        self.lastInsertLength = len(new_items)
        self.pendingRemoveRowsAfterDrop = True
        self.swapOcurred.emit(self.lastSource,row)
        return True
        
    def __len__(self):
        return len(self.list)
        
    def __getitem__(self, ix):
        return self.list[ix]
    
    def __setitem__(self, ix, val):
        self.list[ix]=val
        
    def __iter__(self):
        return iter(self.list)
    
    def __contains__(self, val):
        return val in self.list
    
    def append(self, val):
        self.list.append(val)