# -*- coding: utf-8 -*-
"""Copyright (c) 2019 lileilei <hustlei@sina.cn>
"""
from PyQt5.Qsci import QsciScintilla
from PyQt5.QtWidgets import (QMainWindow, QWidget, QHBoxLayout, QGridLayout, QVBoxLayout, QCheckBox, QPushButton,
                             QLabel, QLineEdit, QSpacerItem, QSizePolicy)
from PyQt5.QtCore import Qt, QMargins


class SearchDialog(QMainWindow):
    def __init__(self, editor, replaceMode=False):
        super().__init__(editor)
        self.__editor = editor
        self.isReplaceMode = replaceMode
        self.setWindowFlags(Qt.Tool)
        self.setMinimumWidth(320)
        self.setMinimumHeight(200)
        self.statusbar = self.statusBar()
        self.statusbar.setSizeGripEnabled(False)

        self.__reFlag = False  # 正则表达式
        self.__caseFlag = False  # 大小写
        self.__wordFlag = False  # 单词匹配
        self.__wrapFlag = False
        self.__forwardFlag = True  # 向下查找
        self.__line = -1  # 起始搜索的行号
        self.__index = -1  # 起始搜索的位置
        self.__show = True  # 搜索所有位置包括折叠代码
        self.__posixFlag = True
        self.__cxx11Flag = False

        self.__startNewSearch = True  # new search or continue previous search
        self.__escape = False
        self.searchText = ""
        self.replaceText = ""
        self.__finded = False

        if replaceMode:
            self.setWindowTitle(self.tr("Replace"))
        else:
            self.setWindowTitle(self.tr("Find"))
        self.setupUi()
        self.setFixedSize(self.sizeHint())

    def setReplaceMode(self, isReplace):
        self.isReplaceMode = isReplace
        self.__findPreBtn.setVisible(not isReplace)
        self.__countBtn.setVisible(not isReplace)
        self.__replaceBtn.setVisible(isReplace)
        self.__replaceAllBtn.setVisible(isReplace)
        self.__replacelabel.setVisible(isReplace)
        self.__replaceTextBox.setVisible(isReplace)
        self.__reverseCheckbox.setVisible(isReplace)
        if isReplace:
            self.setWindowTitle(self.tr("Replace"))
        else:
            self.setWindowTitle(self.tr("Find"))

    def setReverse(self, isReverse):
        if self.__forwardFlag == isReverse:
            self.__forwardFlag = not isReverse
            self.__startNewSearch = True

    def setCase(self, casesencitive):
        self.__caseFlag = casesencitive

    def setWord(self, word):
        self.__wordFlag = word

    def setRe(self, regexpression):
        self.__reFlag = regexpression

    def setEscape(self, escape):
        self.__escape = escape
        self.chText()

    def setupUi(self):
        mainwidget = QWidget()
        layout = QHBoxLayout()
        leftGridLayout = QGridLayout()
        rightVboxLayout = QVBoxLayout()
        layout.addLayout(leftGridLayout)
        layout.addLayout(rightVboxLayout)
        mainwidget.setLayout(layout)
        self.setCentralWidget(mainwidget)
        mainwidget.setFixedHeight(200)

        # from PyQt5.QtCore import QTextCodec
        # QTextCodec.setCodecForTr(QTextCodec.codecForName("UTF-8"))无效
        self.__reverseCheckbox = QCheckBox(self.tr("reverse"))  # ,"反向查找"))
        caseSensitiveCheckbox = QCheckBox(self.tr("case sensitive"))  # ,"匹配大小写"))
        wordCheckbox = QCheckBox(self.tr("match word"))  # ,"单词匹配"))
        # ,r'支持反义字符"\n,\r,\t,\0,\x..."'))
        escapeCheckbox = QCheckBox(self.tr(r"support escape char'\n,\r,\t,\0,\x...'"))
        regCheckbox = QCheckBox(self.tr("regular expression"))  # ,"正则表达式"))

        findlabel = QLabel(self.tr("Search Text"))  # ,"查找内容："))
        self.__replacelabel = QLabel(self.tr("Replace to:"))  # ,"替换为："))
        self.__searchTextBox = QLineEdit()
        self.__replaceTextBox = QLineEdit()
        # self.__searchTextBox.setMinimumWidth(120)
        leftGridLayout.addWidget(findlabel, 0, 0, 1, 1, Qt.AlignRight)
        leftGridLayout.addWidget(self.__replacelabel, 1, 0, 1, 1, Qt.AlignRight)
        leftGridLayout.addWidget(self.__searchTextBox, 0, 1)
        leftGridLayout.addWidget(self.__replaceTextBox, 1, 1)
        leftGridLayout.addItem(QSpacerItem(20, 5), 2, 0)
        leftGridLayout.setRowStretch(2, 1)
        leftGridLayout.addWidget(self.__reverseCheckbox, 3, 0)
        leftGridLayout.addWidget(caseSensitiveCheckbox, 4, 0)
        leftGridLayout.addWidget(wordCheckbox, 5, 0)
        leftGridLayout.addWidget(escapeCheckbox, 6, 0, 1, 2)
        leftGridLayout.addWidget(regCheckbox, 7, 0)
        if not self.isReplaceMode:
            self.__replacelabel.setVisible(False)
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
        self.__findPreBtn.setSizePolicy(QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.__findPreBtn.resize(self.__findPreBtn.sizeHint())
        self.__countBtn = QPushButton(self.tr("Count"))  # ,"计数"))
        cancelBtn = QPushButton(self.tr("Cancel"))  # ,"取消"))
        self.__replaceBtn = QPushButton(self.tr("Replace"))  # ,"替换"))
        self.__replaceAllBtn = QPushButton(self.tr("Replace All"))  # ,"替换全部"))
        stylesheet = "QPushButton { padding: 5 15}"
        self.__findPreBtn.setStyleSheet(stylesheet)  # setContentsMargins(QMargins(50,20,50,20))#setMinimumWidth(120)
        findNextBtn.setStyleSheet(stylesheet)
        self.__countBtn.setStyleSheet(stylesheet)
        self.__replaceBtn.setStyleSheet(stylesheet)
        self.__replaceAllBtn.setStyleSheet(stylesheet)
        rightVboxLayout.addWidget(findNextBtn)
        rightVboxLayout.addWidget(self.__findPreBtn)
        rightVboxLayout.addWidget(self.__replaceBtn)
        rightVboxLayout.addWidget(self.__replaceAllBtn)
        rightVboxLayout.addWidget(self.__countBtn)
        rightVboxLayout.addWidget(cancelBtn)
        rightVboxLayout.addStretch(1)
        if self.isReplaceMode:
            self.__findPreBtn.setVisible(False)
            self.__countBtn.setVisible(False)
        else:
            self.__replaceBtn.setVisible(False)
            self.__replaceAllBtn.setVisible(False)

        findNextBtn.clicked.connect(lambda: (self.setReverse(False), self.findreplace()))
        self.__findPreBtn.clicked.connect(lambda: (self.setReverse(True), self.findreplace()))
        self.__replaceBtn.clicked.connect(lambda: self.findreplace(True))
        self.__countBtn.clicked.connect(lambda: (self.statusbar.showMessage(
            self.tr("Count:{} times matched.").format(self.__editor.count(self.searchText, case=self.__caseFlag)))))

        cancelBtn.clicked.connect(self.close)
        cancelBtn.setShortcut(Qt.Key_Escape)

    def showEvent(self, e):
        self.__searchTextBox.setText(self.searchText)
        self.__replaceTextBox.setText(self.replaceText)
        self.__reverseCheckbox.setChecked(False)
        self.__startNewSearch = True
        self.__line = -1
        self.__index = -1
        self.__finded = False
        self.__searchTextBox.setFocus()
        self.activateWindow()
        e.accept()

    def chText(self):
        self.searchText = self.__searchTextBox.text()
        self.replaceText = self.__replaceTextBox.text()
        self.__startNewSearch = True
        if self.__escape:
            self.searchText = eval(repr(self.searchText).replace('\\\\', '\\'))
            self.replaceText = eval(repr(self.replaceText).replace('\\\\', '\\'))

    def findreplace(self, replace=False):
        if self.__startNewSearch:
            state = (self.__reFlag, self.__caseFlag, self.__wordFlag, self.__wrapFlag, self.__forwardFlag, self.__line,
                     self.__index, self.__show, self.__posixFlag, self.__cxx11Flag)
            self.__finded = self.__editor.findFirst(self.searchText, *state)
            if self.__finded:
                self.__startNewSearch = False
            else:
                self.statusbar.showMessage(self.tr("Nothing finded."))  # ,"未查找到。"))
        else:
            if replace and self.__finded:
                self.__editor.replaceSelectedText(self.replaceText)

            self.__finded = self.__editor.findNext()
            if not self.__finded:
                text = self.tr("bottom") if self.__forwardFlag else self.tr("top")
                self.statusbar.showMessage(self.tr("reach ") + text + ".")

        if self.__forwardFlag:
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
    s1 = SearchDialog(edt, False)
    btn2.stateChanged.connect(s1.setReplaceMode)
    btn1.clicked.connect(s1.show)
    win.show()
    sys.exit(app.exec_())
