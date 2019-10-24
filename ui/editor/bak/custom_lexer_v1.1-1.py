# -*- coding: utf-8 -*-
"""
Copyright (c) 2019 lileilei <hustlei@sina.cn>
"""
from PyQt5.Qsci import QsciLexerCSS
from PyQt5.QtGui import QColor


class QsciLexerQSS(QsciLexerCSS):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setDefault()
        if(parent is not None):
            font = parent.font()
            font.setBold(False)
            # QFont::Light 25 Normal 50 DemiBold 63 Bold 75 Black 87
            font.setWeight(font.Light)
            self.setFont(font, QsciLexerQSS.Comment)  # QsciLexerQSS.Comment=9

    def setDefault(self):
        # high light code
        # self.setColor(QColor("#ffffff"))
        # self.setPaper(QColor("#333333"))
        # self.setColor(QColor("#5BA5F7"), QsciLexerPython.ClassName)
        # self.setColor(QColor("#FF0B66"), QsciLexerPython.Keyword)
        self.setColor(QColor("gray"), QsciLexerCSS.Comment)
        #self.setFont(self.font(), QsciLexerCSS.Comment)
        # self.setColor(QColor("#BD4FE8"), QsciLexerPython.Number)
        # self.setColor(QColor("#F1E607"), QsciLexerPython.DoubleQuotedString)
        # self.setColor(QColor("#F1E607"), QsciLexerPython.TripleSingleQuotedString)
        # self.setColor(QColor("#F1E607"), QsciLexerPython.TripleDoubleQuotedString)
        # self.setColor(QColor("#F1E607"), QsciLexerPython.DoubleQuotedString)
        # self.setColor(QColor("#04F452"), QsciLexerPython.FunctionMethodName)
        # self.setColor(QColor("#FFFFFF"), QsciLexerPython.Operator)
        # self.setColor(QColor("#FFFFFF"), QsciLexerPython.Identifier)
        # self.setColor(QColor("#F1E607"), QsciLexerPython.CommentBlock)
        # self.setColor(QColor("#F1E607"), QsciLexerPython.UnclosedString)
        # self.setColor(QColor("#F1E607"), QsciLexerPython.HighlightedIdentifier)
        # self.setColor(QColor("#F1E607"), QsciLexerPython.Decorator)

        # marker
        # self.markerDefine(QsciScintilla.Minus, QsciScintilla.SC_MARKNUM_FOLDEROPEN)
        # self.markerDefine(QsciScintilla.Plus, QsciScintilla.SC_MARKNUM_FOLDER)
        # self.markerDefine(QsciScintilla.Minus, QsciScintilla.SC_MARKNUM_FOLDEROPENMID)
        # self.markerDefine(QsciScintilla.Plus, QsciScintilla.SC_MARKNUM_FOLDEREND)

        # marker define color
        # self.setMarkerBackgroundColor(QColor("#FFFFFF"), QsciScintilla.SC_MARKNUM_FOLDEREND)
        # self.setMarkerForegroundColor(QColor("#272727"), QsciScintilla.SC_MARKNUM_FOLDEREND)
        # self.setMarkerBackgroundColor(QColor("#FFFFFF"), QsciScintilla.SC_MARKNUM_FOLDEROPENMID)
        # self.setMarkerForegroundColor(QColor("#272727"), QsciScintilla.SC_MARKNUM_FOLDEROPENMID)
        # self.setMarkerBackgroundColor(QColor("#FFFFFF"),QsciScintilla.SC_MARKNUM_FOLDERMIDTAIL)
        # self.setMarkerForegroundColor(QColor("#272727"),QsciScintilla.SC_MARKNUM_FOLDERMIDTAIL)
        # self.setMarkerBackgroundColor(QColor("#FFFFFF"),QsciScintilla.SC_MARKNUM_FOLDERTAIL)
        # self.setMarkerForegroundColor(QColor("#272727"),QsciScintilla.SC_MARKNUM_FOLDERTAIL)
        # self.setMarkerBackgroundColor(QColor("#FFFFFF"), QsciScintilla.SC_MARKNUM_FOLDERSUB)
        # self.setMarkerForegroundColor(QColor("#272727"), QsciScintilla.SC_MARKNUM_FOLDERSUB)
        # self.setMarkerBackgroundColor(QColor("#FFFFFF"), QsciScintilla.SC_MARKNUM_FOLDER)
        # self.setMarkerForegroundColor(QColor("#272727"), QsciScintilla.SC_MARKNUM_FOLDER)
        # self.setMarkerBackgroundColor(QColor("#FFFFFF"), QsciScintilla.SC_MARKNUM_FOLDEROPEN)
        # self.setMarkerForegroundColor(QColor("#272727"),
        # QsciScintilla.SC_MARKNUM_FOLDEROPEN)

        # self.SCI_MARKERDEFINE(QsciScintilla.SC_MARKNUM_FOLDEROPEN,QsciScintilla.SC_MARK_CHARACTER+65)#折叠标签样式
        # self.markerDefine(QsciScintilla.SC_MARKNUM_FOLDEROPEN, QsciScintilla.BoxedMinus)
        # self.markerDefine(QsciScintilla.SC_MARKNUM_FOLDEREND, QsciScintilla.SC_MARK_BOXPLUSCONNECTED)
        # self.markerDefine(QsciScintilla.SC_MARKNUM_FOLDEROPENMID, QsciScintilla.SC_MARK_BOXMINUSCONNECTED)
        # self.markerDefine(QsciScintilla.SC_MARKNUM_FOLDERMIDTAIL, QsciScintilla.SC_MARK_TCORNERCURVE)
        # self.markerDefine(QsciScintilla.SC_MARKNUM_FOLDERSUB, QsciScintilla.SC_MARK_VLINE)
        # self.markerDefine(QsciScintilla.SC_MARKNUM_FOLDERTAIL, QsciScintilla.SC_MARK_LCORNERCURVE)
        # 折叠标签颜色
        # self.setMarkerBackgroundColor(QColor("0xa0a0a0"),QsciScintilla.SC_MARKNUM_FOLDERSUB )
        # SendEditor(SCI_MARKERSETBACK, SC_MARKNUM_FOLDERMIDTAIL, 0xa0a0a0);
        # SendEditor(SCI_MARKERSETBACK, SC_MARKNUM_FOLDERTAIL, 0xa0a0a0);
        # SendEditor(SCI_SETFOLDFLAGS, 16 | 4, 0); // 如果折叠就在折叠行的上下各画一条横线

    @staticmethod
    def language():
        return "QSS"

    # def setDefaultFont(self, font):
    #     self.setFont(font)#super()不起作用
    #     font.setBold(False)
    #     font.setWeight(font.Light)#QFont::Light 25 Normal 50 DemiBold 63 Bold 75 Black 87
    #     self.setFont(font, 9)#QsciLexerQSS.Comment)

    # def setDefaultFont(self,font):
    #     super(QsciLexerQSS,self).setDefaultFont(font)
    #     super(QsciLexerQSS,self).setFont(font, QsciLexerQSS.Comment)
