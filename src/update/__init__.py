# -*- coding: utf-8 -*-
"""functions for version and update check

Copyright (c) 2019 lileilei <hustlei@sina.cn>
"""

import requests
from PyQt5.QtCore import QUrl, QThread, pyqtSignal
from PyQt5.QtGui import QDesktopServices, QFont, QPixmap
from PyQt5.QtWidgets import QDialog, QHBoxLayout, QVBoxLayout, QLabel, QPushButton


def getLatestVer(githubname, projname):  # hustlei #QssStylesheetEditor
    addr = "https://api.github.com/repos/" + githubname + "/" + projname + "/releases/latest"
    response = requests.get(addr)
    return response.json()["tag_name"].strip('Vv')


class AsyncGetLatestVer(QThread):  # 线程2
    got = pyqtSignal(str)  #已执行完成的信号

    def __init__(self, githubname, projname):
        super().__init__()
        self.addr = "https://api.github.com/repos/" + githubname + "/" + projname + "/releases/latest"

    def run(self):
        # response = requests.get(self.addr)
        # ret = response.json()["tag_name"].strip('Vv')
        try:
            s = requests.session()
            s.keep_alive = False
            rst = s.get(self.addr)
            ret = rst.json()["tag_name"].strip('Vv')
        except Exception:
            self.got.emit(None)
            return
        self.got.emit(ret)


class updateinfodialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle(self.tr("Update Information"))
        self.setFixedSize(400, 200)
        self.setFont(QFont("Arial", 10))
        self.verinfo1 = self.tr("This is the newest version.")
        self.verinfo2 = self.tr("New version available.")
        self.initUI()

    def initUI(self):
        mlay = QHBoxLayout()

        vlay = QVBoxLayout()
        pic1 = QLabel()
        pic1.setPixmap(QPixmap(":appres.img/app.png"))
        vlay.addWidget(pic1)
        vlay.addStretch(1)
        mlay.addLayout(vlay)
        mlay.addSpacing(10)

        self.infolabel = QLabel("")
        self.versionlabel = QLabel("")
        self.newverlabel = QLabel("")
        okbtn = QPushButton(self.tr("OK"))
        layout = QVBoxLayout()
        layout.addStretch(1)
        layout.addWidget(self.infolabel)
        layout.addStretch(1)
        layout.addWidget(self.versionlabel)
        layout.addWidget(self.newverlabel)
        layout.addStretch(3)
        hlay = QHBoxLayout()
        hlay.addStretch(1)
        hlay.addWidget(okbtn)
        okbtn.clicked.connect(self.close)
        layout.addStretch(1)
        layout.addLayout(hlay)
        mlay.addLayout(layout)
        self.setLayout(mlay)

        def openUrl(url):
            QDesktopServices.openUrl(QUrl(url))

        self.newverlabel.linkActivated.connect(openUrl)

    def showdialog(self, ver, newver=None, addr=None):
        if not newver or ver >= newver:
            self.infolabel.setText(self.verinfo1)
            self.versionlabel.setText(self.tr("Current Version:") + ver)
        else:
            self.infolabel.setText(self.verinfo2)
            self.versionlabel.setText(self.tr("Current Version:") + ver)
            self.newverlabel.setText(
                self.tr("Update Version:") + newver + "(<a href=" + addr + self.tr(">download</a>)"))
        self.show()


if __name__ == "__main__":
    print(getLatestVer("hustlei", "QssStylesheetEditor"))
    from PyQt5.QtWidgets import *
    import sys
    app = QApplication(sys.argv)
    d = updateinfodialog()
    d.showdialog('v1.6')
    d.showdialog('v1.6', 'v1.7', 'http://baidu.com')
    sys.exit(app.exec())
