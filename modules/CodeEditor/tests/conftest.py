# -*- coding: utf-8 -*-
"""Fixture for pytest"""

from pytest import fixture

import sys
from PyQt5.QtWidgets import QApplication
#from CodeEditor import Editor

# @fixture(scope="function")
# def editor():
#     app = QApplication(sys.argv)
#     editor = Editor()
#     yield editor
#     del editor
#     app.quit()
