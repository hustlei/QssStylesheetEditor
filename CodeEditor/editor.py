# -*- coding: utf-8 -*-
"""CodeEditor

Copyright (c) 2019 lileilei <hustlei@sina.cn>
"""

import sys
import os
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import (QFont, QFontMetrics, QKeyEvent, QColor, QDropEvent)
from PyQt5 import Qsci
from PyQt5.Qsci import QsciScintilla, QsciLexer
from lexer import lexer_qss

import chardet
# if sys.platform.startswith("linux"):
#     font = QFont("DejaVu Sans Mono", 10, 50)
# elif sys.platform.startswith("darwin"):
#     font = QFont("Menlo", 10, 50)
# elif sys.platform.startswith("win"):
#     font = QFont("Courier New", 10, 50)


class Editor(QsciScintilla):
    keyPress = pyqtSignal(QKeyEvent)
    loseFocus = pyqtSignal()
    mouseLeave = pyqtSignal()
    mousePress = pyqtSignal()
    drop = pyqtSignal(QDropEvent)

    def __init__(self, **config):
        super().__init__()
        self.coding = "utf-8"

        self.settings = {}
        # self._setDefaultConfig()
        # Override defaults with any customizations
        self.configure(**config)

    ###
    # extension(core): config extension
    ###
    def getConfig(self, name, *args):
        """Return the current configuration setting for attribute ``name``.
        If ``name`` refers to an enumerated setting, return the string version
        of that enumeration.
        """
        name = name[0].lower() + name[1:]
        getter = getattr(self, name)
        value = getter(*args)
        return value

    def setConfig(self, name, value):
        """Set the current configuration setting for attribute ``name``."""
        conf = {name: value}
        self.configure(**conf)

    def _setDefaultConfig(self):
        """Set default configuration settings.
        """
        self.configure(
            # Fonts
            utf8=True,  # 支持中文字符
            font=QFont('Consolas', 11),  # 设置默认字体
            marginsFont=QFont('Courier New', 10),

            # Wrap mode: Wrap(None|Word|Character|Whitespace) 0,1,2,3
            wrapMode='WrapNone',  # self.setWrapMode(self.WrapWord)    # 自动换行
            # Text wrapping visual flag:
            # WrapFlag(None|ByText|ByBorder|InMargin)
            wrapVisualFlags='WrapFlagNone',  # 无对应getter
            # End-of-line mode
            # EolMode: Eol(Windows|Unix|Mac) SC_EOL_CRLF|SC_EOL_LF|SC_EOL_CR
            eolMode='EolWindows',  # self.SC_EOL_LF,# 以\n换行
            eolVisibility=False,  # 是否显示换行符

            # Whitespace: Ws(Invisible|Visible|VisibleAfterIndent)
            whitespaceVisibility='WsInvisible',  # 是否显示空格，类似word空格处显示为点
            #  WhitespaceSize: (0|1|2) 点大小，0不显示，1小点，2大点
            whitespaceSize=2,

            # indent
            indentationsUseTabs=False,  # False表示用空格代替\t
            tabWidth=4,  # 空格数量，或者\t宽度
            indentationGuides=True,  # 用tab键缩进时，在缩进位置上显示一个竖点线，缩进有效，在字符串后加空格不显示
            indentationWidth=0,  # 如果在行首部空格位置tab，缩进的宽度字符数，并且不会转换为空格
            autoIndent=True,  # 换行后自动缩进
            backspaceUnindents=True,
            tabIndents=True,
            # True如果行前空格数少于tabWidth，补齐空格数,False如果在文字前tab同true，如果在行首tab，则直接增加tabwidth个空格

            # current line color
            caretWidth=2,  # 光标宽度，0表示不显示光标
            caretForegroundColor=QColor("#ff000000"),  # 光标颜色
            caretLineVisible=True,  # 是否高亮显示光标所在行
            caretLineBackgroundColor=QColor('#FFF0F0F0'),  # 光标所在行背景颜色

            # selection color
            # selectionBackgroundColor=QColor("#606060"),
            # selectionForegroundColor=QColor("#FFFFFF"),

            # edges
            edgeColumn=80,
            # Edge mode: Edge(None|Line|Background)
            edgeMode='EdgeLine',
            edgeColor=QColor('#FF88FFFF'),

            # Brace matching: (No|Strict|Sloppy)BraceMatch
            braceMatching='SloppyBraceMatch',

            # AutoComplete
            # Acs[None|All|Document|APIs]禁用自动补全提示功能|所有可用的资源|
            # 当前文档中出现的名称都自动补全提示|使用QsciAPIs类加入的名称都自动补全提示
            autoCompletionSource='AcsAll',  # 自动补全。对于所有Ascii字符
            autoCompletionCaseSensitivity=False,  # 自动补全大小写敏感,不是很有用
            autoCompletionThreshold=1,  # 输入多少个字符才弹出补全提示
            autoCompletionReplaceWord=True,  # 是否用补全的字符串替代光标右边的字符串

            # margins switch
            marginWidthes=((1, 0), (3, 0), (4, 0)),  # 设置边栏宽度，设置宽度为0表示不显示
            marginWidth=(2, 12),  # 设置边栏宽度

            # margin（line number）
            marginLineNumbers=(0, True),  # 设置第0个边栏为行号边栏，True表示显示
            marginsForegroundColor=QColor('#ff000000'),
            marginsBackgroundColor=QColor('lightgray'),  # 行号边栏背景颜色 打开新文件后就不起作用了？

            # margin (folding)
            # Folding: (No|Plain|Circled|Boxed|CircledTree|BoxedTree)FoldStyle
            folding="BoxedTreeFoldStyle",  # 代码可折叠
            foldMarginColors=(QColor('#aad'), QColor('#bbe')),
            # marginType=(2,QsciScintilla.SC_MARGIN_SYMBOL),#页边类型
            # marginMarkerMask=(2,QsciScintilla.SC_MASK_FOLDERS),#页边掩码
            # marginSensitivity=(2,True),#注册通知事件，当用户点击边栏时，scintilla会通知我们
        )

    def configure(self, **config):
        """Configure the editor with the given settings.

        Accepts ``keyword=getValue`` arguments for any attribute ``foo`` that is
        normally set via a ``setFoo`` method.
        For example, instead of this:
            >>> editor.setEdgeColor(QFont('Courier New', 10))
            >>> editor.setEolVisibility(True)
            >>> editor.setEdgeColumn(80)
        This method allows you to do this:
            >>> editor.configure(
            ...     edgeColor = QFont('Courier New', 10),
            ...     eolVisibility = True,
            ...     edgeColumn = 80)
        """
        self.settings.update(config)

        for name, args in config.items():
            # Get the setter method ('setWhatEver')
            setter = getattr(self, 'set' + name[0].upper() + name[1:])

            # Handle setters that accept multiple arguments
            # (like marginLineNumbers)
            if isinstance(args, (tuple, list)):
                setter(*args)
            else:
                setter(args)

        # Adjust margin if line numbers are on
        if 'marginLineNumbers' in config:
            if config['marginLineNumbers'] == (0, True):
                font_metrics = QFontMetrics(self.settings['marginsFont'])  # self.marginsFont())
                self.setMarginWidth(0, font_metrics.width('000') + 5)
            else:
                self.setMarginWidth(0, 0)


    # Language and syntax highlighting
    # Note: These follow the getter/setter pattern of other QsciScintilla settings,
    # to allow `configure` to manipulate them.
    def language(self):
        """Getter for language.
        """
        if isinstance(self.lexer, QsciLexer):
            return self.lexer.language()
        return 'None'

    def setLanguage(self, language):
        """Set syntax highlighting to the given language.
        If ``language`` is ``None``, ``'None'`` or empty, then syntax highlighting is disabled.
        """
        if not language or language == 'None':
            print("Disabling syntax highlighting")
            self.lexer = None
        else:
            custom = False
            for lexer in dir(lexer_qss):
                if lexer[9:] == language:
                    custom = True
                    break

            try:
                if custom:
                    self.lexer = getattr(lexer_qss, 'QsciLexer' + language)(self)
                else:
                    self.lexer = getattr(Qsci, 'QsciLexer' + language)(self)  # lexer = QsciLexerCSS()
            except AttributeError:
                self.lexer = None
                raise AttributeError
                # print("Editor syntax highlighting language error: set to plain text.")
            # raise ValueError("Unknown language: '%s'" % language)
            self.lexer.setDefaultFont(self.font())
        print("Editor syntax highlighting language: %s" % language)
        self.setLexer(self.lexer)

    ###
    # extension: Getters setter
    # Missing Getters 只有set函数，但是没有对应get函数的属性
    # Mssing Setters
    ###
    def setBackgroundColor(self, color):
        if self.lexer:
            try:
                self.lexer.setPapers(color)
            except Exception:
                print("set backgroundcolor err.")

    def setMarginWidthes(self, *widthes):
        for i, w in widthes:
            self.setMarginWidth(i, w)

    def caretLineVisible(self):
        """Return the ``caretLineVisible`` attribute (True or False).
        """
        return self.SendScintilla(self.SCI_GETCARETLINEVISIBLE)

    def caretLineBackgroundColor(self):
        """Return the ``caretLineBackgroundColor`` as a QColor.
        """
        # TODO: Support alpha?
        bgr_int = self.SendScintilla(self.SCI_GETCARETLINEBACK)
        r, g, b = self.__bgr_int2rgb(bgr_int)
        return QColor(r, g, b)


    ###
    # Content operation
    ###
    def clear(self):
        """Clear the contents of the editor."""
        self.setText('')
        self.setModified(False)

    def load(self, filename):
        """Load the given file into the editor."""
        with open(filename, 'rb') as f:
            self.setEnabled(True)
            # lm=os.path.getsize(filename)
            strbytes = f.read()
            deteclen = min(len(strbytes), 1024)
            if not deteclen:
                self.coding = "utf-8"
                self.setText("")
            else:
                try:
                    rst = chardet.detect(strbytes[:deteclen])
                    if rst["confidence"] < 0.8:
                        deteclen = min(len(strbytes), 256 * 1024)
                        rst = chardet.detect(strbytes[:deteclen])  # ['encoding']
                    self.coding = rst["encoding"]
                    if rst["confidence"] > 0.8:
                        self.setText(strbytes.decode(self.coding))
                    else:
                        if self.__isBin(strbytes):
                            raise Exception
                        self.coding = "bin?"
                        self.setText(self.__byte2str(strbytes))
                        self.setReadOnly(True)
                        self.setLanguage("None")
                        self.setWrapMode(self.WrapWod)
                except BaseException:  # Exception:
                    self.coding = "none"
                    self.setText(self.tr("can't open this file, it may be a binary file."))
                    print("open file failue.")
                    self.setEnabled(False)
                    return False
            print("coding: " + self.coding)
            self.setModified(False)
            self.setLanguage(self.guessLang(filename))
            return True

    def save(self, filename):
        """Save the editor contents to the given filename."""
        with open(filename, 'w', newline='') as outfile:
            # 不指定newline，则换行符为各系统默认的换行符（\n, \r, or \r\n, ）
            # newline=''表示不转换
            outfile.write(self.text())
            self.setModified(False)

    ###
    # find and replace dialog
    ###
    def find(self):
        self.searchDialog.setReplaceMode(False)
        self.searchDialog.show()

    def replace(self):
        self.searchDialog.setReplaceMode(True)
        self.searchDialog.show()

    ###
    # extension: get find text infomation
    ###
    def count(self, string, *, case=False):
        """Get the count of string text appeared in editor content"""
        if case:
            counter = self.text().count(string)
        else:
            counter = self.text().lower().count(string.lower())
        return counter

    # Events
    def keyPressEvent(self, event):
        super().keyPressEvent(event)
        self.keyPress.emit(event)

    def focusOutEvent(self, e):
        super().focusOutEvent(e)
        self.loseFocus.emit()

    def leaveEvent(self, objEvent):
        self.mouseLeave.emit()

    def mousePressEvent(self, objQMouseEvent):
        super().mousePressEvent(objQMouseEvent)
        self.mousePress.emit()

    def dropEvent(self, objQDropEvent):
        if objQDropEvent.mimeData().hasUrls():
            self.drop.emit(objQDropEvent)
