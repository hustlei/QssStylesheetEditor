# -*- coding: utf-8 -*-
"""Basic for load save and add item for toml config file

Copyright (c) 2019 lileilei <hustlei@sina.cn>
"""

import os
from config.base import ConfBase


class Config(ConfBase):
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
        if super()._save(self.file):
            print("config file saved.")
