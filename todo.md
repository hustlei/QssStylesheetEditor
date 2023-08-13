English | [简体中文](todo_zh-CN.md)

# ToDo

+ Qsst sample
+ Docs
    - Help
    - Qss tutorial


# ChangeLog

## v1.8
Main Changes: **update ui in-time preview feature，fixed editor bugs, fixed ISSUES**

+ **New Features**
    - in-time preview feature is more responsive, consuming less resources and time
    - update parameter reference features，fixed bugs
    - add comment features
+ **BugsFixed**
    - fixed ISSUE#14#33#34#41#43
    - merge #41#44 request
    - fixed editor BUGs

## v1.7
Main Changes: **add custom ui preview and qpalette and update features, fixed ISSUES**

+ **New Features**
    - add auto export qss features
    - make groupbox in preivew area checkable  ISSUES#25
	- optimize editor lags
	- add ui skin settings
	- add update check feature
	- add using qpalette feature to qsst
	- update chinese for i18n
	- preview only applied on preivewwidget
+ **BugsFixed**
    - fixed ISSUES#11#16#19#20#21#28#29#30#31
    - fixed var export error ISSUES#24
    - fixed wheel package error ISSUES#26


## v1.6
Main Changes: **split editor, config etc to single package, test for multi platform*

+ **New Features**
    - add setup.py for installing by `python setup.py install`
    - rewrite config for editor, and move codeeditor and config to single package and uplaod to pypi;
    - improve code quality by static analysis
+ **BugsFixed**
    - fixed chardet import error
    - fixed binary file detect error

## v1.5
Main Changes: **reference image in resource file in qsst**

+ **New Features**
    - Support reference image in resource file:url(:/img/close.png);
    - When there isn't UI language setted, autodetect the os language, if there isn't tranlation, set to english
    - Readme english version set to default
    - Add code analysis, test scripts and config file

## v1.4
Main Changes: **i18n, settings**

+ **New Features**
    - toml config file
    - recent open list
    - i18n (add english and chinese translation)
    - compile images to resource file
    - refactor installer scripts for win64(add i18n support for installer)
+ **BugsFixed**
    - Fix installer starting error on some OS 

## v1.35
Main Changes: **add installer for windows**

+ **New Features**
    - add Nsis scripts for installer

## v1.3
Main Changes: **portable exe for windows x64**

+ **New Features**
    - display lines count, coding etc. in statusbar
    - tool for display space and breakline
    - tool for auto wrapping
    - font zooming
    - screenSplash
    - drag drop open file for editor
    - syntax prompt for Qss keywords
    - portable win64 binary exe
    - reference image in qss by relative path, base dir set to dir that the qss is in
+ **BugsFixed**
    - Fix display error of Find dialog

## v1.2
Main Changes: **change editor to Qscintilla**

+ **New Features**
    - using QSintilla instead of TextEdit
    - autowrapping
    - auto indent
    - tab default using 4 spaces instead
    - auto detect coding of qss file
    - custom syntax hightlight and code folding
    - change var defination syntax to `$var=value;`
    - about dialog
    - rewrite default qss template
    - find and replace
+ **BugsFixed**
    - fix error of syntax highlight when there is chinese word
    - background of editor auto changed according the qss code

## v1.1
Main Changes: **redesign Ui**

+ **New Features**
    - drag drop to open document
    - optimize dynamic widgets in color pannel, to reduce memory usage

## v1.0

+ **New Features**
    - in-time preview, a little widgets supported
    - code hightlighting, but need to imporve
    - redo undo
    - variable custom
