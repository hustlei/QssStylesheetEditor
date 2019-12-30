# -*- coding: utf-8 -*-
"""config dialog

Copyright (c) 2019 lileilei <hustlei@sina.cn>
"""

from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QListWidget, QStackedWidget, QGroupBox,
                             QLabel, QSpinBox, QPushButton, QComboBox, QFormLayout)
from PyQt5.QtCore import Qt


class ConfDialog(QWidget):
    """config dialog"""

    def __init__(self, mainwin):
        super(ConfDialog, self).__init__()
        self._app = QApplication.instance()  # 获取app实例
        self.setWindowFlags(Qt.Tool | Qt.WindowStaysOnTopHint)
        self.win = mainwin
        self.initUI()

    def initUI(self):
        mainLayout = QVBoxLayout()
        layH1 = QHBoxLayout()
        layH2 = QHBoxLayout()
        self.conflist = QListWidget()
        self.stack = QStackedWidget()
        layH1.addWidget(self.conflist)
        layH1.addWidget(self.stack)
        self.okbtn = QPushButton(self.tr("OK"))
        self.cancelbtn = QPushButton(self.tr("Cancel"))
        layH2.addStretch(1)
        layH2.addWidget(self.okbtn)
        layH2.addWidget(self.cancelbtn)
        mainLayout.addLayout(layH1)
        mainLayout.addLayout(layH2)
        self.setLayout(mainLayout)

        # list
        self.conflist.addItem(self.tr("General"))
        self.conflist.addItem(self.tr("Editor"))
        self.conflist.setMaximumWidth(150)
        # general
        w = QWidget()
        layw = QVBoxLayout()

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
        label3 = QLabel(self.tr("Font Size:"))
        self.fontsizespin = QSpinBox()
        self.fontsizespin.setMinimum(1)
        self.fontsizespin.setMaximum(30)

        glayout.addRow(label1, self.langCombo)
        glayout.addRow(label2, self.recentcountspin)
        glayout.addRow(label3, self.fontsizespin)
        g.setLayout(glayout)

        layw.addWidget(g)
        layw.addStretch(1)
        w.setLayout(layw)
        self.stack.addWidget(w)

        # CodeEditor
        from ui.CodeEditor.settings import EditorSettings
        settings = EditorSettings(self.win.editor)
        w = settings.settingPanel()
        self.stack.addWidget(w)

        self.conflist.currentRowChanged.connect(self.stack.setCurrentIndex)
        self.cancelbtn.clicked.connect(self.close)
        self.cancelbtn.setVisible(False)
        self.okbtn.clicked.connect(lambda: (settings.apply(), self.close()))

        # action
        self.fontsizespin.valueChanged.connect(self.win.editor.font().setPointSize)

        def setCount(x):
            self.win.recent.maxcount = x

        self.recentcountspin.valueChanged.connect(setCount)
        self.langCombo.currentIndexChanged.connect(self.chLang)

    def setLangItems(self, combo):
        from i18n.language import Language
        langs = Language.getLangs()
        for l in langs:
            combo.addItem(l["nativename"], l["lang"])
        return True

    def chLang(self):
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
        self.win.config.getSec("general")["language"] = lang
        print("restart soft to enable.")

    def show(self):
        # default value
        self.fontsizespin.setValue(self.win.editor.font().pointSize())
        self.recentcountspin.setValue(self.win.recent.maxcount)
        lang = self.win.config.getSec("general").get("language", None)
        if lang is None:
            lang = "en"
        from i18n.language import Language
        for l in Language.getLangs():
            if l["lang"] == lang:
                self.langCombo.setCurrentText(l["nativename"])
                break
        super().show()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    win = QWidget()
    dialog = ConfDialog(win)
    dialog.show()
    sys.exit(app.exec())
