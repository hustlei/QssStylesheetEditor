#!/usr/bin/env python3

import os
import sys
from PyQt5.QtCore import (Qt, QEvent, QFile, QFileInfo, QIODevice, QRegExp, QTextStream,
                          pyqtSignal)
from PyQt5.QtWidgets import (QApplication, QMainWindow, QAction, QFileDialog, QMessageBox,
                             QTextEdit)
from PyQt5.QtGui import (QFont, QKeyEvent,QIcon,QColor,QKeySequence,QSyntaxHighlighter,QTextCharFormat,
                         QTextCursor,QCursor)
from PyQt5.Qsci import QsciScintilla,QsciLexerCSS

__version__ = "1.0"

class CodeEditor(QsciScintilla):
    keyPress=pyqtSignal(QKeyEvent)
    loseFocus=pyqtSignal()
    mouseLeave=pyqtSignal()
    mousePress=pyqtSignal()
    def __init__(self):
        super().__init__()
        #self.setEolMode(self.SC_EOL_LF)    # 以\n换行
        self.setWrapMode(self.WrapWord)    # 自动换行。self.WrapWord是父类QsciScintilla的
        self.setAutoCompletionSource(self.AcsAll)  # 自动补全。对于所有Ascii字符
        self.setAutoCompletionCaseSensitivity(False)  # 自动补全大小写敏感
        self.setAutoCompletionThreshold(1)  # 输入多少个字符才弹出补全提示
        self.setFolding(True)  # 代码可折叠
        self.setFont(QFont('Courier,Consolas', 12))  # 设置默认字体
        self.setMarginLineNumbers(0, True)   # 0~4。第0个左边栏显示行号
        self.setMarginType(0, self.NumberMargin)  #我也不知道
        # self.setMarginsBackgroundColor(QtGui.QColor(120, 220, 180))  # 边栏背景颜色
        # self.setMarginWidth(0, 30)  # 边栏宽度
        self.setAutoIndent(True)  # 换行后自动缩进
        self.setUtf8(True)  # 支持中文字符
        self.setSyntax()

    def keyPressEvent(self, event):
        super().keyPressEvent(event)
        self.keyPress.emit(event)

    def focusOutEvent(self, e):
        super().focusOutEvent(e)
        self.loseFocus.emit()

    def leaveEvent(self, e):
        self.mouseLeave.emit()

    def mousePressEvent(self, QMouseEvent):
        super().mousePressEvent(QMouseEvent)
        self.mousePress.emit()

    def setSyntax(self):
        lexer = QsciLexerCSS()
        # lexer.setDefaultFont(这里填 QFont 类型的字体)
        self.setLexer(lexer)  # 关键是这句
