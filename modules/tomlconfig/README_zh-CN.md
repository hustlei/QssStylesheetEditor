简体中文 | [English](https://github.com/hustlei/tomlconfig/blob/master/README.md)

# tomlconfig
最简单，最易用的toml配置文件解析器（python库）.

# 安装

~~~shell
pip install tomlconfig
~~~

# 使用方法

假如有一个toml配置文件 "config.toml", 内容为:

~~~
[general]
language = 'en'

[general.editor]
size = 12
font = 'arial'
~~~

使用 TomlConfig 可以非常简单的解析和修改配置:

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
