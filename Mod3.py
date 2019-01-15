# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 22:51:11 2019

@author: AsteriskAmpersand
"""


class Header():
    def __init__(self, f):
        f. seek(0)
        self. mod3_id = int.from_bytes(f.read(4), byteorder='little', signed=False)
        self.version = int.from_bytes(f.read(1), byteorder='little', signed=False)
        self.version2 = int.from_bytes(f.read(1), byteorder='little', signed=False)
        self.boneCount = int.from_bytes(f.read(2), byteorder='little', signed=False)
        self.meshCount = int.from_bytes(f.read(2), byteorder='little', signed=False)
        self.materialCount = int.from_bytes(f.read(2), byteorder='little', signed=False)
        self.vertexCount = int.from_bytes(f.read(4), byteorder='little', signed=False)
        self.faceCount = int.from_bytes(f.read(4), byteorder='little', signed=False)
        self.vertexIds = int.from_bytes(f.read(4), byteorder='little', signed=False)
        self.vertexBufferSize = int.from_bytes(f.read(4), byteorder='little', signed=False)
        self.secondBufferSize = int.from_bytes(f.read(4), byteorder='little', signed=False)
        self.groupCount = int.from_bytes(f.read(8), byteorder='little', signed=False)
        self.boneMapCount = int.from_bytes(f.read(8), byteorder='little', signed=False)
        self.boneOffset = int.from_bytes(f.read(8), byteorder='little', signed=False)
        self.groupOffset = int.from_bytes(f.read(8), byteorder='little', signed=False)
        self.materialNamesOffset = int.from_bytes(f.read(8), byteorder='little', signed=False)
        self.meshOffset = int.from_bytes(f.read(8), byteorder='little', signed=False)
        self.VertextOffset = int.from_bytes(f.read(8), byteorder='little', signed=False)
        self.FacesOffset = int.from_bytes(f.read(8), byteorder='little', signed=False)
        self.unknOfset = int.from_bytes(f.read(8), byteorder='little', signed=False)

class Mesh_Part():
    def __init__(self, file):
        self.unkn = int.from_bytes(file.read(2), byteorder='little', signed=False)
        self.VertexCount = int.from_bytes(file.read(2), byteorder='little', signed=False)
        self.visibility = int.from_bytes(file.read(2), byteorder='little', signed=False)
        self.materialIdx = int.from_bytes(file.read(2), byteorder='little', signed=False)
        self.lod = int.from_bytes(file.read(4), byteorder='little', signed=False)
        self.unkn2 = int.from_bytes(file.read(2), byteorder='little', signed=False)
        self.blockSize = int.from_bytes(file.read(1), byteorder='little', signed=False)
        self.unkn3 = int.from_bytes(file.read(1), byteorder='little', signed=False)
        self.vertexSub = int.from_bytes(file.read(4), byteorder='little', signed=False)
        self.VertexOffset = int.from_bytes(file.read(4), byteorder='little', signed=False)
        self.blocktype = int.from_bytes(file.read(4), byteorder='little', signed=False)
        self.FaceOffset = int.from_bytes(file.read(4), byteorder='little', signed=False)
        self.FaceCount = int.from_bytes(file.read(4), byteorder='little', signed=False)
        self.vertexBase = int.from_bytes(file.read(4), byteorder='little', signed=False)
        self.boneremapid = int.from_bytes(file.read(1), byteorder='little', signed=False)
        self.unknArray = [int.from_bytes(file.read(1), byteorder='little', signed=False) for _ in range(39)]
        
def parse_mesh_parts(header, file):
    file.seek(header.meshOffset)
    return [Mesh_Part(file) for _ in range(header.meshCount)]

def parse_material_names(header, file):
    file.seek(header.materialNamesOffset)
    return [(file.read(128)).decode().replace('\x00','') for _ in range(header.materialCount)]
            
def filter_idx(meshparts, materialnames):
    return [j for i,j in enumerate(materialnames) if i in set([m.materialIdx for m in meshparts])]   
    
def parse_mod3(filename):
    file = open(filename,"rb")
    header = Header(file)
    parts = parse_mesh_parts(header, file)
    materials = filter_idx(parts, parse_material_names(header,file))
    return header, parts, materials