import os,sys
sys.path.append(os.path.abspath('..'))
from ui.mainwin import MainWin

def test_mainwin(qtbot):
    win=MainWin()
    win.show()
    qtbot.waitForWindowShown(win)
    