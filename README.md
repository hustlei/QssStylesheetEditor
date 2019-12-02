# TomlConfig
Toml configparser made (stupidly) simple.

# install

~~~shell
python setup.py install
~~~

# Usage


~~~python
from tomlconfig import TomlConfig
config=TomlConfig("config.toml")
language=config.getChild("general.language")
size=config.getChild("general.editor.size")
font=config.getChild("general.editor").get("font")
fontWeight=config.getChild("general.editor").get("fontWeight",2)

config.hasChild("general.language") # True
config.hasSec("general") # True
config.hasSec("general.language") # False
config.addSec("otherSection")
config.addChild("general.theme", "simple") # add "theme=simple" to general
~~~

Assume the config.toml content is:

~~~
[general]
language = 'en'

[general.editor]
size = 12
font = 'arial'
~~~