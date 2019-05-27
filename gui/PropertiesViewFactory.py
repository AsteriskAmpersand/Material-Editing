# -*- coding: utf-8 -*-
"""
Created on Wed May 22 22:23:42 2019

@author: AsteriskAmpersand
"""
import sys
#from mrl3 import shadertype
from common import Cstruct
from common.CollapsibleWidget import QCollapsibleWidget

from gui.propertyUI.bbool1 import Ui_Form as bbool1Form
from gui.propertyUI.bbool2 import Ui_Form as bbool2Form
from gui.propertyUI.bbool3 import Ui_Form as bbool3Form
from gui.propertyUI.int4 import Ui_Form as int4Form
from gui.propertyUI.int4x4 import Ui_Form as int4x4Form

from gui.propertyUI.float1 import Ui_Form as float1Form
from gui.propertyUI.float2 import Ui_Form as float2Form
from gui.propertyUI.float3 import Ui_Form as float3Form
from gui.propertyUI.float4 import Ui_Form as float4Form

from gui.propertyUI.float3x4 import Ui_Form as float3x4Form
from gui.propertyUI.float4x4 import Ui_Form as float4x4Form

from PyQt5 import QtCore, QtWidgets

intSize = (-(2**30-1),2**30-1)#(-2**30,2**30)
uintSize = (0,2**31-1)
floatSize = (-(2-2**-23) * 2**127,(2-2**-23) * 2**127)

class propWidget(QtWidgets.QWidget):
    def __init__(self, varname, valget, valset, parent=None, *args, **kwargs):
        #getter(index) -> value, setter(index) -> lambda value:
        super().__init__(parent)
        self.setupUi(self)
        self.getter = valget
        self.setter = valset
        self.valName.setText(varname)
        self.valName.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.layout().setContentsMargins(0,0,0,0)
        self.layout().setSpacing(0)
        self.layout().setStretch(0,720)
        hlen = 616//len(self.uiElements)
        for ix, elementKey in enumerate(self.uiElements):
            self.layout().setStretch(ix+1,720//len(self.uiElements))
            uiElement = self.__getattribute__(elementKey)
            uiElement.setRange(*self.limit)
            uiElement.setMinimumSize(50, 20)
            uiElement.setMaximumSize(hlen, 20)
            uiElement.setSizePolicy(QtWidgets.QSizePolicy.Preferred,QtWidgets.QSizePolicy.Expanding)
            uiElement.setValue(self.getter(ix))
            uiElement.setAlignment(QtCore.Qt.AlignRight)
            uiElement.valueChanged.connect(lambda x: self.setter(ix, x))
                
class bbool1(bbool1Form, propWidget):
    limit = uintSize
    uiElements = ["v0"]
class bbool2(bbool2Form, propWidget):
    limit = uintSize
    uiElements = ["v0","v1"]
class bbool3(bbool3Form, propWidget):
    limit = uintSize
    uiElements = ["v0","v1","v2"]
class bbool4(int4Form, propWidget):
    limit = uintSize
    uiElements = ["v0","v1","v2","v3"]
class int1(bbool1):
    limit = intSize
class int2(bbool2):
    limit = intSize
class int3(bbool3):
    limit = intSize
class int4(bbool4):
    limit = intSize
class int4x4(int4x4Form, propWidget):
    limit = intSize
    uiElements = ["v%d%d"%(i,j) for i in range(4) for j in range(4)]
class float1(float1Form, propWidget):
    limit = floatSize
    uiElements = ["v0"]
class float2(float2Form, propWidget):
    limit = floatSize
    uiElements = ["v0","v1"]
class float3(float3Form, propWidget):
    limit = floatSize
    uiElements = ["v0","v1","v2"]
class float4(float4Form, propWidget):
    limit = floatSize
    uiElements = ["v0","v1","v2","v3"]
class float3x4(float3x4Form, propWidget):
    limit = floatSize
    uiElements = ["v%d%d"%(i,j) for i in range(3) for j in range(4)]
class float4x4(float4x4Form, propWidget):
    limit = floatSize
    uiElements = ["v%d%d"%(i,j) for i in range(4) for j in range(4)]

typeToWidget = {'bbool':bbool1,
                 'bbool2':bbool2,
                 'bbool3':bbool3,
                 'float':float1,
                 'float2':float2,
                 'float3':float3,
                 'float4':float4,
                 'float3x4':float3x4,
                 'float4x4':float4x4,
                 'int':int1,
                 'int2':int2,
                 'int3':int4,
                 'int4':int4,
                # 'ubyte':ubyte1: just ignore align variables
                 'uint':bbool1,
                 'uint2':bbool2,
                 'uint3':bbool3,
                 'uint4':bbool4,
                 'uint4x4':int4x4}

class ParameterWidget(QtWidgets.QWidget):
    def __init__(self, paramBinding, parent = None):
        super().__init__(parent)
        
        self.setLayout(QtWidgets.QVBoxLayout())
        self.params = paramBinding.paramArray
        collapsible = QCollapsibleWidget(self)
        for prop in self.params:
            propView = PropertyView(prop, self)
            collapsible.addSection(prop.__class__.__name__,propView)
        self.layout().addWidget(collapsible)
            
            

class PropertyView(QtWidgets.QWidget):
    flatStruct = True
    collectionStruct = False
    #for shaderParam in self.property: necessary because of how properties .... exist might payoff to add another class
    #that contains this one to preserve the recursiveness

    def __init__(self, propertyBinding, parent = None):
        super().__init__(parent)
        self.setLayout(QtWidgets.QVBoxLayout())
        self.property = propertyBinding
        metatype = self.getMetatype(propertyBinding)
        if metatype == self.flatStruct:
            self.flatStructInit()
        elif metatype == self.collectionStruct:
            self.collectionInit()
            
    @staticmethod
    def getMetatype(propertyObj):
        return not issubclass(type(propertyObj),Cstruct.Mod3Collection)
            
    def flatStructInit(self):
        structurePicker = [self.dataInit,
                           self.containerInit]
        
        for fieldname, fieldtype in self.property.fields.items():
            if "ubyte" not in fieldtype:
                propertyWidget = structurePicker[self.flatPicker(fieldtype)](fieldname,fieldtype,self.property)
                self.layout().addWidget(propertyWidget)
            #handle the new widget by adding it to the widget itself as a vertical layout
    @staticmethod
    def flatPicker(fieldtype):
        return "[" in fieldtype
    def collectionInit(self):
        macroContainer = QCollapsibleWidget(self)
        for mod3class, container in zip(self.property.Mod3Classes, self.property.data):
            #make a frame, set separator
            #add class family title
            frame = QtWidgets.QFrame(self)
            frame.setLayout(QtWidgets.QVBoxLayout())
            for ix, subObj in enumerate(container):
                propertyWidget = PropertyView(subObj, self, self.property)
                collapsible = QCollapsibleWidget(self)
                collapsible.addSection(mod3class.__name__+"[%d]"%ix,propertyWidget)
                frame.layout().addWidget(collapsible)
                #all of this under a single widget
            macroContainer.addSection(mod3class.__name__,frame)
        self.scrollArea.addWidget(macroContainer)
        #add a line of text to frame with index and mod3class  mod3class.__name__
        #add frame to widget layout or add this https://stackoverflow.com/questions/32476006/how-to-make-an-expandable-collapsable-section-widget-in-qt

    @staticmethod
    def arrayNameParse(arrayname):
        name, count = arrayname.replace("]","").split("[")
        return name, int(count)
        
    def containerInit(self,fieldname, fieldtype, shaderParam):
        arrayType, count = self.arrayNameParse(fieldtype)
        #Create frame layout and populate and return the frame
        collapsible = QCollapsibleWidget(self)
        for i in range(count):
            propertyWidget = typeToWidget[arrayType](
                                    fieldname + "[%d]"%i,
                                    shaderParam.__getattribute__(fieldname)[i].__getitem__, 
                                    shaderParam.__getattribute__(fieldname)[i].__setitem__,
                                    self)
            collapsible.addSection(fieldname,propertyWidget)
        return collapsible
    
    def dataInit(self,fieldname, fieldtype, shaderParam):
        propertyWidget = typeToWidget[fieldtype](
                        fieldname,
                        shaderParam.__getattribute__(fieldname).__getitem__,
                        shaderParam.__getattribute__(fieldname).__setitem__, 
                        self)
        return propertyWidget
    
if __name__ == "__main__":
    from mrl3.MaterialMrl3 import MRL3
    m = MRL3()
    with open(r"E:\MHW\FakeChunk\bow007.mrl3","rb") as mf:
        m.marshall(mf)
    params = m.Materials[0].paramArray
    app = QtWidgets.QApplication(sys.argv)
    window = ParameterWidget(params)
    window.show()
    sys.exit(app.exec_())