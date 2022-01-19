# -*- coding: utf-8 -*-
"""Simple editor sample using CodeEditor package.

Copyright (c) 2019 lileilei. <hustlei@sina.cn>
"""

import sys

sys.path.append("..")
from PyQt5.QtWidgets import QApplication, QWidget, QSplitter, QVBoxLayout, QHBoxLayout, QPushButton, QFileDialog
from CodeEditor import Editor

app = QApplication(sys.argv)
win = QWidget()
# create editor
edt = Editor()
text = """#include <stdio.h>
int main()
{
    // 这是一首思念家乡的诗
    printf("床前明月光，");
    printf("疑是地上霜。");
    printf("举头望明月，");
    printf("低头思故乡。"); 
    return 0;    
}"""
edt.setText(text)
edt.setLanguage("CPP")

# setting widgets
settingPanel = edt.settings.settingPanel()
btcancel = QPushButton("Cancel")
btcancel.clicked.connect(edt.settings.cancel)
btok = QPushButton("Apply")
btok.clicked.connect(edt.settings.apply)
# ok cancel button
btnLayout = QHBoxLayout()
btnLayout.addWidget(btcancel)
btnLayout.addWidget(btok)
settingDialogLayout = QVBoxLayout()
settingDialogLayout.addWidget(edt.settings.settingPanel())
settingDialogLayout.addLayout(btnLayout)
# setting dialog
settingDialog = QWidget(win)
settingDialog.setLayout(settingDialogLayout)
# container for editor and setting dialog
splitter = QSplitter()
splitter.addWidget(edt)
splitter.addWidget(settingDialog)
# toolbar
butopen = QPushButton("open")
def openfile():
    dialog, _ = QFileDialog.getOpenFileName()
    if dialog:
        edt.load(dialog)
butopen.clicked.connect(openfile)
butfind = QPushButton("find")
butfind.clicked.connect(edt.find)
butreplace = QPushButton("replace")
butreplace.clicked.connect(edt.replace)
toolbar = QHBoxLayout()
toolbar.addWidget(butopen)
toolbar.addWidget(butfind)
toolbar.addWidget(butreplace)
toolbar.addStretch(1)
# main layout
mainLayout = QVBoxLayout()
mainLayout.addLayout(toolbar)
mainLayout.addWidget(splitter)
win.setLayout(mainLayout)

win.setMinimumWidth(800)
win.show()
sys.exit(app.exec_())
