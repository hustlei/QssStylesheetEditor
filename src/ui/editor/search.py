# -*- coding: utf-8 -*-
"""
Copyright (c) 2019 lileilei <hustlei@sina.cn>
"""
from PyQt5.Qsci import QsciScintilla
from PyQt5.QtWidgets import (QMainWindow, QWidget, QHBoxLayout, QGridLayout, QVBoxLayout, QCheckBox, QPushButton,
                             QLabel, QLineEdit, QSpacerItem, QSizePolicy)
from PyQt5.QtCore import Qt


class searchDialog(QMainWindow):
    def __init__(self, editor, replace=False):
        super().__init__(editor)
        self.__editor = editor
        self.isReplace = replace
        self.setWindowFlags(Qt.Tool)
        self.setMinimumWidth(320)
        self.setMinimumHeight(200)
        self.statusbar = self.statusBar()
        self.statusbar.setSizeGripEnabled(False)

        self.__re = False  # 正则表达式
        self.__case = False  # 大小写
        self.__word = False  # 单词匹配
        self.__wrap = False
        self.__forward = True  # 向下查找
        self.__line = -1  # 起始搜索的行号
        self.__index = -1  # 起始搜索的位置
        self.__show = True  # 搜索所有位置包括折叠代码
        self.__posix = True
        self.__cxx11 = False

        self.__start = True
        self.__escape = False
        self.searchText = ""
        self.replaceText = ""

        if replace:
            self.setWindowTitle(self.tr("Replace"))
        else:
            self.setWindowTitle(self.tr("Find"))
        self.setupUi()
        self.setFixedSize(self.sizeHint())

    def setReplaceMode(self, isReplace):
        self.isReplace = isReplace
        self.__findPreBtn.setVisible(not isReplace)

        self.__replaceBtn.setVisible(isReplace)
        # self.__replaceAllBtn.setVisible(isReplace)
        self.__label2.setVisible(isReplace)
        self.__replaceTextBox.setVisible(isReplace)
        self.__reverseCheckbox.setVisible(isReplace)
        if isReplace:
            self.setWindowTitle(self.tr("Replace"))
        else:
            self.setWindowTitle(self.tr("Find"))

    def setReverse(self, isReverse):
        if self.__forward == isReverse:
            self.__forward = not isReverse
            self.__start = True

    def setCase(self, casesencitive):
        self.__case = casesencitive

    def setWord(self, word):
        self.__word = word

    def setRe(self, re):
        self.__re = re

    def setEscape(self, escape):
        self.__escape = escape
        self.chText()

    def setupUi(self):
        mainw = QWidget()
        layout = QHBoxLayout()
        grid = QGridLayout()
        lay2 = QVBoxLayout()
        layout.addLayout(grid)
        layout.addLayout(lay2)
        mainw.setLayout(layout)
        self.setCentralWidget(mainw)
        mainw.setFixedHeight(200)

        # from PyQt5.QtCore import QTextCodec
        # QTextCodec.setCodecForTr(QTextCodec.codecForName("UTF-8"))无效
        self.__reverseCheckbox = QCheckBox(self.tr("reverse"))  # ,"反向查找"))
        caseSensitiveCheckbox = QCheckBox(self.tr("case sensitive"))  # ,"匹配大小写"))
        wordCheckbox = QCheckBox(self.tr("match word"))  # ,"单词匹配"))
        # ,r'支持反义字符"\n,\r,\t,\0,\x..."'))
        escapeCheckbox = QCheckBox(self.tr(r"support escape char'\n,\r,\t,\0,\x...'"))
        regCheckbox = QCheckBox(self.tr("regular expression"))  # ,"正则表达式"))
        label1 = QLabel(self.tr("Search Text"))  # ,"查找内容："))
        self.__label2 = QLabel(self.tr("Replace to"))  # ,"替换为："))
        self.__searchTextBox = QLineEdit()
        self.__replaceTextBox = QLineEdit()
        # self.__searchTextBox.setMinimumWidth(120)
        grid.addWidget(label1, 0, 0, 1, 1, Qt.AlignRight)
        grid.addWidget(self.__label2, 1, 0, 1, 1, Qt.AlignRight)
        grid.addWidget(self.__searchTextBox, 0, 1)
        grid.addWidget(self.__replaceTextBox, 1, 1)
        grid.addItem(QSpacerItem(20, 5), 2, 0)
        grid.setRowStretch(2, 1)
        grid.addWidget(self.__reverseCheckbox, 3, 0)
        grid.addWidget(caseSensitiveCheckbox, 4, 0)
        grid.addWidget(wordCheckbox, 5, 0)
        grid.addWidget(escapeCheckbox, 6, 0, 1, 2)
        grid.addWidget(regCheckbox, 7, 0)
        if not self.isReplace:
            self.__label2.setVisible(False)
            self.__replaceTextBox.setVisible(False)
            self.__reverseCheckbox.setVisible(False)

        self.__searchTextBox.textChanged.connect(self.chText)
        self.__replaceTextBox.textChanged.connect(self.chText)
        self.__reverseCheckbox.stateChanged.connect(self.setReverse)
        caseSensitiveCheckbox.stateChanged.connect(self.setCase)
        wordCheckbox.stateChanged.connect(self.setWord)
        escapeCheckbox.stateChanged.connect(self.setEscape)
        regCheckbox.stateChanged.connect(self.setRe)

        findNextBtn = QPushButton(self.tr("Find Next"))  # ,"查找下一个"))
        findNextBtn.setShortcut(Qt.Key_Return)
        self.__findPreBtn = QPushButton(self.tr("Find previous"))  # ,"查找上一个"))
        self.__findPreBtn.setMinimumWidth(150)
        self.__findPreBtn.setSizePolicy(QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.__findPreBtn.resize(self.__findPreBtn.sizeHint())
        countBtn = QPushButton(self.tr("Count"))  # ,"计数"))
        cancelBtn = QPushButton(self.tr("Cancel"))  # ,"取消"))
        self.__replaceBtn = QPushButton(self.tr("Replace"))  # ,"替换"))
        self.__replaceAllBtn = QPushButton(self.tr("Replace All"))  # ,"替换全部"))
        self.__replaceAllBtn.setVisible(False)
        lay2.addWidget(findNextBtn)
        lay2.addWidget(self.__findPreBtn)
        lay2.addWidget(countBtn)
        lay2.addWidget(self.__replaceBtn)
        lay2.addWidget(self.__replaceAllBtn)
        lay2.addWidget(cancelBtn)
        lay2.addStretch(1)
        countBtn.setVisible(False)
        if self.isReplace:
            self.__findPreBtn.setVisible(False)
        else:
            self.__replaceBtn.setVisible(False)
            self.__replaceAllBtn.setVisible(False)

        findNextBtn.clicked.connect(lambda: (self.setReverse(False), self.findreplace()))
        self.__findPreBtn.clicked.connect(lambda: (self.setReverse(True), self.findreplace()))
        self.__replaceBtn.clicked.connect(lambda: self.findreplace(True))

        cancelBtn.clicked.connect(self.close)
        cancelBtn.setShortcut(Qt.Key_Escape)

    def showEvent(self, e):
        self.__searchTextBox.setText(self.searchText)
        self.__replaceTextBox.setText(self.replaceText)
        self.__reverseCheckbox.setChecked(False)
        self.__start = True
        self.__line = -1
        self.__index = -1
        self.__finded = False
        self.__searchTextBox.setFocus()
        self.activateWindow()
        e.accept()

    def chText(self):
        self.searchText = self.__searchTextBox.text()
        self.replaceText = self.__replaceTextBox.text()
        self.__start = True
        if self.__escape:
            self.searchText = eval(repr(self.searchText).replace('\\\\', '\\'))
            self.replaceText = eval(repr(self.replaceText).replace('\\\\', '\\'))

    def findreplace(self, replace=False):
        if self.__start:
            state = (self.__re, self.__case, self.__word, self.__wrap, self.__forward, self.__line, self.__index,
                     self.__show, self.__posix, self.__cxx11)
            self.__finded = self.__editor.findFirst(self.searchText, *state)
            if self.__finded:
                self.__start = False
            else:
                self.statusbar.showMessage(self.tr("Nothing finded."))  # ,"未查找到。"))
        else:
            if replace and self.__finded:
                self.__editor.replaceSelectedText(self.replaceText)

            self.__finded = self.__editor.findNext()
            if not self.__finded:
                text = self.tr("bottom") if self.__forward else self.tr("top")
                self.statusbar.showMessage(self.tr("reach ") + text + ".")

        if self.__forward:
            self.__line, self.__index = self.__editor.getSelection()[2:]
        else:
            self.__line, self.__index = self.__editor.getSelection()[:2]


if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    import sys
    app = QApplication(sys.argv)
    win = QWidget()
    btn1 = QPushButton("search", win)
    btn1.move(50, 50)
    btn2 = QCheckBox("replace", win)
    btn2.move(50, 100)
    edt = QsciScintilla()
    s1 = searchDialog(edt, False, win)
    btn2.stateChanged.connect(s1.setReplaceMode)
    btn1.clicked.connect(s1.show)
    win.show()
    sys.exit(app.exec_())
