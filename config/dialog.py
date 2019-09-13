# -*- coding: utf-8 -*-
"""config dialog

Copyright (c) 2019 lileilei <hustlei@sina.cn>
"""

from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QVBoxLayout, QListWidget, QStackedWidget, QGroupBox,
                             QLabel, QLineEdit, QSpinBox, QPushButton, QComboBox)
from PyQt5.QtCore import Qt

class ConfDialog(QWidget):
    def __init__(self):
        super(ConfDialog, self).__init__()
        self.setWindowFlags(Qt.Tool|Qt.WindowStaysOnTopHint)
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

        g=QGroupBox(self.tr("UI Language"))
        glayout=QHBoxLayout()
        label1=QLabel(self.tr("select language:"))
        combo1=QComboBox()
        combo1.addItems(self.findLang())
        combo1.setMinimumWidth(150)
        glayout.addWidget(label1)
        glayout.addWidget(combo1)
        g.setLayout(glayout)
        layw.addWidget(g)

        g=QGroupBox(self.tr("File"))
        glayout=QHBoxLayout()
        label1=QLabel(self.tr("Number of recent files:"))
        spin1=QSpinBox()
        spin1.setMinimum(1)
        spin1.setMaximum(30)
        glayout.addWidget(label1)
        glayout.addWidget(spin1)
        g.setLayout(glayout)
        layw.addWidget(g)

        layw.addStretch(1)
        w.setLayout(layw)
        self.stack.addWidget(w)

        #editor
        w=QWidget()
        layw=QVBoxLayout()

        g=QGroupBox(self.tr("Editor"))
        glayout=QHBoxLayout()
        label1=QLabel(self.tr("Font Size:"))
        spin1=QSpinBox()
        spin1.setMinimum(1)
        spin1.setMaximum(30)
        glayout.addWidget(label1)
        glayout.addWidget(spin1)
        g.setLayout(glayout)
        layw.addWidget(g)

        layw.addStretch(1)
        w.setLayout(layw)
        self.stack.addWidget(w)

    def findLang(self):
        langs=["English"]
        return langs
