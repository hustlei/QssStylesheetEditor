自动收集QssStylesheetEditor在**windows平台上依赖**的所有文件

# 准备工作

dist文件夹中准备好以下文件：

+ libpython文件夹：python3.7的主要文件（python3.dll,python37.dll等）
+ Lib文件夹：PyQt5和requests包
+ DLLs文件夹：Windows共享库（msvcp140.dll,cvruntime140.dll,apims-win-cr-\*.dll等）
+ scripts文件夹：main.py
+ 启动文件：AppStart.exe、AppStart.vbs等

# build

制作windows平台安装包需要的文件的脚本。

1. pipenv shell（如果使用了pipenv虚拟环境，先进入虚拟环境）
2. cd installer（进入installer文件夹）
3. compile_pyscripts.cmd（运行build脚本）

> build文件夹是个中间文件夹，compile_pyscripts运行过程中放临时文件的。
>
> 最终编译的python脚本（pyc）及dll等文件会在“dist\build”文件夹中。


> 其他平台可以忽略本脚本，当然编译为pyc的python码也可以在其他平台上运行。