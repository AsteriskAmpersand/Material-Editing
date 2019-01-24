# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 01:40:48 2019

@author: AsteriskAmpersand
"""
import Mod3 as mod3
import Mrl3 as mrl3
from ShaderListing import shader_strings
from pathlib import Path
from collections import Counter
import os
from crccheck.crc import CrcJamcrc
import zlib
import csv

def intToByteID(intValue):
    bytesArray = intValue.to_bytes(8, byteorder='little')
    return '('+';'.join([str(int(b)) for b in bytesArray])+')'

chunkPath=r"E:\MHW\Merged"

generalhash =  lambda x:  CrcJamcrc.calc(x.encode())
materialcrc = lambda x: CrcJamcrc.calc(x.encode()) & 0x7FFFFFFF
#materialcrc = generalhash
midway = lambda x: CrcJamcrc.calc(x.encode()) & 0x7FFFFFFF
def create_dbs(shader_string_list=shader_strings(), chunkpath = chunkPath):
    remove_extension = lambda path: os.path.splitext(path)[0]
    material_hashes_compendium = set()
    material_ids_compendium = set()
    
    material_hashes = {}
    
    model_files = list(Path(chunkpath).rglob("*.mod3"))
    materials = list(Path(chunkpath).rglob("*.mrl3"))
    
    material_names_compendium = set(sum([mod3.parse_mod3(m)[2] for m in model_files],[])).union(set(shader_string_list))
    hash_to_name = {materialcrc(m):m for m in material_names_compendium}
    
    for material in sum([mrl3.parse_mrl3(m)[2] for m in materials],[]):
        if material.materialHash not in material_hashes:
            material_hashes[material.materialHash] = [material]
        else:
            material_hashes[material.materialHash].append(material)
        material_ids_compendium.add(material.materialId)
        material_hashes_compendium.add(material.materialHash)
    return material_names_compendium, material_ids_compendium, material_hashes_compendium, hash_to_name, sum([mrl3.parse_mrl3(m)[2] for m in materials],[])


default_external_hashes = r"G:\Tools\MRL3ExeHashes.csv"
def external_hash_parsing(external_hashes = default_external_hashes):
    file = csv.DictReader(open(external_hashes,'rt'))
    file_dump = [row for row in file]
    compatible = [entry for entry in file_dump if int(entry['hash'], 16)==materialcrc(entry['name'])]
    incompatible = [entry for entry in file_dump if int(entry['hash'], 16)!=materialcrc(entry['name'])]
    truly_incompatible = [entry for entry in incompatible if int(entry['hash'], 16)!=generalhash(entry['name'])]

"""
if __name__ == '__main__':
    names, ids, hashes, modeldata, materials = create_dbs()
    
    h2=open(r'G:\Wisdom\hash_to_name.csv','w', newline='')
    h2n = csv.DictWriter(h2,['hash','material_name'])
    h2n.writeheader()
    for mathash, matname in modeldata.items():
        h2n.writerow({'hash':mathash,'material_name':matname})
    h2.close()
    
    h2 = open(r'G:\Wisdom\material_name_to_skin_id.csv','w', newline='')
    h2n = csv.DictWriter(h2,['material_name','skin_id'])
    h2n.writeheader()    
    material_name_to_materials = {}
    for m in materials:
        if m.materialHash in modeldata:
            material_name = modeldata[m.materialHash]
        else:
            material_name = "Unknown"
        if material_name not in material_name_to_materials:
            material_name_to_materials[material_name] = set()
        material_name_to_materials[material_name].add(m.materialId)
        
    for matname in sorted(list(set(material_name_to_materials.keys()))):
        h2n.writerow({'material_name':matname,'skin_id':str(list(material_name_to_materials[matname]))})
    h2.close()
    
    for h in hashes:
        if h not in modeldata.keys():
            print (h)
            
    for h in modeldata.keys():
        if h not in hashes:
            print(modeldata[h])
"""