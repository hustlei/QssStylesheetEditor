# -*- coding: utf-8 -*-
"""Basic for load save and add item for toml config file

Copyright (c) 2019 lileilei <hustlei@sina.cn>
"""

from .base import ConfBase
from .dialog import ConfDialog

class Config(ConfBase):
    def __init__(self):
        super().__init__()
        self.dialog=ConfDialog()

    def showDialog(self):
        self.dialog.show()

if __name__=="__main__":
    cfgfile="config.toml"
    conf=ConfBase()
    if(conf.read(cfgfile)):
        filesec=conf._getSec("file")
        conf.listNodeAppend("recent","eeee",filesec)
        fontsec=conf._getSubSec(conf._getSec("editor"), "font")
        fontsec["size"]=12
        conf.rmSec("editor0")
        conf.save()