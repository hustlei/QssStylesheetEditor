# -*- coding: utf-8 -*-
"""config dialog

Copyright (c) 2019 lileilei <hustlei@sina.cn>
"""

from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QVBoxLayout, QListWidget, QStackedWidget, QGroupBox,
                             QLabel, QLineEdit, QSpinBox, QPushButton, QComboBox, QFormLayout)
from PyQt5.QtCore import Qt

class ConfDialog(QWidget):
    def __init__(self, mainwin):
        super(ConfDialog, self).__init__()
        self.setWindowFlags(Qt.Tool|Qt.WindowStaysOnTopHint)
        self.win=mainwin
        self.initUI()

    def initUI(self):
        mainLayout=QVBoxLayout()
        layH1=QHBoxLayout()
        layH2=QHBoxLayout()
        self.conflist=QListWidget()
        self.stack=QStackedWidget()
        layH1.addWidget(self.conflist)
        layH1.addWidget(self.stack)
        self.okbtn=QPushButton(self.tr("OK"))
        self.cancelbtn=QPushButton(self.tr("Cancel"))
        layH2.addStretch(1)
        layH2.addWidget(self.okbtn)
        layH2.addWidget(self.cancelbtn)
        mainLayout.addLayout(layH1)
        mainLayout.addLayout(layH2)
        self.setLayout(mainLayout)

        #list
        self.conflist.addItem(self.tr("General"))
        self.conflist.addItem(self.tr("Editor"))
        self.conflist.setMaximumWidth(150)
        #general
        w=QWidget()
        layw=QVBoxLayout()

        g=QGroupBox(self.tr("General"))
        glayout=QFormLayout()
        label1=QLabel(self.tr("select UI language:"))
        combo1=QComboBox()
        combo1.addItems(self.findLang())
        combo1.setMinimumWidth(150)
        label2=QLabel(self.tr("Number of recent files:"))
        spin1=QSpinBox()
        spin1.setMinimum(1)
        spin1.setMaximum(30)
        label3 = QLabel(self.tr("Font Size:"))
        spin2 = QSpinBox()
        spin2.setMinimum(1)
        spin2.setMaximum(30)

        glayout.addRow(label1,combo1)
        glayout.addRow(label2,spin1)
        glayout.addRow(label3,spin2)
        g.setLayout(glayout)

        layw.addWidget(g)
        layw.addStretch(1)
        w.setLayout(layw)
        self.stack.addWidget(w)

        #editor
        from ui.editor.settings import EditorSettings
        w=EditorSettings(self.win.editor)
        self.stack.addWidget(w)

        self.cancelbtn.clicked.connect(self.close)
        self.conflist.currentRowChanged.connect(self.stack.setCurrentIndex)

    def findLang(self):
        langs=["English"]
        return langs
