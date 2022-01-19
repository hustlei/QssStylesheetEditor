# -*- coding: utf-8 -*-
"""custom lexers for text

Copyright (c) 2019 lileilei. <hustlei@sina.cn>
"""

from PyQt5.Qsci import QsciLexerCustom


class QsciLexerText(QsciLexerCustom):
    """Lexer for styling normal text documents"""
    # Class variables
    styles = {"Default": 0}

    def __init__(self, parent=None):
        """Overridden initialization"""
        # Initialize superclass
        super().__init__()
        # Reset autoindentation style
        self.setAutoIndentStyle(0)

    def language(self):
        return "Plain text"

    def description(self, style):
        if style == 0:
            description = "Text"
        else:
            description = ""
        return description

    def styleText(self, start, end):
        self.startStyling(start)
        self.setStyling(end - start, 0)
