from itertools import chain

def _parseSimpleClass(line, shaderListing):
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
    return data+"\n"

def find_offsets(haystack, needle):
    """
    Find the start of all (possibly-overlapping) instances of needle in haystack
    """
    offs = -1
    while True:
        offs = haystack.find(needle, offs+1)
        if offs == -1:
            break
        else:
            yield offs

def parseSimpleClass(subbuffer,shaderListing):
    data = ""
    for line in subbuffer:
        data += _parseSimpleClass(line,shaderListing)
    return data

def parseCompoundClass(buffer, shaderListing):
    line = buffer[0]
    line = line.replace("\n","").replace("\r","").replace("row_major ","").lstrip()
    code,comment = line.split("//")+([''] if "//" not in line else [])
    superClass = code.replace("struct","").replace(" ","").replace("{","")
    shaderListing.append(superClass)
    
    data = ""
    spacing = ["\t"," ","\n","\r"]
    block = ''.join(buffer[1:])
    collectionClasses = []
    collectionCounts = []
    structMarker = find_offsets(block,"struct")
    blockStart = find_offsets(block,"{")
    blockEnd = find_offsets(block,"}")
    for classNameIx,blockStart,blockEnd in zip(structMarker,blockStart,blockEnd):
        className = block[classNameIx:blockStart].replace("struct","")
        classCount = block[blockEnd:blockEnd+block[blockEnd:].index(";")]
        #print(block[blockEnd:].index(";"))
        classCount = classCount[classCount.index("[")+1:classCount.index("]")]
        for space in spacing: className = className.replace(space,"")
        subbuffer = [line+"\n" for line in block[classNameIx:blockEnd+1].split("\n")]
        data += parseSimpleClass(subbuffer,shaderListing)        
        if "//" in className:
            className = className[:className.index("//")]
        collectionClasses.append(className)
        collectionCounts.append(classCount)
    if len(collectionClasses) > 1:     
        typing = "Mod3Collection"
    else:
        typing = "Mod3Container"
        collectionClasses = collectionClasses[0]
        collectionCounts = collectionCounts[0]
    data+="class %s (%s):\n"%(superClass,typing)
    data+="\tMod3Classes = %s\n"%(str(collectionClasses))
    data+="\tMod3Counts = %s\n"%(str(collectionCounts))
    data += "\n"
    return data

def parseBlock(line,linebuffer,shaderListing):
    if "struct" not in line:
        return line.replace("//","#").strip()
    if "struct" in line:
        compound = False
        subbuffer = [line]
        count = "{" in line
        while not count:
            nline = next(linebuffer)
            subbuffer.append(nline)
            count = "{" in nline
        while count:
            nline = next(linebuffer)
            subbuffer.append(nline)
            count += "{" in nline
            count -= "}" in nline
            if "struct" in nline:
                compound = True
        if not compound:
            data = parseSimpleClass(subbuffer,shaderListing)
        else:
            data = parseCompoundClass(subbuffer,shaderListing)
    return data

def parseBuffer(linebuffer,parsed,shaderListing):
    for line in linebuffer:
        data = parseBlock(line,linebuffer,shaderListing)
        if data is None:
            raise
        parsed.append(data)
    

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
        parseBuffer(linebuffer, parsed, shaderListing)
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
    sin = r"G:\Tools\MaterialEditor\MaterialEditing\utils\mhwib_structures_generated.txt"
    sout = r"G:\Tools\MaterialEditor\MaterialEditing\mrl3\shadertype.py"
    parseStructures(sin,sout)