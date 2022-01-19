#!usr/bin/python
# -*- coding: utf-8 -*-
"""example for TomlConfig

| author: lileilei  email: <hustlei@sina.cn>  @2019, wuhan
"""

import sys, os

currentdir = os.path.dirname(__file__)
sys.path.append(currentdir + "/..")  # test environments, if TomlConfig is installed, this not needed
from tomlconfig import TomlConfig

# read config file
config = TomlConfig()
if config.read(os.path.join(currentdir, "config.toml")):
    print("config file loaded")
else:
    print("config file not loaded")

# in or not
if "general.language" in config:
    print("'general.language' is an option or section in tomlcofig.")

# get item
language = config["general.language"]
print("language content is:" + language)
size = config["general.editor.size"]
print("size:{}".format(size))

# set item or add item
config["general.editor.font"] = "Roman"
config["general.editor.fontWeight"] = 2
print("add item fontWeight, and value is set to:{}".format(config["general.editor.fontWeight"]))
config["newSection"] = {'key1': 1}  # add section

# is a section in toml
if config.hasSec("general.editor"):  # True
    print("'general.editor' is a section in config")

# list item operation
config.insertToChild("general.editor.font", 0, "Arial")  # change font from str to list and insert item
config.appendToChild("general.editor.font", "SimSun")  # font=["Arial", "Roman", "SimSun"]
# same as config["general.editor.file"].append("SimSun")
print("font list is:{}".format(config["general.editor.font"]))

# save toml config file
# config.save()
