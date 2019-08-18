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
from .EditorEnums import enum_string, QsciEnumDict, BadQsciEnum
from .EditorSettings import *

__version__ = "1.0"

class CodeEditor(QsciScintilla):
    keyPress=pyqtSignal(QKeyEvent)
    loseFocus=pyqtSignal()
    mouseLeave=pyqtSignal()
    mousePress=pyqtSignal()
    def __init__(self):
        super().__init__()
        self._set_default_config()
        # Override defaults with any customizations
        self.configure(**config)

        #self.setEolMode(self.SC_EOL_LF)    # 以\n换行
        self.setWrapMode(self.WrapWord)    # 自动换行。self.WrapWord是父类QsciScintilla的
        self.setAutoIndent(True)  # 换行后自动缩进
        self.setIndentationGuides(QsciScintilla.SC_IV_LOOKBOTH)#设置缩进的显示方式
        self.setUtf8(True)  # 支持中文字符
        #self.setFont(QFont('Courier,Consolas', 12))  # 设置默认字体
        self.setMarginType(0, QsciScintilla.NumberMargin)  #设置编号为0的边显示行号
        #页边是显示区左边的竖条区，可以显示行号、书签、断点标记等。Scintilla最多可以有5个页边（从左到右的编号为0~4）,默认是只显示宽度为16的1号页边。
        # 每个页边可以使用SCI_SETMARGINTYPEN命令确定是用于显示行号还是符号,
        self.setMarginLineNumbers(0, True)   # 第0个左边栏启用行号,不太明白什么用
        self.setMarginWidth(0, 30)  # 设置边栏宽度，设置宽度为0表示不显示
        self.setMarginWidth(1, 0)  # 设置边栏宽度，设置宽度为0表示不显示
        #self.setMarginsBackgroundColor(Qt.gray)  # 行号边栏背景颜色
        self.setCaretLineVisible(True)
        self.setCaretLineBackgroundColor(Qt.lightGray)

        self.setFolding(True)  # 代码可折叠
        #self.setMarginWidth(2,12)
        #self.setMarginType(2,QsciScintilla.SC_MARGIN_SYMBOL)#页边类型
        self.setMarginMarkerMask(2,QsciScintilla.SC_MASK_FOLDERS)#页边掩码
        self.setMarginSensitivity(2,True)#注册通知事件，当用户点击边栏时，scintilla会通知我们
        self.SCI_MARKERDEFINE(QsciScintilla.SC_MARKNUM_FOLDEROPEN,QsciScintilla.SC_MARK_CHARACTER+65)#折叠标签样式
        self.markerDefine(QsciScintilla.SC_MARKNUM_FOLDEROPEN, QsciScintilla.BoxedMinus)
        # self.markerDefine(QsciScintilla.SC_MARKNUM_FOLDEREND, QsciScintilla.SC_MARK_BOXPLUSCONNECTED)
        # self.markerDefine(QsciScintilla.SC_MARKNUM_FOLDEROPENMID, QsciScintilla.SC_MARK_BOXMINUSCONNECTED)
        # self.markerDefine(QsciScintilla.SC_MARKNUM_FOLDERMIDTAIL, QsciScintilla.SC_MARK_TCORNERCURVE)
        # self.markerDefine(QsciScintilla.SC_MARKNUM_FOLDERSUB, QsciScintilla.SC_MARK_VLINE)
        # self.markerDefine(QsciScintilla.SC_MARKNUM_FOLDERTAIL, QsciScintilla.SC_MARK_LCORNERCURVE)
        #折叠标签颜色
        #self.setMarkerBackgroundColor(QColor("0xa0a0a0"),QsciScintilla.SC_MARKNUM_FOLDERSUB )
        # SendEditor(SCI_MARKERSETBACK, SC_MARKNUM_FOLDERMIDTAIL, 0xa0a0a0);
        # SendEditor(SCI_MARKERSETBACK, SC_MARKNUM_FOLDERTAIL, 0xa0a0a0);
        # SendEditor(SCI_SETFOLDFLAGS, 16 | 4, 0); // 如果折叠就在折叠行的上下各画一条横线

        self.setAutoCompletionSource(self.AcsAll)  # 自动补全。对于所有Ascii字符
        self.setAutoCompletionCaseSensitivity(False)  # 自动补全大小写敏感
        self.setAutoCompletionThreshold(1)  # 输入多少个字符才弹出补全提示
        self.setBraceMatching(QsciScintilla.SloppyBraceMatch)#设置括号匹配

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


    def _set_default_config(self):
        """Set default configuration settings.
        """
        self.configure(
            language = 'None',

            # Flags and numeric values
            tabIndents = True,
            tabWidth = 4,
            indentationsUseTabs = False,
            backspaceUnindents = True,
            autoIndent = False,
            indentationGuides = False,
            eolVisibility = False,
            edgeColumn = 80,
            caretLineVisible = True,
            marginLineNumbers = (0, True),

            # Fonts
            font = QFont('Courier New', 10),
            marginsFont = QFont('Courier New', 10),

            # Colors
            edgeColor = QColor('#FF0000'),
            caretLineBackgroundColor =QColor('#F0F0F0'),
            marginsBackgroundColor = QColor('#C0C0C0'),
            marginsForegroundColor = QColor('#000000'),
            foldMarginColors = (QColor('#AAAAFF'), QColor('#333300')),

            # Whitespace: Ws(Invisible|Visible|VisibleAfterIndent)
            whitespaceVisibility = 'WsInvisible',
            # Edge mode: Edge(None|Line|Background)
            edgeMode = 'EdgeLine',
            # Brace matching: (No|Strict|Sloppy)BraceMatch
            braceMatching = 'SloppyBraceMatch',
            # Folding: (No|Plain|Circled|Boxed|CircledTree|BoxedTree)FoldStyle
            folding = 'NoFoldStyle',
            # Wrap mode: Wrap(None|Word|Character)
            wrapMode = 'WrapWord',
        )


    ###
    ### Extensions
    ###

    def get_config(self, name, *args):
        """Return the current configuration setting for attribute ``name``.
        If ``name`` refers to an enumerated setting, return the string version
        of that enumeration.
        """
        getter = getattr(self, name)
        value = getter(*args)
        try:
            return enum_string(value)
        except BadQsciEnum:
            return value


    def set_config(self, name, value):
        """Set the current configuration setting for attribute ``name``.
        """
        conf = {name: value}
        self.configure(**conf)


    def configure(self, **config):
        """Configure the editor with the given settings.
        Accepts ``keyword=value`` arguments for any attribute ``foo`` that is
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
        print(QsciEnumDict)
        for name, args in config.items():
            # Get the setter method ('setWhatEver')
            setter = getattr(self, 'set' + name[0].upper() + name[1:])

            # Handle setters that accept multiple arguments
            # (like marginLineNumbers)
            if isinstance(args, (tuple, list)):
                setter(*args)

            # Convert strings to enum value
            elif args in QsciEnumDict:
                setter(QsciEnumDict[args])

            # Single-argument setting
            else:
                setter(args)

        # Adjust margin if line numbers are on
        if 'marginLineNumbers' in config:
            if config['marginLineNumbers'] == (0, True):
                font_metrics = QtGui.QFontMetrics(self.font())
                self.setMarginWidth(0, font_metrics.width('00000') + 5)
            else:
                self.setMarginWidth(0, 0)


    def line_rect(self, line_number):
        """Return (x, y, width, height) of the text on ``line_number``.
        """
        pos = self.positionFromLineIndex(line_number, 0)
        x = self.SendScintilla(self.SCI_POINTXFROMPOSITION, 0, pos)
        y = self.SendScintilla(self.SCI_POINTYFROMPOSITION, 0, pos)
        # FIXME: Do we need to use a specific styleNumber here?
        width = self.SendScintilla(self.SCI_TEXTWIDTH, 0, self.text(line_number))
        height = self.textHeight(line_number)

        return (x, y, width, height)


    # Buffer content operations

    def modified(self, set_modified=None):
        """Get or set the modification status of the editor.
        If ``set_modified`` is True or False, set the modification status;
        otherwise, return current modification status (True or False).
        """
        if set_modified in (True, False):
            self.setModified(set_modified)
        else:
            return self.isModified()


    def clear(self):
        """Clear the contents of the editor.
        """
        self.setText('')
        self.modified(False)


    def load(self, filename):
        """Load the given file into the editor.
        """
        infile = open(filename, 'r')
        self.setText(''.join(infile.readlines()))
        self.modified(False)
        self.setHightlightLang(guess_language(filename))


    def save(self, filename):
        """Save the editor contents to the given filename.
        """
        outfile = open(filename, 'w')
        outfile.write(self.text())
        self.modified(False)

        QtGui.QMessageBox.information(self, 'Success', 'Saved: "%s"' % filename)


    # Language and syntax highlighting
    # Note: These follow the getter/setter pattern of other
    # QsciScintilla settings, to allow `configure` to manipulate them.

    def language(self):
        """Getter for language.
        """
        lexer = self.lexer()
        if lexer:
            return lexer.language()
        else:
            return 'None'


    def setHightlightLang(self, language):
        """Set syntax highlighting to the given language.
        If ``language`` is ``None``, ``'None'`` or empty, then
        syntax highlighting is disabled.
        """
        if not language or language == 'None':
            print("Disabling syntax highlighting")
            lexer = None
        else:
            print("%s syntax highlighting" % language)
            try:
                lexer = getattr(Qsci, 'QsciLexer%s' % language)(self)
            except AttributeError:
                raise ValueError("Unknown language: '%s'" % language)
            lexer.setFont(self.font())

        self.setLexer(lexer)


    ###
    ### The Missing Getters
    ###

    def caretLineVisible(self):
        """Return the ``caretLineVisible`` attribute (True or False).
        """
        return self.SendScintilla(self.SCI_GETCARETLINEVISIBLE)


    def caretLineBackgroundColor(self):
        """Return the ``caretLineBackgroundColor`` as a QColor.
        """
        # TODO: Support alpha?
        bgr_int = self.SendScintilla(self.SCI_GETCARETLINEBACK)
        r, g, b = bgr_int_to_rgb(bgr_int)
        return QtGui.QColor(r, g, b)

    def guess_language(self,filename):
        """Guess the language based on the given filename's extension, and return
        the name of the language, or the string 'None' if no extension matches.
        """
        # Get the file's extension
        root, ext = os.path.splitext(filename)

        # See if any known language extensions match
        for language, extensions in language_extensions:
            if ext in extensions.split(' '):
                return language

        # No match -- asume plain text
        return 'None'