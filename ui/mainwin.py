# -*- coding: utf-8 -*-
"""
Copyright (c) 2019 lileilei <hustlei@sina.cn>
"""
import os
import re

from PyQt5.QtWidgets import (qApp, QMainWindow, QWidget, QLabel, QPushButton,
                             QColorDialog, QFileDialog, QMessageBox, QAction)
from PyQt5.QtGui import QIcon, QColor, qGray, QFont
from PyQt5.QtCore import Qt, QSize, QTranslator
# import sip

from ui import Ui_Mainwin
from ui.flow_layout import QFlowLayout
from qss_template import Qsst
from .recent import Recent
from config import Config, ConfDialog

class MainWin(QMainWindow, Ui_Mainwin):
    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.ver = "v1.40"
        self.title = "QssStylesheet Editor " + self.ver
        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon("img/colorize.ico"))
        self.qsst = Qsst()
        self.clrBtnDict = {}
        self.file = None
        self.lastSavedText = ""
        self.newIndex = 0
        self.confDialog=None
        #ui
        self.setAcceptDrops(True)
        self.setupUi(self)
        self.setupActions()
        self.recent=Recent(self.open, self.submenus["recent"])
        if self.tr("LTR") == "RTL":
            self.setLayoutDirection(Qt.RightToLeft)
        #conf
        self.config=Config()
        self.configfile=os.path.join(os.path.dirname(__file__),"../config/config.toml")
        self.useConfig()
        #lang
        # from i18n.language import Language as Lang
        # Lang.getConfigLang(self)
        # Lang.setLang()
        #init
        self.__isNewFromTemplate=False
        self.newWithTemplate()
        self.statusbar.showMessage(self.tr("Ready"))

    def setupActions(self):
        # theme  toolbarWidget
        self.actions["DisableQss"].toggled.connect(self.unuseQss)
        self.themeCombo.currentTextChanged.connect(qApp.setStyle)

        # menubar toolbar
        self.actions["new"].triggered.connect(self.new)
        self.actions["open"].triggered.connect(self._openact)
        self.actions["save"].triggered.connect(self.save)
        self.actions["saveas"].triggered.connect(self.saveAs)
        self.actions["export"].triggered.connect(self.export)
        self.actions["undo"].triggered.connect(self.editor.undo)
        self.actions["redo"].triggered.connect(self.editor.redo)
        self.actions["undo"].setEnabled(self.editor.isUndoAvailable())
        self.actions["redo"].setEnabled(self.editor.isRedoAvailable())
        self.actions["cut"].triggered.connect(self.editor.cut)
        self.actions["copy"].triggered.connect(self.editor.copy)
        self.actions["paste"].triggered.connect(self.editor.paste)
        self.actions["ShowColor"].triggered.connect(
            self.docks["color"].setVisible)
        self.actions["ShowPreview"].triggered.connect(
            self.docks["preview"].setVisible)
        self.actions["find"].triggered.connect(self.editor.find)
        self.actions["replace"].triggered.connect(self.editor.replace)
        self.actions["echospace"].triggered.connect(
            lambda: self.editor.setWhitespaceVisibility(
                not self.editor.whitespaceVisibility()))
        self.actions["echoeol"].triggered.connect(
            lambda: self.editor.setEolVisibility(
                not self.editor.eolVisibility()))
        self.actions["fontup"].triggered.connect(self.editor.zoomIn)
        self.actions["fontdown"].triggered.connect(self.editor.zoomOut)
        self.actions["autowrap"].triggered.connect(
            lambda: self.editor.setWrapMode(
                0 if self.editor.wrapMode() else 2))

        # contianerWidget.setSizePolicy(QSizePolicy.Maximum,QSizePolicy.Minimum)
        def sizeDock(dockLoc):
            if(dockLoc == Qt.TopDockWidgetArea or dockLoc == Qt.BottomDockWidgetArea):
                # self.colorPanelWidget.resize(self.docks["color"].width(),self.colorPanelLayout.minimumSize().height())
                self.docks["color"].widget().resize(
                    self.docks["color"].width(),
                    self.colorPanelLayout.minimumSize().height())
        self.docks["color"].dockLocationChanged.connect(sizeDock)

        # main editor
        self.editor.keyPress.connect(self.textChanged)

        def rend():
            self.renderStyle()
            self.loadColorPanel()
        self.editor.loseFocus.connect(rend)
        self.editor.mouseLeave.connect(rend)
        self.editor.mousePress.connect(rend)
        self.editor.linesChanged.connect(lambda: self.status["lines"].setText(
            self.tr("lines:") + str(self.editor.lines())))
        self.editor.cursorPositionChanged.connect(lambda l, p: self.status["line"].setText(
            self.tr("line:") + str(l + 1) + self.tr("  pos:") + str(p)))
        self.editor.selectionChanged.connect(self.__setSelectStatus)
        self.editor.modificationChanged.connect(self.motifyChanged)
        self.editor.drop.connect(self.dropEvent)

        # setting
        self.confDialog=ConfDialog(self)
        self.actions["config"].triggered.connect(self.confDialog.show)

        # help
        aboutText = "<b><center>" + self.title + "</center></b><br><br>"
        aboutText += self.tr("This software is a advanced editor for QtWidget stylesheet(Qss), <br>support custom variable and real-time preview.<br><br>")
        aboutText += self.tr("author: lileilei<br>website: <a href='https://blog.csdn.net/hustlei/article/details/87887369'>https://blog.csdn.net/hustlei</a><br><br>welcom communicate with me: hustlei@sina.cn")
        aboutText += "<br>copyright &copy; 2019, lilei."
        self.actions["about"].triggered.connect(
            lambda: QMessageBox.about(self, "about", aboutText))

    def __setSelectStatus(self):
        linefrom, posfrom, lineto, posto = self.editor.getSelection()
        linefrom += 1
        lineto += 1
        if(linefrom == 0 or lineto == 0):
            text = self.tr("select: none")
        else:
            text = self.tr("select:ln") + str(linefrom) + self.tr(" - ln") + str(lineto)
        self.status["select"].setText(text)

    def unuseQss(self, unuse):
        if(unuse):
            qApp.setStyleSheet('')
        else:
            self.renderStyle()
            self.loadColorPanel()

    def renderStyle(self):
        self.qsst.srctext = self.editor.text()
        self.qsst.loadVars()
        self.qsst.convertQss()

        norand = self.actions["DisableQss"].isChecked()
        if(norand):
            qApp.setStyleSheet('')
        else:
            # self.setStyleSheet(self.qsst.qss)#tooltip透明等显示不出来
            # try:
            # saved=os.path.exists(self.file)
            # lastcwd=os.getcwd()
            # if saved:
            #     dir=os.path.dirname(self.file)
            #     os.chdir(dir)
            path = os.path.dirname(self.file).replace("\\", "/")
            styleSheet = re.sub(
                r'url\([\s]*[\"\']*[\s]*([^\/\s][^:\s\"\'\)]*)[\s]*[\"\']*[\s]*\)',
                r'url("{}/\1")'.format(path).format(path),
                self.qsst.qss)  # 不支持带空格路径
            qApp.setStyleSheet(styleSheet)

            #     self.statusbar.showMessage("")#不起作用
            # except Exception:
            #     self.statusbar.showMessage("qss parse failed")
            cstr = self.qsst.varDict.get("background", "")
            if cstr:
                try:
                    c = QColor()
                    c.setNamedColor(cstr)
                    self.editor.setBackgroundColor(c)
                except Exception:
                    pass

    def textChanged(self, e):  # QKeyEvent(QEvent.KeyPress, Qt.Key_Enter, Qt.NoModifier)
        # if (32<e.key()<96 or 123<e.key()<126 or 0x1000001<e.key()<0x1000005
        # or e.key==Qt.Key_Delete):
        if (e.key() == Qt.Key_Return or e.key() == Qt.Key_Enter  # 大键盘为Ret小键盘为Enter
            or e.key() == Qt.Key_Semicolon or e.key() == Qt.Key_BraceRight or e.key() == Qt.Key_Tab
                or e.key() == Qt.Key_Up or e.key() == Qt.Key_Down or e.key() == Qt.Key_Left or e.key() == Qt.Key_Right):
            self.renderStyle()
            self.loadColorPanel()

        self.actions["undo"].setEnabled(self.editor.isUndoAvailable())
        self.actions["redo"].setEnabled(self.editor.isRedoAvailable())

    def motifyChanged(self, e):
        if(self.editor.isModified()):
            self.setWindowTitle(
                self.title +
                " - *" +
                os.path.basename(
                    self.file))
            self.actions["save"].setEnabled(True)
        else:
            self.setWindowTitle(
                self.title +
                " - " +
                os.path.basename(
                    self.file))
            self.actions["save"].setEnabled(False)

    def loadColorPanel(self):
        self.qsst.srctext = self.editor.text()
        self.qsst.loadVars()
        #item = self.colorGridLayout.itemAt(0)
        # while (item != None):
        #     self.colorGridLayout.removeItem(item)
        #     # self.colorGridLayout.removeWidget(item.widget())
        #     # item.widget().setParent(None)#这三行没有作用
        #     sip.delete(item.widget())  # 虽然控件删除了，但是grid的行数列数没减少，但是不影响使用
        #     sip.delete(item)
        #     item = self.colorGridLayout.itemAt(0)
        # self.colorGridLayout.update()  # 不起作用

        # a,b=list(self.clrBtnDict.keys()),list(self.qsst.varDict.keys());a.sort();b.sort()
        if(sorted(list(self.clrBtnDict.keys())) != sorted(list(self.qsst.varDict.keys()))):
            while(self.colorPanelLayout.count() > 0):
                self.colorPanelLayout.removeItem(
                    self.colorPanelLayout.itemAt(0))
            self.clrBtnDict = {}
            for varName, clrStr in self.qsst.varDict.items():
                contianerWidget = QWidget()
                contianerWidget.setMinimumSize(QSize(140, 25))
                label = QLabel(varName, contianerWidget)
                label.setFont(QFont("Arial", 9, QFont.Medium))
                btn = QPushButton(clrStr, contianerWidget)
                self.clrBtnDict[varName] = btn
                # label.setFixedWidth(80)
                # btn.setFixedWidth(100)
                label.move(5, 10)
                btn.move(80, 5)
                self.colorPanelLayout.addWidget(contianerWidget)
                self.colorPanelLayout.setSpacing(5)
                btn.clicked.connect(lambda x, var=varName: self.chclr(var))

        for varName, btn in self.clrBtnDict.items():
            clrStr = self.qsst.varDict[varName]
            btn.setText(clrStr)
            if ("rgb" in clrStr):
                t = clrStr.strip(r" rgba()")
                c = t.split(',')
                if (len(c) > 3):
                    lable = c[3]
                else:
                    lable = 255
                color = QColor(c[0], c[1], c[2], lable)
            else:
                color = QColor(clrStr)
            s = ''
            if (qGray(color.rgb()) < 100):
                s += "color:white;"
            else:
                s += "color:black;"

            btn.setStyleSheet(s + "background:" + btn.text())

    def chclr(self, var):
        c = QColor()
        cstr = self.sender().text()
        if(cstr):
            c.setNamedColor(cstr)
        else:
            c.setNamedColor("white")
        color = QColorDialog.getColor(
            c, self, self.tr("color pick"), QColorDialog.ShowAlphaChannel)
        if (color.isValid()):
            s = ''
            clrstr = color.name()
            if (color.alpha() == 255):
                clrstr = color.name().upper()
            else:
                # 'rgba({},{},{},{})'.format(color.red(), color.green(), color.blue(), color.alpha())
                clrstr = color.name(QColor.HexArgb).upper()
            #     s = 'font-size:8px;'
            if (qGray(color.rgb()) < 100):
                s += 'color:white;'
            self.clrBtnDict[var].setText(clrstr)
            self.clrBtnDict[var].setStyleSheet(s + "background:" + clrstr)
            self.qsst.varDict[var] = clrstr
            self.qsst.writeVars()
            # 用setText之后undo redo堆栈全部消失，所以暂时用这种方法
            pos = self.editor.verticalScrollBar().sliderPosition()
            self.editor.selectAll()
            self.editor.replaceSelectedText(
                self.qsst.srctext)  # setText(self.qsst.srctext)
            # self.editor.setCursorPosition(xp,yp)
            self.editor.verticalScrollBar().setSliderPosition(pos)
            self.renderStyle()

    def _openact(self, _=None, file=None):
        self.open(file)

    def open(self, file=None):  # _参数用于接收action的event参数,bool类型
        if (file is None):
            file, _ = QFileDialog.getOpenFileName(
                self, self.tr("Open File"), file, "QSS(*.qss *.qsst);;qsst(*.qsst);;qss(*.qss);;all(*.*)")  # _是filefilter
        if (os.path.exists(file)):
            self.file = file
            self.statusbar.showMessage(self.tr("opening file..."))
            self.lastSavedText = self.editor.text()
            ok = self.editor.load(self.file)
            if ok:
                self.statusbar.showMessage(self.tr("load file successfully"))
            else:
                self.statusbar.showMessage(self.tr("load file failed"))
            self.renderStyle()
            self.loadColorPanel()
            self.setWindowTitle(self.title + " - " + os.path.basename(file))
            self.status["coding"].setText(self.editor.coding)
            if(not self.__isNewFromTemplate):
                self.recent.addFile(self.file)
        else:
            self.statusbar.showMessage(self.tr("file not found."))

    def new(self):
        if(self.editor.isModified()):
            ret = QMessageBox.question(
                self,
                self.title,
                self.tr("Current file is not saved, do you want to save?"),
                QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel,
                QMessageBox.No)
            if(ret == QMessageBox.Yes):
                self.save()
            elif(ret == QMessageBox.Cancel):
                return

        self.newIndex = self.newIndex + 1
        self.file = self.tr("new{}.qsst").format(self.newIndex)
        self.lastSavedText = ""
        self.editor.setText("")
        self.renderStyle()
        self.loadColorPanel()
        self.setWindowTitle(self.title + " - " + os.path.basename(self.file))
        self.editor.setModified(False)

    def newWithTemplate(self, templatefile="data/default.qsst"):
        if(self.editor.isModified()):
            ret = QMessageBox.question(
                self,
                self.title,
                self.tr("Current file is not saved，do you want to save?"),
                QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel,
                QMessageBox.No)
            if(ret == QMessageBox.Yes):
                self.save()
            elif(ret == QMessageBox.Cancel):
                return
        self.__isNewFromTemplate=True
        self.open(file=templatefile)
        self.__isNewFromTemplate=False
        self.statusbar.showMessage(self.tr("new file created, using template"))
        self.newIndex = self.newIndex + 1
        self.file = self.tr("new{}.qsst").format(self.newIndex)
        self.setWindowTitle(self.title + " - " + os.path.basename(self.file))
        self.editor.setModified(False)

    def save(self):
        if (self.file and os.path.exists(self.file)):
            self.lastSavedText = self.editor.text()
            self.editor.save(self.file)
            self.setWindowTitle(
                self.title +
                " - " +
                os.path.basename(
                    self.file))
            self.actions["save"].setEnabled(False)
            self.recent.addFile(self.file)
        else:
            self.saveAs()

    def saveAs(self):
        # f="." if self.file==None else self.file
        file, filefilter = QFileDialog.getSaveFileName(
            self, self.tr("save file"), self.file, "qsst(*.qsst);;qss(*.qss);;all(*.*)")
        if (file):
            self.file = file
            self.lastSavedText = self.editor.text()
            self.editor.save(self.file)
            self.setWindowTitle(self.title + " - " + os.path.basename(file))
            self.actions["save"].setEnabled(False)
            self.recent.addFile(self.file)

    def export(self):
        self.qsst.convertQss()
        if(self.file is None):
            f = "."
        else:
            # f=self.file[:-1]
            f = os.path.splitext(self.file)[0]
        file, _ = QFileDialog.getSaveFileName(
            self, self.tr("export Qss"), f, "Qss(*.qss);;all(*.*)")
        if file:
            with open(file, 'w', newline='') as f:
                f.write(self.qsst.qss)

    def dragEnterEvent(self, qDragEnterEvent):
        if(qDragEnterEvent.mimeData().hasUrls()):
            qDragEnterEvent.acceptProposedAction()
            # print(qDragEnterEvent.possibleActions())
            # qDragEnterEvent.setDropAction(Qt::CopyAction Qt::MoveAction
            # Qt::LinkAction Qt::IgnoreAction Qt::TargetMoveAction)

    def dropEvent(self, QDropEvent):
        if (QDropEvent.mimeData().hasUrls()):
            file = QDropEvent.mimeData().urls()[0].toLocalFile()
            if(os.path.exists(file)):
                self.open(file=file)

    def closeEvent(self, e):
        if(self.editor.isModified()):
            if(self.lastSavedText != self.editor.text()):
                msg = QMessageBox(
                    QMessageBox.Question,
                    self.title,
                    self.tr(
                        self.tr("Save before close?") +
                        os.path.basename(
                            self.file)),
                    QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)
                msg.setDefaultButton(QMessageBox.Cancel)
                msg.button(QMessageBox.Save).setText(self.tr("Save"))
                msg.button(QMessageBox.Discard).setText(self.tr("Discard"))
                msg.button(QMessageBox.Cancel).setText(self.tr("Cancel"))
                ret = msg.exec_()
                # ret=QMessageBox.information(self,"Qss Style Editor",self.tr("是否将更改保存到"+os.path.basename(self.file)),
                #                             QMessageBox.Yes|QMessageBox.No|QMessageBox.Cancel,QMessageBox.Yes)
                if(ret == QMessageBox.Save or ret == QMessageBox.Yes):
                    self.save()
                    e.ignore()
                elif(ret == QMessageBox.Discard or ret == QMessageBox.No):
                    self.updateConfig()
                    self.config.save()
                    qApp.exit()
                else:
                    e.ignore()
        else:
            self.updateConfig()
            self.config.save()

    def updateConfig(self):
        self.config.getSec("file")["recent"]=self.recent.getList()
        self.config.getSec("file")["recentcount"]=self.recent.maxcount
        self.config.getSec("editor")["fontsize"]=self.editor.font().pointSize()

    def useConfig(self):
        self.config.read()
        recentlist=self.config.getSec("file")["recent"]
        self.recent.setList(recentlist)
        self.recent.maxcount=self.config.getSec("file")["recentcount"]
        self.editor.font().setPointSize(self.config.getSec("editor")["fontsize"])