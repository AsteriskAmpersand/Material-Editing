# -*- coding: utf-8 -*-
"""
Created on Sat May 25 03:28:08 2019

@author: AsteriskAmpersand
"""

import sys
from PyQt5.QtWidgets import (QPushButton, QDialog, QTreeWidget,
                             QTreeWidgetItem, QVBoxLayout,
                             QHBoxLayout, QFrame, QLabel,
                             QApplication, QWidget)

class SectionExpandButton(QPushButton):
    """a QPushbutton that can expand or collapse its section
    """
    def __init__(self, item, text = "", parent = None):
        super().__init__(text, parent)
        self.section = item
        self.clicked.connect(self.on_clicked)
        self.setStyleSheet("Text-align:left")

    def on_clicked(self):
        """toggle expand/collapse of section by clicking
        """
        if self.section.isExpanded():
            self.section.setExpanded(False)
        else:
            self.section.setExpanded(True)


class QCollapsibleWidget(QWidget):
    """a dialog to which collapsible sections can be added;
    subclass and reimplement define_sections() to define sections and
        add them as (title, widget) tuples to self.sections
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tree = QTreeWidget()
        self.tree.setHeaderHidden(True)
        self.tree.setVerticalScrollMode(QTreeWidget.ScrollPerPixel)
        layout = QVBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(0)
        layout.addWidget(self.tree)
        self.setLayout(layout)
        self.tree.setIndentation(0)

    def addSection(self, title, widget):
        """adds a collapsible sections for every 
        (title, widget) tuple in self.sections
        """
        button1 = self.addButton(title)
        section1 = self.addWidget(button1, widget)
        button1.addChild(section1)

    def addButton(self, title):
        """creates a QTreeWidgetItem containing a button 
        to expand or collapse its section
        """
        item = QTreeWidgetItem()
        self.tree.addTopLevelItem(item)
        self.tree.setItemWidget(item, 0, SectionExpandButton(item, text = title))
        return item

    def addWidget(self, button, widget):
        """creates a QWidgetItem containing the widget,
        as child of the button-QWidgetItem
        """
        section = QTreeWidgetItem(button)
        section.setDisabled(True)
        self.tree.setItemWidget(section, 0, widget)
        return section


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QCollapsibleWidget()
    l = QLabel()
    l.setText("Test2")
    window.addSection("Test",l)
    window.show()
    sys.exit(app.exec_())