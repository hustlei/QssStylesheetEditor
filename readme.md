QssStylesheetEditor是一个编译Qt样式表,即Qss样式文件的软件。

QssStylesheetEditor使用Python编写，GUI使用Pyqt5。



# 功能简介

+ 能够实时预览Qss样式效果。
+ 本软件中能够直接编辑Qss文件。
+ 也可以定义变量，在Qss中引用。编辑完后，可以导出为Qss格式。
+ 变量的颜色可以在颜色对话框中拾取。

# 使用

+ 基于Python3。
+ 依赖PyQt5。


# GUI截图

** GUI(V1.1) **
![GUI(v1.1版本) screeshot](img/screenshot/QssStylesheetEditor_v1.1.png "GUI(v1.0版本)")

** GUI(V1.0) **
![GUI(v1.0版本) screeshot](img/screenshot/QssStylesheetEditor_v1.0.png "GUI(v1.0版本)")

** Color pick Dialog **
![color pick screeshot](img/screenshot/ColorDlg_v1.0.png "Color Pick")

# 变量定义

变量定义方式如下：

~~~
/*
background=#fff
border=#888
*/
~~~

> 变量需要在/* */内

变量通过“$变量名”方式引用。参考如下：
~~~
QWidget
{
    color: $text;
    background-color: $background;
}
~~~


