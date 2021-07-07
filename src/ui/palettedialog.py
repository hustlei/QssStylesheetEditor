# -*- coding: utf-8 -*-
"""Class for palette color setting

Copyright (c) 2019 lileilei <hustlei@sina.cn>
"""
from PyQt5.QtGui import QPalette, QFont, QColor
from PyQt5.QtWidgets import (QDialog, QHBoxLayout, QTableWidget, QTableWidgetItem, QAbstractItemView, QPushButton, qApp,
                             QColorDialog, QVBoxLayout, QTextEdit)


class PaletteDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.p = qApp.palette()
        self.oldclr = {}
        self.newclr = {}
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.tr("Palette Color Setting"))
        self.setMinimumSize(500, 500)
        self.tab = {
            "Window": QPalette.Window,
            "WindowText": QPalette.WindowText,
            "Base": QPalette.Base,
            "AlternateBase": QPalette.AlternateBase,
            "Text": QPalette.Text,
            "Button": QPalette.Button,
            "ButtonText": QPalette.ButtonText,
            "BrightText": QPalette.BrightText,
            "ToolTipBase": QPalette.ToolTipBase,
            "ToolTipText": QPalette.ToolTipText,
            "PlaceholderText": QPalette.PlaceholderText,
            "Light": QPalette.Light,
            "Midlight": QPalette.Midlight,
            "Dark": QPalette.Dark,
            "Mid": QPalette.Mid,
            "Shadow": QPalette.Shadow,
            "Highlight": QPalette.Highlight,
            "HighlightedText": QPalette.HighlightedText,
            "Link": QPalette.Link,
            "LinkVisited": QPalette.LinkVisited,
            "NoRole": QPalette.NoRole
        }
        layout = QVBoxLayout()
        t = QTableWidget()
        t.setRowCount(len(self.tab))
        t.setColumnCount(5)
        t.setHorizontalHeaderLabels(["ColorRole", "Active", "Inactive", "Disabled", "reset"])
        t.verticalHeader().setVisible(False)
        t.setEditTriggers(QAbstractItemView.NoEditTriggers)
        t.setDragEnabled(False)
        t.setSelectionMode(QAbstractItemView.NoSelection)
        t.horizontalHeader().setSectionsClickable(False)
        i = 0
        f = t.font()
        f.setPointSize(9)
        t.setFont(f)
        t.setColumnWidth(1, 80)
        t.setColumnWidth(2, 80)
        t.setColumnWidth(3, 80)
        t.setColumnWidth(4, 60)

        def changclr():
            rowNum = t.currentRow()
            colNum = t.currentColumn()
            btn = t.cellWidget(rowNum, colNum)
            clrRoletext = t.item(rowNum, 0).text()
            c = self.oldclr[clrRoletext][colNum - 1]
            color = QColorDialog.getColor(QColor(c), self, self.tr("color pick"), QColorDialog.ShowAlphaChannel)
            if color.isValid():
                clrstr = color.name()
                if color.alpha() == 255:
                    clrstr = color.name().upper()
                else:
                    clrstr = color.name(QColor.HexArgb).upper()
                if clrRoletext not in self.newclr:
                    self.newclr[clrRoletext] = [0, 0, 0]
                self.newclr[clrRoletext][colNum - 1] = clrstr
                btn.setStyleSheet("background:" + clrstr)
                btn1 = t.cellWidget(rowNum, 4)
                btn1.setEnabled(True)

        def resetrow():
            rowNum = t.currentRow()
            colNum = t.currentColumn()
            clrRoletext = t.item(rowNum, 0).text()
            self.newclr.pop(clrRoletext)

            for i in (1, 2, 3):
                btn = t.cellWidget(rowNum, i)
                c = self.oldclr[clrRoletext][i - 1]
                btn.setStyleSheet("background:" + c)

            btn = t.cellWidget(rowNum, 4)
            btn.setEnabled(False)

        for key, val in self.tab.items():
            t.setRowHeight(i, 15)
            t.setItem(i, 0, QTableWidgetItem(key))
            btn1 = QPushButton()
            clrRole = self.tab[t.item(i, 0).text()]
            c1 = self.p.color(QPalette.Active, clrRole).name()
            c2 = self.p.color(QPalette.Inactive, clrRole).name()
            c3 = self.p.color(QPalette.Disabled, clrRole).name()
            self.oldclr[t.item(i, 0).text()] = [c1, c2, c3]
            btn1.setStyleSheet("background:" + c1)
            t.setCellWidget(i, 1, btn1)
            btn2 = QPushButton()
            btn2.setStyleSheet("background:" + c2)
            t.setCellWidget(i, 2, btn2)
            btn3 = QPushButton()
            btn3.setStyleSheet("background:" + c3)
            t.setCellWidget(i, 3, btn3)
            btn4 = QPushButton("reset")
            btn4.setEnabled(False)
            t.setCellWidget(i, 4, btn4)
            i += 1
            btn1.clicked.connect(changclr)
            btn2.clicked.connect(changclr)
            btn3.clicked.connect(changclr)
            btn4.clicked.connect(resetrow)

        t.setEditTriggers(QAbstractItemView.NoEditTriggers)
        layout.addWidget(t)
        self.setLayout(layout)

        hlay = QHBoxLayout()
        btncode = QPushButton(self.tr("ViewPaletteCode"))
        btncancel = QPushButton(self.tr("Cancel"))
        btnok = QPushButton(self.tr("OK"))
        btncode.setMinimumSize(220, 35)
        btncancel.setMinimumSize(520, 55)
        btnok.setMinimumSize(120, 35)
        hlay.addWidget(btncode)
        hlay.addStretch(1)
        hlay.addWidget(btncancel)
        hlay.addWidget(btnok)
        layout.addLayout(hlay)

        self.d = CodeDialog(self)
        btncode.clicked.connect(self.getcode)
        btncancel.clicked.connect(self.cancel)
        btnok.clicked.connect(self.apply)

    def getcode(self):
        t = ""
        for k, v in self.newclr.items():
            c1, c2, c3 = v
            if c1:
                t += "palette.setColor(QPalette.Active, QPalette." + k + ", QColor(" + c1 + "))\n"
            if c2:
                t += "palette.setColor(QPalette.Inactive, QPalette." + k + ", QColor(" + c2 + "))\n"
            if c3:
                t += "palette.setColor(QPalette.Disabled, QPalette." + k + ", QColor(" + c3 + "))\n"
        self.d.showdialog(t)

    def cancel(self):
        self.newclr = {}
        self.close()

    def apply(self):
        for k, v in self.newclr.items():
            c1, c2, c3 = v
            if c1:
                self.p.setColor(QPalette.Active, self.tab[k], QColor(c1))
                self.oldclr[k][0] = c1
            if c2:
                self.p.setColor(QPalette.Inactive, self.tab[k], QColor(c2))
                self.oldclr[k][1] = c2
            if c3:
                self.p.setColor(QPalette.Disabled, self.tab[k], QColor(c3))
                self.oldclr[k][2] = c3
        qApp.setPalette(self.p)
        self.close()


class CodeDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.tr("Custom Palette Code"))
        self.setMinimumSize(650, 400)
        layout = QVBoxLayout()
        self.edit = QTextEdit()
        layout.addWidget(self.edit)
        self.setLayout(layout)

    def showdialog(self, text):
        if not len(text.strip()):
            self.edit.setText(self.tr("No Custom QPalette, using the default palette."))
            self.edit.setEnabled(False)
        else:
            self.edit.setEnabled(True)
            self.edit.setReadOnly(True)
            self.edit.setText(text)
        self.show()


if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)
    w = PaletteDialog()
    w.show()
    sys.exit(app.exec_())
