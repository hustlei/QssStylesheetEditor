# -*- coding: utf-8 -*-
"""load add save recent opened list
Copyright (c) 2019 lileilei <hustlei@sina.cn>
"""

import os
from PyQt5.QtWidgets import QAction

class Recent():
    def __init__(self, openfn, menu=None):
        super().__init__()
        self._pathes=[]
        self.maxcount=4
        self.open=openfn
        self.menu=menu

    def _updateMenu(self, recentMenu=None):
        if(recentMenu==None): recentMenu=self.menu
        if(recentMenu!=None):
            recentMenu.clear()
            for path in self._pathes:
                f=os.path.basename(path)
                action=QAction(f,recentMenu)
                action.setToolTip(path)
                action.setStatusTip(path)
                action.triggered.connect(lambda _,p=path:self._recentact(p))
                recentMenu.addAction(action)

    def _recentact(self,path):
        self._isact=True
        self.open(path)

    def addFile(self,filePath):
        if(filePath in self._pathes):
            self._pathes.remove(filePath)
        self._pathes.insert(0, filePath)
        if(len(self._pathes)>self.maxcount):
            self._pathes.pop()
        if(self.menu!=None):
            self._updateMenu()

    def setList(self, filelist):
        self._pathes=filelist
        if filelist==None:
            self._pathes=[]
        self._updateMenu()

    def getList(self):
        return self._pathes
