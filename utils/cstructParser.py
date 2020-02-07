from itertools import chain

def parseClass(line, shaderListing):
    classDeclaration = "class %s(EPyCStruct):"
    #containerDeclaration = "class %s(Mod3Container):"
    #containerForm = "Mod3Class = %s"
    #containerCount = "baseCount = %s"
    typeStart = "\tfields = OrderedDict(["
    typeEnd = "\t])"
    
    line = line.replace("\n","").replace("\r","").replace("row_major ","").lstrip()
    code,comment = line.split("//")+([''] if "//" not in line else [])
    data = ""
    if "struct" in code:
        className = code.replace("struct","").replace(" ","").replace("{","")
        data = classDeclaration%className+"\n"+typeStart
        shaderListing.append(className)
    elif "}" in code:
        data = typeEnd
    elif code.replace(" ","") and code.replace(" ","")!="{":        
        typing, varname = code.lstrip().rstrip().replace(";","").split(" ")
        if "[" in varname:
            varname, arrCount = varname.replace("]","").split("[")
            typing += "[%s]"%arrCount
        data = '\t\t("%s", "%s"),'%(varname,typing.replace("bool","bbool"))
    return data

def parseStructures(inf,outf):
    parsed = []
    shaderListing = []
    
    shaderListStart = "shaderListing = 	{"
    shaderListEnd = "}"
    
    header = """from collections import OrderedDict
from common.crc import CrcJamcrc
from common.Cstruct import ExtendedPyCStruct as EPyCStruct
from common.Cstruct import Mod3Container, Mod3Collection

if __name__=="__main__":
    import sys, inspect
    fieldTypes = set()
    for name, obj in inspect.getmembers(sys.modules[__name__]):
        if inspect.isclass(obj):
            try:
                fieldTypes.union(set(obj.fields.values()))
            except:
                pass
    print(fieldTypes)"""

    footer = """
generalhash =  lambda x:  CrcJamcrc.calc(x.encode())
shaderTranslation = {generalhash(key) & 0xFFFFF:shaderListing[key] for key in shaderListing}"""
    
    with open(inf,"r") as infile:
        linebuffer = iter(infile)
        for line in linebuffer:
            data = parseClass(line,shaderListing)
            parsed.append(data)
        declarations = "\n".join(parsed)
    
    
    mapping = shaderListStart+"\n".join(['"%s":%s,'%(classing,classing) for classing in shaderListing])+shaderListEnd
    
    sections = [header,
                declarations,
                mapping,
                footer]
    
    with open(outf,"w") as outfile:
        for section in sections:
            outfile.write(section+"\n")
if __name__ in "__main__":
    sin = r"G:\Tools\MaterialEditor\MaterialEditing\utils\mhwib_structures_generated_rajang.txt"
    sout = r"G:\Tools\MaterialEditor\MaterialEditing\mrl3\shadertype.py"
    parseStructures(sin,sout)