import sys

from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout
from PyQt5.QtCore import Qt

sys.path.append("..")
from CodeEditor import Editor

app = QApplication(sys.argv)
win = QWidget()
layout = QHBoxLayout()

edt = Editor()
text = """床前明月光，
疑是地上霜。
举头望明月，
低头思故乡。"""
edt.setText(text)
# edt.configure(language="CPP") # some error exist if convert language from lexers to None
# edt.configure(language=None)
edt.setLanguage(None)
edt.setColor(QColor("#FF0000"))
edt.setFontSize(20)
edt.setFontFamily("Microsoft YaHei")

layout.addWidget(edt)
win.setLayout(layout)
win.show()
sys.exit(app.exec_())
