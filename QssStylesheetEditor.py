# -*- coding: utf-8 -*-
import os
from PyQt5.QtWidgets import (QApplication,QMainWindow,QLabel,QPushButton,
                            QColorDialog,QFileDialog)
from PyQt5.QtGui import QIcon,QColor,qGray
from PyQt5.QtCore import Qt
import sys
import sip

from Ui import QssWin
from QssTemplate import Qsst
  
class QssWin(QMainWindow,QssWin):
    def __init__(self,parent=None):
        super(QMainWindow,self).__init__(parent)
        import os
        os.chdir(os.path.dirname(__file__))
        self.setWindowTitle(self.tr("Qss Template Editor"))
        self.setWindowIcon(QIcon("Ui/img/Colorize.ico"))
        self.qsst=Qsst()
        self.dlg=QColorDialog(self)
        
        self.setupUi(self)
        self.renderAct.triggered.connect(lambda:self.render(True))
        self.norenderAct.triggered.connect(lambda:self.render(False))
        self.textEdit.keyPressed.connect(self.textChanged)
        self.modeBtn.toggled.connect(self.chToColorMode)
        self.textEdit.loseFocus.connect(self.render)
        self.textEdit.mouseLeave.connect(self.render)
        self.saveAct.triggered.connect(self.save)
        self.openAct.triggered.connect(self.open)
        self.exportAct.triggered.connect(self.export)
        self.open(file="data/default.qsst")
        self.file="data/new-1.qsst"
        self.setWindowTitle("Qss Template Editor  -  "+os.path.basename(self.file))
        self.statusbar.showMessage("Ready")
        
    def open(self,_=None,file=None):
        if(file is None):
            file,_=QFileDialog.getOpenFileName(self,"open Qsst File",".",
                "Qsst(*.qsst);;all(*.*)")
        if(os.path.exists(file)):
            self.textEdit.setText(open(file,'r').read())
            self.loadColors()
            self.render()
            self.setWindowTitle("Qss Template Editor  -  "+os.path.basename(file))
            
    
    def save(self):
        if(os.path.exists(self.file)):
            file=self.file
        else:
            file,_=QFileDialog.getSaveFileName(self,"save file",".","Qsst(*.qsst);;all(*.*)")
        if(file):
            self.file=file
            with open(file,'w') as f:
                f.write(self.textEdit.toPlainText())
                self.setWindowTitle("Qss Template Editor  -  "+os.path.basename(file))
                
    def export(self):
        self.qsst.convertQss()
        #f=os.path.join(os.path.splitext(f)[0],"Qss")
        file,_=QFileDialog.getSaveFileName(self,"export Qss file",".","Qss(*.qss);;all(*.*)")
        with open(file,'w') as f:
            f.write(self.qsst.qss)
        
    def loadColors(self):
        self.qsst.srctext=self.textEdit.toPlainText()
        self.qsst.loadVars()
        item=self.colorGridLayout.itemAt(0)
        while(item!=None):
            self.colorGridLayout.removeItem(item)
            #self.colorGridLayout.removeWidget(item.widget())
            #item.widget().setParent(None)#这三行没有作用
            sip.delete(item.widget())#虽然控件删除了，但是grid的行数列数没减少，但是不影响使用
            sip.delete(item)
            item=self.colorGridLayout.itemAt(0)
        self.colorGridLayout.update()#不起作用
        i=0
        self.dict={}
        for var,clr in self.qsst.varDict.items():
            a=QLabel(var,self)
            b=QPushButton(clr,self)
            b.setMinimumSize(100,10)
            b.clicked.connect(lambda x,var=var:self.chclr(var))
            self.colorGridLayout.addWidget(a,i,0)
            self.colorGridLayout.addWidget(b,i,1)
            self.dict[var]=b
            i=i+1
        self.colorGridLayout.setSpacing(15)
        self.colorGridLayout.setRowStretch(i,1)
        
    def chclr(self,var):
        color=self.dlg.getColor(self.dlg.currentColor(),self,"color pick",QColorDialog.ShowAlphaChannel)
        if(color.isValid()):
            s=''
            if(color.alpha()==255):
                clrstr=color.name()
            else:
                clrstr='rgba({},{},{},{})'.format(color.red(),color.green(),color.blue(),color.alpha())
                s='font-size:8px;'
            if(qGray(color.rgb())<100):
                s+='color:white;'
            self.dict[var].setText(clrstr)
            self.dict[var].setStyleSheet(s+"background:"+clrstr)
            self.qsst.varDict[var]=clrstr
            self.qsst.writeVars()
            self.textEdit.setPlainText(self.qsst.srctext)
            self.render()
        
    def render(self,rend=True):
        if(rend):
            if(self.modeBtn.isChecked()):
                self.qsst.srctext=self.textEdit.toPlainText()
                self.qsst.loadVars()
            self.qsst.convertQss()
            self.setStyleSheet(self.qsst.qss)
        else:
            self.setStyleSheet('')
            
        for var,btn in self.dict.items():
            if("rgb" in btn.text()):
                t=btn.text().strip(r" rgba()")
                c=t.split(',')
                if(len(c)>3):
                    a=c[3]
                else:
                    a=255
                color=QColor(r,g,b,a)
            else:
                color=QColor(btn.text())
            s=''
            if(qGray(color.rgb())<100):
                s+="color:white;"
            btn.setStyleSheet(s+"background:"+btn.text())
            
    def textChanged(self,e):#QKeyEvent(QEvent.KeyPress, Qt.Key_Enter, Qt.NoModifier)
        if(not self.textEdit.isReadOnly()):
            if(e.key()==Qt.Key_Enter or e.key()==Qt.Key_Return
                or e.key()==Qt.Key_Tab or e.key()==Qt.Key_Semicolon):
                self.render()
            
    def chToColorMode(self,iseditable):
        if(not iseditable):
            self.loadColors()
            self.render()
        
if __name__=="__main__":
    app=QApplication(sys.argv)
    win=QssWin()
    win.show()
    sys.exit(app.exec_())  
