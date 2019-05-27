import os
import sys
from common.crc import CrcJamcrc
from common.FileLike import FileLike
from mrl3.MaterialMrl3 import MRL3
import json
from collections import OrderedDict
from  gui.materialMime import packMatHash, packMat, unpackMatHashes

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt

generalhash =  lambda x:  CrcJamcrc.calc(x.encode())

class Mrl3Resolver():
    def __init__(self, resolutionDict = None):
        if resolutionDict is None:
            try:
                if getattr(sys, 'frozen', False):
                    # If the application is run as a bundle, the pyInstaller bootloader
                    # extends the sys module by a flag frozen=True and sets the app 
                    # Inside Exe: path into variable _MEIPASS'.
                    # Outside Exe: os.path.dirname(sys.executable)
                    application_path = sys._MEIPASS#os.path.dirname(sys.executable)
                elif __file__:
                    application_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
                path_to_resolution = application_path+r"\HashToMaterial.ryo"
                resolution = open(path_to_resolution,"r")
                self.knownResolutions = {generalhash(string):string for string in resolution.read().split(',')}
            except:
                self.knownResolutions = {}
        else:
            self.knownResolutions = {int(key):val for key, val in resolutionDict.items()}
            
    def __getitem__(self, item):
        if item in self.knownResolutions:
            return self.knownResolutions[item]
        else:
            return hex(item)

class Mrl3Compendium():
    def __init__(self, compendiumFile = None):
        self.Resolver = Mrl3Resolver()
        if compendiumFile:
            try:
                with open(compendiumFile,"r") as compendiumF:
                    savedData = json.load(compendiumF)
                self.MaterialSources = MaterialSources({material:linklist for material, linklist in savedData.items()})
                return
            except Exception as e:
                pass
        self.MaterialSources = MaterialSources()
            
    def Model(self):
        return self.MaterialSources
    
    def resolveHashToName(self, nameHash):
        return self.Resolver[nameHash]
    
    def expand(self, files):
        dictList = []
        for file in files:
            try:
                with open(file,"rb") as matf:
                    mat = MRL3()
                    mat.marshall(FileLike(matf.read()))
                    hashes = mat.getMaterialHashes()
            except:
                hashes = []
            dictList += [(self.resolveHashToName(hashId), file) for hashId in hashes]
        materialDict = {}
        for key, ele in dictList:
            if key not in materialDict: materialDict[key]=[]
            materialDict[key].append(ele)
        self.MaterialSources.expand(materialDict)
        return
    
    def rebase(self,files):
        self.MaterialSources = MaterialSources()
        self.expand(files)
        
    def model(self):
        return self.MaterialSources
    
    def save(self,path):
        with open(path,"w") as outf:
            json.dump(self.MaterialSources.dictSerialize(),outf)
    
class MaterialSources (QtGui.QStandardItemModel):
    def __init__(self, resourceDict={}, parent=None):
        super().__init__()
        self.keyObjMap = {}
        self.pathsObjMap = {}
        self.expand(resourceDict)
    
    @staticmethod
    def mimeTypes():
        return ["custom/mrl3Path"]
    
    def mimeData(self, indexes):
        if len(indexes)>1:
            raise ValueError
        index = indexes[0]
        if index.isValid():
            return packMat(self, index)  
    
    def flags(self, index):
        if not index.isValid():
            return Qt.NoItemFlags
        else:
            return Qt.ItemIsSelectable | Qt.ItemIsDragEnabled | Qt.ItemIsEnabled
    
    def expand(self, resourceDict):
        for material, paths in resourceDict.items():
            if material not in self.keyObjMap:
                item = QtGui.QStandardItem(material)
                item.setFlags(item.flags() & (~Qt.ItemIsEditable) & (~Qt.ItemIsDragEnabled) & (~Qt.ItemIsDropEnabled))
                self.keyObjMap[material] = item
                self.pathsObjMap[material] = set()
                self.appendRow(item)
            parent = self.keyObjMap[material]
            for path in paths:
                if path not in self.pathsObjMap[material]:
                    self.pathsObjMap[material].add(path)
                    subitem = QtGui.QStandardItem(str(path))
                    subitem.setFlags(subitem.flags() & (~Qt.ItemIsEditable) & (~Qt.ItemIsDropEnabled) | (Qt.ItemIsDragEnabled))
                    parent.appendRow(subitem)
    
    def dictSerialize(self):
        return {key:list(map(str,subset)) for key, subset in self.pathsObjMap.items()}