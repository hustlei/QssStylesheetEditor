# -*- coding: utf-8 -*-
"""Tutorial for using CodeEditor package.

Copyright (c) 2019 lileilei. <hustlei@sina.cn>
"""

import sys

from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout
from PyQt5.QtCore import Qt

sys.path.append("..")
from CodeEditor import Editor

# create application
app = QApplication(sys.argv)
# create editor
edt = Editor()
text = """床前明月光，
疑是地上霜。
举头望明月，
低头思故乡。"""
edt.setText(text)
# config color and font
edt.setLanguage("Text")
edt.setColor(QColor("#FF0000"))
edt.setFontSize(20)
edt.setFontFamily("Microsoft YaHei")
from PyQt5.Qsci import QsciScintilla
edt.setEdgeMode(QsciScintilla.EdgeLine)

### second way to config editor ###
# edt.configure(color=QColor("#00FF00"), fontSize=20, edgeMode=QsciScintilla.EdgeLine)
## or ##
# edt.setConfig('color', QColor("#00FF00"))

### third way to config editor ###
# edt.settings.configure(color="#0000FF", fontSize=20, edgeMode="EdgeLine")
## or ##
# edt.settings.set("color", "#0000FF")

edt.show()
sys.exit(app.exec_())
