# -*- coding: utf-8 -*-   
from PyQt5.QtGui import *  
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *  
import sys  

'''
QPalette.Window:设置布局控件、容器控件空白部分背景
QPalette.Base：设置ComboBox下拉框、TextEdit的背景(不包含LineEdit，LineEdit背景一直是白色)
QPalette.Button:不起作用
QPalette.WindowText：lable的文字颜色
QPalette.Text:Combobox，文本编辑框的文字颜色
QPalette.ButtonText: 按钮、下拉框箭头颜色
self.setAutoFillBackground貌似不起作用。所有palette设置并不会影响子窗口的颜色
'''
  
class Palette(QDialog):  
    def __init__(self,parent=None):  
        super().__init__(parent)  
        self.setWindowTitle(self.tr("QPalette对话框"))     
        #self.setAutoFillBackground(True)  
        self.p=self.palette() 
  
        mainLayout=QHBoxLayout(self)  
        self.ctrlFrame=QFrame()  
        self.contentFrame=QFrame()  
        self.createCtrlFrame()  
        self.createContentFrame()  
        mainLayout.addWidget(self.ctrlFrame)  
        mainLayout.addWidget(self.contentFrame)      
  
    def createCtrlFrame(self):  
        label1=QLabel("QPalette.Window")  
        self.windowComboBox=QComboBox()  
        label2=QLabel("QPalette.WindowText")  
        self.windowTextComboBox=QComboBox()  
        label3=QLabel("QPalette.Button")  
        self.buttonComboBox=QComboBox()  
        label4=QLabel("QPalette.ButtonText")  
        self.buttonTextComboBox=QComboBox()  
        label5=QLabel("QPalette.Base")  
        self.baseComboBox=QComboBox()  
        label6=QLabel("QPalette.Text")  
        self.textComboBox=QComboBox()  
  
        self.fillColorList(self.windowComboBox)  
        self.fillColorList(self.windowTextComboBox)  
        self.fillColorList(self.buttonComboBox)  
        self.fillColorList(self.buttonTextComboBox)  
        self.fillColorList(self.baseComboBox) 
        self.fillColorList(self.textComboBox)  
        self.windowComboBox.currentIndexChanged.connect(self.slotWindow)  
        self.windowTextComboBox.currentIndexChanged.connect(self.slotWindowText)  
        self.buttonComboBox.currentIndexChanged.connect(self.slotButton)  
        self.buttonTextComboBox.currentIndexChanged.connect(self.slotButtonText)  
        self.baseComboBox.currentIndexChanged.connect(self.slotBase)   
        self.textComboBox.currentIndexChanged.connect(self.slotText)  
          
        gridLayout=QGridLayout()  
        gridLayout.addWidget(label1,0,0)  
        gridLayout.addWidget(self.windowComboBox,0,1)  
        gridLayout.addWidget(label2,1,0)  
        gridLayout.addWidget(self.windowTextComboBox,1,1)  
        gridLayout.addWidget(label3,2,0)  
        gridLayout.addWidget(self.buttonComboBox,2,1)  
        gridLayout.addWidget(label4,3,0)  
        gridLayout.addWidget(self.buttonTextComboBox,3,1)  
        gridLayout.addWidget(label5,4,0)  
        gridLayout.addWidget(self.baseComboBox) 
        gridLayout.addWidget(label6,5,0)  
        gridLayout.addWidget(self.textComboBox)  
  
        self.ctrlFrame.setLayout(gridLayout)  
  
    def fillColorList(self,comboBox):  
        colorList=QColor.colorNames()  
          
        for color in colorList:  
            pix=QPixmap(QSize(70,20))  
            pix.fill(QColor(color))  
            comboBox.addItem(QIcon(pix),color)  
            comboBox.setIconSize(QSize(70,20))  
            comboBox.setSizeAdjustPolicy(QComboBox.AdjustToContents)  
          
    def createContentFrame(self):  
        label1=QLabel(self.tr("请选择一个值"))  
        valueComboBox=QComboBox()  
        valueComboBox.addItem("1")  
        valueComboBox.addItem("2")  
        label2=QLabel(self.tr("请输入字符串"))  
        stringLineEdit=QLineEdit()  
        textEditText=QTextEdit(self.tr("请输入"))  
        hLayout=QHBoxLayout()  
        okButton=QPushButton(self.tr("确定"))  
        cancelButton=QPushButton(self.tr("newWIn"))  
        hLayout.addStretch()  
        hLayout.addWidget(okButton)  
        hLayout.addWidget(cancelButton)  
        gridLayout=QGridLayout()  
        gridLayout.addWidget(label1,0,0)  
        gridLayout.addWidget(valueComboBox,0,1)  
        gridLayout.addWidget(label2,1,0)  
        gridLayout.addWidget(stringLineEdit,1,1)  
        gridLayout.addWidget(textEditText,2,0,1,2)  
        gridLayout.addLayout(hLayout,3,0,1,2)  
        self.contentFrame.setLayout(gridLayout)  
        cancelButton.pressed.connect(self.newwin)
  
    def slotWindow(self):  
        colorList=QColor.colorNames()  
        color=QColor(colorList[self.windowComboBox.currentIndex()])  
        self.p.setColor(QPalette.Window,color)  
        self.setPalette(self.p)  
  
    def slotWindowText(self):  
        colorList=QColor.colorNames()  
        color=QColor(colorList[self.windowTextComboBox.currentIndex()])  
        self.p.setColor(QPalette.WindowText,color)  
        self.setPalette(self.p)  
  
    def slotButton(self):  
        colorList=QColor.colorNames()  
        color=QColor(colorList[self.buttonComboBox.currentIndex()])  
        self.p.setColor(QPalette.Button,color)
        self.setPalette(self.p)  
  
    def slotButtonText(self):  
        colorList=QColor.colorNames()  
        color=QColor(colorList[self.buttonTextComboBox.currentIndex()])  
        self.p.setColor(QPalette.ButtonText,color)  
        self.setPalette(self.p)  
  
    def slotBase(self):  
        colorList=QColor.colorNames()  
        color=QColor(colorList[self.baseComboBox.currentIndex()])  
        self.p.setColor(QPalette.Base,color)  
        self.setPalette(self.p)  
  
    def slotText(self):  
        colorList=QColor.colorNames()  
        color=QColor(colorList[self.textComboBox.currentIndex()])  
        self.p.setColor(QPalette.Text,color)  
        self.setPalette(self.p)  
        
    def newwin(self):
        w=Palette(self)
        w.show()
  
app=QApplication(sys.argv)
main=Palette()  
main.show()  
app.exec_()  