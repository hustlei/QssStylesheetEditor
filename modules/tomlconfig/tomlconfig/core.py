# -*- coding: utf-8 -*-
"""Basic for load save and add item for toml config file

Copyright (c) 2019 lileilei <hustlei@sina.cn>
"""

import os
import toml
from .base import TomlSection


class TomlConfig(TomlSection):
    """Paser for toml config file"""
    def __init__(self, tomlFile=None):
        super().__init__()
        self.configFile = tomlFile
        if not self.configFile:
            self.read(self.configFile)

    def readString(self, tomlString=""):
        """Read toml config from  a TOML-formatted string, all config will be clear when reading the string

        :param tomlString: toml string same as text in toml file
        :return: if success return True, else False
        """
        try:
            self.clear()
            tomdict = toml.loads(tomlString, _dict=dict)
            self.update(TomlSection(tomdict))
        except:
            return False
        return True

    def read(self, tomlFile):
        """Read a toml config file

        Toml file shall be coded in utf-8
        Parser toml file and store config into self.dict

        :pram tomlFile:  toml config file path
        :return: Success or failed, return true if read success
        """
        if tomlFile is None:
            return False
        if not os.path.exists(tomlFile):
            print('Toml config file: "' + os.path.basename(tomlFile) + '" not found.')
            return False
        with open(tomlFile, mode='rb') as f:
            content = f.read()
        self.configFile = tomlFile
        if content.startswith(b'\xef\xbb\xbf'):  # 去掉 utf8 bom 头 #TOML要求使用UTF-8 编码
            content = content[3:]
        self.clear()
        tomldict = toml.loads(content.decode('utf8'))  # _dict=TomlSection))
        self.update(TomlSection(tomldict))  # ,
        return True

    def save(self, tomlFile=None, coding='utf-8'):
        """Save toml config to toml file.

        :param tomlFile: file to be saved. if toml is None, default save to self.configFile
        :param coding: tomlFile coding, default is 'utf-8', it's not recommanded to change it
        :return: True if successed else False
        """
        if tomlFile is None:
            tomlFile = self.configFile
        if tomlFile is not None:
            with open(tomlFile, 'w', newline='', encoding=coding) as outfile:
                # 不指定newline，则换行符自动转换为各系统默认的换行符(\n, \r, or \r\n,), newline=''表示不转换
                s = toml.dumps(self)
                outfile.write(s)
                return True
        return False
