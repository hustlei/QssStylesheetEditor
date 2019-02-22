# -*- coding: utf-8 -*-   
from PyQt5.QtGui import *  
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *  
import sys  

from .Editor import TextEdit
  
class QssWin(object):  
    def setupUi(self,MainWindow):
        MainWindow.setWindowTitle(self.tr("Qss Template Editor"))
        MainWindow.resize(800,600)
        
        self.createActions()
        self.menubar=MainWindow.menuBar()
        self.setupMenubar()
        self.setupToolbar()
        self.statusbar=self.statusBar()
        
        self.dockColors=QDockWidget("Color Setting",self)
        self.dockColors.setMinimumSize(QSize(150,50))
        self.dockColors.setFeatures(QDockWidget.DockWidgetMovable)
        self.dockColors.setAllowedAreas(Qt.LeftDockWidgetArea|Qt.RightDockWidgetArea)        
        input=QWidget(self.dockColors)
        self.dockColors.setWidget(input)
        self.colorGridLayout=QGridLayout(input)
        self.addDockWidget(Qt.LeftDockWidgetArea,self.dockColors)
        centralLayout=QVBoxLayout()
        self.modeBtn=QPushButton(" ",self)
        self.modeBtn.setCheckable(True)
        self.modeBtn.setProperty("class","toggle")
        self.modeLabel=QLabel("配色模式",self)
        hLayout0=QHBoxLayout()
        hLayout0.addStretch(1)
        hLayout0.addWidget(self.modeBtn)
        hLayout0.addWidget(self.modeLabel)
        centralLayout.addLayout(hLayout0)
        self.textEdit=TextEdit()
        self.textEdit.resize(300,300)
        self.textEdit.setMinimumSize(300,50)
        self.modeBtn.toggled.connect(self.chTextMode)
        self.modeBtn.setChecked(False)#不知道为何没有触发信号
        self.chTextMode(False)
        splitter=QSplitter(Qt.Vertical,self)        
        splitter.addWidget(self.textEdit)
        self.contentTabWidget=QTabWidget(self)
        self.contentTabWidget.setMinimumSize(300,100)
        splitter.addWidget(self.contentTabWidget)
        centralLayout.addWidget(splitter)
        widget=QWidget()
        widget.setLayout(centralLayout)
        self.setCentralWidget(widget)
        self.setupContent()
        self.colorPannelView.triggered.connect(self.dockColors.setVisible)
        self.widgetsPannelView.triggered.connect(self.contentTabWidget.setVisible)
        
    def chTextMode(self,editable):
        btns=self.dockColors.findChildren(QPushButton)
        if(editable):
            self.textEdit.setReadOnly(False)
            for b in btns:
                b.setEnabled(False)
            self.dockColors.setVisible(False)
            self.modeLabel.setText("编辑模式")
        else:
            self.textEdit.setReadOnly(True)
            for b in btns:
                b.setEnabled(True)
            self.dockColors.setVisible(True)
            self.modeLabel.setText("配色模式")
        
    def createActions(self):
        self.newAct=QAction(QIcon('Ui/img/bt_invite_normal.bmp'),"&New",self)
        self.newAct.setShortcut("Ctrl+N")
        self.newAct.setStatusTip("new")
        self.openAct=QAction(QIcon('Ui/img/bt_addto_normal.bmp'),"&Open",self)
        self.openAct.setShortcut("Ctrl+O")
        self.openAct.setStatusTip(self.tr("Open"))
        self.saveAct=QAction(QIcon('Ui/img/bt_filesend_normal.bmp'),"&Save",self)
        self.saveAct.setShortcut("Ctrl+S")
        self.saveAct.setStatusTip(self.tr("Save"))
        self.exportAct=QAction("&ExportQss",self)
        self.exportAct.setShortcut("Ctrl+Shift+E")
        self.exportAct.setStatusTip(self.tr("ExportQss"))
        self.exitAct=QAction(QIcon('Ui/img/close.png'),"&Exit",self)
        self.exitAct.setShortcut("Ctrl+Q")
        self.exitAct.setStatusTip(self.tr("Close"))
        self.cutAct=QAction(QIcon('Ui/img/broadcast_send_cut_normal.bmp'),"&Cut",self)
        self.cutAct.setShortcut("Ctrl+X")
        self.cutAct.setStatusTip(self.tr("Cut"))
        self.copyAct=QAction(QIcon('Ui/img/broadcast_send_copy_normal.bmp'),"&Copy",self)
        self.copyAct.setShortcut("Ctrl+C")
        self.copyAct.setStatusTip(self.tr("Copy"))
        self.pasteAct=QAction(QIcon('Ui/img/broadcast_send_paste_normal.bmp'),"&Paste",self)
        self.pasteAct.setShortcut("Ctrl+V")
        self.pasteAct.setStatusTip(self.tr("Paste"))
        self.fontcolorAct=QAction(QIcon("Ui/img/broadcast_send_fontcolor_normal.bmp"),"&FontColor",self)
        self.fontcolorAct.setShortcut("Ctr+Shit+C")
        self.fontcolorAct.setStatusTip("FontColor")
        
        self.renderAct=QAction("refresh",self)
        self.norenderAct=QAction("nostyle",self)
        self.colorPannelView=QAction("Color Pannel",self)
        self.widgetsPannelView=QAction("Widgets Pannel",self)
        self.colorPannelView.setCheckable(True)
        self.colorPannelView.setChecked(True)
        self.widgetsPannelView.setCheckable(True)
        self.widgetsPannelView.setChecked(True)
        
        #self.exitAct.triggered.connect(qApp.exit)#等价于qApp.quit
        self.exitAct.triggered.connect(self.close)

        
    def setupMenubar(self):        
        filemenu=self.menubar.addMenu("&File")
        filemenu.addAction(self.newAct)
        filemenu.addAction(self.openAct)
        filemenu.addAction(self.saveAct)
        filemenu.addAction(self.exportAct)
        filemenu.addSeparator()
        filemenu.addAction(self.exitAct)
        editmenu=self.menubar.addMenu("&Edit")
        textSubmenu=editmenu.addMenu("&Text Edit")
        textSubmenu.addAction(self.cutAct)
        textSubmenu.addAction(self.copyAct)
        textSubmenu.addAction(self.pasteAct)
        editmenu.addSeparator()
        editmenu.addAction(self.fontcolorAct)
        viewMenu=self.menubar.addMenu("&View")
        viewMenu.addAction(self.colorPannelView)
        viewMenu.addAction(self.widgetsPannelView)
        
        
    def setupToolbar(self):
        self.editToolbar=self.addToolBar("Edit")
        self.editToolbar.addAction(self.cutAct)
        self.editToolbar.addAction(self.copyAct)
        self.editToolbar.addAction(self.pasteAct)
        self.mainToolbar=self.addToolBar("main")
        self.mainToolbar.addAction(self.renderAct)
        self.mainToolbar.addAction(self.norenderAct)
        
    def setupContent(self):
        self.tab1=QWidget(self)
        self.tab2=QWidget(self)
        self.tab3=QWidget(self)
        self.tab4=QWidget(self)
        self.tab5=QWidget(self)
        self.tab6=QWidget(self)
        self.contentTabWidget.addTab(self.tab1,"常用组件")
        self.contentTabWidget.addTab(self.tab2,"容器组件")
        self.contentTabWidget.addTab(self.tab3,"列表组件")
        self.contentTabWidget.addTab(self.tab4,"MDI组件")
        self.contentTabWidget.addTab(self.tab5,"tab选型卡")
        self.contentTabWidget.addTab(self.tab6,"日历等")
        self.setuptab1()
        
    def setuptab1(self):
        layout=QVBoxLayout(self.tab1)
        #button group
        hLayout1=QHBoxLayout()
        btn1=QPushButton("按钮1")
        btn2=QPushButton("按钮2")
        btn2.setEnabled(False)
        btn3=QToolButton(self)
        btn3.setText('ToolButton')#btn3.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        btn3.setPopupMode(QToolButton.MenuButtonPopup)
        btn3.addAction(self.cutAct)
        btn3.addAction(self.copyAct)
        btn4=QToolButton(self)
        btn4.setText('ToolButton')
        btn4.setPopupMode(QToolButton.MenuButtonPopup)
        btn4.setEnabled(False)
        btn5=QCommandLinkButton("LinkButton")
        btn6=QCommandLinkButton("LinkButton")
        btn6.setEnabled(False)
        hLayout1.addWidget(btn1)
        hLayout1.addWidget(btn2)
        hLayout1.addWidget(btn3)
        hLayout1.addWidget(btn4)
        hLayout1.addWidget(btn5)
        hLayout1.addWidget(btn6)
        #checkbox combobox
        hLayout2=QHBoxLayout()
        rbox1=QRadioButton("RadioBtn1",self)
        rbox2=QRadioButton("RadioBtn2",self)
        cbox1=QCheckBox("CheckBox1",self)
        cbox2=QCheckBox("CheckBox2",self)
        combo1=QComboBox(self)
        combo1.addItem("item1")
        combo1.addItem("item2")
        combo1.addItem("item3")
        combo2=QComboBox(self)
        combo2.addItem("item1")
        combo3=QFontComboBox(self)
        rbox1.setChecked(True)
        cbox1.setChecked(True)
        combo2.setEnabled(False)
        hLayout2.addWidget(rbox1)
        hLayout2.addWidget(rbox2)
        hLayout2.addWidget(cbox1)
        hLayout2.addWidget(cbox2)
        hLayout2.addWidget(combo1)
        hLayout2.addWidget(combo2)
        hLayout2.addWidget(combo3)
        #input group
        hLayout3=QHBoxLayout()
        label=QLabel("一个Label标签:",self)
        lineedit=QLineEdit("请输入：",self)
        pswedit=QLineEdit("password",self)
        pswedit.setEchoMode(QLineEdit.Password)
        hLayout3.addWidget(label)
        hLayout3.addWidget(lineedit)
        hLayout3.addWidget(pswedit)
        #picble input
        hLayout4=QHBoxLayout()
        spin1=QSpinBox(self)
        spin2=QSpinBox(self)
        spin2.setEnabled(False)
        spin3=QDoubleSpinBox(self)
        date1=QDateEdit(self)
        date2=QDateEdit(self)
        date2.setEnabled(False)
        date3=QDateTimeEdit(self)
        hLayout4.addWidget(spin1)
        hLayout4.addWidget(spin2)
        hLayout4.addWidget(spin3)
        hLayout4.addWidget(date1)
        hLayout4.addWidget(date2)
        hLayout4.addWidget(date3)
        #slider progress
        hLayout5=QHBoxLayout()
        slider=QSlider(self)
        slider.setOrientation(Qt.Horizontal)
        progress=QProgressBar(self)
        slider.setMaximum(100)
        slider.valueChanged.connect(progress.setValue)
        hLayout5.addWidget(slider)
        hLayout5.addWidget(progress)
        
        textedit=QTextEdit("Authored by hustlei.https://github.com/hustlei/QssStylesheetEditor")
        textedit.setPlainText("Authored by hustlei.\nhttps://github.com/hustlei/QssStylesheetEditor")
        layout.addLayout(hLayout1)
        layout.addLayout(hLayout2)
        layout.addLayout(hLayout3)
        layout.addLayout(hLayout4)
        layout.addLayout(hLayout5)
        layout.addWidget(textedit)
        
        
"""
+ 常用组件:
    - PushButton,CommandlinkButton
    - RadioButton, CheckButton, Combobox
    - Lable, LineEdit
    - SpinBox,DoubleSpinBox,DateEdit ,DateTimeEdit
    - Slider,ProgressBar
    - Textedit
+ 容器组件
    - GroupBox
    - Scroll Area
    - Tool Box
    - stacked widget
+ 列表组件
    - Table
    - List
    - Tree
+ tab选型卡
+ MDI组件
+ 显示组件
    - Calender
    - LCD
    - Dail
    - KeySequence Edit
    - Graphics
+ 对话框
    - https://blog.csdn.net/taiyang1987912/article/details/31770757
"""