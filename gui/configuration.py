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
        
    def save(self, libpath, filepaths):
        if libpath: self.libpath=libpath
        if filepaths: self.filepaths=filepaths
        config = {"libpath" : libpath, "compendiumpath" : 'compendium.ast', "filepaths" : filepaths}
        with open("Config.ini","w") as configf:
            configf.write(json.dumps(config))
        return
    
    
    def createConfig(self):
        config = {"libpath" : '', "compendiumpath" : 'compendium.ast', "filepaths" : []}
        with open("Config.ini","w") as configf:
            configf.write(json.dumps(config))
        return config
    
    def load(self, config):
        for setting in config:
            self.__setattr__(setting, config[setting])
            