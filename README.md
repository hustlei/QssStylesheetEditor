English | [简体中文](https://github.com/hustlei/tomlconfig/blob/master/README_zh-CN.md)

# tomlconfig
Toml configparser made (stupidly) simple for python.

# install

~~~shell
pip install tomlconfig
~~~

# Usage

Define the toml config file "config.toml" as following:

~~~
[general]
language = 'en'

[general.editor]
size = 12
font = 'arial'
~~~

TomlConfig parse it very simply:

~~~python
from tomlconfig import TomlConfig

# read config file
config = TomlConfig("config.toml")

# get item
language = config["general.language"] # "en"
size = config["general.editor.size"]  # 12

# in operation
"general.language" in  config  # True"
config.hasSec("general") # True
config.hasSec("general.language") #False

# set item
config["general.editor.font"] = "Roman" # set font=Roman in toml

# add item
config["server.name"] = 'server1' # add a new item
config["newSection"] = {"k1":1} # add a new config section

# delete item
del config["server.name"]

# list item operation
config.insertToChild("general.editor.font", 0, "Arial") # change font from str to list and insert item
config.appendToChild("general.editor.font", "SimSun") # font=["Arial", "Roman", "SimSun"]
# same as config["general.editor.file"].append("SimSun")

# save
config.save()
# saveas
config.save("newfile.toml")
~~~
