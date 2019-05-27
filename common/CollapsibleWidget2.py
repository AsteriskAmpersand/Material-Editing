# -*- coding: utf-8 -*-
"""
Created on Sat May 25 17:39:11 2019

@author: AsteriskAmpersand
"""

__author__ = 'Caroline Beyne'

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import pyqtSignal

class QCollapsibleWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QFrame.__init__(self, parent=parent)
        self._main_v_layout = QtWidgets.QVBoxLayout(self)
    def addSection(self, title, widget):
        newFrame = CollapsibleFrame(self, title)
        newFrame.addWidget(widget)

class CollapsibleFrame(QtWidgets.QWidget):
    def __init__(self, parent=None, title=None):
        QtWidgets.QFrame.__init__(self, parent=parent)

        self._is_collasped = True
        self._title_frame = None
        self._content, self._content_layout = (None, None)

        self._main_v_layout = QtWidgets.QVBoxLayout(self)
        self._main_v_layout.addWidget(self.initTitleFrame(title, self._is_collasped))
        self._main_v_layout.addWidget(self.initContent(self._is_collasped))

        self.initCollapsable()

    def initTitleFrame(self, title, collapsed):
        self._title_frame = self.TitleFrame(title=title, collapsed=collapsed)

        return self._title_frame

    def initContent(self, collapsed):
        self._content = QtWidgets.QWidget()
        self._content_layout = QtWidgets.QVBoxLayout()

        self._content.setLayout(self._content_layout)
        self._content.setVisible(not collapsed)

        return self._content

    def addWidget(self, widget):
        self._content_layout.addWidget(widget)

    def initCollapsable(self):
        self._title_frame.clicked.connect(self.toggleCollapsed)

    def toggleCollapsed(self):
        self._content.setVisible(self._is_collasped)
        self._is_collasped = not self._is_collasped
        self._title_frame._arrow.setArrow(int(self._is_collasped))

    ############################
    #           TITLE          #
    ############################
    class TitleFrame(QtWidgets.QFrame):
        clicked = pyqtSignal()
        def __init__(self, parent=None, title="", collapsed=False):
            QtWidgets.QFrame.__init__(self, parent=parent)

            self.setMinimumHeight(24)
            self.move(QtCore.QPoint(24, 0))
            self.setStyleSheet("border:1px solid rgb(41, 41, 41); ")

            self._hlayout = QtWidgets.QHBoxLayout(self)
            self._hlayout.setContentsMargins(0, 0, 0, 0)
            self._hlayout.setSpacing(0)

            self._arrow = None
            self._title = None

            self._hlayout.addWidget(self.initArrow(collapsed))
            self._hlayout.addWidget(self.initTitle(title))

        def initArrow(self, collapsed):
            self._arrow = CollapsibleFrame.Arrow(collapsed=collapsed)
            self._arrow.setStyleSheet("border:0px")

            return self._arrow

        def initTitle(self, title=None):
            self._title = QtWidgets.QLabel(title)
            self._title.setMinimumHeight(24)
            self._title.move(QtCore.QPoint(24, 0))
            self._title.setStyleSheet("border:0px")

            return self._title

        def mousePressEvent(self, event):
            self.clicked.emit()
            return super(CollapsibleFrame.TitleFrame, self).mousePressEvent(event)


    #############################
    #           ARROW           #
    #############################
    class Arrow(QtWidgets.QFrame):
        def __init__(self, parent=None, collapsed=False):
            QtWidgets.QFrame.__init__(self, parent=parent)

            self.setMaximumSize(24, 24)

            # horizontal == 0
            self._arrow_horizontal = (QtCore.QPointF(7.0, 8.0), QtCore.QPointF(17.0, 8.0), QtCore.QPointF(12.0, 13.0))
            # vertical == 1
            self._arrow_vertical = (QtCore.QPointF(8.0, 7.0), QtCore.QPointF(13.0, 12.0), QtCore.QPointF(8.0, 17.0))
            # arrow
            self._arrow = None
            self.setArrow(int(collapsed))

        def setArrow(self, arrow_dir):
            if arrow_dir:
                self._arrow = self._arrow_vertical
            else:
                self._arrow = self._arrow_horizontal

        def paintEvent(self, event):
            painter = QtWidgets.QPainter()
            painter.begin(self)
            painter.setBrush(QtWidgets.QColor(192, 192, 192))
            painter.setPen(QtWidgets.QColor(64, 64, 64))
            painter.drawPolygon(*self._arrow)
            painter.end()
            
            
from PyQt5 import QtWidgets, QtCore
import sys

if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)

    win = QtWidgets.QMainWindow()
    w = QtWidgets.QWidget()
    w.setMinimumWidth(350)
    win.setCentralWidget(w)
    l = QtWidgets.QVBoxLayout()
    l.setSpacing(0)
    l.setAlignment(QtCore.Qt.AlignTop)
    w.setLayout(l)

    t = CollapsibleFrame(title="Buttons")
    t.addWidget(QtWidgets.QPushButton('a'))
    t.addWidget(QtWidgets.QPushButton('b'))
    t.addWidget(QtWidgets.QPushButton('c'))

    f = CollapsibleFrame(title="TableWidget")
    rows, cols = (6, 3)
    data = {'col1': ['1', '2', '3', '4', '5', '6'],
            'col2': ['7', '8', '9', '10', '11', '12'],
            'col3': ['13', '14', '15', '16', '17', '18']}
    table = QtWidgets.QTableWidget(rows, cols)
    headers = []
    for n, key in enumerate(sorted(data.keys())):
        headers.append(key)
        for m, item in enumerate(data[key]):
            newitem = QtWidgets.QTableWidgetItem(item)
            table.setItem(m, n, newitem)
    table.setHorizontalHeaderLabels(headers)
    f.addWidget(table)

    l.addWidget(t)
    l.addWidget(f)

    win.show()
    win.raise_()
    sys.exit(app.exec_())