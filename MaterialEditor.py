# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 16:23:21 2019

@author: AsteriskAmpersand
"""
import os
import sys
import Mod3
import Mrl3
import MaterialListing
import re
import traceback
import copy
import ShaderListing
from collections import OrderedDict
remove_extension = lambda path: os.path.splitext(path)[0]

class Material_Library_File():
    def __init__(self, path):
        self.path = path
        self.header, self.textures, self.materials = Mrl3.parse_mrl3(path)
        
    def index(self, materialID, *args):
        for i,m in enumerate(self.materials):
            if m.skinid == materialID:
                return i
        if len(args)<1:
            raise ValueError("Id not in File")
        else:
            return args[0]

class Material_Library():
    def __init__(self, path = None):
        self.library = OrderedDict()
        if path is not None:
            self.parse_library(path)
        
    def add(self, path):
        if os.path.splitext(path)[1] != '.mrl3':
            raise ValueError("Not a Materials File")
        else:
            self.library[remove_extension(os.path.basename(path))]=Material_Library_File(path)
    
    def remove(self, path):
        if isinstance(path,int):
            path = list(self.library.keys())[path]
        else:
            path = remove_extension(os.path.basename(path))
        self.library.pop(path,None)
        
    def parse_library(self, path):
        infile = open(path, 'r')
        for line in infile:
            self.add(line.replace('\n',''))
    
    def save_to_file(self, path = ".\MaterialLibrary.lib"):
        outfile = open(path,'w')
        for mlf in self.library.values():
            outfile.write(mlf.path+'\n')
        outfile.close()
        
    def status(self):
        print("Files in Library:")
        for i, key in enumerate(self.library):
            print("\t%d. %s"%(i, key))
            for j, m in enumerate(self.library[key].materials):
                print("\t\t%d. %d"%(j, m.materialHash))
                
    def info(self, path, material = None, encyclopaedia = None):
        if isinstance(path,int):
            path = list(self.library.keys())[path]
        else:                
            path = os.path.basename(path)
            if "mrl3" in path:
                path = remove_extension(path)
        if material is None:
            print(path+':')
            for j, m in enumerate(self.library[path].materials):
                print("\t%d. %d"%(j, m.materialHash)),
                if encyclopaedia is not None:
                    try:
                        for string in encyclopaedia[m.materialHash]:
                            print("\t\t%s"%string)
                    except:
                        print("\t\tNo entry Found")
                else:
                    print()
        else:
            m = self.library[path].materials[material]
            print("\t%d. %d"%(material, m.materialHash)),
            if encyclopaedia is not None:
                try:
                    for string in encyclopaedia[m.materialHash]:
                        print("\t\t%s"%string)
                except:
                    print("\t\tNo entry Found")
            else:
                print()   
        return            
        
        
class Material_File():
    def __init__(self, base = None):
        if base == None:
            self.header, self.textures, self.materials =  Mrl3.Header(), [], []
        else:
            self.header, self.textures, self.materials =  Mrl3.parse_mrl3(base)
            
    def status(self):
        print("TextureList:")
        for i, t in enumerate(self.textures):
            print("\t%d. %s"%(i,t.path))
        print("MaterialList:")
        for i,  m in enumerate(self.materials):
            print("\t%d. %d"%(i,m.materialHash))

    def add_texture(self, texture):
        if isinstance(texture, str):
            newtex = Mrl3.Texture()
            newtex.path = texture
            texture = newtex
        self.textures.append(copy.deepcopy(texture))
    
    def add_library(self, materials):
        for material in materials:
            self.add_material(material)  
        for i in reversed(range(len(self.materials))):
            if self.materials[i].materialHash in self.materials[:i]:
                self.remove_material(i)                
    
    def add_material(self, material):
        self.materials.append(copy.deepcopy(material))
        
    def remove_material(self, index):
        self.materials.pop(index)
    
    def remove_texture(self, index):
        #ACTUALLY CLEAN REFERENCES FFS
        
        self.textures.pop(index)
        
    def rename_texture(self, texture, newpath):
        if isinstance(texture, int):
            textureName = self.textures[texture]
        else:
            textureName = texture
            texture = self.textures.index(texture)
        for material in self.materials:
            for i in range(len(material.texturePaths)):
                if material.texturePaths[i] == textureName:
                    material.texturePaths[i] == newpath
        self.textures[texture].path = newpath
        
    def mass_rename_texture(self, scheme):
        for texture in self.textures:
            if "Assets" not in texture.path:
                texture.path = scheme + "_" + texture.path.split('_')[-1]
        self.heuristic_texture_matching()
    
    def reindex_material(self, material, newidx, positions):
        print (newidx)
        print (positions)
        for i in positions:
            self.materials[material].textureArguments[i].texIdx = newidx+1
            self.materials[material].texturePaths[i] = self.textures[newidx].path
        return
    
    def transfer_id(self, fromix, toix):
        self.materials[toix].materialHash = self.materials[fromix].materialHash
        self.remove_material(fromix)
        
    def assign_hash(self, material, string_to_hash):
        self.materials[material].materialHash = MaterialListing.materialcrc(string_to_hash)
        
    def assign_general_hash(self, material, string_to_hash):
        self.materials[material].materialHash = MaterialListing.generalhash(string_to_hash)

    def leak_material_textures(self, material):
        if not isinstance(material, int):
            material = self.materials.index(material)
        self.materials[material].coalesce(self.textures)
        return
    
    def heuristic_texture_matching(self):
        for material in self.materials:
            material.heuristic_coalesce(self.textures)
    
    def export(self, pathname):
        open(pathname,"wb").write(Mrl3.serialize_mrl3(self.header, self.textures, self.materials))
        return
        
class Encyclopaedia():
    chunkPath=r"E:\MHW\Merged"
    def __init__(self, path=''):
        if path == '':
            path = self.chunkPath
#        self.nameCompendium, self.idCompendium, self.nameList, self.idList, _, _ = MaterialListing.create_dbs(path)
        self.nameEquiv, self.idEquiv = MaterialListing.sibling_compendium(self.nameCompendium, self.idCompendium)
    
    def __getitem__(self,value):
        if isinstance(value, str):
            return self.nameCompendium[value]
        elif isinstance(value, int):
            return self.idCompendium[value]
        elif isinstance(value, tuple):
            if isinstance(value[0], str):
                return self.nameEquiv[value]
            elif isinstance(value[0], int):
                return self.idEquiv[value]
        raise ValueError("Indexed access not recognised as legal type for Encyclopaedia")
        
    def status(self):
        print("%d Name Entries, %d ID Entries"%(len(self.nameCompendium),len(self.idCompendium)))
        
class CommandConsole():
    start = 0
    library = 1
    file_editing = 2
    encyclopaedia = 3
    
    def __init__(self):
        self.state = CommandConsole.start
        self.status = [None,Material_Library(),None,None,None]
        return
    def options(self):
        if self.state == 0:
            try:
                print (self.status[self.state].status())
            except:
                pass
            print("""Select Mode: Populate/Clear [L]ibrary,
Create/Edit MRL3 [F]ile, Access [E]ncyclopaedia, [P]ython Eval Loop, 
[H]elp, [Q]uit""")
        if self.state == 1:
            try:
                print (self.status[self.state].status())
            except:
                pass
            print("""[L]oad Library from File, [S]ave Library to File, [A]dd MRL3 File, [R]emove MRL3 File, 
Show [M]aterials on library file, [I]nfo on Material, [C]hange Mode, [H]elp, [Q]uit""")
        if self.state == 2:
            try:
                print (self.status[self.state].status())
            except:
                print("No MRL3 open currently")
            print("""Create [N]ew, [LL]oad Base from Library, [LF]oad Base from File, [E]export Material
Add [M]aterial from Library File, [AL]dd mrl3 from Library File,
Add [T]exture Path, Add [TL]exture from Library File,
[RM]emove Material, [RT]emove Texture, [RI]eindex Material's Texture,
[RN]ename Texture, [MRN]ass Rename Textures, 
[TM]ransplant Material ID, [GH]enerate ID from Truncated Hash, [GH*]enerate ID from Full Hash,
[U]pdate Texture List from Material, Heuristic Texture Paths [S]ummary,
[LMP]ist Material's Texture List Paths, [LMI]ist Material's Texture List IDx,
[H]elp, [C]hange Mode, [Q]uit
                  """)
        if self.state == 3:
            try:
                print (self.status[self.state].status())
            except:
                print("No Encyclopaedia file loaded")
            print("""[P]opulate from Merged Chunk Path, [CE]heck entry, [C]hange Mode, [H]elp, [Q]uit""")
    
    def change_state(self):
        self.state = 0
        return
    
    def create_encyclopaedia(self, path):
        if path != None:
            self.status[3]=Encyclopaedia(path)
        else:
            self.status[3]=Encyclopaedia()
        
    def create_file(self, *args):
        if len(args)<1:
            mrl3 = Material_File()
        else:
            mrl3 = Material_File(args[0])
        self.status[2] = mrl3
        
    def eval_loop(self):
        while (True):
            exec(input())
            
    def load_library(self, path):
        self.status[1] = Material_Library(path)
        
    def get_library_material(self, file, mat):
        if isinstance(file,int):
            file = list(self.status[1].library.keys())[file]
        self.status[self.state].add_material(self.status[1].library[file].materials[mat])
    
    def parse_command(self, command):
        for i, c in enumerate(command):
            try:
                k = int(c)
            except:
                k = c.replace('"','')
            command[i]=k
        if command[0]=='Q':
            sys.exit(0)
        if command[0]=='H':
            self.help_call()
            return
        if self.state == 0:
            if command[0] == 'P':
                try:
                    self.eval_loop()
                except:
                    pass
                return
            self.state = {'L':1,'F':2,'E':3}[command[0]]
            return
        elif command[0] == 'C':
            self.change_state()
            return
        elif self.state == 1:
            {'L':lambda: self.load_library(command[1]),
             'S':lambda: self.status[self.state].save_to_file(command[1]) if len(command)>1 else self.status[self.state].save_to_file(),
             'A':lambda: self.status[self.state].add(command[1]),'R':lambda: self.status[self.state].remove(command[1]),
             'M':lambda: self.status[self.state].info(command[1], encyclopaedia = self.status[3]),
             'I':lambda: self.status[self.state].info(command[1], command[2], encyclopaedia = self.status[3]),
             }[command[0]]()
        elif self.state == 2:
            {'N':lambda: self.create_file(), 
             'LL':lambda: self.create_file(self.status[1].library[list(self.status[1].library.keys())[command[1]]].path) if\
                 isinstance(command[1],int) else\
                 self.create_file(self.status[1].library[command[1]]),
             'LF':lambda: self.create_file(command[1]),
             'E':lambda: self.status[self.state].export(command[1]),
             'M':lambda: self.get_library_material(command[1], command[2]),
             'AL':lambda: self.status[self.state].add_library(list(self.status[1].library.values())[command[1]].materials) if \
                         isinstance(command[1],int) else \
                         self.status[self.state].add_library(self.status[1].library[command[1]].materials),
             'T':lambda: self.status[self.state].add_texture(command[1]),
             'TL':lambda:self.status[self.state].add_texture(self.status[1].library.values()[command[1]].textures[command[2]]) if \
                         isinstance(command[1],int) else \
                         self.status[self.state].add_texture(self.status[1].library[command[1]].textures[command[2]]),
             'RM':lambda: self.status[self.state].remove_material(command[1]),
             'RT':lambda: self.status[self.state].remove_texture(command[1]),
             'RN':lambda: self.status[self.state].rename_texture(command[1],command[2]),
             'MRN':lambda: self.status[self.state].mass_rename_texture(command[1]),
             'TM':lambda: self.status[self.state].transfer_id(command[1], command[2]),
             'GH':lambda: self.status[self.state].assign_hash(command[1], ' '.join(command[2:])),
             'GH*':lambda: self.status[self.state].assign_general_hash(command[1], ' '.join(command[2:])),
             'RI':lambda: self.status[self.state].reindex_material(command[1], command[2], command[3:]),
             'U':lambda: self.status[self.state].leak_material_textures(command[1]),
             'S':lambda: self.status[self.state].heuristic_texture_matching(),
             'LMP':lambda: [print("\t%i. %s"%(i,p)) for i,p in enumerate(self.status[self.state].materials[command[1]].texturePaths)],
             'LMI':lambda: [print("\t%i. %d"%(i,p.texIdx-1)) for i,p in enumerate(self.status[self.state].materials[command[1]].textureArguments)]
            }[command[0]]()
        elif self.state == 3:
            {'P':lambda: self.create_encyclopaedia(command[1] if len(command)>1 else None), 
             'CE':lambda: self.status[self.state][tuple(command[1:])] if \
                         len(command[1:])>0 else\
                         self.status[self.state][command[1]]
             }[command[0]]()
        return
    
    help_strings = {0:
        [
        "Populate/Clear [L]ibrary:\n\tSyntax: L\n\tExplanation: Enters library editing mode. Build libraries of commonly used files for quicker editing of mrl3 files.",
        "Create/Edit MRL3 [F]ile:\n\tSyntax: F\n\tExplanation: Enters MRL3 editing mode. Create or edit mrl3 file materials.",
        "Access [E]ncyclopaedia: \n\tSyntax: E\n\tExplanation: Allows populating the material encyclopaedia, required for information display on material names.",
        "[P]ython Eval Loop: \n\tSyntax: P\n\tExplanation: Enters a python eval loop to directly write python code against the created objects. Use at your own risk."
        ],
        1:
        [
        "[L]oad Library from File:\n\tSyntax: L file_path\n\tExplanation: Loads a previously exported material library from a file.",
        "[S]ave Library to File:\n\tSyntax: S file_path\n\tExplanation: Saves the current library to a file for future use.",
        "[A]dd MRL3 File:\n\tSyntax: A file_path\n\tExplanation: Adds an mrl3 file path to the current library.",
        "[R]emove MRL3 File:\n\tSyntax:R file_name|index\n\tExplanation: Removes the indicated mrl3 file from the current library.",
        "Show [M]aterials on library file:\n\tSyntax: M file_name|mrl3_index\n\tExplanation: List all the materials with candidate names on the MRL3.\n\tRequires a populated encyclopaedia.",
        "[I]nfo on Material:\n\tSyntax: M file_name|mrl3_index material_index\n\tExplanation: Lists all the candidate names for a material on the specified MRL3.\n\tRequires a populated encyclopaedia."
        ],
        2:
        [
        "[N]ew:\n\tSyntax: N\n\tExplanation: Creates a blank mrl3 (Except for the header)",
        "[LL]oad Base from Library:\n\tSyntax: LL file_name|index\n\tExplanation: Creates a copy of an mrl3 from the library. ",
        "[LF]oad Base from File:\n\tSyntax: LF path\n\tExplanation: Creates a copy of an mrl3 from the given path.",
        "[E]export Material:\n\tSyntax: E path\n\tExplanation: Exports the finalised mrl3.",
        "Add [M]aterial from Library File:\n\tSyntax: M file_name|index material_index\n\tExplanation: Adds a material to the mrl3 from the file specified in the library.",
        "[AL]dd mrl3 from Library File:\n\tSyntax: AL file_name|index\n\tExplanation: Copies the entire file and removes duplicates on the later entries."
        "Add [T]exture Path:\n\tSyntax: T path\n\tExplanation: Adds a texture path to the mrl3.",
        "Add [TL]exture from Library File:\n\tSyntax: TL file_name|index texture_index\n\tExplanation: Adds a texture path to the mrl3 from the file specified in the library.",
        "[RM]emove Material:\n\tSyntax: RM material_index\n\tExplanation: Removes the material_index-ith material from the mrl3.",
        "[RT]emove Texture:\n\tSyntax: RT texture_index\n\tExplanation: Removes the texture_index-ith texture path from the mrl3.",
        "[RN]ename Texture:\n\tSyntax: RN texture_index new_name\n\tExplanation: Renames a texture path (and propagates the new name to all matches inside materials).",
        "[MRN]ass Rename Textures:\n\tSyntax: MRN base_path_files\n\tExplanation: Renames all textures in the mrl3 which are not in Assets to base_path_file+'_'+map_type. Will perform a summarization after renaming.",
        "[TM]ransplant Material ID:\n\tSyntax: TM from_index to_index\n\tExplanation: Transfers the material hash from one material to another and then drops the original material.",
        "[GH]enerate Hash:\n\tSyntax: GH material_index material_name_to_hash\n\tExplanation: Assigns the hash of the passed string to the material id linking the material to the mod3 name."
        "[GH*]enerate ID from Full Hash:\n\tSyntax: GH material_index material_name_to_hash\n\tExplanation: Assigns the hash of the passed string to the material id linking the material to the mod3 name."
        "[RI]eindex Material's Texture:\n\tSyntax: RI material_index new_texIdx position1 [position2..n]\n\tExplanation: Replaces the positions given in the material with the new idx.",
        "[U]pdate Texture List from Material:\n\tSyntax: U material_id\n\tExplanation: Adds a materials original texture names to the texture path list on the mrl3.",
        "Heuristic Texture Paths [S]ummary:\n\tSyntax: S\n\tExplanation: Attempts to summarise all of the materials original path names (Grouping all BML paths into 1 but keeping Assets paths unique).",
        "[LMP]ist Material's Texture List Paths:\n\tSyntax: LMP material_index\n\tExplanation: Lists the material's original texture paths.",
        "[LMI]ist Material's Texture List IDx:\n\tSyntax: LMI material_index\n\tExplanation: Lists the material's texture path texIdx."
        ],
        3:
        [
        "[P]opulate from Merged Chunk Path:\n\tSyntax: P merged_chunk_root\n\tExplanation: Generates an encyclopaedia of texture names and ids for information functions."
        ]}
        
    def help_call(self):
        print("================================================")
        for s in self.help_strings[self.state]:
            print(s)
            print()
        print("================================================")
        
if __name__ == "__main__":
    cc = CommandConsole()
    while(True):
        cc.options()
        try:
            command = re.findall(r'(?:[^\s,"]|"(?:\\.|[^"])*")+', input())
            cc.parse_command(command)
        except Exception as exc:
            print (traceback.format_exc())
            print (exc)
            