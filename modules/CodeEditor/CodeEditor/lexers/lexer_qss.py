# -*- coding: utf-8 -*-
"""custom lexers for qt stylesheet syntex

Copyright (c) 2019 lileilei. <hustlei@sina.cn>
"""
import re

from PyQt5.Qsci import QsciScintilla, QsciLexerCustom, QsciAPIs
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
    Param = 14  # 括号内参数

    namelist = {
        0: 'Default',
        1: 'Tag',
        2: 'IDSelector',
        3: 'ClassSelector',
        4: 'PseudoElement',
        5: 'PseudoClass',
        6: 'Attribute',
        7: 'Operator',
        8: 'Property',
        9: 'Value',
        10: 'Comment',
        11: 'DoubleQuotedString',
        12: 'SingleQuotedString',
        13: 'Variable',
        14: 'Param'
    }
    operatorList = ('{', '}', '[', ']', '(', ')', '::', '.', ':', ';', ',', '/*', '*/', '#', '$', '=', '"', "'", '\r',
                    '\n')  # '!' * @ > + ~ |
    unitList = ('pt', 'px', 'ex', 'em')

    def __init__(self, codeEditor):
        super().__init__(codeEditor)
        self.__editor = codeEditor
        self.setDefaultStyle()
        self.setQssAutocomplete()

    def setDefaultStyle(self):
        # Default text settings
        # ----------------------
        self.setDefaultColor(QColor("#ff000000"))
        self.setDefaultPaper(QColor("#ffffffff"))
        self.setDefaultFont(QFont("Consolas", 12))

        # Initialize colors per style
        # ----------------------------
        self.setColor(QColor("#000"), self.Default)
        self.setColor(QColor("#099"), self.Tag)  # 青色
        self.setColor(QColor("#a11"), self.IDSelector)  # 紫红969
        self.setColor(QColor("#a11"), self.ClassSelector)
        self.setColor(QColor("#a11"), self.PseudoElement)
        self.setColor(QColor("#a11"), self.PseudoClass)
        self.setColor(QColor("#aaa"), self.Attribute)  # 浅灰
        self.setColor(QColor("gray"), self.Operator)
        self.setColor(QColor("#04e"), self.Property)  # 浅蓝03c
        self.setColor(QColor("#808"), self.Value)  # 深红 a11
        self.setColor(QColor("gray"), self.Comment)  # 灰
        self.setColor(QColor("#690"), self.DoubleQuotedString)  # 浅绿
        self.setColor(QColor("#690"), self.SingleQuotedString)
        self.setColor(QColor("#a60"), self.Variable)  # 05a深蓝
        self.setColor(QColor("#aaa"), self.Param)  # 浅灰

        # Initialize paper colors per style
        # ----------------------------------
        # self.setPaper(QColor("#ffffffff"), 0)   # Style 0: white
        # self.setPaper(QColor("#ffffffff"), 1)   # Style 1: white

        # Initialize fonts per style
        # ---------------------------
        # self.setFont(QFont("Consolas", 14, weight=QFont.Normal), 0)   # Style 0: Consolas 14pt
        # self.setFont(QFont("Consolas", 14, weight=QFont.Normal), 1)

        SC = QsciScintilla
        # 折叠标签颜色
        self.__editor.SendScintilla(SC.SCI_MARKERSETBACK, SC.SC_MARKNUM_FOLDERSUB, QColor("0xa0a0a0"))
        self.__editor.SendScintilla(SC.SCI_MARKERSETBACK, SC.SC_MARKNUM_FOLDERMIDTAIL, QColor("0xa0a0a0"))
        self.__editor.SendScintilla(SC.SCI_MARKERSETBACK, SC.SC_MARKNUM_FOLDERTAIL, QColor("0xa0a0a0"))

        # if (self.__editor.folding() == QsciScintilla.BoxedTreeFoldStyle):
        # 显示这些标记的掩码是0xFE000000，同样头文件里已经定义好了
        # define SC_MASK_FOLDERS 0xFE000000
        # self.__editor..SendScintilla(SC.SCI_SETMARGINMASKN, SC.MARGIN_FOLD_INDEX, SC.SC_MASK_FOLDERS)# 页边掩码
        # self.__editor..setMarginMarkerMask(2,0x7e000000)#fold margin只显示25-31的图标
        # 折叠标签样式
        # self.__editor.markerDefine(65,SC.SC_MARKNUM_FOLDEROPEN)
        # self.__editor.SendScintilla(SC.SCI_MARKERDEFINE,SC.SC_MARKNUM_FOLDEROPEN,SC.SC_MARK_BOXMINUS)
        # self.__editor.SendScintilla(SC.SCI_MARKERDEFINE,SC.SC_MARKNUM_FOLDER,SC.SC_MARK_BOXPLUS)
        # self.__editor.SendScintilla(SC.SCI_MARKERDEFINE,SC.SC_MARKNUM_FOLDERSUB,SC.SC_MARK_VLINE)
        # self.__editor.SendScintilla(SC.SCI_MARKERDEFINE,SC.SC_MARKNUM_FOLDERTAIL,SC.SC_MARK_LCORNER)
        # self.__editor.SendScintilla(SC.SCI_MARKERDEFINE,SC.SC_MARKNUM_FOLDEROPENMID,SC.SC_MARK_BOXMINUSCONNECTED)
        # self.__editor.SendScintilla(SC.SCI_MARKERDEFINE,SC.SC_MARKNUM_FOLDEREND,SC.SC_MARK_BOXPLUSCONNECTED)
        # self.__editor.SendScintilla(SC.SCI_MARKERDEFINE,SC.SC_MARKNUM_FOLDERMIDTAIL,SC.SC_MARK_TCORNER)

        # define SC_MARKNUM_FOLDEROPEN  31      //展开
        # define SC_MARKNUM_FOLDER      30      //折叠
        # define SC_MARKNUM_FOLDERSUB   29      //普通文本(各级内部) |部分
        # define SC_MARKNUM_FOLDERTAIL  28      //尾部
        # define SC_MARKNUM_FOLDEROPENMID 26    //子级展开
        # define SC_MARKNUM_FOLDEREND     25    //子级折叠
        # define SC_MARKNUM_FOLDERMIDTAIL 27    //子级尾部

    def setPapers(self, clr):
        self.setDefaultPaper(clr)
        for i in range(len(self.namelist)):
            self.setPaper(clr, i)

    def language(self):
        return "QSS"

    def setDefaultFont(self, font):
        for i in self.namelist:
            self.setFont(font, i)

    def description(self, style):
        # 必须定义重载这个函数，否则不着
        return self.namelist.get(style, "")

    def styleText(self, start, end):
        # 1. Slice out a part from the text
        # ----------------------------------
        text = self.__editor.text()

        # 扩大着色范围，避免修改文件过程中局部着色出错。
        t = str.encode(text)  # start end是byte字节数，如果有非注意和len(text)长度不一样
        while start > 0:
            if t[start] == "{" or not start:  # start == 0
                break
            start -= 1

        # 2. Initialize the styling procedure
        # ------------------------------------
        self.startStyling(start)
        text = bytes.decode(t[start:end])

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
        # op = ' '  # last operator
        opPrev = ' '  # last operator
        # nestedLevel=0 #1在{}内，2在{{}}内
        inBrace = False
        inBracket = False
        inParentheses = False  # true if currently in a CSS url() or similar construct
        # varPrefix = '$'

        ###
        # 4.2 Style the text in a loop
        for tokeni in token_list:
            token, count = tokeni

            # 任意位置都可以注释，除注释外其他任何位置字符串都识别
            if state == self.Comment:
                if token == "*/":
                    self.setStyling(count, self.Operator)
                    if inBrace:
                        lastState, state = state, self.Property
                    else:
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
                opStyle = True  # 是否显示为Operator

                lastState = state
                if token == "/*":  # 注释
                    state = self.Comment
                elif token == "*/":
                    lastState = self.Comment
                    state = self.Property if inBrace else self.Tag
                elif token == '"':
                    state = self.DoubleQuotedString
                    opStyle = False
                elif token == "'":
                    state = self.SingleQuotedString
                    opStyle = False
                elif token == "$":  # 变量
                    state = self.Variable
                    opStyle = False
                elif token == "=":
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
                    state = self.Param
                    inParentheses = True
                elif token == ")":
                    state = lastState
                    inParentheses = False
                elif token == ",":
                    if not inBrace:
                        lastState, state = state, self.Tag
                elif token == ";":
                    if opPrev == "=":
                        state = self.Tag
                    else:  # opPrev == ":":#inBrace:
                        state = self.Property
                elif "\r" in token or "\n" in token:
                    if opPrev == "=":
                        state = self.Tag
                else:
                    state = lastState
                opPrev = token
                if opStyle:
                    self.setStyling(count, self.Operator)
                else:
                    self.setStyling(count, state)
            else:
                self.setStyling(count, state)

        # Folding Setting
        # Initialize the folding variables
        SCI = self.__editor.SendScintilla
        GETFOLDLEVEL = QsciScintilla.SCI_GETFOLDLEVEL
        SETFOLDLEVEL = QsciScintilla.SCI_SETFOLDLEVEL
        HEADERFLAG = QsciScintilla.SC_FOLDLEVELHEADERFLAG
        LEVELBASE = QsciScintilla.SC_FOLDLEVELBASE
        NUMBERMASK = QsciScintilla.SC_FOLDLEVELNUMBERMASK
        WHITEFLAG = QsciScintilla.SC_FOLDLEVELWHITEFLAG

        index = SCI(QsciScintilla.SCI_LINEFROMPOSITION, start)
        if not index:  # index==0
            level = LEVELBASE
        else:
            lastLevel = SCI(GETFOLDLEVEL, index - 1)
            level = lastLevel

        lines = text.splitlines(True)
        for line in iter(lines):
            open_count = line.count('{')
            close_count = line.count('}')
            isBlankLine = (not line.strip)  # ==""
            flag = 0x000

            if isBlankLine:
                flag = WHITEFLAG
            elif open_count > close_count:
                flag = HEADERFLAG
            else:
                flag &= NUMBERMASK

            SCI(SETFOLDLEVEL, index, level | flag)
            level += open_count
            level -= close_count
            index += 1

            # l=(level & ~HEADERFLAG)-LEVELBASE
            # print("{}:{}".format(index+1,l))
        # Reset the fold level of the last line
        # editor.SendScintilla(QsciScintilla.SCI_SETFOLDLEVEL, len(lines), 0)
        # editor.SendScintilla(QsciScintilla.SCI_SETFOLDFLAGS, 16 | 4, 0)# //
        # 如果折叠就在折叠行的上下各画一条横线

    # token 判断
    ###
    def isOperator(self, aChar):
        # if (ord(ch[0]) > 0x80 or not ch.isalnum()):
        if not aChar[0].isascii():
            return False
        if aChar in self.operatorList:
            return True
        return False

    def isAWordChar(self, aChar):
        return aChar >= 0x80 or aChar.isalnum() or aChar == "-" or aChar == "_"

    def setQssAutocomplete(self):
        api = QsciAPIs(self)
        widgets = ("QAbstractScrollArea", "QCheckBox", "QColumnView", "QComboBox", "QDateEdit", "QDateTimeEdit",
                   "QDialog", "QDialogButtonBox", "QDockWidget", "QDoubleSpinBox", "QFrame", "QGroupBox", "QHeaderView",
                   "QLabel", "QLineEdit", "QListView", "QListWidget", "QMainWindow", "QMenu", "QMenuBar", "QMessageBox",
                   "QProgressBar", "QPushButton", "QRadioButton", "QScrollBar", "QSizeGrip", "QSlider", "QSpinBox",
                   "QSplitter", "QStatusBar", "QTabBar", "QTabWidget", "QTableView", "QTableWidget", "QTextEdit",
                   "QTimeEdit", "QToolBar", "QToolButton", "QToolBox", "QToolTip", "QTreeView", "QTreeWidget",
                   "QWidget")
        properties = ("alternate-background-color", "background", "background-color", "background-image",
                      "background-repeat", "background-position", "background-attachment", "background-clip",
                      "background-origin", "border", "border-top", "border-right", "border-bottom", "border-left",
                      "border-color", "border-top-color", "border-right-color", "border-bottom-color",
                      "border-left-color", "border-image", "border-radius", "border-top-left-radius",
                      "border-top-right-radius", "border-bottom-right-radius", "border-bottom-left-radius",
                      "border-style", "border-top-style", "border-right-style", "border-bottom-style",
                      "border-left-style", "border-width", "border-top-width", "border-right-width",
                      "border-bottom-width", "border-left-width", "bottom", "button-layout", "color",
                      "dialogbuttonbox-buttons-have-icons", "font", "font-family", "font-size", "font-style",
                      "font-weight", "gridline-color", "height", "icon-size", "image", "image-position", "left",
                      "lineedit-password-character", "lineedit-password-mask-delay", "margin", "margin-top",
                      "margin-right", "margin-bottom", "margin-left", "max-height", "max-width",
                      "messagebox-text-interaction-flags", "min-height", "min-width", "opacity*", "outline",
                      "outline-color", "outline-offset", "outline-style", "outline-radius",
                      "outline-bottom-left-radius", "outline-bottom-right-radius", "outline-top-left-radius",
                      "outline-top-right-radius", "padding", "padding-top", "padding-right", "padding-bottom",
                      "padding-left", "paint-alternating-row-colors-for-empty-area", "position", "right",
                      "selection-background-color", "selection-color", "show-decoration-selected", "spacing",
                      "subcontrol-origin", "subcontrol-position", "titlebar-show-tooltips-on-buttons",
                      "widget-animation-duration", "text-align", "text-decoration", "top", "width")
        subcontrols = ("add-line", "add-page", "branch", "chunk", "close-button", "corner", "down-arrow", "down-button",
                       "drop-down", "float-button", "groove", "indicator", "handle", "icon", "item", "left-arrow",
                       "left-corner", "menu-arrow", "menu-button", "menu-indicator", "right-arrow", "pane",
                       "right-corner", "scroller", "section", "separator", "sub-line", "sub-page", "tab", "tab-bar",
                       "tear", "tearoff", "text", "title", "up-arrow", "up-button")
        pseudostates = ("active", "adjoins-item", "alternate", "bottom", "checked", "closable", "closed", "default",
                        "disabled", "editable", "edit-focus", "enabled", "exclusive", "first", "flat", "floatable",
                        "focus", "has-children", "has-siblings", "horizontal", "hover", "indeterminate", "last", "left",
                        "maximized", "middle", "minimized", "movable", "no-frame", "non-exclusive", "off", "on",
                        "only-one", "open", "next-selected", "pressed", "previous-selected", "read-only", "right",
                        "selected", "top", "unchecked", "vertical", "window")
        kwset = (widgets, properties, subcontrols, pseudostates)
        for ks in kwset:
            for k in ks:
                api.add(k)
        api.prepare()


if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication, QStyleFactory
    import sys

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
    lexer = QsciLexerQSS(win)
    win.setLexer(lexer)
    win.show()
    QApplication.setStyle(QStyleFactory.create('Fusion'))
    sys.exit(app.exec_())
