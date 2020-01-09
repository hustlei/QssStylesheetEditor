简体中文 | [English](https://github.com/hustlei/CodeEditor/blob/master/README.md)

# CodeEditor
支持语法高亮，非常容易自定义配置的编辑器库。

CodeEditor是一个基于 QScintilla 的python库。支持的功能有：

1. 自带搜索和替换对话框
2. 自带配置面板控件
3. 易用的配置 api

# 用法

创建编辑器, 打开文件，使用搜索和替换对话框:

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

搜索和替换对话框截图:

![search dialog screenshot](https://github.com/hustlei/CodeEditor/blob/master/docs/assets/screenshot/find.png?raw=true)
![replace dialog screenshot](https://github.com/hustlei/CodeEditor/blob/master/docs/assets/screenshot/replace.png?raw=true)

创建配置面板控件:

~~~python
from CodeEditor import editor

edt = editor()                  # create editor
panel = edt.settings.settingPanel()  # create setting panel
panel.apply()  # apply all change options in setting panel
panel.cancel() # cancel all change options and refresh setting panel
~~~

配置面板控件是一个可滚动的 Qt 控件, 实际显示效果如下:

![setting panel screenshot](https://github.com/hustlei/CodeEditor/blob/master/docs/assets/screenshot/settingpanel.png?raw=true)

配置编辑器:

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
