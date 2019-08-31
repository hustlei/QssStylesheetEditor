# -*- coding: utf-8 -*-

import sys,os
os.chdir(os.path.dirname(__file__))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtWidgets import QApplication

def main():
    #sys.setrecursionlimit(1500)
    app = QApplication(sys.argv)
    print("starting...")
    from ui.splash import SplashScreen
    splash = SplashScreen("img/splash.png")
    splash.loadProgress()
    from ui.mainwin import MainWin
    win = MainWin()
    win.show()
    splash.finish(win)

    sys.exit(app.exec_())

main()
