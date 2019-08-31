
from PyQt5.Qsci import QsciScintilla
from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QGridLayout,QVBoxLayout,QCheckBox,QPushButton,
                             QLabel,QLineEdit,QSpacerItem,QStatusBar)
from PyQt5.QtCore import Qt

class searchDialog(QWidget):
    def __init__(self, editor, replace=False):
        super().__init__(editor)
        self.__editor=editor
        self.isReplace=replace
        self.setWindowFlags(Qt.Tool)
        if replace:
            self.setWindowTitle("替换")
        else:
            self.setWindowTitle("查找")
        self.setupUi()

        self.searchText=""
        self.replaceText=""

        self.__re=False#正则表达式
        self.__case=False#大小写
        self.__word=False#单词匹配
        self.__wrap=False
        self.__forward=True#向下查找
        self.__line=-1#起始搜索的行号
        self.__index=-1#起始搜索的位置
        self.__show=True#搜索所有位置包括折叠代码
        self.__posix=True
        self.__cxx11=False

        self.__start=True
        self.__escape=False

    def setReplaceMode(self, isReplace):
        self.isReplace=isReplace
        self.__findPreBtn.setVisible(not isReplace)

        self.__replaceBtn.setVisible(isReplace)
        #self.__replaceAllBtn.setVisible(isReplace)
        self.__label2.setVisible(isReplace)
        self.__replaceTextBox.setVisible(isReplace)
        self.__reverseCheckbox.setVisible(isReplace)
        if isReplace:
            self.setWindowTitle("替换")
        else:
            self.setWindowTitle("查找")

    def setReverse(self,isReverse):
        if(self.__forward==isReverse):
            self.__forward=not isReverse
            self.__start=True
    def setCase(self,casesencitive):
        self.__case=casesencitive
    def setWord(self,word):
        self.__word=word
    def setRe(self,re):
        self.__re=re
    def setEscape(self,escape):
        self.__escape=escape
        self.chText()

    def setupUi(self):
        mainLayout=QVBoxLayout()
        layout=QHBoxLayout()
        grid=QGridLayout()
        lay2=QVBoxLayout()
        layout.addLayout(grid)
        layout.addLayout(lay2)
        mainLayout.addLayout(layout)
        self.statusbar=QStatusBar(self)
        mainLayout.addWidget(self.statusbar)
        self.setLayout(mainLayout)

        self.__reverseCheckbox=QCheckBox("反向查找")
        caseSensitiveCheckbox=QCheckBox("匹配大小写")
        wordCheckbox=QCheckBox("单词匹配")
        escapeCheckbox=QCheckBox(r'支持反义字符"\n,\r,\t,\0,\x..."')
        regCheckbox=QCheckBox("正则表达式")
        label1=QLabel("查找内容：")
        self.__label2=QLabel("替换为：")
        self.__searchTextBox=QLineEdit()
        self.__replaceTextBox=QLineEdit()
        self.__searchTextBox.setMinimumWidth(160)
        self.__searchTextBox.setMinimumWidth(160)
        grid.addWidget(label1,0,0,1,1,Qt.AlignRight)
        grid.addWidget(self.__label2,1,0,1,1,Qt.AlignRight)
        grid.addWidget(self.__searchTextBox,0,1)
        grid.addWidget(self.__replaceTextBox,1,1)
        grid.addItem(QSpacerItem(20,20),2,0)
        grid.addWidget(self.__reverseCheckbox,3,0)
        grid.addWidget(caseSensitiveCheckbox,4,0)
        grid.addWidget(wordCheckbox,5,0)
        grid.addWidget(escapeCheckbox,6,0,1,2)
        grid.addWidget(regCheckbox,7,0)
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


        findNextBtn=QPushButton("查找下一个")
        self.__findPreBtn=QPushButton("查找上一个")
        countBtn=QPushButton("计数")
        cancelBtn=QPushButton("取消")
        self.__replaceBtn=QPushButton("替换")
        self.__replaceAllBtn=QPushButton("替换全部")
        self.__replaceAllBtn.setVisible(False)
        lay2.addWidget(findNextBtn)
        lay2.addWidget(self.__findPreBtn)
        lay2.addWidget(countBtn)
        lay2.addWidget(self.__replaceBtn)
        lay2.addWidget(self.__replaceAllBtn)
        lay2.addWidget(cancelBtn)
        lay2.addStretch(1)
        countBtn.setVisible(False)
        if(self.isReplace):
            self.__findPreBtn.setVisible(False)
        else:
            self.__replaceBtn.setVisible(False)
            self.__replaceAllBtn.setVisible(False)

        findNextBtn.clicked.connect(lambda :(self.setReverse(False),self.findreplace()))
        self.__findPreBtn.clicked.connect(lambda :(self.setReverse(True),self.findreplace()))
        self.__replaceBtn.clicked.connect(lambda : self.findreplace(True))

        cancelBtn.clicked.connect(self.close)

    def show(self):
        self.__searchTextBox.setText(self.searchText)
        self.__replaceTextBox.setText(self.replaceText)
        self.__reverseCheckbox.setChecked(False)
        self.__start=True
        self.__line=-1
        self.__index=-1
        self.__ok=False
        super().show()

    def chText(self):
        self.searchText=self.__searchTextBox.text()
        self.replaceText=self.__replaceTextBox.text()
        self.__start=True
        if(self.__escape):
            self.searchText=eval(repr(self.searchText).replace('\\\\', '\\'))
            self.replaceText=eval(repr(self.replaceText).replace('\\\\', '\\'))

    def findreplace(self,replace=False):
        if self.__start:
            state=(self.__re,self.__case,self.__word,self.__wrap,self.__forward
                  ,self.__line,self.__index,self.__show,self.__posix,self.__cxx11)
            self.__ok=self.__editor.findFirst(self.searchText, *state)
            if self.__ok:
                self.__start=False
            else:
                self.statusbar.showMessage("未查找到。")
        else:
            if replace and self.__ok:
                self.__editor.replaceSelectedText(self.replaceText)

            self.__ok=self.__editor.findNext()
            if not self.__ok:
                text="底部" if self.__forward else "顶部"
                self.statusbar.showMessage("已经到达"+text+".")

        if self.__forward:
            self.__line, self.__index = self.__editor.getSelection()[2:]
        else:
            self.__line, self.__index = self.__editor.getSelection()[:2]

if __name__ == "__main__":
    from PyQt5.QtWidgets import *
    import sys
    app=QApplication(sys.argv)
    win=QWidget()
    btn1=QPushButton("search",win)
    btn1.move(50,50)
    btn2=QCheckBox("replace",win)
    btn2.move(50,100)
    edt=QsciScintilla()
    s1=searchDialog(edt,False,win)
    btn2.stateChanged.connect(s1.setReplaceMode)
    btn1.clicked.connect(s1.show)
    win.show()
    sys.exit(app.exec_())