# -*- coding: utf-8 -*-
"""test for ui module.

Copyright (c) 2019 lileilei <hustlei@sina.cn>
"""

from PyQt5.QtCore import Qt, QThread

from PyQt5.QtWidgets import QApplication


class TestMain():
    @classmethod
    def setup_class(cls):
        print("\nsetup_class       class:%s" % cls.__name__)

    @classmethod
    def teardown_class(cls):
        print("teardown_class    class:%s" % cls.__name__)

    def setup_method(self, method):
        print("setup_method      method:%s" % method.__name__)

    def teardown_method(self, method):
        print("teardown_method   method:%s" % method.__name__)

    def test_find_dialog(cls, qtbot, sharedwin):
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
        TestMain.preivew(sharedwin)
        assert win.actions["DisableQss"].isChecked()

    def test_var_refresh(self, qtbot, sharedwin):
        win = sharedwin["main"]
        qtbot.keyPress(win.editor, Qt.Key_Up)
        assert "*" not in win.windowTitle()

    def test_confDialog(self, qtbot, sharedwin):
        sharedwin["main"].confDialog.show()
        qtbot.waitForWindowShown(sharedwin["main"].confDialog)

    def test_fileop_and_clrpic(self, qapp, qtbot, sharedwin, tmpdir):
        """Test file new and save, test color pick, this test will effect CodeEditor text
        """
        mainwin = sharedwin["main"]

        def file():
            mainwin.new()
            f = tmpdir.join("new.qsst").ensure()
            mainwin.file = str(f)
            mainwin.save()
            assert not mainwin.editor.text()

        file()
        mainwin.newFromTemplate()
        mainwin.editor.setModified(False)

        import sys
        if sys.platform.startswith('win'):

            class DialogCloseThread(QThread):
                def __init__(self, parent=None):
                    super().__init__(parent)

                def run(self):
                    while not qapp.activeModalWidget():
                        qtbot.wait(10)
                    dial = qapp.activeModalWidget()
                    qtbot.keyPress(dial, Qt.Key_Enter)

            t1 = DialogCloseThread()
            t1.finished.connect(lambda: print("t1 finished"))
            t1.start()
            qtbot.mouseClick(mainwin.clrBtnDict["text"], Qt.LeftButton)
            t1.wait()
            t1.quit()
            del t1
            assert mainwin.clrBtnDict["text"].text() == "#222222" or mainwin.clrBtnDict["text"].text() == "#222"
