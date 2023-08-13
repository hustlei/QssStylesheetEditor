# -*- coding: utf-8 -*-
"""Copyright (c) 2019 lileilei <hustlei@sina.cn>
"""
import os
import re
import sys

from PyQt5.QtWidgets import (qApp, QWidget, QLabel, QPushButton, QColorDialog, QFileDialog, QMessageBox, QFormLayout,
                             QVBoxLayout, QHBoxLayout)
from PyQt5.QtGui import QIcon, QColor, qGray, QFont
from PyQt5.QtCore import Qt, QSize, QTimer
# import sip

from config import Config, ConfDialog
from qss_template import Qsst
from .mainwinbase import MainWinBase
from .palettedialog import PaletteDialog
from .recent import Recent


class MainWin(MainWinBase):
    def __init__(self):
        super().__init__()
        self.ver = "v1.80"
        self.title = "QssStylesheet Editor " + self.ver
        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon("res/app.ico"))
        self.qsst = Qsst()
        self.clrBtnDict = {}
        self.file = None
        self.lastSavedText = ""
        self.newIndex = 0
        self.firstAutoExport = True
        # ui
        self.setAcceptDrops(True)
        self.currentUIqss = ""
        self.paletteDailog = PaletteDialog(self)
        self.updateDialog = None
        # conf
        self.recent = Recent(self.open, self.submenus["recent"])
        self.config = Config.current()
        self.confDialog = ConfDialog(self)  # , self)
        self.confDialog.setMinimumWidth(650)
        # self.setupUi()
        self.setupActions()
        if self.tr("LTR") == "RTL":
            self.setLayoutDirection(Qt.RightToLeft)

        # lang
        # from i18n.language import Language as Lang
        # Lang.getConfigLang(self)
        # Lang.setLang()
        # init
        self.__isNewFromTemplate = False
        self.newFromTemplate()

        self.checkforupdate()
        self.statusbar.showMessage(self.tr("Ready"))

        # new fetures 202204
        self.timer = QTimer()
        self.timer.timeout.connect(lambda: {self.renderStyle(), self.loadColorPanel(), self.timer.stop()})

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
        self.actions["comment"].triggered.connect(self.commentcode)
        self.actions["uncomment"].triggered.connect(self.uncommentcode)
        self.actions["ShowColor"].triggered.connect(self.docks["color"].setVisible)
        self.actions["ShowPreview"].triggered.connect(self.docks["preview"].setVisible)
        self.actions["Palette"].triggered.connect(self.paletteDailog.show)
        self.actions["find"].triggered.connect(self.editor.find)
        self.actions["replace"].triggered.connect(self.editor.replace)
        self.actions["echospace"].triggered.connect(
            lambda: self.editor.setWhitespaceVisibility(not self.editor.whitespaceVisibility()))
        self.actions["echoeol"].triggered.connect(lambda: self.editor.setEolVisibility(not self.editor.eolVisibility()))
        self.actions["fontup"].triggered.connect(self.editor.zoomIn)
        self.actions["fontdown"].triggered.connect(self.editor.zoomOut)
        self.actions["autowrap"].triggered.connect(lambda: self.editor.setWrapMode(0 if self.editor.wrapMode() else 2))

        # contianerWidget.setSizePolicy(QSizePolicy.Maximum,QSizePolicy.Minimum)
        def sizeDock(dockLoc):
            if dockLoc in (Qt.TopDockWidgetArea, Qt.BottomDockWidgetArea):
                # self.colorPanelWidget.resize(self.docks["color"].width(),
                #   self.colorPanelLayout.minimumSize().height())
                self.docks["color"].widget().resize(self.docks["color"].width(),
                                                    self.colorPanelLayout.minimumSize().height())

        self.docks["color"].dockLocationChanged.connect(sizeDock)

        # main CodeEditor
        self.changed = False
        self.editor.textChanged.connect(self.textChanged)
        self.editor.keyPress.connect(self.keyPressed)

        def rend():
            self.renderStyle()
            self.loadColorPanel()

        self.editor.loseFocus.connect(rend)
        # self.editor.mouseLeave.connect(rend)
        self.editor.mousePress.connect(rend)
        self.editor.linesChanged.connect(
            lambda: self.status["lines"].setText(self.tr("lines:") + str(self.editor.lines())))
        self.editor.cursorPositionChanged.connect(
            lambda l, p: self.status["line"].setText(self.tr("line:") + str(l + 1) + self.tr("  pos:") + str(p)))
        self.editor.selectionChanged.connect(self.__setSelectStatus)
        self.editor.modificationChanged.connect(self.motifyChanged)
        self.editor.drop.connect(self.dropEvent)

        # setting
        self.actions["config"].triggered.connect(self.confDialog.show)

        # help
        aboutText = "<b><center>" + self.title + "</center></b><br><br>"
        aboutText += self.tr(
            "This software is a advanced CodeEditor for QtWidget stylesheet(Qss), support custom variable and "
            "real-time preview.<br><br> ")
        aboutText += self.tr(
            "author: lileilei<br>website: <a href='https://github.com/hustlei/QssStylesheetEditor'>https"
            "://github.com/hustlei/QssStylesheetEditor</a><br><br>welcom communicate with me: hustlei@sina.cn ")
        aboutText += "<br>copyright &copy; 2019, lilei."
        self.actions["about"].triggered.connect(lambda: QMessageBox.about(self, "about", aboutText))
        self.actions["checkupdate"].triggered.connect(lambda: self.checkforupdate(True))

    def __setSelectStatus(self):
        linefrom, _, lineto, _ = self.editor.getSelection()  # __ is posfrom posto
        linefrom += 1
        lineto += 1
        if not (linefrom and lineto):
            text = self.tr("select: none")
        else:
            text = self.tr("select:ln") + str(linefrom) + self.tr(" - ln") + str(lineto)
        self.status["select"].setText(text)

    def commentcode(self):
        linefrom, colfrom, lineto, colto = self.editor.getSelection()
        if linefrom == -1:
            linefrom, _ = self.editor.getCursorPosition()
            colfrom = 0
            lineto = linefrom
            colto = self.editor.lineLength(lineto) + 1
        self.editor.insertAt("/* ", linefrom, colfrom)
        self.editor.insertAt(" */ ", lineto, colto)

    def uncommentcode(self):
        linefrom, colfrom, lineto, colto = self.editor.getSelection()
        start, end = -1, -1
        if linefrom == -1:
            linefrom, colcursor = self.editor.getCursorPosition()
            lineto = linefrom
            linetext = self.editor.text(linefrom)
            linebytes = linetext.encode()
            if len(linetext.encode()) < 4 or colcursor<2 or colcursor >len(linetext.encode())-2:
                return
            for i in range(colcursor - 1, -1, -1):
                if linebytes[i] == ord("*") and linebytes[i - 1] == ord("/"):
                    start = i - 1
                    break
            for i in range(colcursor, len(linebytes) - 1):
                if linebytes[i] == ord("*") and linebytes[i + 1] == ord("/"):
                    print(i, linebytes[i], linebytes[i+1])
                    end = i
                    break
        else:
            linestart = self.editor.text(linefrom).encode()
            colend = len(linestart) if lineto>linefrom else colto
            for i in range(colfrom, colend):
                if linestart[i] == ord('/') and linestart[i+1] == ord('*'):
                    start = i
                    break
            if start == -1:
                for i in range(colfrom, 0, -1):
                    if linestart[i] == ord('/') and linestart[i-1] == ord('*'):
                        start = -2
                        break
                    elif linestart[i] == ord('*') and linestart[i-1] == ord('/'):
                        start = i-1
                        break
            if start ==-1 and linefrom > 0:
                while linefrom > 0:
                    linefrom = linefrom -1
                    if self.editor.text(linefrom).strip() != "":
                        break
                linestart = self.editor.text(linefrom).encode()
                for i in range(len(linestart)-1, 0, -1):
                    if linestart[i] == ord('/') and linestart[i-1] == ord('*'):
                        break
                    elif linestart[i] == ord('*') and linestart[i-1] == ord('/'):
                        start = i-1
                        break

            if start > 0:
                lineend = self.editor.text(lineto).encode()
                colstart = 0 if lineto>linefrom else colfrom
                for i in range(colto, colstart, -1):
                    if lineend[i] == ord('/') and lineend[i - 1] == ord('*'):
                        end = i
                        break
                if end == -1:
                    for i in range(colto, len(lineend)-1):
                        if lineend[i] == ord('/') and lineend[i + 1] == ord('*'):
                            end = -2
                            break
                        elif lineend[i] == ord('*') and lineend[i + 1] == ord('/'):
                            end = i
                            break
                if end < 0 and lineto < self.editor.lines()-1:
                    while lineto < self.editor.lines()-1:
                        lineto = lineto + 1
                        if self.editor.text(lineto).strip() != "":
                            break
                    print(lineto)
                    lineend = self.editor.text(lineto).encode()
                    for i in range(len(lineend)-1):
                        if lineend[i] == ord('/') and lineend[i + 1] == ord('*'):
                            break
                        elif lineend[i] == ord('*') and lineend[i + 1] == ord('/'):
                            end = i
            print(linefrom,start, lineto, end)

        if start>=0 and end>=0:
            # try:
            # self.editor.positionFromLineIndex(linefrom, lineto)
            self.editor.setSelection(lineto, end, lineto, end + 2)
            self.editor.removeSelectedText()
            self.editor.setSelection(linefrom, start, linefrom, start + 2)
            self.editor.removeSelectedText()
            # except:
            # print("uncomment err")

    def unuseQss(self, unuse):
        if unuse:
            self.docks["preview"].setStyleSheet('')
            self.setStyleSheet('')
        else:
            self.setStyleSheet(self.currentUIqss)
            self.renderStyle()
            self.loadColorPanel()

    def renderStyle(self):
        self.qsst.srctext = self.editor.text()
        if not self.qsst.loadVars():
            return
        self.qsst.convertQss()

        norand = self.actions["DisableQss"].isChecked()
        if norand:
            self.docks["preview"].setStyleSheet('')
        else:
            # self.setStyleSheet(self.qsst.qss)#tooltip透明等显示不出来
            # try:
            # saved=os.path.exists(self.file)
            # lastcwd=os.getcwd()
            # if saved:
            #     dir=os.path.dirname(self.file)
            #     os.chdir(dir)
            path = os.path.dirname(self.file).replace("\\", "/")
            styleSheet = re.sub(r'url\([\s]*[\"\']?[\s]*([^\s\/:\"\'\)]+)[\s]*[\"\']?[\s]*\)',
                                r'url("{}/\1")'.format(path).format(path), self.qsst.qss)  # 不支持带空格路径
            if os.path.exists(self.file):
                name, _ = os.path.splitext(self.file)
                res = name + ".py"
                resp = os.path.dirname(res)
                resn, _ = os.path.splitext(os.path.basename(res))
                if os.path.exists(res):
                    if resp not in sys.path:
                        sys.path.appendToChild(resp)
                    try:
                        __import__(resn)
                    except BaseException:
                        pass
            self.docks["preview"].setStyleSheet(styleSheet)

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
                    print("set background clolor exception.")

    def keyPressed(self, e):  # QKeyEvent(QEvent.KeyPress, Qt.Key_Enter, Qt.NoModifier)
        # if (32<e.key()<96 or 123<e.key()<126 or 0x1000001<e.key()<0x1000005 or e.key==Qt.Key_Delete):
        # 大键盘为Ret小键盘为Enter
        if self.changed:
            self.timer.stop()
            if e.key() in (Qt.Key_Return, Qt.Key_Enter, Qt.Key_Semicolon, Qt.Key_BraceRight):
                self.timer.start(300)  # 普通人正常打字速度
                self.changed = False
            else:
                self.timer.start(600)  # 很慢的打字速度

    def textChanged(self):
        self.changed = True
        self.actions["undo"].setEnabled(self.editor.isUndoAvailable())
        self.actions["redo"].setEnabled(self.editor.isRedoAvailable())

    def motifyChanged(self):  # , e):
        if self.editor.isModified():
            self.setWindowTitle(self.title + " - *" + os.path.basename(self.file))
            self.actions["save"].setEnabled(True)
        else:
            self.setWindowTitle(self.title + " - " + os.path.basename(self.file))
            self.actions["save"].setEnabled(False)

    def loadColorPanel(self):
        self.qsst.srctext = self.editor.text()
        if not self.qsst.loadVars():
            return
        # item = self.colorGridLayout.itemAt(0)
        # while (item != None):
        #     self.colorGridLayout.removeItem(item)
        #     # self.colorGridLayout.removeWidget(item.widget())
        #     # item.widget().setParent(None)#这三行没有作用
        #     sip.delete(item.widget())  # 虽然控件删除了，但是grid的行数列数没减少，但是不影响使用
        #     sip.delete(item)
        #     item = self.colorGridLayout.itemAt(0)
        # self.colorGridLayout.update()  # 不起作用

        # a,b=list(self.clrBtnDict.keys()),list(self.qsst.varDict.keys());a.sort();b.sort()
        if sorted(list(self.clrBtnDict.keys())) != sorted(list(self.qsst.varDict.keys())):
            while self.colorPanelLayout.count() > 0:
                self.colorPanelLayout.removeItem(self.colorPanelLayout.itemAt(0))
            self.clrBtnDict = {}
            labels = {}
            widLabel = 0
            widBtn = 0
            for varName, clrStr in self.qsst.varDict.items():
                label = QLabel(varName)  # , contianerWidget)
                btn = QPushButton(clrStr)  # , contianerWidget)
                if sys.platform.startswith("win"):
                    font1 = QFont("Arial", 10, QFont.Medium)
                    font2 = QFont("sans-serif", 9, QFont.Medium)
                    label.setFont(font1)
                    btn.setFont(font2)
                self.clrBtnDict[varName] = btn
                labels[varName] = label
                label.adjustSize()
                widLabel = label.width() if label.width() > widLabel else widLabel
                btn.adjustSize()
                widBtn = btn.width() if btn.width() > widBtn else widBtn
                # label.move(5, 5)
                # btn.move(100, 5)
                btn.clicked.connect(lambda x, var=varName: self.chclr(var))
            for name, btn in self.clrBtnDict.items():
                contianerWidget = QWidget()
                lay = QHBoxLayout()
                labels[name].setFixedWidth(widLabel)
                btn.setFixedWidth(widBtn)
                lay.addWidget(labels[name])
                lay.addWidget(btn)
                contianerWidget.setLayout(lay)
                # contianerWidget.setMinimumSize(QSize(185, 25))
                self.colorPanelLayout.addWidget(contianerWidget)

        for varName, btn in self.clrBtnDict.items():
            clrStr = self.qsst.varDict[varName]
            btn.setText(clrStr)
            if "rgb" in clrStr:
                t = clrStr.strip(r" rgba()")
                c = t.split(',')
                if len(c) > 3:
                    lable = c[3]
                else:
                    lable = 255
                try:
                    color = QColor(int(c[0]), int(c[1]), int(c[2]), lable)
                except Exception:
                    continue
            else:
                try:
                    color = QColor(clrStr)
                except Exception:
                    continue
            s = ''
            if qGray(color.rgb()) < 100:
                s += "color:white;"
            else:
                s += "color:black;"

            btn.setStyleSheet(s + "background:" + btn.text())

    def chclr(self, var):
        c = QColor()
        cstr = self.sender().text()
        if cstr:
            c.setNamedColor(cstr)
        else:
            c.setNamedColor("white")
        color = QColorDialog.getColor(c, self, self.tr("color pick"), QColorDialog.ShowAlphaChannel)
        if color.isValid():
            s = ''
            clrstr = color.name()
            if color.alpha() == 255:
                clrstr = color.name().upper()
            else:
                # 'rgba({},{},{},{})'.format(color.red(), color.green(), color.blue(), color.alpha())
                clrstr = color.name(QColor.HexArgb).upper()
            # s = 'font-size:8px;'
            if qGray(color.rgb()) < 100:
                s += 'color:white;'
            self.clrBtnDict[var].setText(clrstr)
            self.clrBtnDict[var].setStyleSheet(s + "background:" + clrstr)
            self.qsst.varDict[var] = clrstr
            self.qsst.writeVars()
            # 用setText之后undo redo堆栈全部消失，所以暂时用这种方法
            pos = self.editor.verticalScrollBar().sliderPosition()
            self.editor.selectAll()
            self.editor.replaceSelectedText(self.qsst.srctext)  # setText(self.qsst.srctext)
            # self.CodeEditor.setCursorPosition(xp,yp)
            self.editor.verticalScrollBar().setSliderPosition(pos)
            self.renderStyle()

    def _openact(self, _=None, file=None):
        self.open(file)

    def open(self, file=None):  # _参数用于接收action的event参数,bool类型
        if file is None:
            file, _ = QFileDialog.getOpenFileName(
                self, self.tr("Open File"), file,
                "QSS(*.qss *.qsst);;qsst(*.qsst);;qss(*.qss);;all(*.*)")  # _是filefilter
        if os.path.exists(file):
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
            if not self.__isNewFromTemplate:
                self.recent.addFile(self.file)
        else:
            self.statusbar.showMessage(self.tr("file not found."))

    def new(self):
        if self.editor.isModified():
            ret = QMessageBox.question(self, self.title,
                                       self.tr("Current file hasn't been saved, do you want to save?"),
                                       QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel, QMessageBox.No)
            if ret == QMessageBox.Yes:
                self.save()
            elif ret == QMessageBox.Cancel:
                return

        self.newIndex = self.newIndex + 1
        self.file = self.tr("new{}.qsst").format(self.newIndex)
        self.lastSavedText = ""
        self.editor.setText("")
        self.renderStyle()
        self.loadColorPanel()
        self.setWindowTitle(self.title + " - " + os.path.basename(self.file))
        self.editor.setModified(False)

    def newFromTemplate(self, templatefile="data/default.qsst"):
        if self.editor.isModified():
            ret = QMessageBox.question(self, self.title,
                                       self.tr("Current file hasn't been saved, do you want to save?"),
                                       QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel, QMessageBox.No)
            if ret == QMessageBox.Yes:
                self.save()
            elif ret == QMessageBox.Cancel:
                return
        self.__isNewFromTemplate = True
        self.open(file=templatefile)
        self.__isNewFromTemplate = False
        self.statusbar.showMessage(self.tr("new file created, using template"))
        self.newIndex = self.newIndex + 1
        self.file = self.tr("new{}.qsst").format(self.newIndex)
        self.setWindowTitle(self.title + " - " + os.path.basename(self.file))
        self.editor.setModified(False)

    def save(self):
        if (self.file and os.path.exists(self.file)):
            self.lastSavedText = self.editor.text()
            self.editor.save(self.file.encode("utf-8"))
            self.status["coding"].setText("utf-8")
            self.setWindowTitle(self.title + " - " + os.path.basename(self.file))
            self.actions["save"].setEnabled(False)
            self.recent.addFile(self.file)
            self.autoExport(self.file)
        else:
            self.saveAs()

    def saveAs(self):
        # f="." if self.file==None else self.file
        file, _ = QFileDialog.getSaveFileName(
            self,
            self.tr(  # __ is filefilter
                "save file"),
            self.file,
            "qsst(*.qsst);;qss(*.qss);;all(*.*)")
        if file:
            self.file = file
            self.lastSavedText = self.editor.text()
            self.editor.save(self.file.encode("utf-8"))
            self.status["coding"].setText("utf-8")
            self.setWindowTitle(self.title + " - " + os.path.basename(file))
            self.actions["save"].setEnabled(False)
            self.recent.addFile(self.file)
            self.autoExport(self.file)
            self.firstAutoExport = True

    def export(self):
        self.qsst.convertQss()
        if self.file is None:
            f = "."
        else:
            # f=self.file[:-1]
            f = os.path.splitext(self.file)[0]
        savefile, _ = QFileDialog.getSaveFileName(self, self.tr("export Qss"), f, "Qss(*.qss);;all(*.*)")
        if savefile:
            with open(savefile, 'w', newline='', encoding='utf-8') as f:
                f.write(self.qsst.qss)

    def autoExport(self, file):
        if self.config["advance.autoexportqss"]:
            self.qsst.convertQss()
            qssfile = os.path.splitext(file)[0] + ".qss"
            backupfile = qssfile + ".backup"
            if self.firstAutoExport and os.path.exists(qssfile):
                if os.path.exists(backupfile):
                    os.remove(backupfile)
                os.rename(qssfile, backupfile)
            with open(qssfile, 'w', newline='', encoding='utf-8') as f:
                f.write(self.qsst.qss)
                self.firstAutoExport = False

    def dragEnterEvent(self, qDragEnterEvent):
        if qDragEnterEvent.mimeData().hasUrls():
            qDragEnterEvent.acceptProposedAction()
            # print(qDragEnterEvent.possibleActions())
            # qDragEnterEvent.setDropAction(Qt::CopyAction Qt::MoveAction
            # Qt::LinkAction Qt::IgnoreAction Qt::TargetMoveAction)

    def dropEvent(self, objQDropEvent):
        if objQDropEvent.mimeData().hasUrls():
            file = objQDropEvent.mimeData().urls()[0].toLocalFile()
            if os.path.exists(file):
                self.open(file=file)

    def closeEvent(self, e):
        if self.editor.isModified():
            if self.lastSavedText != self.editor.text():
                msg = QMessageBox(QMessageBox.Question, self.title,
                                  self.tr("Current file hasn't been saved, do you want to save?"),
                                  QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)
                msg.setDefaultButton(QMessageBox.Cancel)
                msg.button(QMessageBox.Save).setText(self.tr("Save"))
                msg.button(QMessageBox.Discard).setText(self.tr("Discard"))
                msg.button(QMessageBox.Cancel).setText(self.tr("Cancel"))
                ret = msg.exec_()
                # ret=QMessageBox.information(self,"Qss Style Editor",self.tr("是否将更改保存到"+os.path.basename(self.file)),
                #                             QMessageBox.Yes|QMessageBox.No|QMessageBox.Cancel,QMessageBox.Yes)
                if ret in (QMessageBox.Save, QMessageBox.Yes):
                    self.save()
                    e.ignore()
                elif ret in (QMessageBox.Discard, QMessageBox.No):
                    self.updateSpecialConfig()
                    self.config.save()
                    qApp.exit()
                else:
                    e.ignore()
        else:
            self.updateSpecialConfig()
            self.config.saveDefault()

    def updateSpecialConfig(self):
        """get new options, some option canbe changed without config dialog."""
        self.config.getSec("file")["recent"] = self.recent.getList()

    def autocheckforupdate(self):
        from datetime import datetime
        today = datetime.now().date()
        tmp1 = self.config["update.autocheck"]
        if not isinstance(tmp1, bool):
            tmp1 = True
        if tmp1:
            tmp2 = self.config["update.checkfreq"]
            if not tmp2:
                tmp2 = "start"
            if tmp2 == "start":
                self.checkforupdate()
            lastcheckday = self.config["update.lastcheckday"]
            if not lastcheckday:
                self.checkforupdate()
            else:
                deltaday = today - lastcheckday
                d = deltaday.days
                if (tmp2 == "day" and d >= 1) or (tmp2 == "week" and d >= 7) or (tmp2 == "month" and d >= 30):
                    self.checkforupdate()

    def checkforupdate(self, showdialogifnotupdate=False):
        self.statusbar.showMessage(self.tr("checking for update..."))

        def aftcall(newver):
            ver = self.ver.strip('vV')
            if not newver:
                if not showdialogifnotupdate:
                    return
                newver = "[network err]"
            if showdialogifnotupdate or newver > ver:
                if not self.updateDialog:
                    self.updateDialog = updateinfodialog(self)
                self.updateDialog.setWindowIcon(self.windowIcon())
                self.updateDialog.showdialog(ver, newver, "https://github.com/hustlei/QssStylesheetEditor/releases")

            from datetime import datetime
            today = datetime.now().date()
            self.config["update.lastcheckday"] = today

        from update import AsyncGetLatestVer, updateinfodialog
        self.t = AsyncGetLatestVer("hustlei", "QssStylesheetEditor")
        self.t.got.connect(aftcall)
        self.t.start()
