English | [简体中文](readme.md)

# QssStylesheetEditor

[![Build Status](https://api.travis-ci.com/hustlei/QssStylesheetEditor.svg?branch=master)](https://travis-ci.com/hustlei/QssStylesheetEditor)
[![Platform](https://img.shields.io/badge/platform-windows%20%7C%20macos%20%7C%20linux-green)](https://travis-ci.com/hustlei/QssStylesheetEditor)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/220d511b3ab146d0b03fef0245e00525)](https://www.codacy.com/manual/hustlei/QssStylesheetEditor?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=hustlei/QssStylesheetEditor&amp;utm_campaign=Badge_Grade)
[![Licence](https://img.shields.io/badge/license-LGPL--3.0-blue)](https://opensource.org/licenses/LGPL-3.0)

<br>

QssStylesheetEditor is a powerful qt stylesheet(QSS) editor, it's opensource and free.

# introduction

+ Qss editor, preview Qss(qt stylesheet) in-time(almost all the qtwidgets can be previewed in the soft)
+ support code highlighting and code folding
+ automatic prompt and completion the QSS keywords, attributes, pseudo elements, etc
+ support to customize variables and reference them in QSS
+ custom variable will be automatically displayed in the color panel, and your can change the color through the color dialog box
+ reference image by relative path, image in resource files can be referenced too
+ Support switching different system themes, such as xp theme, vista theme, etc.
+ Support windows, Linux, UNIX and macos
+ Support Internationalization(chinese and english language for ui is available)

# screenshot

![GUI(v1.3版本) screeshot](res/img/screenshot/QssStylesheetEditor_v1.3.png "GUI(v1.3版本)")

# download and install

## windows 64bit
installer for windows 64bit is available.

Download:

+ QssStylesheetEditor_1.4_win64_installer **[[Download]](https://pan.baidu.com/s/1_Uf1lPHj14fs9iMG2SVXuQ)**(secuirity code: gwf8)
+ QssStylesheetEditor_1.4_win64_portable  **[[Download]](https://pan.baidu.com/s/1kGLlpD52N5-wg9IFf0CHPA)**(secuirity code: ze32)

## other os

there is no bin installer for other os. you can run QssStylesheetEditor following these steps:

+ install python3: following <http://python.org/>
+ install PyQt5: `pip instll PyQt5`
+ install Qscintilla: `pip instll Qscintilla`
+ Download and unzip QssStylesheetEditor, double click app.py or `python app.py`

# variable

In QssStylesheetEditor, users can define and use custome variables in QSS. Folowing this steps to define variable:

~~~
$background = #fff;
$border     = red;
~~~

Variable name following $ to reference variable, such as "$variable name". sample as follows:

~~~
QWidget
{
    color: $text;
    background-color: $background;
}
~~~

> + qss that used custom variable in QssStylesheetEditor will be saved as qsst file
> + user can export qsst to qss file in QssStylesheetEditor
>> directly edit qss in QssStylesheetEditor is ok too

**QssStylesheetEditor Automatic recognition add variable**

When you customizing a variable in QssStylesheetEditor, the variable name and color will be automatically displayed in the color p of the software. Click the color to select the variable color through the color pick-up box.

<img src="https://raw.githubusercontent.com/hustlei/QssStylesheetEditor/master/res/img/screenshot/ColorDlg_v1.3.png" height=180 />

If an undefined variable is referenced in Qssstylesheeteditor, the software will automatically recognize it and display the variable name in the color panel. If a color is selected for the variable through the color pick box, the software automatically adds the variable definition to the document.

# image reference

## relative path

~~~css
background-image: url("img/close.png");
/* background-image: url(img/close.png); */
~~~

The software will find the img/close.png file in the folder where the xxx.qss file is opened.

## image in resource file

~~~css
background-image: url(":/img/close.png");
/* background-image: url(:/img/close.png); */
~~~

The software searches for the resource file xxx.py in the directory of the currently opened xxx.qss style file and loads it automatically.

# screenshot

## AutoComplete

![AutoComplete screeshot](res/img/screenshot/AutoComplete.png "AutoComplete")


## old version

<div><span><b>QssStylesheetEditor GUI V1.2</b></span></div>
    <img src="https://raw.githubusercontent.com/hustlei/QssStylesheetEditor/master/res/img/screenshot/QssStylesheetEditor_v1.2.png" alt="v1.2" height=200/>
<div><span><b>QssStylesheetEditor GUI V1.1</b></span></div>
    <img src="https://raw.githubusercontent.com/hustlei/QssStylesheetEditor/master/res/img/screenshot/QssStylesheetEditor_v1.1.png" alt="v1.1" height=200/>
<div><span><b>QssStylesheetEditor GUI V1.0</b></span></div>
    <img src="https://raw.githubusercontent.com/hustlei/QssStylesheetEditor/master/res/img/screenshot/QssStylesheetEditor_v1.0.png" alt="v1.0" height=200/>


