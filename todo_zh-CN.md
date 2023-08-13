简体中文 | [English](todo.md)

# ToDo

+ 增加 Qsst 示例
+ 帮助文档
    - 帮助
    - Qss 教程


# ChangeLog

## v1.8
主要修改: **预览更新功能升级，修复编辑器，修复ISSUE中提到的bug**

+ **New Features**
    - 实时预览功能响应更快，消耗资源和时间更少
    - 更新参数引用功能，修复bug
    - 增加注释功能
+ **BugsFixed**
    - 修复ISSUE#14#33#34#41#43中提到的BUG，合并#41#44request
    - 修复编辑器BUG

## v1.7
主要修改: **增加自定义UI预览、qpalette、自动更新功能, 修复ISSUE中提到的bug**

+ **New Features**
    - 减少编辑中的卡顿
    - 增加自定义ui界面代码预览功能
    - 增加QPalette设置，并能在qss中引用QPalette的功能
    - 为UI提供皮肤设置功能，qss预览仅作用于预览控件
	- 增加保存自动导出qss选项和功能
    - 增加版本更新检查功能
	- 更新国际化中中文文本资源
+ **BugsFixed**
    - 修复ISSUE#11#16#19#20#21#24#26#28#29#30#31中提到的BUG
    - 修复配置文件BUG
    
## v1.6
主要修改: **重构config, 修复ISSUE中提到的bug**

+ **New Features**
    - 增加自动导出qss的功能，每次保存自动导出qss
+ **BugsFixed**
    - 修复ISSUE中提到的BUG

## v1.6
主要修改: **重构editor和config部分到单独的包中，各个操作系统测试**

+ **New Features**
    - 增加用 `python setup.py install` 命令安装的zip包
    - 重写编辑器的设置部分, 并把codeeditor和config部分分离到单独的包中，并上传到pypi
+ **BugsFixed**
    - 修复 chardet import 错误
    - 修复二进制文件失败错误

## v1.5
主要修改：**引用资源文件中的图片**

+ **New Features**
    - 支持应用资源文件中的图片：url(:/img/close.png);
    - 如果没有设置界面语言，则使用操作系统语言，如果找不到对应的翻译包，则界面设置为英语
    - Readme 默认设置为英语，增加中文版链接
    - 增加代码自动测试，代码质量检查脚本及配置文件 


## v1.4
主要修改：**国际化、配置功能**

+ **New Features**
    - toml 配置文件
    - 最近打开的文档目录
    - 国际化
    - 资源文件编译
    - 重构安装包脚本，增加安装包中英文界面
+ **BugsFixed**
    - 修复安装包部分 OS 无法打开等问题

## v1.35
主要修改：**制作 windows 版本安装包**

+ **New Features**
    - 增加安装包制作的 Nsis 源码

## v1.3
主要修改：**制作 windows x64 版本 exe 软件**

+ **New Features**
    - 状态栏显示文件行数、编码、当前鼠标位置、选择的行号
    - 增加是否显示空格符号，换行符
    - 增加字体大小调节功能，自动换行设置功能
    - 增加 ScreenSplash
    - 增加拖放打开文件功能
    - 语法提示增加 Qss 关键字
    - 打包 win64 binary exe portable
    - qss 内用相对路径图片，修改为相对 qss 文件位置
+ **BugsFixed**
    - 修复 Find 对话框 statusbar 显示问题

## v1.2

主要修改：**使用 Qscintilla 编辑器**

+ **New Features**
    - 使用 QSintilla 替换了 TextEdit
    - 编辑器增加自动换行功能
    - 编辑器增加了缩进功能
    - tab 自动转换为 4 个空格
    - 增加了自动识别文件编码功能
    - 自定义代码高亮和代码折叠
    - 修改变量语法为$var=value;
    - 增加了 about 菜单
    - 完善了默认 qss 模板
    - 增加了查找和替换功能
+ **BugsFixed**
    - 修复语法高亮对中文支持问题
    - 编辑器背景色自动更新

## v1.1
主要修改：**修改布局界面，Ui 重构**

+ **New Features**
    - 已添加拖放打开功能
    - 优化 pyqt5 动态增减控件部分，减少内存使用

## v1.0

+ **New Features**
    - 已添加拖放打开功能
    - 支持实时预览，实时预览控件还待完善
    - 支持代码高亮，但是高亮质量不高
    - 支持 redo undo
    - 支持自定义变量
