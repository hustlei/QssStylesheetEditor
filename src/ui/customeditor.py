# -*- coding:utf-8 -*-
"""editor for custom widget preview panel
"""
import os
import sys
from os import path
from importlib import import_module, reload
from CodeEditor import Editor
from PyQt5.Qsci import QsciLexer, QsciLexerPython
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox, QWidget, QFileDialog
from data import cache


class SrcEditor(Editor):
    def __init__(self):
        super().__init__()
        self.dir = path.join(path.dirname(__file__), "../data/custompreview")
        self.file = path.join(self.dir, "__init__.py")
        self.cachedir = path.join(self.dir, "../cache")
        self.cachefile = path.join(self.cachedir, "custom.py")
        self.setLexer(QsciLexerPython(self))
        self.load(self.file)
        self.custom = None

    def open(self):
        file, _ = QFileDialog.getOpenFileName(self, self.tr("Open File"), '', "Python(*.py);;all(*.*)")
        if os.path.exists(file):
            self.file = file
            ok = self.load(self.file)
            if not ok:
                QMessageBox.information(self, "Error", self.tr("load file failed"), QMessageBox.Ok, QMessageBox.Ok)
        else:

            QMessageBox.information(self, "Error", self.tr("file not found."), QMessageBox.Ok, QMessageBox.Ok)

    def saveslot(self):
        if (self.file):
            self.save(self.file)
        else:
            self.saveAs()

    def saveas(self):
        file, _ = QFileDialog.getSaveFileName(
            self,
            self.tr(  # __ is filefilter
                "save file"),
            self.file,
            "Python(*.py);;all(*.*)")
        if file:
            self.file = file.encode("utf-8")
            self.save(self.file)

    def preview(self):
        with open(self.cachefile, 'w', newline='') as file:
            # 不指定newline，则换行符为各系统默认的换行符（\n, \r, or \r\n, ）
            # newline=''表示不转换
            pretext = """# -*- coding: utf-8 -*-
\"""Qss preview for Custom QtWidgets\"""

import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
"""
            file.write(pretext)
            file.write(self.text())

        dir1 = os.getcwd()
        try:
            os.chdir(self.dir)
            #del self.custom
            if "data.cache.custom" in sys.modules:
                sys.modules.pop("data.cache.custom")
            # self.custom = import_module(".custom", "data.cache")
            self.custom = import_module(".cache.custom", "data")
            reload(self.custom)
            if (hasattr(self.custom, "MainWindow")):
                self.w = self.custom.MainWindow()
                self.w.setParent(self)
                self.w.setWindowFlags(Qt.Window)
                self.w.setMinimumSize(400, 280)
                self.w.show()
            else:
                raise Exception(self.tr('Please define the "MainWindow" class.'))
            # w.raise_()
        except Exception as e:
            # del self.custom
            # del self.w
            QMessageBox.information(self, "Error",
                                    self.tr("Preview error, please check the code.\n\n") + str(e), QMessageBox.Ok,
                                    QMessageBox.Ok)
        finally:
            os.chdir(dir1)
