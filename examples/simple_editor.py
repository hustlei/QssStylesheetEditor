

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton
sys.path.append("..")
from CodeEditor import Editor, EditorSettings

app = QApplication(sys.argv)
win = QWidget()
layout = QHBoxLayout()
win.setLayout(layout)

ed = Editor()
confpannel = QWidget(win)
conflayout = QVBoxLayout()
confpannel.setLayout(conflayout)

setting = EditorSettings(ed)
conflayout.addLayout(setting.defaultLayout())
btcancel = QPushButton("Cancel")
btcancel.clicked.connect(setting.cancel)
btok = QPushButton("Apply")
btok.clicked.connect(setting.apply)
layout1 = QHBoxLayout()
layout1.addWidget(btcancel)
layout1.addWidget(btok)
conflayout.addLayout(layout1)

layout.addWidget(ed)
layout.addWidget(confpannel)
win.setMinimumWidth(800)
win.show()
sys.exit(app.exec_())