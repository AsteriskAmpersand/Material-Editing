# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 13:38:38 2019

@author: AsteriskAmpersand
"""
import struct
from collections import OrderedDict
from binascii import hexlify

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]

def HalfToFloat(h):
    s = int((h >> 15) & 0x00000001)    # sign
    e = int((h >> 10) & 0x0000001f)    # exponent
    f = int(h & 0x000003ff)            # fraction
    if s==0 and e==0 and f==0:
        return 0
    return (-1)**s*2**(e-15)*(f/(2**10)+1)

def minifloatDeserialize(x):
    v = struct.unpack('H', x)
    return HalfToFloat(v[0])
#   x = HalfToFloat(v[0])
#    # hack to coerce int to float
#    bstring = struct.pack('I',x)
#    f=struct.unpack('f', bstring)
#    return f[0]

def minifloatSerialize(x):
    F16_EXPONENT_BITS = 0x1F
    F16_EXPONENT_SHIFT = 10
    F16_EXPONENT_BIAS = 15
    F16_MANTISSA_BITS = 0x3ff
    F16_MANTISSA_SHIFT =  (23 - F16_EXPONENT_SHIFT)
    F16_MAX_EXPONENT =  (F16_EXPONENT_BITS << F16_EXPONENT_SHIFT)
    a = struct.pack('>f',x)
    b = hexlify(a)
    f32 = int(b,16)
    f16 = 0
    sign = (f32 >> 16) & 0x8000
    exponent = ((f32 >> 23) & 0xff) - 127
    mantissa = f32 & 0x007fffff
    if exponent == 128:
    	f16 = sign | F16_MAX_EXPONENT
    	if mantissa:
    		f16 |= (mantissa & F16_MANTISSA_BITS)
    elif exponent > 15:#hack
    	f16 = sign | F16_MAX_EXPONENT
    elif exponent >= -15:#hack
    	exponent += F16_EXPONENT_BIAS
    	mantissa >>= F16_MANTISSA_SHIFT
    	f16 = (sign | exponent << F16_EXPONENT_SHIFT | mantissa)
    else:
    	f16 = sign
    return struct.pack('H',f16)

class Cstruct():
    deserializer = lambda y: {'deserializer':lambda x: struct.unpack(y,x)[0], 'serializer': lambda x: struct.pack(y,x)}
    CTypes = {"byte":       {'size':1,**deserializer('b')},
                "int8":     {'size':1,**deserializer('b')},
                "ubyte":    {'size':1,**deserializer('B')},
                "uint8":    {'size':1,**deserializer('B')},
                "short":    {'size':2,**deserializer('h')},
                "int16":    {'size':2,**deserializer('h')},
                "ushort":   {'size':2,**deserializer('H')},
                "uint16":   {'size':2,**deserializer('H')},
                "long":     {'size':4,**deserializer('i')},
                "int32":    {'size':4,**deserializer('i')},
                "int":      {'size':4,**deserializer('i')},
                "ulong":    {'size':4,**deserializer('I')},
                "uint32":   {'size':4,**deserializer('I')},
                "uint":     {'size':4,**deserializer('I')},
                "quad":     {'size':8,**deserializer('q')},
                "int64":    {'size':8,**deserializer('q')},
                "uquad":    {'size':8,**deserializer('Q')},
                "uint64":   {'size':8,**deserializer('Q')},
                "hfloat":   {'size':2,'deserializer':minifloatDeserialize, 'serializer':minifloatSerialize},
                "float":    {'size':4,**deserializer('f')},
                "double":   {'size':8,**deserializer('d')},
                "char":     {'size':1,**deserializer('c')},
                "bool":     {'size':1,**deserializer('b')},
            }
    StructTypes = {}
    
    def isArrayType(self,typeStr):
        return '[' in typeStr and (typeStr[:typeStr.index('[')] in self.CTypes or typeStr[:typeStr.index('[')] in self.StructTypes)
        
    def arrayType(self,typeStr):
        base = typeStr[:typeStr.index('[')]
        size = typeStr[typeStr.index('[')+1:typeStr.index(']')]
        #baseTypeCall = Cstruct.CTypes if base in Cstruct.CTypes else Cstruct.StructTypes
        baseTypeCall = self.CTypes
        
        intSize = int(size)
        return {
                'size': intSize*baseTypeCall[base]['size'], 
                'deserializer': lambda x: [baseTypeCall[base]['deserializer'](chunk) for chunk in chunks(x,baseTypeCall[base]['size']) ], 
                'serializer':   lambda x: b''.join(map(baseTypeCall[base]['serializer'],x))
                } if base != "char" else {
                'size': intSize*baseTypeCall[base]['size'], 
                'deserializer': lambda x: ''.join([( baseTypeCall[base]['deserializer'](chunk) ).decode("utf-8") for chunk in chunks(x,baseTypeCall[base]['size']) ]), 
                'serializer':   lambda x: x.encode('utf-8').ljust(intSize, b'\x00')
                }
                
    def __init__(self, fields):
       self.struct = OrderedDict()
       self.initialized = True
       for name in fields:
            if fields[name] in self.CTypes:
                self.struct[name]=self.CTypes[fields[name]]
            elif self.isArrayType(fields[name]):
                self.struct[name]=self.arrayType(fields[name])
            else:
                raise ValueError("%s Type is not C Struct class compatible."%fields[name])
            
    def __len__(self):
        return sum([self.struct[element]['size'] for element in self.struct])
        
    def marshall(self, data):
        return {varName:typeOperator['deserializer'](data.read(typeOperator['size'])) for varName, typeOperator in self.struct.items()}
    
    def serialize(self, data):
        return b''.join([typeOperator['serializer'](data[varName]) for varName, typeOperator in self.struct.items()])

class ExtendedCStruct(Cstruct):
    extendedDeserializer = lambda y: {'deserializer':lambda x: list(struct.unpack(y,x)), 'serializer': lambda x: struct.pack(y,*x)}
    matrixDeserializer = lambda y, colC, rowC, size: {
                            'deserializer':lambda x: [[struct.unpack(y,x[r*colC*size+c*size:r*colC*size+(c+1)*size]) for c in range(colC)]for r in range(rowC)], 
                            'serializer': lambda x: struct.pack(y,*(sum(x,[])))}
    ECTypes = {"bbool":     {'size':4,**extendedDeserializer('I')},
               "bbool2":    {'size':8,**extendedDeserializer('II')},
               "bbool3":    {'size':12,**extendedDeserializer('III')},
               "float":     {'size':4,**extendedDeserializer('f')},
               "float2":    {'size':8,**extendedDeserializer('ff')},
               "float3":    {'size':12,**extendedDeserializer('fff')},
               "float4":    {'size':16,**extendedDeserializer('ffff')},
               "float3x4":  {'size':4*3*4,**matrixDeserializer('f',3,4,4)},
               "float4x4":  {'size':4*4*4,**matrixDeserializer('f',4,4,4)},
               "uint4x4":   {'size':4*4*4,**matrixDeserializer('I',4,4,4)},
               "uint":      {'size':4,**extendedDeserializer('I')},
               "uint2":     {'size':8,**extendedDeserializer('II')},
               "uint3":     {'size':12,**extendedDeserializer('III')},
               "uint4":     {'size':16,**extendedDeserializer('IIII')},
               "int":       {'size':4,**extendedDeserializer('i')},
               "int2":      {'size':8,**extendedDeserializer('ii')},
               "int3":      {'size':12,**extendedDeserializer('iii')},
               "int4":      {'size':16,**extendedDeserializer('iiii')},
               
            }
    CTypes = {ctp:ser for ctp,ser in list(Cstruct.CTypes.items())+list(ECTypes.items())}

class PyCStruct():
    structClass = Cstruct
    def __init__(self, data = None, **kwargs):
        self.CStruct = self.structClass(self.fields)
        if data != None:
            self.marshall(data)
        elif kwargs:
            fieldskeys = set(self.fields.keys())
            entrykeys=set(kwargs.keys())
            if fieldskeys == entrykeys:
                [self.__setattr__(attr, value) for attr, value in kwargs.items()]
            else:
                if fieldskeys > entrykeys:
                    raise AttributeError("Missing fields to Initialize")
                if fieldskeys < entrykeys:
                    raise AttributeError("Excessive Fields passed")
                raise AttributeError("Field Mismatch")
        
    def __len__(self):
        return len(self.CStruct)
                
    def marshall(self,data):
        [self.__setattr__(attr, value) for attr, value in self.CStruct.marshall(data).items()]
        
    def serialize(self):
        return self.CStruct.serialize({key:self.__getattribute__(key) for key in self.fields})
    
    def __eq__(self, other):
        return all([self.__getattribute__(key)==other.__getattribute__(key) for key in self.fields])

    defaultProperties = {}
    requiredProperties = {}
    def construct(self,data):
        for field in self.fields:
            if field in data:
                self.__setattr__(field,data[field])
            elif field in self.defaultProperties:
                self.__setattr__(field,self.defaultProperties[field])
            elif field in self.requiredProperties:
                raise KeyError("Required Property missing in supplied data")
            else:
                self.__setattr__(field,None)
                
    def verify(self):
        for attr in self.fields:
            if self.__getattribute__(attr) is None:
                raise AssertionError("Attribute %s is not initialized."%attr)

class ExtendedPyCStruct(PyCStruct):
    structClass = ExtendedCStruct
 
class Mod3Container():
    baseCount = 0
    Mod3Class = None
    def __init__(self, Mod3Class = Mod3Class, containeeCount = baseCount):
        self.mod3Array = [Mod3Class() for _ in range(containeeCount)]
    
    def marshall(self, data):
        [x.marshall(data) for x in self.mod3Array]
        
    def construct(self, data):
        if len(data) != len(self.mod3Array):
            raise AssertionError("Cannot construct container with different amounts of data")
        [x.construct(d) for x,d in zip(self.mod3Array,data)]
        
    def serialize(self):
        return b''.join([element.serialize() for element in self.mod3Array])
    
    def __iter__(self):
        return self.mod3Array.__iter__()
    
    def __getitem__(self, ix):
        return self.mod3Array.__getitem__(ix)
    
    def __len__(self):
        return self.baseCount * len(self.Mod3Class())
        if self.mod3Array:
            return len(self.mod3Array)*len(self.mod3Array[0])
        return 0
    
    def append(self, ele):
        self.mod3Array.append(ele)
    
    def pop(self,ix):
        self.mod3Array.pop(ix)
        
    def Count(self):
        return len(self.mod3Array)
    
    def verify(self):
        [x.verify() for x in self.mod3Array]
        
class Mod3Collection():
    Mod3Classes = []
    Mod3Counts = []
    def __init__(self,classes = Mod3Classes, counts = Mod3Counts):
        self.data = [Mod3Container(c3, k3) for c3, k3 in zip(classes, counts)]
    def marshall(self, data):
        for container in self.data:
            container.marshall(data)
    def serialize(self, data):
        return b''.join([datum.serialize() for datum in self.data])
    def __len__(self):
        return sum([len(datum) for datum in self.data])
    def Count(self):
        return len(self.data)