# -*- coding: utf-8 -*-
"""Basic for load save and add item for toml config file

Copyright (c) 2019 lileilei <hustlei@sina.cn>
"""

import os
import toml
from config.base import Section

class ConfigParser(Section):
    """Paser for toml config file"""
    def __init__(self):
        self.cfgFile=None
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

    def save(self, cfgFile=None, coding='utf-8'):
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

class Config(ConfigParser):
    """Config parser for config.toml"""
    def __init__(self, cfgfile=None):
        super().__init__()
        default = os.path.join(os.path.dirname(__file__), "config.toml")
        if cfgfile is None:
            cfgfile = default
        if not os.path.exists(cfgfile):
            s = """[general]

            [editor]

            """
            with open(cfgfile, "w", newline="") as newf:
                newf.write(s)
        self.file = cfgfile
        if self.read(cfgfile):
            print('config file load successed!')

    def save(self):
        if super().save(self.file):
            print("config file saved.")
