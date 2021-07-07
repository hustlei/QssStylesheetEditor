# -*- coding: utf-8 -*-
"""Base class for Mainwin

Copyright (c) 2019 lileilei <hustlei@sina.cn>
"""
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QKeySequence, QIcon
from PyQt5.QtWidgets import (QMainWindow, QApplication, QStyleFactory, QAction, QMenu, QToolBar, QWidget, QLabel,
                             QCheckBox, QComboBox, QTabWidget, QDockWidget)

# from res.img_rc import *
from CodeEditor import Editor
from .preview import PreviewWidget
from .flow_layout import QFlowLayout


class MainWinBase(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(1200, 600)
        self.menubar = self.menuBar()
        self.statusbar = self.statusBar()
        self.mainWidget = QTabWidget()
        self.editor = Editor()

        self.actions = {}
        self.menus = {}
        self.submenus = {}
        self.contexMenus = {}
        self.toolbars = {}
        self.status = {}
        self.docks = {}
        self.documents = {}

        self.createActions()
        self.themeCombo = QComboBox()
        self.createMenubar()
        self.createContexMenus()
        self.createToolbars()
        self.createStatusBar()
        self.colorPanelLayout = QFlowLayout()
        self.createDocks()
        self.createMainWidget()

    def createActions(self):
        def createAct(text, tip=None, shortcut=None, iconimg=None, checkable=False, slot=None):
            action = QAction(self.tr(text), self)
            if iconimg is not None:
                action.setIcon(QIcon(iconimg))
            if shortcut is not None:
                action.setShortcut(shortcut)
            if tip is not None:
                tip = self.tr(tip)
                action.setToolTip(tip)
                action.setStatusTip(tip)
            if checkable:
                action.setCheckable(True)
            if slot is not None:
                action.triggered.connect(slot)
            return action

        def keys2str(standardkey):
            return "".join(("(", QKeySequence(standardkey).toString(), ")"))

        self.actions["new"] = createAct(self.tr("&New", "&New"),
                                        self.tr("new") + keys2str(QKeySequence.New), QKeySequence.New,
                                        ':appres.img/NewDocument.png')
        self.actions["open"] = createAct(self.tr("&Open"),
                                         self.tr("Open") + keys2str(QKeySequence.Open), QKeySequence.Open,
                                         ':appres.img/openHS.png')
        self.actions["save"] = createAct(self.tr("&Save"),
                                         self.tr("Save") + keys2str(QKeySequence.Save), QKeySequence.Save,
                                         ':appres.img/save.png')
        self.actions["saveas"] = createAct(self.tr("&Save as..."), self.tr("Save as..."), None,
                                           ':appres.img/SaveAs.png')
        self.actions["export"] = createAct(self.tr("&ExportQss"), self.tr("ExportQss"), "Ctrl+Alt+E",
                                           ':appres.img/export5.png')
        self.actions["exit"] = createAct(self.tr("&Exit"), self.tr("Exit"), "Ctrl+Q", ':appres.img/close.png')
        self.actions["undo"] = createAct(self.tr("&Undo"),
                                         self.tr("Undo") + keys2str(QKeySequence.Undo), QKeySequence.Undo,
                                         ':appres.img/undo.png')
        self.actions["redo"] = createAct(self.tr("&Redo"),
                                         self.tr("Redo") + keys2str(QKeySequence.Redo), QKeySequence.Redo,
                                         ':appres.img/redo.png')
        self.actions["cut"] = createAct(self.tr("&Cut"),
                                        self.tr("Cut") + keys2str(QKeySequence.Cut), QKeySequence.Cut,
                                        ':appres.img/cut.png')
        self.actions["copy"] = createAct(self.tr("&Copy"),
                                         self.tr("Copy") + keys2str(QKeySequence.Copy), QKeySequence.Copy,
                                         ':appres.img/copy.png')
        self.actions["paste"] = createAct(self.tr("&Paste"),
                                          self.tr("Paste") + keys2str(QKeySequence.Paste), QKeySequence.Paste,
                                          ':appres.img/paste.png')
        self.actions["find"] = createAct(self.tr("&Find"),
                                         self.tr("Find") + keys2str(QKeySequence.Find), QKeySequence.Find,
                                         ':appres.img/find.png')
        self.actions["replace"] = createAct(self.tr("&Replace"),
                                            self.tr("Replace") + keys2str(QKeySequence.Replace), QKeySequence.Replace,
                                            ':appres.img/replace.png')
        self.actions["fontup"] = createAct(self.tr("&BiggerFont"), self.tr("Bigger Font"), None,
                                           ':appres.img/fontup.png')
        self.actions["fontdown"] = createAct(self.tr("&SmallerFont"), self.tr("Smaller Font"), None,
                                             ':appres.img/fontdown.png')
        self.actions["echospace"] = createAct(self.tr("&Space"), self.tr("Show Spaces"), None, ':appres.img/space.png')
        self.actions["echoeol"] = createAct(self.tr("&Eol"), self.tr("Show Eol"), None, ':appres.img/eol.png')
        self.actions["autowrap"] = createAct(self.tr("&AutoWrap"), self.tr("Auto wrap text"), None,
                                             ":appres.img/autowrap.png")

        # self.fontcolorAct=QAction(QIcon(":appres.img/broadcast_send_fontcolor_normal.bmp"),"&FontColor",self)
        # self.fontcolorAct.setShortcut("Ctr+Shit+C")
        # self.fontcolorAct.setStatusTip("FontColor")
        self.actions["DisableQss"] = createAct(self.tr("&DisableQss"), self.tr("DisableQss"), checkable=True)
        self.actions["DisableQss"].setChecked(False)
        self.actions["ShowColor"] = createAct(self.tr("&ColorPanel"),
                                              self.tr("ShowColorPanel"),
                                              None,
                                              ":appres.img/color.png",
                                              checkable=True)
        self.actions["ShowColor"].setChecked(True)
        self.actions["ShowPreview"] = createAct(self.tr("&PreviewPanel"),
                                                self.tr("ShowPreviewPanel"),
                                                None,
                                                ":appres.img/view.png",
                                                checkable=True)
        self.actions["Palette"] = createAct(self.tr("&Palette"), self.tr("ShowPaletteSettingDialog"), None,
                                            ":appres.img/texture.png")
        self.actions["ShowPreview"].setChecked(True)

        self.actions["config"] = createAct(self.tr("&Config"), self.tr("settings."), None, ":appres.img/config.png")

        self.actions["checkupdate"] = createAct(self.tr("&Check for Updates..."),
                                                self.tr("Check is there new version released for update."))
        self.actions["about"] = createAct(self.tr("&About"), self.tr("About"))

        # self.exitAct.triggered.connect(qApp.exit)#等价于qApp.quit
        self.actions["exit"].triggered.connect(self.close)

    def createMenubar(self):
        self.menus["File"] = QMenu(self.tr("&File"))
        self.menus["Edit"] = QMenu(self.tr("&Edit"))
        self.menus["View"] = QMenu(self.tr("&View"))
        self.menus["Tool"] = QMenu(self.tr("&Tool"))
        self.menus["Help"] = QMenu(self.tr("&Help"))

        recentMenu = QMenu(self.tr("Recent"), self.menus["File"])
        recentMenu.setIcon(QIcon(":appres.img/none.png"))

        editMenu = QMenu(self.tr("Text"), self.menus["Edit"])
        editMenu.setIcon(QIcon(":appres.img/edit_whitepage.png"))
        editMenu.addAction(self.actions["undo"])
        editMenu.addAction(self.actions["redo"])
        editMenu.addSeparator()
        editMenu.addAction(self.actions["cut"])
        editMenu.addAction(self.actions["copy"])
        editMenu.addAction(self.actions["paste"])

        searchMenu = QMenu(self.tr("Search"), self.menus["Edit"])
        searchMenu.setIcon(QIcon(":appres.img/findnext.png"))
        searchMenu.addAction(self.actions["find"])
        searchMenu.addAction(self.actions["replace"])

        self.submenus["recent"] = recentMenu
        self.submenus["text"] = editMenu
        self.submenus["search"] = searchMenu

        self.menus["File"].addAction(self.actions["new"])
        self.menus["File"].addAction(self.actions["open"])
        self.menus["File"].addAction(self.actions["save"])
        self.menus["File"].addAction(self.actions["saveas"])
        self.menus["File"].addAction(self.actions["export"])
        self.menus["File"].addMenu(self.submenus["recent"])
        self.menus["File"].addSeparator()
        self.menus["File"].addAction(self.actions["exit"])

        self.menus["Edit"].addMenu(editMenu)
        self.menus["Edit"].addMenu(searchMenu)

        self.menus["View"].addAction(self.actions["ShowColor"])
        self.menus["View"].addAction(self.actions["ShowPreview"])
        self.menus["View"].addAction(self.actions["Palette"])

        self.menus["Tool"].addAction(self.actions["config"])

        self.menus["Help"].addAction(self.actions["about"])
        self.menus["Help"].addAction(self.actions["checkupdate"])

        for m in self.menus.values():
            self.menubar.addMenu(m)

    def createContexMenus(self):
        self.contexMenus["Edit"] = QMenu(self.tr("Edit"))
        self.contexMenus["Edit"].addAction(self.actions["cut"])
        self.contexMenus["Edit"].addAction(self.actions["copy"])
        self.contexMenus["Edit"].addAction(self.actions["paste"])

    def createToolbars(self):
        checkbox = QCheckBox(self.tr("DisableQSS"))
        # self.themeCombo = QComboBox()
        checkbox.setToolTip(self.tr("Using system style, disable qss."))
        self.themeCombo.setToolTip(self.tr("Select system style."))
        self.themeCombo.addItems(QStyleFactory.keys())
        self.themeCombo.setMinimumWidth(105)
        theme = QApplication.style().objectName()
        self.themeCombo.setCurrentIndex(self.themeCombo.findText(theme, Qt.MatchFixedString))
        # self.themeCombo.setEnabled(False)
        # themeCombo.activated[str].connect(qApp.setStyle)
        # themeCombo.currentTextChanged.connect(qApp.setStyle)
        # checkbox.stateChanged.connect(self.themeCombo.setEnabled)
        checkbox.stateChanged.connect(self.actions["DisableQss"].setChecked)
        # checkbox.stateChanged.connect(lambda x:self.actions["DisableQss"].setChecked(checkbox.isChecked()))

        self.toolbars["Main"] = QToolBar(self.tr("Main", "toolbar"))
        self.toolbars["Main"].addWidget(checkbox)
        self.toolbars["Main"].addWidget(self.themeCombo)

        self.toolbars["File"] = QToolBar(self.tr("File"))
        self.toolbars["File"].addAction(self.actions["new"])
        self.toolbars["File"].addAction(self.actions["open"])
        self.toolbars["File"].addAction(self.actions["save"])
        # self.toolbars["File"].addAction(self.actions["saveas"])
        self.toolbars["File"].addAction(self.actions["export"])

        self.toolbars["Edit"] = QToolBar(self.tr("Edit"))
        self.toolbars["Edit"].addAction(self.actions["undo"])
        self.toolbars["Edit"].addAction(self.actions["redo"])
        self.toolbars["Edit"].addSeparator()
        self.toolbars["Edit"].addAction(self.actions["cut"])
        self.toolbars["Edit"].addAction(self.actions["copy"])
        self.toolbars["Edit"].addAction(self.actions["paste"])
        self.toolbars["Search"] = QToolBar(self.tr("Search"))
        self.toolbars["Search"].addAction(self.actions["find"])
        self.toolbars["Search"].addAction(self.actions["replace"])

        self.toolbars["View"] = QToolBar(self.tr("View"))
        self.toolbars["View"].addAction(self.actions["ShowColor"])
        self.toolbars["View"].addAction(self.actions["ShowPreview"])
        self.toolbars["View"].addAction(self.actions["Palette"])

        self.toolbars["Echo"] = QToolBar(self.tr("Echo"))
        self.toolbars["Echo"].addAction(self.actions["fontup"])
        self.toolbars["Echo"].addAction(self.actions["fontdown"])
        self.toolbars["Echo"].addAction(self.actions["echospace"])
        self.toolbars["Echo"].addAction(self.actions["echoeol"])
        self.toolbars["Echo"].addAction(self.actions["autowrap"])

        for t in self.toolbars.values():
            self.addToolBar(t)

    def createStatusBar(self):
        self.statusbar.showMessage(self.tr("Ready"))
        # self.statusbar.addWidget(QWidget(),1)
        # self.status["date"] = QLabel()
        # self.statusbar.addPermanentWidget(self.status["date"])
        # self.status["date"].setText(QDate.currentDate().toString())
        # self.status["date"].setVisible(False)

        self.status["line"] = QLabel(self.tr("line:0 pos:0"))
        self.status["select"] = QLabel(self.tr("select: none"))
        self.status["coding"] = QLabel(self.tr("coding"))
        self.status["lines"] = QLabel(self.tr("lines:0"))
        self.status["line"].setMinimumWidth(120)
        self.status["select"].setMinimumWidth(150)
        self.status["coding"].setMinimumWidth(80)
        self.status["coding"].setAlignment(Qt.AlignCenter)
        self.status["lines"].setMinimumWidth(60)
        self.status["lines"].setAlignment(Qt.AlignRight)
        self.statusbar.addPermanentWidget(self.status["line"])
        self.statusbar.addPermanentWidget(self.status["select"])
        self.statusbar.addPermanentWidget(self.status["coding"])
        self.statusbar.addPermanentWidget(self.status["lines"])

    def createDocks(self):
        self.docks["color"] = QDockWidget(self.tr("Color Variables"))
        self.docks["preview"] = QDockWidget(self.tr("Preview"))

        self.docks["color"].setMinimumSize(QSize(80, 20))
        self.docks["color"].setFeatures(QDockWidget.AllDockWidgetFeatures)
        self.docks["preview"].setMinimumSize(QSize(200, 200))
        self.docks["preview"].setFeatures(QDockWidget.DockWidgetMovable | QDockWidget.DockWidgetFloatable)

        self.addDockWidget(Qt.LeftDockWidgetArea, self.docks["color"])
        self.addDockWidget(Qt.RightDockWidgetArea, self.docks["preview"])

        class ColorPanelWidget(QWidget):
            def sizeHint(self):
                return self.layout().sizeHint()

        colorPanelWidget = ColorPanelWidget()
        # self.colorPanelLayout = QFlowLayout()
        colorPanelWidget.setLayout(self.colorPanelLayout)
        self.docks["color"].setWidget(colorPanelWidget)
        self.docks["preview"].setWidget(PreviewWidget())

        self.docks["color"].visibilityChanged.connect(self.actions["ShowColor"].setChecked)

    def createMainWidget(self):
        self.setCentralWidget(self.mainWidget)
        self.mainWidget.setTabBarAutoHide(True)
        self.mainWidget.addTab(self.editor, self.tr("main", "CodeEditor tab in tabwidget of mainwidget"))
