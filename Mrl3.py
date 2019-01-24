# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 00:07:45 2019

@author: AsteriskAmpersand
"""
import struct
intBytes = lambda x: int.from_bytes(x, byteorder='little', signed=False)
hex_read = lambda f,x: intBytes(f.read(x))

class Header():
    def __init__(self, f=None):
        if f == None:
            self.headId = intBytes(b'MRL\x00')
            self.unknArray = [bytearray([i]) for i in [11,0,0,0,0xA9,0xBC,0xBB,0x59,0,0,0,0]]
            self.materialCount = 0
            self.textureCount = 0
            self.textureOffset = 0x28
            self.materialOffset = 0x28
        else:
            self.headId = hex_read(f,4)
            self.unknArray = [f.read(1) for i in range(12)]
            self.materialCount = hex_read(f,4)
            self.textureCount = hex_read(f,4)
            self.textureOffset = hex_read(f,8)
            self.materialOffset = hex_read(f,8)
        
    def serialize(self):
        serialization = bytearray()
        serialization += self.headId.to_bytes(4, byteorder='little')
        serialization += b''.join(self.unknArray)
        serialization += self.materialCount.to_bytes(4, byteorder='little')
        serialization += self.textureCount.to_bytes(4, byteorder='little')
        serialization += self.textureOffset.to_bytes(8, byteorder='little')
        serialization += self.materialOffset.to_bytes(8, byteorder='little')
        return serialization

class Texture():
    size = 4+12+256
    def __init__(self, f = None):
        if f == None:
            self.unkn1 = 0x241F5DEB
            self.unknArray = [b'\x00' for _ in range(12)]
            self.path = ''
        else:
            self.unkn1 = hex_read(f,4)
            self.unknArray = [f.read(1) for i in range(12)]
            self.path = f.read(256).decode().replace('\x00','')
    def serialize(self):
        serial = bytearray()
        serial += self.unkn1.to_bytes(4, byteorder='little')
        serial += b''.join(self.unknArray)
        bytepath = self.path.encode('utf-8')
        serial += bytepath+bytearray(256-len(bytepath))
        return serial
    def __eq__(self, other):
        if isinstance(type(other), type(self)):
            return self.unkn1 == other.unkn1 and self.path == other.path and all([a == b for a,b in zip(self.unknArray, other.unknArray)])
        else:
            return other == self.path
        

class TextureArgument():
    def __init__(self, f):
        self.unknArr = [f.read(1) for _ in range(8)]
        self.texIdx = hex_read(f,4)
        self.unkn5 = hex_read(f,4)     
        
    def serialize(self):
        serialization = bytearray()
        serialization += b''.join(self.unknArr)
        serialization += self.texIdx.to_bytes(4, byteorder='little')
        serialization += self.unkn5.to_bytes(4, byteorder='little')
        return serialization

class Material():
    size = 4+4+8+4+2+1+25+4+4
    def __init__(self, f):
        self.headId = hex_read(f,4)
        self.materialHash = hex_read(f,4)
        self.materialId = hex_read(f,8)
        self.matSize = hex_read(f,4)
        self.unkn4 = hex_read(f,2)
        self.parameterOffset = hex_read(f,1)
        self.unknArray = [f.read(1) for i in range(25)]
        self.startAddr = hex_read(f,4)
        self.unkn8 = hex_read(f,4)
        self.textureArguments = self.parse_arguments(f)
        self.paramArray = self.parse_parameters(f)
        
    def parse_arguments(self, f):
        f.seek(self.startAddr)
        return [TextureArgument(f) for _ in range(self.parameterOffset//2)]
    
    def parse_parameters(self, f):
        float_array = []
        while (f.tell()<self.startAddr + self.matSize):
            float_array.append(struct.unpack('f',f.read(4))[0])
        return float_array
    
    def name_textures(self, textures):
        self.texturePaths = [textures[i.texIdx-1].path if 0<i.texIdx<=len(textures) else '' for i in self.textureArguments]
        return self
    
    def serialize_header(self):
        serialization = bytearray()
        serialization += self.headId.to_bytes(4, byteorder='little')
        serialization += self.materialHash.to_bytes(4, byteorder='little')
        serialization += self.materialId.to_bytes(8, byteorder='little')
        serialization += self.matSize.to_bytes(4, byteorder='little')
        serialization += self.unkn4.to_bytes(2, byteorder='little')
        serialization += self.parameterOffset.to_bytes(1, byteorder='little')
        serialization += b''.join(self.unknArray)
        serialization += self.startAddr.to_bytes(4, byteorder='little')
        serialization += self.unkn8.to_bytes(4, byteorder='little')
        return serialization
        
    def serialize_data(self):
        return b''.join([x.serialize() for x in self.textureArguments])+b''.join([bytearray(struct.pack("f", f)) for f in self.paramArray])
    
    def coalesce(self, textures):
        for index, name in enumerate(self.texturePaths):
            if name == '':
                continue
            try:
                loc = textures.index(name)
                self.textureArguments[index].texIdx = loc+1
            except:
                texture = Texture()
                texture.path = name
                self.textureArguments[index].texIdx = len(textures)+1
                textures.append(texture)
        return
    
    def heuristic_coalesce(self, textures):
        for index, name in enumerate(self.texturePaths):
            heuristic_path = [t.path.split('_')[-1] for t in textures]
            if name == '':
                continue
            try:
                if "Assets" in name:
                    loc = textures.index(name)
                    self.textureArguments[index].texIdx = loc+1
                else:
                    loc = heuristic_path.index(name.split('_')[-1])
                    self.textureArguments[index].texIdx = loc+1
                    self.texturePaths[index] = textures[loc].path
            except:
                texture = Texture()
                texture.path = name
                self.textureArguments[index].texIdx = len(textures)+1
                textures.append(texture)
        return
                
    
    def __eq__(self, other):
        if isinstance(other, int):
            return other == self.trueId
        else:
            return other.trueId == self.trueId
                
    
def parse_textures(header, file):
    file.seek(header.textureOffset)
    return [Texture(file) for _ in range(header.textureCount)]
    
def parse_materials(header, file, textures):
    materialList = []
    for i in range(header.materialCount):
        file.seek(header.materialOffset+i*Material.size)
        materialList.append(Material(file).name_textures(textures))
    return materialList
    
def parse_mrl3(filename):
    file = open(filename,"rb")
    header = Header(file)
    textures = parse_textures(header, file)
    materials = parse_materials(header, file, textures)
    file.close()
    return header, textures, materials
    
def serialize_mrl3(header, textures, materials):
    for material in materials:
        material.coalesce(textures)
    header.materialCount = len(materials)
    header.textureCount = len(textures)
    print(header.materialCount)
    header.materialOffset = len(textures)*Texture.size+header.textureOffset
    for index, material in enumerate(materials):
        material.startAddr = header.materialOffset + len(materials)*Material.size + sum([mat.matSize for mat in materials[:index]])
    return header.serialize()+b''.join([t.serialize() for t in textures])+b''.join([m.serialize_header() for m in materials])+b''.join([m.serialize_data() for m in materials])