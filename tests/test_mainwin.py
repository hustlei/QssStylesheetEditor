# -*- coding: utf-8 -*-
"""
test for ui module.

Copyright (c) 2019 lileilei <hustlei@sina.cn>
"""

import sys
import os
from ui.mainwin import MainWin

sys.path.append(os.path.abspath('..'))


def test_mainwin(qtbot):
    win = MainWin()
    win.show()
    qtbot.waitForWindowShown(win)
