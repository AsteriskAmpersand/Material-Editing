# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 23:57:13 2019

@author: AsteriskAmpersand
"""

sdf_default_path = "E:\MHW\Merged\system\shader\ShaderPackage.sdf"
def shader_strings(sdf_path=sdf_default_path):
    shader = open(sdf_path, "rb")
    offset= 0xA5A25B0# 0xA5A1c40+0xF+0x8
    shader.seek(offset)
    return list(map(lambda x: x.decode(),shader.read().split(b'\x00')))  
    