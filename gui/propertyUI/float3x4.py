# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'float3x4.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(727, 86)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.valName = QtWidgets.QLabel(Form)
        self.valName.setMinimumSize(QtCore.QSize(225, 0))
        self.valName.setObjectName("valName")
        self.horizontalLayout.addWidget(self.valName)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.v00 = QtWidgets.QDoubleSpinBox(self.frame_2)
        self.v00.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.v00.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.v00.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToNearestValue)
        self.v00.setProperty("showGroupSeparator", False)
        self.v00.setMinimum(-1e+97)
        self.v00.setMaximum(1e+51)
        self.v00
        self.v00.setProperty("value", 0.0)
        self.v00.setObjectName("v00")
        self.horizontalLayout_2.addWidget(self.v00)
        self.v01 = QtWidgets.QDoubleSpinBox(self.frame_2)
        self.v01.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.v01.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.v01.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToNearestValue)
        self.v01.setProperty("showGroupSeparator", False)
        self.v01.setMinimum(-1e+97)
        self.v01.setMaximum(1e+51)
        self.v01
        self.v01.setProperty("value", 0.0)
        self.v01.setObjectName("v01")
        self.horizontalLayout_2.addWidget(self.v01)
        self.v02 = QtWidgets.QDoubleSpinBox(self.frame_2)
        self.v02.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.v02.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.v02.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToNearestValue)
        self.v02.setProperty("showGroupSeparator", False)
        self.v02.setMinimum(-1e+97)
        self.v02.setMaximum(1e+51)
        self.v02
        self.v02.setProperty("value", 0.0)
        self.v02.setObjectName("v02")
        self.horizontalLayout_2.addWidget(self.v02)
        self.v03 = QtWidgets.QDoubleSpinBox(self.frame_2)
        self.v03.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.v03.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.v03.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToNearestValue)
        self.v03.setProperty("showGroupSeparator", False)
        self.v03.setMinimum(-1e+97)
        self.v03.setMaximum(1e+51)
        self.v03
        self.v03.setProperty("value", 0.0)
        self.v03.setObjectName("v03")
        self.horizontalLayout_2.addWidget(self.v03)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.v10 = QtWidgets.QDoubleSpinBox(self.frame_3)
        self.v10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.v10.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.v10.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToNearestValue)
        self.v10.setProperty("showGroupSeparator", False)
        self.v10.setMinimum(-1e+97)
        self.v10.setMaximum(1e+51)
        self.v10
        self.v10.setProperty("value", 0.0)
        self.v10.setObjectName("v10")
        self.horizontalLayout_3.addWidget(self.v10)
        self.v11 = QtWidgets.QDoubleSpinBox(self.frame_3)
        self.v11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.v11.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.v11.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToNearestValue)
        self.v11.setProperty("showGroupSeparator", False)
        self.v11.setMinimum(-1e+97)
        self.v11.setMaximum(1e+51)
        self.v11
        self.v11.setProperty("value", 0.0)
        self.v11.setObjectName("v11")
        self.horizontalLayout_3.addWidget(self.v11)
        self.v12 = QtWidgets.QDoubleSpinBox(self.frame_3)
        self.v12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.v12.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.v12.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToNearestValue)
        self.v12.setProperty("showGroupSeparator", False)
        self.v12.setMinimum(-1e+97)
        self.v12.setMaximum(1e+51)
        self.v12
        self.v12.setProperty("value", 0.0)
        self.v12.setObjectName("v12")
        self.horizontalLayout_3.addWidget(self.v12)
        self.v13 = QtWidgets.QDoubleSpinBox(self.frame_3)
        self.v13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.v13.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.v13.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToNearestValue)
        self.v13.setProperty("showGroupSeparator", False)
        self.v13.setMinimum(-1e+97)
        self.v13.setMaximum(1e+51)
        self.v13
        self.v13.setProperty("value", 0.0)
        self.v13.setObjectName("v13")
        self.horizontalLayout_3.addWidget(self.v13)
        self.verticalLayout.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.v20 = QtWidgets.QDoubleSpinBox(self.frame_4)
        self.v20.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.v20.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.v20.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToNearestValue)
        self.v20.setProperty("showGroupSeparator", False)
        self.v20.setMinimum(-1e+97)
        self.v20.setMaximum(1e+51)
        self.v20
        self.v20.setProperty("value", 0.0)
        self.v20.setObjectName("v20")
        self.horizontalLayout_4.addWidget(self.v20)
        self.v21 = QtWidgets.QDoubleSpinBox(self.frame_4)
        self.v21.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.v21.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.v21.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToNearestValue)
        self.v21.setProperty("showGroupSeparator", False)
        self.v21.setMinimum(-1e+97)
        self.v21.setMaximum(1e+51)
        self.v21
        self.v21.setProperty("value", 0.0)
        self.v21.setObjectName("v21")
        self.horizontalLayout_4.addWidget(self.v21)
        self.v22 = QtWidgets.QDoubleSpinBox(self.frame_4)
        self.v22.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.v22.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.v22.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToNearestValue)
        self.v22.setProperty("showGroupSeparator", False)
        self.v22.setMinimum(-1e+97)
        self.v22.setMaximum(1e+51)
        self.v22
        self.v22.setProperty("value", 0.0)
        self.v22.setObjectName("v22")
        self.horizontalLayout_4.addWidget(self.v22)
        self.v23 = QtWidgets.QDoubleSpinBox(self.frame_4)
        self.v23.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.v23.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.v23.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToNearestValue)
        self.v23.setProperty("showGroupSeparator", False)
        self.v23.setMinimum(-1e+97)
        self.v23.setMaximum(1e+51)
        self.v23
        self.v23.setProperty("value", 0.0)
        self.v23.setObjectName("v23")
        self.horizontalLayout_4.addWidget(self.v23)
        self.verticalLayout.addWidget(self.frame_4)
        self.horizontalLayout.addWidget(self.frame)
        for i,j in [(i,j) for i in range(3) for j in range(4)]:
            getattr(self,"v%d%d"%(i,j)).decimals = 4
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.valName.setText(_translate("Form", "fWaterCustomRefractionTangentNormalBlend"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
