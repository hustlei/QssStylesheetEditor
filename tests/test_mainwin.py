# -*- coding: utf-8 -*-
"""test for ui module.

Copyright (c) 2019 lileilei <hustlei@sina.cn>
"""

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from unittest import mock

from PyQt5.QtWidgets import QApplication


def test_confDialog(qtbot, windows):
    windows["main"].confDialog.show()
    qtbot.waitForWindowShown(windows["main"].confDialog)


def test_findDialog(qtbot, mainwin):
    mainwin.editor.searchDialog.show()
    qtbot.waitForWindowShown(mainwin.editor.searchDialog)


def test_theme(windows):
    win = windows["main"]
    win.actions["DisableQss"].setChecked(True)
    win.actions["DisableQss"].setChecked(False)
    win.actions["DisableQss"].setChecked(True)
    win.themeCombo.setCurrentIndex(win.themeCombo.maxCount() - 1)
    assert win.actions["DisableQss"].isChecked()


def test_clrpic(qapp, qtbot, mainwin):
    def closedialog():
        while not qapp.activeModalWidget():
            qtbot.wait(100)
        qtbot.wait(200)
        dial=qapp.activeModalWidget()
        qapp.processEvents()
        # dial.setCurrentColor(QColor(255,0,0)) # must in ui thread
        # qapp.processEvents()
        # dial.done(0)    # dial.close()
        qtbot.keyPress(dial, Qt.Key_Enter)
        # qtbot.keyPress(qapp.focusWidget(), Qt.Key_Return, delay=50)
    from threading import Thread
    t1=Thread(target=closedialog)
    t1.start()
    qtbot.mouseClick(mainwin.clrBtnDict["text"], Qt.LeftButton)
    t1.join()
    qapp.processEvents()
    qtbot.wait(200)
    assert mainwin.clrBtnDict["text"].text() == "#222222"

def test_file(windows, tmpdir):
    win = windows["main"]
    win.new()
    f = tmpdir.join("new.qsst").ensure()
    # f.write("") # create file new.qsst
    win.file = str(f)
    win.save()
    assert not win.editor.text()

def test_textchange(qtbot, windows):
    win = windows["main"]
    qtbot.keyPress(win.editor, Qt.Key_Up)
    assert "*" not in win.windowTitle()

def test_win(qtbot, windows):
    windows["main"].show()
    windows["main"].docks["preview"].widget().setCurrentIndex(2)
    # qtbot.waitForWindowShown(windows["main"])
    with mock.patch.object(QApplication, "exit"):
        assert QApplication.exit.call_count == 0
