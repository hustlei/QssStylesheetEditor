QssStylesheetEditor是一个编译Qt样式表,即Qss样式文件的软件。

# 功能简介

+ 支持在编辑Qss文件的同时，实时预览Qss样式效果。
+ 支持自定义变量，在Qss中引用。
+ 自定义变量会自动显示在颜色编辑面板，可以通过颜色对话框中拾取变量的颜色。
+ 编辑器支持代码高亮，代码折叠。

# screenshot

![GUI(v1.2版本) screeshot](img/screenshot/QssStylesheetEditor_v1.2.png "GUI(v1.2版本)")

# 使用

本软件基于Python3，依赖PyQt5, Qscintilla。

所以使用之前需要安装python3，然后`pip instll PyQt5`和`pip instll Qscintilla`安装两个依赖库。

# 变量定义

变量定义方式如下：

~~~
$background = #fff;
$border     = red;
~~~


变量通过“$变量名”方式引用。参考如下：
~~~
QWidget
{
    color: $text;
    background-color: $background;
}
~~~


# screenshot(old version)

<div><span><b>QssStylesheetEditor GUI V1.1</b></span></div>
    <img src="https://raw.githubusercontent.com/hustlei/QssStylesheetEditor/master/img/screenshot/QssStylesheetEditor_v1.1.png" alt="v1.1" height=200/>
<div><span><b>QssStylesheetEditor GUI V1.0</b></span></div>
    <img src="https://raw.githubusercontent.com/hustlei/QssStylesheetEditor/master/img/screenshot/QssStylesheetEditor_v1.0.png" alt="v1.0" height=200/>


