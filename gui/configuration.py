# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 00:55:10 2019

@author: AsteriskAmpersand
"""
import json

class Configuration():
    def __init__(self):
        try:
            preconfig = json.load(open("Config.ini","r"))
        except:
            preconfig = self.createConfig()
        self.load(preconfig)
        
    def save(self, iblibpath, ibfilepaths):
        if iblibpath: self.iblibpath=iblibpath
        if ibfilepaths: self.ibfilepaths=ibfilepaths
        config = {"iblibpath" : iblibpath, "ibcompendiumpath" : 'ibcompendium.ast', "ibfilepaths" : ibfilepaths}
        with open("Config.ini","w") as configf:
            configf.write(json.dumps(config))
        return
    
    def createConfig(self):
        config = {"iblibpath" : '', "ibcompendiumpath" : 'ibcompendium.ast', "ibfilepaths" : []}
        with open("Config.ini","w") as configf:
            configf.write(json.dumps(config))
        return config
    
    def load(self, config):
        for setting in config:
            self.__setattr__(setting, config[setting])
            
            