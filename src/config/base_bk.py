# -*- coding: utf-8 -*-
"""Toml config file parser

Copyright (c) 2019 lileilei <hustlei@sina.cn>
"""

import os
from . import toml


class Section(dict):
    """A section object in toml

    Extended dict.

    Examples:
        sec = Section()
        if not sec.hasSec("sec1.sec11"):
            sec.addSec("sec1.sec11")
        sec11 = sec.getSec("sec1.sec11")
        sec11.setValue("abc")
    """
    def __init__(self):
        super().__init__()

    def _addSec(self, secName):
        """Add a section to root of self"""
        secName = secName.strip()
        if len(secName) < 1:
            return None
        if secName not in self:
            self[secName] = Section()
        return self[secName]

    def _addSubSec(self, sec, subName):
        """Add section to section sec

        Args:
            sec: a section in self(section type must be dict)
            subName: name of section will be added
        """
        subName = subName.strip()
        if len(subName) < 1:
            return None
        if subName in sec:
            return sec[subName]
        sec[subName] = Section()
        return sec[subName]

    def _getSec(self, secName=None, addifnotfound=True):
        """Get section by name

        Args:
            secName: name of section in toml root, if None it's mean root
            defaultadd: if not found add the section
        """
        if secName is None:
            return self
        if secName in self:
            return (self[secName])
        if addifnotfound:
            return self._addSec(secName)
        return None

    def _getSubSec(self, sec, subName, addifnotfound=True):
        """Get section in section sec

        Args:
            sec: a section, type must be dict
        """
        if subName in sec:
            return sec[subName]
        if addifnotfound:
            return self._addSubSec(sec, subName)
        return None

    def _rmSec(self, secName):
        """Remove section in root of toml

        Returns:
            return the section removed, if section not exist return None
        """
        if secName not in self:
            return None
        return self.pop(secName, None)

    def _rmSubSec(self, sec, subName):
        """Remove section in sec"""
        return sec.pop(subName, None)

    #
    # Section Operate
    #
    def hasSec(self, secString):
        """If section exist and type is dict return true, else false

        Args:
            secString: "secname.subsecname" format path to ditermine section
        """
        secString = secString.strip(". ")
        if len(secString) < 1:
            return False
        secs = secString.split(".")
        sec = self
        for i in range(0, len(secs)):
            if secs[i] not in sec:
                return False
            sec = sec[secs[i]]
        if isinstance(sec, dict):
            return True
        return False

    def addSec(self, secString):
        """Add section using format secname.subsecname string

        Example:
            `self.addSec("general.subsection")`: aaa subsection of general section
        """
        secString = secString.strip()
        if len(secString) < 1:
            return self
        secString = secString.strip(".")
        secs = secString.split(".")
        sec = self._addSec(secs[0])
        for i in range(1, len(secs)):
            sec = self._addSubSec(sec, secs[i])
        return sec

    def rmSec(self, secString):
        """Remove secname.subsecname sections if exist"""
        secString = secString.strip()
        if len(secString) < 1:
            return None
        secString = secString.strip(".")
        secs = secString.split(".")
        sec = self
        for i in range(0, len(secs) - 1):
            sec = sec[secs[i]]
            if not isinstance(sec, dict):
                return None
        return self._rmSubSec(sec, secs[-1])

    def getSec(self, secString=None, addifnotfound=True):
        """Get section by secname.subsecname string

        Example:
            `self.getSec()`: get root section
            `self.getSec("general.subsection")`: get the subsection of general section

        Args:
            addifnotfound: if True, if section is not found, add it to toml
        """
        if secString is None:
            return self
        secString = secString.strip()
        if len(secString) < 1:
            return None
        secString = secString.strip(".")
        secs = secString.strip().split(".")
        if len(secs) == 1:
            return self._getSec(secs[0], addifnotfound)
        sec = self._getSec(secs[0])
        for i in range(1, len(secs)):
            sec = self._getSubSec(sec, secs[i], addifnotfound)
            if sec is None:
                return None
        return sec

    #
    # Child Item Operate
    #
    def hasChild(self, childString):
        """If child item exist return true, else false

        Args:
            childString: "childname.subchildname" format path to ditermine child item
        """
        childString = childString.strip()
        if len(childString) < 1:
            return False
        childNames = childString.split(".")
        item = self
        for i in range(0, len(childNames)):
            if childNames[i] not in item:
                return False
            item = item[childNames[i]]
        return True

    def addChild(self, childString, obj):
        """Add child using format childname.subchildname string

        Example:
            `self.addChild("child.key1", "value")`: aaa subsection of general section
        """
        childString = childString.strip()
        if len(childString) < 1:
            return self
        childString = childString.strip(".")
        childNames = childString.split(".")
        sec = self
        for i in range(0, len(childNames) - 1):
            sec = self._addSubSec(sec, childNames[i])
        return sec._addSubSec(sec, obj)

    def rmChild(self, childString):
        pass

    def getChild(self, childString):
        pass

    def appendToChild(self, node, child, sec=None):
        if sec is None:
            sec = self.dict
        if node not in sec or not isinstance(sec[node], list):
            sec[node] = []
        if child in sec[node]:
            for _ in range(sec[node].count(child)):
                sec[node].remove(child)
        sec[node].appendToChild(child)

    def insertToChild(self, node, child, sec=None):
        if sec is None:
            sec = self.dict
        if node not in sec or not isinstance(sec[node], list):
            sec[node] = []
        if child in sec[node]:
            for _ in range(sec[node].count(child)):
                sec[node].remove(child)
        sec[node].insertToChild(0, child)


class ConfigParser(Section):
    """Paser for toml config file"""
    def __init__(self):
        # self.dict = {}
        self.cfgFile = None
        super().__init__()

    def read(self, cfgFile=None):
        """Read a toml config file

        Toml file shall be coded in utf-8
        Parser toml file and store config into self.dict

        Args:
            cfgFile:  config file path
        Returns:
            Success or failed, return true if read success
        """
        if cfgFile is None:
            return False
        if not os.path.exists(cfgFile):
            print("Toml config file: \"" + os.path.basename(cfgFile) + '\" not found.')
            return False
        with open(cfgFile, mode='rb') as f:
            content = f.read()
        if content.startswith(b'\xef\xbb\xbf'):  # 去掉 utf8 bom 头 #TOML要求使用UTF-8 编码
            content = content[3:]
        self.clear()
        self.update(toml.loads(content.decode('utf8'), _dict=Section))
        return True

    def _save(self, cfgFile=None, coding='utf-8'):
        """save config in self.dict to toml file."""
        if cfgFile is None:
            cfgFile = self.cfgFile
        if cfgFile is not None:
            with open(cfgFile, 'w', newline='', encoding=coding) as outfile:
                # 不指定newline，则换行符自动转换为各系统默认的换行符(\n, \r, or \r\n,)
                # newline=''表示不转换
                s = toml.dumps(self.dict)
                outfile.write(s)
                return True
        return False

    # def sections(self):
