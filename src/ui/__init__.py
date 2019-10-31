# -*- coding: utf-8 -*-
"""
Copyright (c) 2019 lileilei <hustlei@sina.cn>
"""


def redirect():
    """
    redirect classes in submodule to current module
    """
    from .mainwinbase import MainWinBase


def preload():
    """
    import all modules, user can call this method in splash to accelorate app.
    but it may consume more memory.
    """
    from .preview import previewWidget
    from .flow_layout import QFlowLayout


redirect()
