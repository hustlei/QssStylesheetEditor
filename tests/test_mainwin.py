# -*- coding: utf-8 -*-
"""test for ui module.

Copyright (c) 2019 lileilei <hustlei@sina.cn>
"""

from PyQt5.QtCore import Qt
# from PyQt5.QtGui import QColor
# from unittest import mock

from PyQt5.QtWidgets import QApplication


class TestMain():
    def test_find_dialog(self, qtbot, sharedwin):
        win = sharedwin["main"]
        win.editor.searchDialog.show()
        qtbot.waitForWindowShown(win.editor.searchDialog)

    @staticmethod
    def preivew(sharedwin):
        sharedwin["main"].docks["preview"].widget().setCurrentIndex(2)
        # qtbot.waitForWindowShown(windows["main"])
        # with mock.patch.object(QApplication, "exit"):
        #     assert QApplication.exit.call_count == 0

    def test_theme(self, sharedwin):
        win = sharedwin["main"]
        win.actions["DisableQss"].setChecked(True)
        win.actions["DisableQss"].setChecked(False)
        win.actions["DisableQss"].setChecked(True)
        win.themeCombo.setCurrentIndex(win.themeCombo.maxCount() - 1)
        assert win.actions["DisableQss"].isChecked()
        TestMain.preivew(sharedwin)

    def test_var_refresh(self, qtbot, sharedwin):
        win = sharedwin["main"]
        qtbot.keyPress(win.editor, Qt.Key_Up)
        assert "*" not in win.windowTitle()

    def test_confDialog(self, qtbot, sharedwin):
        sharedwin["main"].confDialog.show()
        qtbot.waitForWindowShown(sharedwin["main"].confDialog)
