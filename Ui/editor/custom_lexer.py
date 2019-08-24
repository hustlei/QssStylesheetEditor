import re

from PyQt5.Qsci import QsciLexerCustom
from PyQt5.QtGui import QColor, QFont


class QsciLexerQSS(QsciLexerCustom):
    Default = 0  # 默认
    Tag = 1  # 控件
    IDSelector = 2  # #选择器
    ClassSelector = 3  # .类选择器
    PseudoElement = 4  # ::子控件，伪元素选择器
    PseudoClass = 5  # 伪类hover等选择器
    Attribute = 6  # []选择器
    Operator = 7  # {}：；等语法标记
    Property = 8  # 属性
    Value = 9  # 属性值
    Comment = 10  # 注释
    DoubleQuotedString = 11  # 字符串
    SingleQuotedString = 12  # 字符串
    Variable = 13  # qsst变量$引用
    Param = 14 # 括号内参数

    operatorList = ('{', '}', '[', ']', '(', ')', '::', '.', ':', ';', ',', '/*', '*/', '#',
                    '$', '=', '"', "'", '\r', '\n')  # '!' * @ > + ~ |
    unitList=('pt','px','ex','em')

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setDefaultStyle()

    def setDefaultStyle(self):
        # Default text settings
        # ----------------------
        self.setDefaultColor(QColor("#ff000000"))
        self.setDefaultPaper(QColor("#ffffffff"))
        self.setDefaultFont(QFont("Consolas", 12))

        # Initialize colors per style
        # ----------------------------
        self.setColor(QColor("#000"), self.Default)
        self.setColor(QColor("#099"), self.Tag)#青色
        self.setColor(QColor("#a11"), self.IDSelector)#紫红969
        self.setColor(QColor("#a11"), self.ClassSelector)
        self.setColor(QColor("#a11"), self.PseudoElement)
        self.setColor(QColor("#a11"), self.PseudoClass)
        self.setColor(QColor("#aaa"), self.Attribute)#浅灰
        self.setColor(QColor("gray"), self.Operator)
        self.setColor(QColor("#04e"), self.Property)#浅蓝03c
        self.setColor(QColor("#808"), self.Value)#深红 a11
        self.setColor(QColor("gray"), self.Comment)#灰
        self.setColor(QColor("#690"), self.DoubleQuotedString)#浅绿
        self.setColor(QColor("#690"), self.SingleQuotedString)
        self.setColor(QColor("#a60"), self.Variable)#05a深蓝
        self.setColor(QColor("#aaa"), self.Param)#浅灰

        # Initialize paper colors per style
        # ----------------------------------
        # self.setPaper(QColor("#ffffffff"), 0)   # Style 0: white
        # self.setPaper(QColor("#ffffffff"), 1)   # Style 1: white

        # Initialize fonts per style
        # ---------------------------
        # self.setFont(QFont("Consolas", 14, weight=QFont.Normal), 0)   # Style 0: Consolas 14pt
        # self.setFont(QFont("Consolas", 14, weight=QFont.Normal), 1)

    def language(self):
        return "QSS"

    def description(self, style):
        #必须定义重载这个函数，否则不着
        namelist={
            0:'Default',1:'Tag',2:'IDSelector',3:'ClassSelector',
            4:'PseudoElement',5:'PseudoClass',6:'Attribute',7:'Operator',
            8:'Property',9:'Value',10:'Comment',11:'DoubleQuotedString',
            12:'SingleQuotedString',13:'Variable',14:'Param'}
        return namelist.get(style,"")

    def styleText(self, start, end):
        # 1. Slice out a part from the text
        # ----------------------------------
        editor = self.parent()
        text = editor.text()

        #扩大着色范围，避免修改文件过程中局部着色出错。
        while start>0:
            if(text[start]=="{" or text[start]=="}"):
                break
            else:
                start=start-1

        # 2. Initialize the styling procedure
        # ------------------------------------
        self.startStyling(start)
        text=text[start:end]

        # 3. Tokenize the text
        # ---------------------
        p = re.compile(r"\/[*]|[*]\/|\/\/|::|\r|\n|\s+|[*]+|=+|\"|'|\W|\w+|[\u0080-\uffff]+")

        # 'token_list' is a list of tuples: (token_name, token_len)
        token_list = [(token, len(bytearray(token, "utf-8"))) for token in p.findall(text)]

        # 4. Style the text
        # ------------------
        # 4.1 multiline token flag
        state = -1
        lastState = -1  # before operator
        # lastStateC = -1  # before comment
        # lastStateS = -1  # before single-quoted/double-quoted string
        # lastStateVar = -1  # before variable (SCSS)
        # lastStateVal = -1  # before value (SCSS)
        op = ' '  # last operator
        opPrev = ' '  # last operator
        # nestedLevel=0 #1在{}内，2在{{}}内
        inBrace = False
        inBracket = False
        inParentheses = False  # true if currently in a CSS url() or similar construct
        # varPrefix = '$'

        ###
        # 4.2 Style the text in a loop
        for i, tokeni in enumerate(token_list):
            token, count = tokeni

            #任意位置都可以注释，除注释外其他任何位置字符串都识别
            if state == self.Comment:
                if token == "*/":
                    self.setStyling(count,self.Operator)
                    lastState, state = state, self.Tag
                else:
                    self.setStyling(count, self.Comment)
            elif state == self.DoubleQuotedString:
                if token == '"':
                    lastState, state = state, lastState
                self.setStyling(count, self.DoubleQuotedString)
            elif state == self.SingleQuotedString:
                if token == "'":
                    lastState, state = state, lastState
                self.setStyling(count, self.SingleQuotedString)
            elif inParentheses:
                if token == ")":
                    inParentheses = False
                    lastState, state = state, lastState
                    self.setStyling(count, self.Operator)
                else:
                    self.setStyling(count, self.Param)

            elif self.isOperator(token):
                opStyle=True #是否显示为Operator

                op=token
                lastState=state
                if token == "/*":#注释
                    state = self.Comment
                elif token =="*/":
                    lastState = self.Comment
                    state = self.Property if inBrace else self.Tag
                elif token == '"':
                    state = self.DoubleQuotedString
                    opStyle = False
                elif token == "'":
                    state = self.SingleQuotedString
                    opStyle = False
                elif token =="$":#变量
                    state = self.Variable
                    opStyle = False
                elif token =="=":
                    if inBracket:
                        state = self.Attribute
                    else:
                        state = self.Value
                elif token == "{":
                    state = self.Property
                    inBrace = True
                elif token == "}":
                    state = self.Tag
                    inBrace = False
                elif token == ":":
                    if inBrace:
                        state = self.Value
                    else:
                        state = self.PseudoClass
                elif token == "::":
                    lastState, state = self.Property, self.PseudoElement
                elif token == "#":
                    if inBrace:
                        state = self.Param
                    else:
                        state = self.IDSelector
                elif token == "[":
                    lastState, state = self.Property, self.Attribute
                    inBracket = True
                elif token == "]":
                    state = self.Tag
                    inBracket = False
                elif token == "(":
                    state=self.Param
                    inParentheses = True
                elif token == ")":
                    state = lastState
                    inParentheses = False
                elif token == ",":
                    pass
                elif token ==";":
                    if opPrev == "=":
                        state = self.Tag
                    else:# opPrev == ":":#inBrace:
                        state = self.Property
                elif "\r" in token or "\n" in token:
                    if opPrev == "=":
                        state = self.Tag
                else:
                    state = lastState
                opPrev=token
                if opStyle:
                    self.setStyling(count, self.Operator)
                else:
                    self.setStyling(count, state)
            else:
                self.setStyling(count,state)

    ###
    ### token 判断
    ###
    def isOperator(self, ch):
        #if (ord(ch[0]) > 0x80 or not ch.isalnum()):
        if not ch[0].isascii():
            return False
        if ch in self.operatorList:
            return True
        return False

    def isAWordChar(self, ch):
        return ch >= 0x80 or ch.isalnum() or ch == "-" or ch == "_"


if __name__ == '__main__':
    from PyQt5.QtWidgets import *
    import sys
    from PyQt5.Qsci import *

    myCodeSample = r"""
    /* author:lei
    text=#222*/
        
    QWidget
    {
        color: $text;
        background-color: rgb(255,255,20);
    }    
    /* ======================== */
    /* MENU==================== */
    QMenuBar[aa="bbb"], #xxxx .abcc {
        background-color: "red";
        aaa: 'bbb';
    }
    
    QMenuBar::item
    {
        background: transparent;
    }
    
    QMenuBar::item:selected
    {
        background:#8bf;
        border: 1px solid #8bf;
    }    
    """.replace("\n", "\r\n")

    app = QApplication(sys.argv)
    win = QsciScintilla()
    win.setText(myCodeSample)
    l = QsciLexerQSS(win)
    win.setLexer(l)
    win.show()
    QApplication.setStyle(QStyleFactory.create('Fusion'))
    sys.exit(app.exec_())
