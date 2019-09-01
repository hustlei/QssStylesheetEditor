QssStylesheetEditor是一个功能强大的Qt样式表(QSS)编辑器，免费开源。

# 功能简介

+ 编辑Qss，实时预览Qss样式效果。
+ 支持代码高亮，代码折叠。
+ 支持Qss关键字、属性、伪元素等的自动提示，自动补全。
+ 支持在Qss中自定义变量，在Qss中引用。
+ 自定义变量会自动显示在颜色编辑面板，可以通过颜色对话框中拾取变量的颜色。

# screenshot

![GUI(v1.3版本) screeshot](img/screenshot/QssStylesheetEditor_v1.3.png "GUI(v1.3版本)")

# 使用

## windows 64bit
windows 64bit 操作系统可以下载exe，直接运行。

下载地址：

+ QssStylesheetEditor_1.3_win64_portable **[[zip Download]](https://pan.baidu.com/s/1dbC9rq91SlxguRONlUOocg)**(secuirity code: mq3c)
+ QssStylesheetEditor_1.3_win64_portable **[[7z Download]](https://pan.baidu.com/s/1HM9SW6BRlCkGKyUxonbh1w)**(secuirity code: bcaz) 


## 其他
如果在python环境下运行则需要PyQt5和Qscintilla。

+ 安装python3
+ 安装PyQt5:`pip instll PyQt5`
+ 安装Qscintilla：`pip instll Qscintilla`
+ 解压本软件源码，直接双击app.py即可运行

# 变量定义

本软件支持在qss中自定义变量，变量定义方式如下：

~~~
$background = #fff;
$border     = red;
~~~


变量引用方法：通过“$变量名”方式引用。参考如下：

~~~
QWidget
{
    color: $text;
    background-color: $background;
}
~~~

# screenshot(old version)

<div><span><b>QssStylesheetEditor GUI V1.2</b></span></div>
    <img src="https://raw.githubusercontent.com/hustlei/QssStylesheetEditor/master/img/screenshot/QssStylesheetEditor_v1.2.png" alt="v1.2" height=200/>
<div><span><b>QssStylesheetEditor GUI V1.1</b></span></div>
    <img src="https://raw.githubusercontent.com/hustlei/QssStylesheetEditor/master/img/screenshot/QssStylesheetEditor_v1.1.png" alt="v1.1" height=200/>
<div><span><b>QssStylesheetEditor GUI V1.0</b></span></div>
    <img src="https://raw.githubusercontent.com/hustlei/QssStylesheetEditor/master/img/screenshot/QssStylesheetEditor_v1.0.png" alt="v1.0" height=200/>


