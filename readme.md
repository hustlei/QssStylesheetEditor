English | [简体中文](readme_zh-CN.md)

# QssStylesheetEditor

[![Build Status](https://api.travis-ci.com/hustlei/QssStylesheetEditor.svg?branch=master)](https://travis-ci.com/hustlei/QssStylesheetEditor)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/220d511b3ab146d0b03fef0245e00525)](https://www.codacy.com/manual/hustlei/QssStylesheetEditor?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=hustlei/QssStylesheetEditor&amp;utm_campaign=Badge_Grade)
[![Coverage Status](https://coveralls.io/repos/github/hustlei/QssStylesheetEditor/badge.svg?branch=master)](https://coveralls.io/github/hustlei/QssStylesheetEditor?branch=master)
[<img alt="Platform:win|osx|linux" src="https://raw.githubusercontent.com/hustlei/QssStylesheetEditor/master/docs/assets/badge/platform.svg?sanitize=true" onerror="this.src='https://hustlei.github.io/assets/badge/platform.svg';this.onerror=null" />](https://travis-ci.com/hustlei/QssStylesheetEditor)

<br>

QssStylesheetEditor is a powerful qt stylesheet(QSS) editor.
Real-time preview, automatically completion, and user can define custom variables.


# screenshot

![GUI(v1.5) screeshot](https://hustlei.github.io/software/QssStylesheetEditor/screenshot/en/QssStylesheetEditor_v1.5.png  "GUI(v1.5)")

# Features

+ Qss code highlight and code folding
+ Automatic completion
+ In-time preview
+ Almost all of the qtwidgets can be previewed
+ Customize variables and reference in Qss
+ Change variable color through color dialog box
+ Reference image by relative path
+ Reference image in resource files
+ Switch different system themes(xp, vista etc.)
+ Internationalization
  + Now Chinese and English translation is available

# Platform

+ Windows(maybe can't run on xp)
+ macOS
+ Linux
+ UNIX


# Usage

Follow the steps as below, or install the binary installation package:

1. install python3: following <http://python.org/>
2. install dependecies:
    - PyQt5: `pip instll PyQt5`
    - Qscintilla: `pip instll Qscintilla`
3. download and unzip package:
    + download [QssStylesheetEditor_v1.5.zip](https://github.com/hustlei/QssStylesheetEditor/releases)
    + unzip and change dir to QssStylesheetEditor_v1.5 `cd QssStylesheetEditor_v1.5`
4. Run QssStylesheetEditor:
    + double click qsseditor.pyw
    + or run `python qsseditor.pyw`

> Alternatively, use the egg package is ok too
> 
> 1. download [QssStylesheetEditor_v1.5.egg.pkg.zip](https://pan.baidu.com/s/1ZFvbbropak1FbFhllYJ1Sw) (secuirity code: w9hx) and upzip
> 2. run `python3 setup.py install` install QssStylesheetEditor to python3
> 3. run `qsseditor` or `QssStylesheetEditor`

or

If you are windows 64bit user, binary package and installer is available now.

+ QssStylesheetEditor_1.5_win64_installer **[[Download]](https://pan.baidu.com/s/1Wd_j_KMBcI9JBY4qDgswMg)**(secuirity code: auhq)
+ QssStylesheetEditor_1.5_win64_portable  **[[Download]](https://pan.baidu.com/s/1cIValPom3TWRGdpwDlKtdw)**(secuirity code: brtj)

## Using custom variable 

In QssStylesheetEditor, users can define and use custome variables in QSS. 

Using following statement to define new variable:

~~~js
/*example of custom variable definition*/
$background = #fff;  /* define var with name "background" */
$text = red; /* define var with name "text" */
~~~

A variable definition end with a ";".

Reference defined variable as following:

~~~css
/* example of custom variable reference */
QWidget
{
    color: $text; /* reference variable text*/
    background-color: $background; /* reference variable background*/
}
~~~


Users can export the code to qss file without vars by the "File>Export" menu.


**Variable Color pick dialog**

When a variable is defined in QssStylesheetEditor, the variable will be automatically displayed in the color pannel. You can click the color button to select the variable color through the color pick-up box.

<img src="https://raw.githubusercontent.com/hustlei/QssStylesheetEditor/master/docs/assets/screenshot/ColorDlg_v1.3.png" style="max-height:480px;max-width:960px"/>

> If an undefined variable is referenced, it will be automatically recognized and displayed in the color panel too. 

## Image reference path

When images are use in the qss code, if the url is relative,  QssStylesheetEditor will find the image file in the folder where the qss code file is.

~~~css
background-image: url("img/close.png");
/* the img folder must be in the same directory of the qss code file*/
~~~


## image in resource file

If your image files is converted to resource file by pyrcc5(pyrcc5 xxx.qrc -o xxxresource.py).

You can reference images in the resource file as following:

~~~css
background-image: url(":/img/close.png");
~~~

QssStylesheetEditor will search the resource file filename.py(filename must be same of qss file) in the directory of the currently opened qss stylesheet code file and loads it automatically.

# screenshot

<div><span><b>AutoComplete</b></span></div>
    <img src="https://raw.githubusercontent.com/hustlei/QssStylesheetEditor/master/docs/assets/screenshot/AutoComplete.png" alt="AutoComplete" style="max-height:480px;max-width:960px"/>

<div><span><b>QssStylesheetEditor on macOS</b></span></div>
    <img src="https://hustlei.github.io/software/QssStylesheetEditor/screenshot/en/QssStylesheetEditor_mac_v1.5.png" alt="Gui on macOS" style="max-height:480px;max-width:960px"/>

<div><span><b>QssStylesheetEditor GUI V1.2</b></span></div>
    <img src="https://raw.githubusercontent.com/hustlei/QssStylesheetEditor/master/docs/assets/screenshot/QssStylesheetEditor_v1.2.png" alt="v1.2" style="max-height:480px;max-width:960px"/>
<div><span><b>QssStylesheetEditor GUI V1.0</b></span></div>
    <img src="https://raw.githubusercontent.com/hustlei/QssStylesheetEditor/master/docs/assets/screenshot/QssStylesheetEditor_v1.0.png" alt="v1.0" style="max-height:480px;max-width:960px"/>


# License
Like PyQt5, this software is available under two licenses: the GPL v3, and Commercial License.

If you are willing to follow the terms of the GPL, this software is available to you under Open Source licenses which allows you to develop, modify and distribute your software freely.

Alternatively, if you, your company or your organisation derive commercial benefit from the software and do not wish to distribute your complete source code you are required to use commercial licenses and purchase commercial version PyQt5.
