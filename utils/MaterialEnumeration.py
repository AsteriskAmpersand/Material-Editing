# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 21:03:53 2020

@author: AsteriskAmpersand
"""
import OldCode.Mod3 as mod3
from pathlib import Path

def shader_strings():
    with open(r"G:\Tools\MaterialEditor\MaterialEditing\HashToMaterial.ryo","r") as inf:
        textdump = inf.read()
        return textdump.split(",")
    with open(r"G:\Tools\MaterialEditor\MaterialEditing\utils\ShaderExtractors\ListBindingNames.ryo","r") as inf:
        textdump = inf.read()
        return textdump.split(",")
    
def write_strings(keys):
    with open(r"G:\Tools\MaterialEditor\MaterialEditing\IBHashToMaterial.ryo","w") as inf:
        inf.write(",".join(keys))

def basicDenum(stringSet):
    superset = set()
    for s in stringSet:
        for i in range(1000):
            superset.add(s+"__%d"%i)
    return superset

"""
import matplotlib.pyplot as plt
import numpy as np

from collections import Counter

def histoplot(string,counter):
    #print(counter)
    # An "interface" to matplotlib.axes.Axes.hist() method
    plt.scatter(list(counter.keys()),list(counter.values()))
    #plt.grid(axis='y', alpha=0.5)
    #plt.xlabel('Value')
    #plt.ylabel('Frequency')
    plt.title(string)
    plt.gca().set_yticks(range(0,max(counter.values())))
    #plt.text(23, 45, r'$\mu=15, b=3$')
    #maxfreq = n.max()
    # Set a clean upper y-axis limit.
    #plt.ylim(ymax=np.ceil(maxfreq / 10) * 10 if maxfreq % 10 else maxfreq + 10)
    plt.show()
    #raise
"""

def stochasticDenum(densitySets):
    new = set()
    for key,group in densitySets.items():
        indices = []
        for string in group:
            candidate = string.split("__")[-1]
            try:
                c = int(candidate)
                if c>10**5:
                    continue
            except:
                continue
            indices.append(c)
        if indices:
            if max(indices) > 999:
                #histoplot(key,dict(Counter(indices)))
                for i in range(max(indices)+1):
                    new.add(key+"__%d"%i)
    return new
            
def generatePermutators(stringSet):
    anonStr = {}
    for string in stringSet:
        parts = string.split("__")
        if len(parts) > 1:
            result = "__".join(parts[:-1])
            if result not in anonStr:
                anonStr[result] = []
            anonStr[result].append(string)
    basicPerms = basicDenum(anonStr.keys())
    stochasticPerms = stochasticDenum(anonStr)    
    return basicPerms.union(stochasticPerms).union(stringSet).union(anonStr.keys())

shader_string_list = shader_strings()
chunkPath=r"E:\MHW\ChunkG0"
model_files = list(Path(chunkPath).rglob("*.mod3"))
material_names_compendium = generatePermutators(set(sum([mod3.parse_mod3(m)[2] for m in model_files],[]))).union(set(shader_string_list))
write_strings(material_names_compendium)


