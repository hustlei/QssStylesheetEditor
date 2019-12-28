

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout
sys.path.append("..")
from CodeEditor import Editor

app = QApplication(sys.argv)
win = QWidget()
layout = QHBoxLayout()

ed = Editor()
text="""床前明月光，
疑是地上霜。
举头望明月，
低头思故乡。"""
ed.setText(text)
# ed.configure(language="CPP")
# font=ed.font()
# font.setFamily("Arial")
# ed.setFont(font)
# ed.lexer.setFont(font)
# print(ed.lexer.font(0).family())

layout.addWidget(ed)
win.setLayout(layout)
win.show()
sys.exit(app.exec_())