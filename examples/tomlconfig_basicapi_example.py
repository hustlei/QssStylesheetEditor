#!usr/bin/python
# -*- coding: utf-8 -*-
"""example for TomlConfig

| author: lileilei  email: <hustlei@sina.cn>  @2019, wuhan
"""

import sys, os
currentdir = os.path.dirname(__file__)
sys.path.append(currentdir + "/..")  # test environments, if TomlConfig is installed, this not needed
from tomlconfig import TomlConfig

config = TomlConfig()
if config.read(os.path.join(currentdir, "config.toml")):
    print("config file loaded")
else:
    print("config file not loaded")

language = config.getChild("general.language")
print("language:" + language)
size = config.getChild("general.editor.size")
print("size:{}".format(size))
fontWeight = config.getChild("general.editor").get("fontWeight", 2)
print("fontWeight:{}".format(fontWeight))

haslang = config.hasChild("general.language")  # True
print("has general.language:{}".format(haslang))
hasgen = config.hasSec("general")  # True
print("has general section:{}".format(hasgen))
haslangsec = config.hasSec("general.language")  # False, language is not a section
print("has general.language section:{}".format(haslangsec))
config.addSec("otherSection")
config.addChild("general.theme", "simple")  # add "theme=simple" to general

# config.save(os.path.join(currentdir, "a.toml"))
