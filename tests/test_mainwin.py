# -*- coding: utf-8 -*-
"""test for ui module.

Copyright (c) 2019 lileilei <hustlei@sina.cn>
"""

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from unittest import mock

from PyQt5.QtWidgets import QApplication

def test_findDialog(qtbot, sharedwin):
    win = sharedwin["main"]
    win.editor.searchDialog.show()
    qtbot.waitForWindowShown(win.editor.searchDialog)

def test_theme(sharedwin):
    win = sharedwin["main"]
    win.actions["DisableQss"].setChecked(True)
    win.actions["DisableQss"].setChecked(False)
    win.actions["DisableQss"].setChecked(True)
    win.themeCombo.setCurrentIndex(win.themeCombo.maxCount() - 1)
    assert win.actions["DisableQss"].isChecked()

def test_var_refresh(qtbot, sharedwin):
    win = sharedwin["main"]
    qtbot.keyPress(win.editor, Qt.Key_Up)
    assert "*" not in win.windowTitle()

def test_preivew(qtbot, sharedwin):
    sharedwin["main"].docks["preview"].widget().setCurrentIndex(2)
    # qtbot.waitForWindowShown(windows["main"])
    with mock.patch.object(QApplication, "exit"):
        assert QApplication.exit.call_count == 0

def test_confDialog(qtbot, sharedwin):
    sharedwin["main"].confDialog.show()
    qtbot.waitForWindowShown(sharedwin["main"].confDialog)


def test_fileop_and_clrpic(qapp, qtbot, mainwin, tmpdir):
    """Test file new and save, test color pick, this test will effect editor text
    """
    def file():
        mainwin.new()
        f = tmpdir.join("new.qsst").ensure()
        # f.write("") # create file new.qsst
        mainwin.file = str(f)
        mainwin.save()
        assert not mainwin.editor.text()
    file()
    mainwin.newFromTemplate()
    mainwin.editor.setModified(False)

    def closeclrdialog():
        while not qapp.activeModalWidget():
            qtbot.wait(100)
        qtbot.wait(200)
        dial = qapp.activeModalWidget()
        qapp.processEvents()
        # dial.setCurrentColor(QColor(255,0,0)) # must in ui thread
        # qapp.processEvents()
        # dial.done(0)    # dial.close()
        qtbot.keyPress(dial, Qt.Key_Enter)
        # qtbot.keyPress(qapp.focusWidget(), Qt.Key_Return, delay=50)

    from threading import Thread
    t1 = Thread(target=closeclrdialog)
    t1.start()
    qtbot.mouseClick(mainwin.clrBtnDict["text"], Qt.LeftButton)
    t1.join()
    qapp.processEvents()
    qtbot.wait(200)
    assert mainwin.clrBtnDict["text"].text() == "#222222"
