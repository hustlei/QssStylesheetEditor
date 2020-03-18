# -*- coding: utf-8 -*-
"""config dialog

Copyright (c) 2019 lileilei <hustlei@sina.cn>
"""

from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QListWidget, QStackedWidget, QGroupBox,
                             QLabel, QSpinBox, QPushButton, QComboBox, QFormLayout, QDialog, QCheckBox, QMessageBox)
from PyQt5.QtCore import Qt


class ConfDialog(QDialog):
    """config dialog"""
    def __init__(self, mainwin):
        super(ConfDialog, self).__init__()
        self._app = QApplication.instance()  # 获取app实例
        self.setWindowFlags(Qt.Tool | Qt.WindowStaysOnTopHint)
        self.win = mainwin
        self.leftList = QListWidget()
        self.rightStack = QStackedWidget()
        self.changedOptions = {}
        self.initUI()
        recentlist = self.win.config["file.recent"]
        if recentlist:
            self.win.recent.setList(recentlist)
        self.first = True

    def initUI(self):
        mainLayout = QVBoxLayout()
        layH1 = QHBoxLayout()
        layH2 = QHBoxLayout()
        layH1.addWidget(self.leftList)
        layH1.addWidget(self.rightStack)
        self.okbtn = QPushButton(self.tr("OK"))
        self.cancelbtn = QPushButton(self.tr("Cancel"))
        layH2.addStretch(1)
        layH2.addWidget(self.okbtn)
        layH2.addWidget(self.cancelbtn)
        mainLayout.addLayout(layH1)
        mainLayout.addLayout(layH2)
        self.setLayout(mainLayout)

        # left list
        self.leftList.addItem(self.tr("General"))
        self.leftList.addItem(self.tr("Editor"))
        self.leftList.setMaximumWidth(150)

        #right stack
        w = QWidget()
        layw = QVBoxLayout()
        # general
        g = QGroupBox(self.tr("General"))
        glayout = QFormLayout()
        label1 = QLabel(self.tr("select UI language:"))
        self.langCombo = QComboBox()
        self.setLangItems(self.langCombo)  # .addItems(self.getLangList())
        self.langCombo.setMinimumWidth(150)
        label2 = QLabel(self.tr("Number of recent files:"))
        self.recentcountspin = QSpinBox()
        self.recentcountspin.setMinimum(1)
        self.recentcountspin.setMaximum(30)
        glayout.addRow(label1, self.langCombo)
        glayout.addRow(label2, self.recentcountspin)
        g.setLayout(glayout)
        layw.addWidget(g)
        # advanced
        g2 = QGroupBox(self.tr("Advanced"))
        labeladv1 = QLabel(self.tr("Export qss When save qsst:"))
        self.checkboxAutoExportQss = QCheckBox()
        self.checkboxAutoExportQss.setToolTip(self.tr("Option for whether export qss when save qsst file each time."))
        layh1 = QHBoxLayout()
        layh1.addWidget(labeladv1)
        layh1.addStretch(1)
        layh1.addWidget(self.checkboxAutoExportQss)
        g2layout = QVBoxLayout()
        g2layout.addLayout(layh1)
        g2.setLayout(g2layout)
        layw.addWidget(g2)

        layw.addStretch(1)
        w.setLayout(layw)
        self.rightStack.addWidget(w)

        # CodeEditor SettingPannel
        self.rightStack.addWidget(self.win.editor.settings.settingPanel())

        self.leftList.currentRowChanged.connect(self.rightStack.setCurrentIndex)
        self.cancelbtn.clicked.connect(self.close)
        self.cancelbtn.setVisible(False)
        self.okbtn.clicked.connect(lambda: (self.win.editor.settings.apply(), self.apply(), self.close()))

        # action
        def setCount(x):
            self.win.recent.maxcount = x

        self.recentcountspin.valueChanged.connect(lambda x: self.changedOptions.__setitem__("file.recentcount",x))
        self.langCombo.currentIndexChanged.connect(lambda i: self.changedOptions.__setitem__("general.language",i))
        self.checkboxAutoExportQss.stateChanged.connect(lambda b: self.changedOptions.update({"advance.autoexportqss":b}))


    def setLangItems(self, combo):
        """set combo list for language
        """
        from i18n.language import Language
        langs = Language.getLangs()
        for l in langs:
            combo.addItem(l["nativename"], l["lang"])
        return True

    def chLang(self):
        """change ui luanguage setting."""
        # print("Change language to "+lang)
        # try:
        #     if lang.lower()=="english":
        #         self._app.removeTranslator(self.win.trans)
        #         return
        #     self.win.trans.load("i18n-"+lang+".qm")
        #     self._app.installTranslator(self.win.trans)
        #     #self._app.retranslateUi(self)# 重新翻译界面
        # except Exception as Argument:
        #     print(Argument)
        lang = self.langCombo.currentData()
        print("Setting Language to " + lang)
        self.win.config["general.language"] = lang
        print("restart soft to enable.")
        if not self.first:
            QMessageBox.information(self, self.tr("Change Language Info"), self.tr("You must restart soft to enable luanguage change."))

    def showEvent(self, QShowEvent):
        if self.first:
            count = self.win.config["file.recentcount"]
            if count:
                self.recentcountspin.setValue(count)
            # lang = self.win.config.get("general.language","en") #self.win.config.getSec("general").get("language", "en")
            # lang = self.win.config["general.language"]
            # if lang is None:
            #     lang = "en"
            from i18n.language import Language
            lang = Language.lang
            for l in Language.getLangs():
                if l["lang"].replace("-","_") == lang.replace("-","_"):
                    self.langCombo.setCurrentText(l["nativename"])
                    break
            self.checkboxAutoExportQss.setChecked(bool(self.win.config["advance.autoexportqss"]))
            self.first = False
            self.changedOptions.clear()

        # # update changed value
        # if self.changedOptions["file.recentcount"]:
        #     self.recentcountspin.setValue(int(self.changedOptions["file.recentcount"]))
        # if self.changedOptions["general.language"]:
        #     self.langCombo.setLan


    def apply(self):
        """get config and apply to app.
        """
        recentlist = self.win.config["file.recent"]
        self.win.recent.setList(recentlist)
        if "file.recentcount" in self.changedOptions:
            self.win.config["file.recentcount"] = self.changedOptions["file.recentcount"]
        self.win.recent.maxcount = int(self.win.config["file.recentcount"])

        if "general.language" in self.changedOptions:
            self.chLang()
        self.changedOptions.clear()



if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    win = QWidget()
    dialog = ConfDialog(win)
    dialog.show()
    sys.exit(app.exec())
