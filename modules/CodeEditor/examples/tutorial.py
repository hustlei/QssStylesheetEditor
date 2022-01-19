# -*- coding: utf-8 -*-
"""Tutorial for using CodeEditor package.

Copyright (c) 2019 lileilei. <hustlei@sina.cn>
"""

import sys

from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout

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
from PyQt5.Qsci import QsciScintilla

edt.setEdgeMode(QsciScintilla.EdgeLine)

### another way to config editor ###
# edt.settings.configure(color="#0000FF", fontSize=20, edgeMode="EdgeLine")
## or ##
# edt.settings.set("color", "#0000FF")

# get settings
color = edt.getConfig("Color")  # QColor("#FF0000")
colorfortoml = edt.settings.get("Color")  # "#FF0000"

edt.show()
sys.exit(app.exec_())
