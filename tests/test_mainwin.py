# -*- coding: utf-8 -*-
"""
test for ui module.

Copyright (c) 2019 lileilei <hustlei@sina.cn>
"""

import sys
import os
from pytest import fixture
from ui.mainwin import MainWin

sys.path.append(os.path.abspath('..'))

@fixture
def win():
    win = MainWin()
    return win



def test_mainwin(qtbot, win):
    win.show()
    qtbot.waitForWindowShown(win)
