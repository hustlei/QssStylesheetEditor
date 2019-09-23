QssStylesheetEditor是一个功能强大的Qt样式表(QSS)编辑器，免费开源。

# 功能简介

+ 编辑Qss，实时预览Qss样式效果(可以预览几乎所有的qtwidget控件效果)。
+ 支持代码高亮，代码折叠。
+ 支持Qss关键字、属性、伪元素等的自动提示，自动补全。
+ 支持在Qss中自定义变量，在Qss中引用。
+ 自定义变量会自动显示在颜色编辑面板，可以通过颜色对话框中拾取变量的颜色。
+ 支持相对路径引用图片，以及引用资源文件中的图片
+ 支持切换不同的系统theme，如xp主题,vista主题等(不同theme下qss效果会略有差异)
+ 自带已编写好的qsst模板样式文件
+ 能够在windows，linux，unix上运行

# screenshot

![GUI(v1.3版本) screeshot](res/img/screenshot/QssStylesheetEditor_v1.3.png "GUI(v1.3版本)")

# 安装使用

## windows 64bit
windows 64bit 操作系统可以下载exe，直接运行。

下载地址：

+ QssStylesheetEditor_1.4_win64_installer **[[Download]](https://pan.baidu.com/s/1_Uf1lPHj14fs9iMG2SVXuQ)**(secuirity code: gwf8)
+ QssStylesheetEditor_1.4_win64_portable  **[[Download]](https://pan.baidu.com/s/1kGLlpD52N5-wg9IFf0CHPA)**(secuirity code: ze32)


## 其他操作系统

其他操作系统暂时没有编译好的二进制软件包，需要在python环境下运行，并且依赖PyQt5和Qscintilla。具体安装使用步骤如下：

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

> qss中颜色等有很多相同的，使用变量后会大大减少工作量，方便修改。
> + 定义了变量的qss文件在QssStylesheetEditor中扩展名定义为qsst
> + 可以通过软件的导出功能，将qsst导出为qss文件
> > 当然也可以直接在QssStylesheetEditor软件中编辑qss样式

**QssStylesheetEditor自动识别添加变量,颜色拾取功能**

在QssStylesheetEditor中自定义一个变量后，在软件的颜色栏会自动显示变量名字和颜色，点击颜色可以用通过颜色拾取框选取变量颜色。

<img src="https://raw.githubusercontent.com/hustlei/QssStylesheetEditor/master/res/img/screenshot/ColorDlg_v1.3.png" height=180 />

在QssStylesheetEditor中引用一个未定义的变量后，软件会自动识别，并在颜色栏显示该变量名字。如果通过颜色拾取框为该变量选择了颜色，这软件会自动在文档中添加该变量定义。

# 图片引用

## 相对路径引用

~~~css
background-image: url("img/close.png");
/* background-image: url(img/close.png); */
~~~

软件会在打开的xxx.qss文件所在的文件夹下查找img/close.png文件。

## 资源文件引用

~~~css
background-image: url(":/img/close.png");
/* background-image: url(:/img/close.png); */
~~~

软件会在当前打开的xxx.qss样式文件所在目录中搜索资源文件xxx.py并自动加载。

# screenshot

## 自动补全

![AutoComplete screeshot](res/img/screenshot/AutoComplete.png "AutoComplete")


## old version

<div><span><b>QssStylesheetEditor GUI V1.2</b></span></div>
    <img src="https://raw.githubusercontent.com/hustlei/QssStylesheetEditor/master/res/img/screenshot/QssStylesheetEditor_v1.2.png" alt="v1.2" height=200/>
<div><span><b>QssStylesheetEditor GUI V1.1</b></span></div>
    <img src="https://raw.githubusercontent.com/hustlei/QssStylesheetEditor/master/res/img/screenshot/QssStylesheetEditor_v1.1.png" alt="v1.1" height=200/>
<div><span><b>QssStylesheetEditor GUI V1.0</b></span></div>
    <img src="https://raw.githubusercontent.com/hustlei/QssStylesheetEditor/master/res/img/screenshot/QssStylesheetEditor_v1.0.png" alt="v1.0" height=200/>


