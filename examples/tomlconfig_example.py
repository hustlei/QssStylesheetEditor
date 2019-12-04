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

# in or not
if "general.language" in config:
    print("'general.language' is an option or section in tomlcofig.")
language = config["general.language"]
print("language content is:" + language)

size = config.getChild("general.editor.size")
print("size:{}".format(size))
font = config.getSec("general.editor").get("font")
# print("font:" + font)
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
