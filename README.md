English | [简体中文](https://github.com/hustlei/CodeEditor/blob/master/README_zh-CN.md)

# CodeEditor
Syntax highlighting code editor. Easy to config.
 
A python editor package, based on QScintilla. support:

+ find and replace dialog
+ setting panel for config dialog
+ easy config api

# usage

Create editor, open file or find text:

~~~python
from CodeEditor import editor

edt = editor()      # create editor object
edt.load("file.c")  # file.c will be opened, and highlighted under c syntax
edt.save("file.c")  # file will be saved.
edt.setText("abc")  # content in editor will be replace by "abc"
edt.clear() # content in editor will be cleaned.
edt.find()  # show find dialog
edt.replace() # show replace dialog
~~~

find and replace dialog will dispaly as follow:

![search dialog screenshot](https://github.com/hustlei/CodeEditor/blob/master/docs/assets/screenshot/find.png?raw=true)
![replace dialog screenshot](https://github.com/hustlei/CodeEditor/blob/master/docs/assets/screenshot/replace.png?raw=true)

create setting panel:

~~~python
from CodeEditor import editor

edt = editor()                  # create editor
panel = edt.settings.settingPanel()  # create setting panel
panel.apply()  # apply all change options in setting panel
panel.cancel() # cancel all change options and refresh setting panel
~~~

settingPanel is a Scrollable Qt Widget, it will display as follow:

![setting panel screenshot](https://github.com/hustlei/CodeEditor/blob/master/docs/assets/screenshot/settingpanel.png?raw=true)

config editor:

~~~python
from CodeEditor import editor
from PyQt5.QtCore import Qt

edt = editor()
# config method
edt.setLanguage("CSS")
edt.setFontSize(12)
edt.setBackgroundColor(Qt.blue)
# anothor config method
edt.settings.configuate(language="CSS", fontSize=12, backgroundColor="blue",
                        color="#FF0000", edgeMode="EdgeLine")
~~~

get config of editor:

~~~python
from CodeEditor import editor
edt = editor()

color = edt.color() # color=QColor("#FF0000")
color = edt.settings.get("color")  # color="#FF0000"
~~~
