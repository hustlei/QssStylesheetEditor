# -*- coding: utf-8 -*-
"""test for file operation and color pic.

Copyright (c) 2019 lileilei <hustlei@sina.cn>
"""

from PyQt5.QtCore import Qt


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
        import os
        os._exit(0)  # exit thread

    from threading import Thread
    t1 = Thread(target=closeclrdialog)
    t1.start()
    qtbot.mouseClick(mainwin.clrBtnDict["text"], Qt.LeftButton)
    t1.join()
    qapp.processEvents()
    qtbot.wait(200)
    assert mainwin.clrBtnDict["text"].text() == "#222222"
