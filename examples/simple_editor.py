

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton
sys.path.append("..")
from CodeEditor import Editor, EditorSettings

app = QApplication(sys.argv)
win = QWidget()
hlayout = QHBoxLayout()

ed = Editor()
ed.setMinimumWidth(600)
text="""#include <stdio.h>
int main()
{
    // 这是一首思念家乡的诗
    printf("床前明月光，");
    printf("疑是地上霜。");
    printf("举头望明月，");
    printf("低头思故乡。"); 
    return 0;    
}"""
ed.setText(text)
ed.setLanguage("CPP")

confpannel = QWidget(win)
conflayout = QVBoxLayout()
confpannel.setLayout(conflayout)

setting = EditorSettings(ed)
conflayout.addWidget(setting.settingPanel())
btcancel = QPushButton("Cancel")
btcancel.clicked.connect(setting.cancel)
btok = QPushButton("Apply")
btok.clicked.connect(setting.apply)
layout1 = QHBoxLayout()
layout1.addWidget(btcancel)
layout1.addWidget(btok)
conflayout.addLayout(layout1)

hlayout.addWidget(ed)
hlayout.addWidget(confpannel)

mainLayout = QVBoxLayout()
toolbar = QHBoxLayout()
butfind = QPushButton("find")
butfind.clicked.connect(ed.find)
butreplace = QPushButton("replace")
butreplace.clicked.connect(ed.replace)
toolbar.addWidget(butfind)
toolbar.addWidget(butreplace)
toolbar.addStretch(1)
mainLayout.addLayout(toolbar)
mainLayout.addLayout(hlayout)

win.setLayout(mainLayout)
win.setMinimumWidth(800)
win.show()
sys.exit(app.exec_())