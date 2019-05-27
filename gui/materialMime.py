# -*- coding: utf-8 -*-
"""
Created on Wed May 15 18:59:07 2019

@author: AsteriskAmpersand
"""

import struct
from PyQt5 import QtCore
from common.crc import CrcJamcrc
generalhash =  lambda x:  CrcJamcrc.calc(x.encode())

def safeCastHash(data):
    try:
        data = int(data,base=16)
    except:
        data = generalhash(data)
    return data

def packMatHash(obj, index):
    data = obj.data(index)
    mime = QtCore.QMimeData()
    data = safeCastHash(data)
    parent = obj.data(index.parent())
    mime.setData("custom/mrl3MaterialHash",parent.encode("utf-8")+b'\x00'+struct.pack("I",data))
    return mime

def packAllMatHash(obj, index):
    data = obj.data(index)
    mime = QtCore.QMimeData()
    hashes = [struct.pack("I",safeCastHash(obj.data(ix))) for ix in (obj.index(r,0,index) for r in range(obj.rowCount(index)))]
    mime.setData("custom/mrl3MaterialHash",data.encode("utf-8")+b'\x00'+b''.join(hashes))
    return mime

def packMat(obj, index):
    data = obj.data(index)
    mime = QtCore.QMimeData()
    mime.setData("custom/mrl3Path",data.encode("utf-8")+b'\x00')
    return mime
        
def unpackMatHashes(matMime):
    split = matMime.split(b'\x00')
    path, matHashes = bytearray(split[0]).decode("utf-8"),b'\x00'.join(split[1:])
    matHashes =  struct.unpack("I"*(len(matHashes)//4),bytearray(matHashes))
    return path, matHashes