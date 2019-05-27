# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 13:18:43 2019

@author: AsteriskAmpersand
"""
from mod3 import Mod3Components as Mod3C
from mod3 import Mod3Mesh as Mod3M
from mod3 import Mod3Skeleton as Mod3S
from mod3.Mod3VertexBuffers import Mod3Vertex

class Mod3():    
    def __init__(self):
        self.Header = Mod3C.MOD3Header
        self.Skeleton = Mod3S.Mod3SkelletalStructure
        self.GroupProperties = Mod3C.Mod3GroupProperties#Can be completely nulled out for no risk
        self.Materials = Mod3C.Mod3Materials
        self.MeshParts = Mod3M.Mod3MeshCollection
        self.Trailing = Mod3C.GenericRemnants
        
    def marshall(self, data):
        self.Header = self.Header()
        self.Header.marshall(data)
        data.seek(self.Header.boneOffset)
        self.Skeleton = self.Skeleton(self.Header.boneCount, self.Header.boneMapCount)
        self.Skeleton.marshall(data)
        data.seek(self.Header.groupOffset)
        self.GroupProperties = self.GroupProperties(self.Header.groupCount)
        self.GroupProperties.marshall(data)
        data.seek(self.Header.materialNamesOffset)
        self.Materials = self.Materials(self.Header.materialCount)
        self.Materials.marshall(data)
        data.seek(self.Header.meshOffset)
        self.MeshParts = self.MeshParts(self.Header.meshCount, self.Header.vertexOffset, self.Header.facesOffset)
        self.MeshParts.marshall(data)
        data.seek(self.Header.unknOffset)
        self.Trailing = self.Trailing()
        self.Trailing.marshall(data)

    def construct(self, fileHeader, materials, groupStuff, skeleton, lmatrices, amatrices, meshparts, meshData, trailingData):
        self.Header = self.Header()
        self.Header.construct(fileHeader)
        self.Skeleton = self.Skeleton(len(skeleton), None)
        self.Skeleton.construct(skeleton,lmatrices,amatrices)#TODO
        self.GroupProperties = self.GroupProperties(self.Header.groupCount)
        self.GroupProperties.construct(groupStuff)
        self.Materials = self.Materials(len(materials))
        self.Materials.construct(materials)
        self.MeshParts = self.MeshParts(len(meshparts))
        self.MeshParts.construct(meshparts, meshData)#TODO
        self.Trailing = self.Trailing()
        self.Trailing.construct(trailingData)
        self.calculateCountsOffsets()
        self.MeshParts.realignFaces()
        self.verify()
        
    def verify(self):
        self.Header.verify()
        self.Skeleton.verify()
        self.GroupProperties.verify()
        self.Materials.verify()
        self.MeshParts.verify()
        self.Trailing.verify()

    @staticmethod
    def pad(current,finalposition):
        return b''.join([b'\x00']*(finalposition-current))
           
    def calculateCountsOffsets(self):
        #TODO - Sanity Checks
        vCount, fCount, vBufferLen = self.MeshParts.updateCountsOffsets()
    
        #Header
        #("boneCount","short"),
        self.Header.boneCount = self.Skeleton.Count()
        #("meshCount","short"),
        self.Header.meshCount = self.MeshParts.Count()
        #("materialCount","short"),
        self.Header.materialCount = self.Materials.Count()
        #("vertexCount","long"),
        self.Header.vertexCount = vCount
        #("faceCount","long"),
        self.Header.faceCount = fCount*3
        #("vertexIds","long"),#notModifiedEver
        #("vertexBufferSize","long"),#length of vertices section
        self.Header.vertexBufferSize = vBufferLen
        #("secondBufferSize","long"),#unused
        #("groupCount","uint64"),#unchanged
        #("boneMapCount","uint64"),
        #self.Header.boneMapCount = self.Skeleton.Count()
        self.Header.boneCount = self.Skeleton.Count()
        
        currentOffset = len(self.Header)
        #("boneOffset","uint64"),
        self.Header.boneOffset = self.align(currentOffset) if self.Header.boneCount else 0
        #("groupOffset","uint64"),
        currentOffset = self.Header.groupOffset = self.align(currentOffset+len(self.Skeleton))
        #("materialNamesOffset","uint64"),
        currentOffset = self.Header.materialNamesOffset = self.align(currentOffset+len(self.GroupProperties))
        #("meshOffset","uint64"),
        self.Header.meshOffset = self.align(currentOffset + len(self.Materials))
        #("vertexOffset","uint64"),
        self.Header.vertexOffset = self.Header.meshOffset + self.MeshParts.getVertexOffset()
        #("facesOffset","uint64"),
        self.Header.facesOffset = self.Header.meshOffset + self.MeshParts.getFacesOffset()
        #("unknOffset","uint64"),
        self.Header.unknOffset = self.align(self.Header.meshOffset + self.MeshParts.getBlockOffset(),4)
          
    @staticmethod
    def align(offset, grid = 16):
        return offset+(grid - offset%grid if offset%grid else 0)
    
    def serialize(self):
        serialization = b''
        serialization+=self.Header.serialize()
        serialization+=self.pad(len(serialization),self.Header.boneOffset)
        serialization+=self.Skeleton.serialize()
        #serialization+=self.pad(len(serialization),self.Header.groupOffset)
        #serialization+=self.GroupProperties.serialize()
        serialization+=self.pad(len(serialization),self.Header.materialNamesOffset)
        serialization+=self.Materials.serialize()
        serialization+=self.pad(len(serialization),self.Header.meshOffset)
        serialization+=self.MeshParts.serialize()
        serialization+=self.pad(len(serialization),self.Header.unknOffset)
        serialization+=self.Trailing.serialize()
        return serialization
    
    def sceneProperties(self):
        sceneProp = self.Header.sceneProperties()
        sceneProp.update(self.Materials.sceneProperties())
        sceneProp.update(self.Trailing.sceneProperties())
        #TODO - Separate properties per sections leave only Header, Materials and Trailing
        return sceneProp
    
    def prepareArmature(self):
        return self.Skeleton.traditionalSkeletonStructure()  

    def meshProperties(self):
        return self.MeshParts.sceneProperties()
    
    def prepareMeshparts(self, weightSplit):
        meshes = []
        for traditionalMesh in self.MeshParts.traditionalMeshStructure(weightSplit):
            traditionalMesh["properties"]["material"] = self.Materials[traditionalMesh["properties"]["materialIdx"]]
            traditionalMesh["properties"].pop("materialIdx")
            traditionalMesh["properties"]["blockLabel"] = Mod3Vertex.blocklist[traditionalMesh["properties"]["blocktype"]]["name"]
            traditionalMesh["properties"].pop("blocktype")
            meshes.append(traditionalMesh)
        return meshes
    
    def filterLOD(self):
        self.MeshParts.filterLOD()

def doublesidedEval(v1, v2):
    if v1 != v2:
        print(v1)
        print(v2)
        raise ValueError()