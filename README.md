# TomlConfig
Toml configparser made (stupidly) simple.

# install

~~~shell
pip install TomlConfig
~~~

# Usage

~~~python
from tomlconfig import TomlConfig

# read config file
config=TomlConfig("config.toml")

# get config item
language=config["general.language"]
size=config["general.editor.size"]
font=config["general.editor"].get("font")
fontWeight=config["general.editor"].get("fontWeight",2)

# in operation
"general.language" in  config # True

# set config item
config["otherSection.key1"] = 'value1' # set to config
config["otherSection2"] = {"k1":1} # add config section
~~~

Assume the "config.toml" file content is:

~~~
[general]
language = 'en'

[general.editor]
size = 12
font = 'arial'
~~~