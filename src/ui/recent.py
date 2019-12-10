# -*- coding: utf-8 -*-
"""load add save recent opened list

Example::

    recent = Recent(openfilefn, recentmenu)
    recent.setList(['file1', 'file2'])
    recent.addFile('newfile')

Copyright (c) 2019 lileilei <hustlei@sina.cn>
"""

import os
from PyQt5.QtWidgets import QAction


class Recent():
    """Class for add recent opened file path to recent menu"""
    def __init__(self, openfn, menu=None):
        super().__init__()
        self._pathes = []
        self.maxcount = 4
        self.open = openfn
        self.menu = menu

    def _updateMenu(self, recentMenu=None):
        """Update files in recent to menubar"""
        if recentMenu is None:
            recentMenu = self.menu
        if recentMenu is not None:
            recentMenu.clear()
            for path in self._pathes:
                f = os.path.basename(path)
                action = QAction(f, recentMenu)
                action.setToolTip(path)
                action.setStatusTip(path)
                action.triggered.connect(lambda _, p=path: self._recentact(p))
                recentMenu.addAction(action)

    def _recentact(self, path):
        """Method implemented when recent menu clicked"""
        self.open(path)

    def addFile(self, filePath):
        """Add one file to recent and update menu"""
        if filePath in self._pathes:
            self._pathes.remove(filePath)
        self._pathes.insert(0, filePath)
        if len(self._pathes) > self.maxcount:
            self._pathes.pop()
        if self.menu is not None:
            self._updateMenu()

    def setList(self, filelist):
        """Set filelist to recent and update menu"""
        self._pathes = filelist
        if filelist is None:
            self._pathes = []
        self._updateMenu()

    def getList(self):
        """Get filelist in recent"""
        return self._pathes
