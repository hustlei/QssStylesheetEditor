# -*- coding: utf-8 -*-
"""
Copyright (c) 2019 lileilei <hustlei@sina.cn>
"""
from .editor import CodeEditor
from .settings import EditorSettings


def preload():
    from .enums import BadEnum, EditorEnums
    from .settings import EditorSettings, language_extensions, _settings, _setting_groups, _other_color_settings
    from ui.editor.lexer import lexer_qss
    from .search import searchDialog
