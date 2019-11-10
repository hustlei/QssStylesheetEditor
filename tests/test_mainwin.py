# -*- coding: utf-8 -*-
"""test for ui module.

Copyright (c) 2019 lileilei <hustlei@sina.cn>
"""


def test_confDialog(qtbot, windows):
    windows["main"].confDialog.show()
    qtbot.waitForWindowShown(windows["main"].confDialog)


def test_findDialog(qtbot, windows):
    windows["main"].editor.searchDialog.show()
    qtbot.waitForWindowShown(windows["main"].editor.searchDialog)


def test_mainwin(qtbot, windows):
    windows["main"].show()
    qtbot.waitForWindowShown(windows["main"])
