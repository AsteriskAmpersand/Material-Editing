from pathlib import Path
import os
 
dirpath = os.getcwd()
for uiFile in Path(dirpath).rglob("*.py"):
    if "cleanup" not in str(uiFile):
        with open(uiFile,"r") as uiF:
            data = uiF.read()
        print(len(data))
        data = data.replace(".setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)","")
        data = data.replace(".setStepType(QtWidgets.QAbstractSpinBox.AdaptiveDecimalStepType)","")
        print(len(data))
        with open(uiFile,"w") as uiF:
            uiF.write(data)