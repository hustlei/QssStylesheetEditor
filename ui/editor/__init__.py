# -*- coding: utf-8 -*-
"""
Copyright (c) 2019 lileilei <hustlei@sina.cn>
"""
import sys
import os
from .editor import CodeEditor
from .settings import EditorSettings


def preload():
    from PyQt5.Qsci import QsciLexer, QsciAPIs, QsciCommand, QsciDocument, QsciStyle
    from PyQt5 import Qsci
    from .enums import BadEnum, EditorEnums
    from .settings import EditorSettings, language_extensions, _settings, _setting_groups, _other_color_settings
    from ..editor import custom_lexer
    from .search import searchDialog
