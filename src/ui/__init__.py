# -*- coding: utf-8 -*-
"""win and widgets for app

Copyright (c) 2019 lileilei <hustlei@sina.cn>
"""

from .mainwinbase import MainWinBase


def preload():
    """import all modules, user can call this method in splash to accelorate app.
    but it may consume more memory.
    """
    from .preview import PreviewWidget
    from .flow_layout import QFlowLayout
