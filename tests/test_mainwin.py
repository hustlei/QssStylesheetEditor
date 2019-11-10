# -*- coding: utf-8 -*-
"""test for ui module.

Copyright (c) 2019 lileilei <hustlei@sina.cn>
"""

# from PyQt5.QtCore import Qt
from unittest import mock

from PyQt5.QtWidgets import QApplication


def test_confDialog(qtbot, windows):
    windows["main"].confDialog.show()
    qtbot.waitForWindowShown(windows["main"].confDialog)


def test_findDialog(qtbot, windows):
    windows["main"].editor.searchDialog.show()
    qtbot.waitForWindowShown(windows["main"].editor.searchDialog)


def test_theme(windows):
    win = windows["main"]
    win.actions["DisableQss"].setChecked(True)
    win.themeCombo.setCurrentIndex(win.themeCombo.maxCount() - 1)
    assert win.actions["DisableQss"].isChecked()


# def test_clrpic(qtbot, windows, monkeypatch):
#     win=windows["main"]
#     qtbot.mouseClick(win.clrBtnDict["text"], Qt.LeftButton)
#     qtbot.wait(1)
#     # qtbot.keyPress(win.focusWidget(), Qt.Key_Return, delay=100)
#     # qtbot.keyPress(win.focusWidget(), Qt.Key_Enter)
#     assert win.clrBtnDict["text"].text() == "#222222"


def test_file(windows, tmpdir):
    win = windows["main"]
    win.new()
    f = tmpdir.join("new.qsst").ensure()
    # f.write("") # create file new.qsst
    win.file = str(f)
    win.save()
    assert not win.editor.text()


def test_mainwin(qtbot, windows):
    windows["main"].show()
    # qtbot.waitForWindowShown(windows["main"])
    with mock.patch.object(QApplication, "exit"):
        windows["main"].close()
        assert QApplication.exit.call_count == 0
