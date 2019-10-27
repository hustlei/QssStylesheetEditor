#!/usr/bin/python
# -*- coding: utf-8 -*-
"""QssStylesheetEditor app start module

Create QApplication and show splash. Include minimal module to accelerate spalsh load.

Copyright (c) 2019 lileilei <hustlei@sina.cn>
"""

import sys
import os
from PyQt5.QtWidgets import QApplication
from ui.splash import SplashScreen
from i18n.language import Language
try:
    os.chdir(os.path.dirname(__file__))
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
except Exception:
    print('__file__ of app.py load err')


def main():
    """
    main function for start QssStylesheetEditor
    """
    # sys.setrecursionlimit(1500)
    app = QApplication(sys.argv)
    print("starting...")
    Language.setTrans()
    splash = SplashScreen("res/splash.png")
    splash.loadProgress()
    from ui.mainwin import MainWin
    win = MainWin()
    win.show()
    splash.finish(win)
    sys.exit(app.exec_())


main()
