QssStylesheetEditor是一个编译Qt样式表,即Qss样式文件的软件。

QssStylesheetEditor使用Python编写，GUI使用Pyqt5。

# 功能简介

+ 编辑Qss文件，能够实时预览Qss样式效果。
+ 支持定义变量，在Qss中引用。
+ 文档中定义的变量会自动显示在颜色编辑面板，可以通过颜色对话框中拾取变量的颜色。

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


# GUI截图

** GUI(V1.1) **
![GUI(v1.1版本) screeshot](img/screenshot/QssStylesheetEditor_v1.1.png "GUI(v1.0版本)")

** Color pick Dialog **
![color pick screeshot](img/screenshot/ColorDlg_v1.0.png "Color Pick")

## 老版本截图

** GUI(V1.0) **
![GUI(v1.0版本) screeshot](img/screenshot/QssStylesheetEditor_v1.0.png "GUI(v1.0版本)")