# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 01:40:48 2019

@author: AsteriskAmpersand
"""
import Mod3 as mod3
import Mrl3 as mrl3
from pathlib import Path
from collections import Counter
import os

def intToByteID(intValue):
    bytesArray = intValue.to_bytes(4, byteorder='little')
    return '('+';'.join([str(int(b)) for b in bytesArray])+')'

chunkPath=r"E:\MHW\Merged"
def create_dbs(chunkpath = chunkPath):
    remove_extension = lambda path: os.path.splitext(path)[0]
    
    compendium = {}
    idcompendium = {}
    name_list = {}
    id_list = {}
    global_count_name = Counter()
    global_count_id = Counter()
    
    
    results = list(Path(chunkpath).rglob("*.mod3"))#r"G:\MHW"
    model_material_pairs = [(result, remove_extension(result)+".mrl3") for result in results if os.path.isfile(remove_extension(result)+".mrl3")]
    for model, material in model_material_pairs:
        _, _, modelmaterials = mod3.parse_mod3(model)
        _, _, materialmaterials = mrl3.parse_mrl3(material)
        
        materialsId = list(map(lambda x: x.trueId, materialmaterials))
        for identifier in modelmaterials:
            if identifier not in compendium:
                #compendium[identifier] = Counter(materialsId)
                compendium[identifier] = set(materialsId)
            else:
                #compendium[identifier].update(materialsId)
                compendium[identifier].intersection(set(materialsId))
                
        for identifier in materialsId:
            if identifier not in idcompendium:
                #compendium[identifier] = Counter(materialsId)
                idcompendium[identifier] = set(modelmaterials)
            else:
                #compendium[identifier].update(materialsId)
                idcompendium[identifier].intersection(set(modelmaterials))
                
        for identifier in modelmaterials:
            if identifier not in name_list:
                name_list[identifier]=[model]
            else:
                name_list[identifier].append(model)
                
        for identifier in materialsId:
            if identifier not in id_list:
                id_list[identifier]=[material]
            else:
                id_list[identifier].append(material)
        global_count_name.update(modelmaterials)
        global_count_id.update(materialsId)
    return compendium, idcompendium, name_list, id_list, global_count_name, global_count_id
    
def sibling_compendium(compendium, idcompendium):
    found = set()
    sibling_names = {}
    for mb in compendium:
        if mb in found:
                continue
        found.update([mb])
        sibling_names[mb]=[]
        for ms in compendium:
            if ms in found:
                continue
            if len(compendium[mb].intersection(compendium[ms]))!=0:
                found.update([ms])
                sibling_names[mb].append(ms)
                
    sibling_id = {}
    for mb in idcompendium:
        if mb in found:
                continue
        found.update([mb])
        sibling_id[mb]=[]
        for ms in idcompendium:
            if ms in found:
                continue
            if len(idcompendium[mb].intersection(idcompendium[ms]))!=0:
                found.update([ms])
                sibling_id[mb].append(ms)
    return sibling_names, sibling_id

def create_files(compendium, idcompendium, name_list, id_list, global_count_name, global_count_id, sibling_names, sibling_id):
    with open("G:\Wisdom\MaterialCompendium.csv",'w') as outfile:
        outfile.write('\n'.join([material+','+','.join(map(intToByteID,compendium[material])) for material in compendium]))
    
    with open("G:\Wisdom\MaterialIDCompendium.csv",'w') as outfile:
        outfile.write('\n'.join([intToByteID(material)+','+','.join(idcompendium[material]) for material in idcompendium]))
    
    with open("G:\Wisdom\MaterialNames.csv",'w') as outfile:
        outfile.write('\n'.join([str(material)+','+','.join(map(str,name_list[material])) for material in name_list]))
    
    with open("G:\Wisdom\MaterialIDs.csv",'w') as outfile:
        outfile.write('\n'.join([intToByteID(material)+','+','.join(map(str,id_list[material])) for material in id_list]))
        
    with open("G:\Wisdom\EquivalentNames.csv",'w') as outfile:
        outfile.write('\n'.join([intToByteID(material)+','+','.join(map(intToByteID,sibling_id[material])) for material in sibling_id]))            
                
    with open("G:\Wisdom\EquivalentIDs.csv",'w') as outfile:
        outfile.write('\n'.join([material+','+','.join(map(str,sibling_names[material])) for material in sibling_names]))
        