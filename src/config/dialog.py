# -*- coding: utf-8 -*-
"""config dialog

Copyright (c) 2019 lileilei <hustlei@sina.cn>
"""

from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QListWidget, QStackedWidget, QGroupBox,
                             QLabel, QSpinBox, QPushButton, QComboBox, QFormLayout, QDialog, QCheckBox, QMessageBox)
from PyQt5.QtCore import Qt


def setValue(vartobeassign):
    def innerset(value):
        vartobeassign = value

    return innerset


class ConfDialog(QDialog):
    """config dialog"""

    def __init__(self, mainwin):
        super(ConfDialog, self).__init__()
        self._app = QApplication.instance()  # 获取app实例
        self.setWindowFlags(Qt.Tool | Qt.WindowStaysOnTopHint)
        self.win = mainwin
        self.leftList = QListWidget()
        self.rightStack = QStackedWidget()
        self.optionActions = {}
        self.changedOptions = {}
        self.initUI()
        self.initConfOptions()
        self.initOptionActions()
        recentlist = self.win.config["file.recent"]
        if recentlist:
            self.win.recent.setList(recentlist)
        self.alertChLang = False

    def initUI(self):
        mainLayout = QVBoxLayout()
        layH1 = QHBoxLayout()
        layH2 = QHBoxLayout()
        layH1.addWidget(self.leftList)
        layH1.addWidget(self.rightStack)
        self.cancelbtn = QPushButton(self.tr("Cancel"))
        self.okbtn = QPushButton(self.tr("OK"))
        # self.cancelbtn.setVisible(False)
        self.okbtn.setDefault(True)
        layH2.addStretch(1)
        layH2.addWidget(self.cancelbtn)
        layH2.addWidget(self.okbtn)
        mainLayout.addLayout(layH1)
        mainLayout.addLayout(layH2)
        self.setLayout(mainLayout)

        # left list
        self.leftList.addItem(self.tr("General"))
        self.leftList.addItem(self.tr("Editor"))
        self.leftList.setMaximumWidth(150)

        # right stack
        w = QWidget()
        layw = QVBoxLayout()
        # general
        g = QGroupBox(self.tr("General"))
        glayout = QFormLayout()
        label1 = QLabel(self.tr("select UI language:"))
        self.langCombo = QComboBox()
        self.fillLangItems(self.langCombo)  # .addItems(self.getLangList())
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

        # action for dialog
        self.leftList.currentRowChanged.connect(self.rightStack.setCurrentIndex)
        self.cancelbtn.clicked.connect(lambda: (self.cancel(), self.close()))
        self.okbtn.clicked.connect(lambda: (self.apply(), self.close()))

        # actions
        self.recentcountspin.valueChanged.connect(lambda x: self.changedOptions.__setitem__("file.recentcount", x))
        self.langCombo.currentIndexChanged.connect(lambda i: self.changedOptions.__setitem__("general.language", i))
        self.checkboxAutoExportQss.stateChanged.connect(
            lambda b: self.changedOptions.update({"advance.autoexportqss": b}))

    # def showEvent(self, QShowEvent):
    def initConfOptions(self):
        """load option and display on ui when dialog first start"""
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
            if l["lang"].replace("-", "_") == lang.replace("-", "_"):
                self.langCombo.setCurrentText(l["nativename"])
                break
        self.checkboxAutoExportQss.setChecked(bool(self.win.config["advance.autoexportqss"]))

    def initOptionActions(self):
        self.optionActions = {
            # option: [applyaction, updateuiaction]
            "general.language": [lambda l: (self.chLang(l), self.win.config.setChild("general.language",l)),
                                 self.updateLangCombo],
            "file.recentcount": [lambda n: (setValue(self.win.recent.maxcount)(n), self.win.config.setChild("file.recentcount",n)),
                                 self.recentcountspin.setValue],
            "advance.autoexportqss": [lambda b:self.win.config.setChild("advance.autoexportqss", bool(b)),
                                      self.checkboxAutoExportQss.setChecked],
        }

    def fillLangItems(self, combo):
        """set combo list for language
        """
        from i18n.language import Language
        langs = Language.getLangs()
        for l in langs:
            combo.addItem(l["nativename"], l["lang"])
        return True

    def chLang(self, lang="en"):
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
        if self.alertChLang:
            QMessageBox.information(self, self.tr("Change Language Info"),
                                    self.tr("You must restart soft to enable luanguage change."))

    def updateLangCombo(self, lang=None):
        """update setting ui to lang"""
        from i18n.language import Language
        if not lang:
            lang = Language.lang
        for l in Language.getLangs():
            if l["lang"].replace("-", "_") == lang.replace("-", "_"):
                self.langCombo.setCurrentText(l["nativename"])
                break

    def apply(self):
        """get config and apply to app.
        """
        recentlist = self.win.config["file.recent"]
        self.win.recent.setList(recentlist)

        for option, val in self.changedOptions.items():
            self.optionActions[option][0](val)
        self.changedOptions.clear()
        self.win.editor.settings.apply()

    def cancel(self):
        for option in self.changedOptions.keys():
            if option in self.win.config:
                self.optionActions[option][1](self.win.config[option])
            else:
                self.optionActions[option][1](self.win.config.defaultOptions[option])
        self.changedOptions.clear()
        self.win.editor.settings.cancel()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    win = QWidget()
    dialog = ConfDialog(win)
    dialog.show()
    sys.exit(app.exec())
