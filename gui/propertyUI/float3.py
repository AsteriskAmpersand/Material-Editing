# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'float3.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(600, 38)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.valName = QtWidgets.QLabel(Form)
        self.valName.setMinimumSize(QtCore.QSize(225, 0))
        self.valName.setObjectName("valName")
        self.horizontalLayout.addWidget(self.valName)
        self.v0 = QtWidgets.QDoubleSpinBox(Form)
        self.v0.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.v0.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.v0.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToNearestValue)
        self.v0.setProperty("showGroupSeparator", False)
        self.v0.setMinimum(-1e+97)
        self.v0.setMaximum(1e+51)
        self.v0
        self.v0.setProperty("value", 0.0)
        self.v0.setObjectName("v0")
        self.horizontalLayout.addWidget(self.v0)
        self.v1 = QtWidgets.QDoubleSpinBox(Form)
        self.v1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.v1.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.v1.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToNearestValue)
        self.v1.setProperty("showGroupSeparator", False)
        self.v1.setMinimum(-1e+97)
        self.v1.setMaximum(1e+51)
        self.v1
        self.v1.setProperty("value", 0.0)
        self.v1.setObjectName("v1")
        self.horizontalLayout.addWidget(self.v1)
        self.v2 = QtWidgets.QDoubleSpinBox(Form)
        self.v2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.v2.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.v2.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToNearestValue)
        self.v2.setProperty("showGroupSeparator", False)
        self.v2.setMinimum(-1e+97)
        self.v2.setMaximum(1e+51)
        self.v2
        self.v2.setProperty("value", 0.0)
        self.v2.setObjectName("v2")
        self.horizontalLayout.addWidget(self.v2)

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
