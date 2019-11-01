python 代码静态分析

# pep8代码格式

PEP8 是一种 Python 代码规范指南，可以参阅官网：https://www.python.org/dev/peps/pep-0008/，其目的
是为了保持代码的一致性、可读性。

检查自己代码是否符合 PEP8 规范，一个简单的工具就是：pycodestyle （以前的pep8，最新版改名为
 pycodestyle。
 
## 使用方法
 
 ```
 > pip install pycodestyle
 > pycodestyle [file name or directory name]
 ```

## 常用参数
 
+ 参数 --statistics -qq ：统计结果，汇总每种错误出现的次数。

`pycodestyle file.py --statistics -qq`


+ 参数 --show-source：更详细的输出

`pycodestyle file.py --statistics -qq`

+ 参数 --ignore：忽略指定输出

`pycodestyle file.py --ignore=E225,E501,E231`

## 错误代码含义

+ E...：错误
+ W...：警告

+ 100 型：缩进问题
+ 200 型：空格问题
+ 300 型：空行问题
+ 400 型：导入问题
+ 500 型：行长度问题
+ 600 型：已弃用
+ 700 型：声明问题
+ 900 型：语法错误


## python代码格式化

Python的大多数当前格式化程序（例如，autopep8 和 pep8ify），用于从代码中删除lint错误。
这有一些明显的局限性。例如，符合PEP 8指南的代码可能无法重新格式化。但这并不意味着代码看起来很好。
YAPF采用不同的方法。它基于由 Daniel Jasper 开发的 'clang-format'。
从本质上讲，算法会获取代码并将其重新格式化为符合样式指南的最佳格式，即使原始代码没有违反样式指南。
这个想法也类似于Go编程语言的'gofmt'工具。

如果项目的整个代码库只是通过YAPF进行修改，只要进行修改，样式在整个项目中保持一致。
最终目标是YAPF生成的代码与程序员在遵循样式指南时编写的代码一样好。它消除了维护代码的一些苦差事。


## 安装使用

~~~
pip install yapf
yapf [files [files ...]]
~~~

## 参数

[-h] [-v] [-d | -i] [-r] [-e PATTERN] [--style STYLE] [-p] [-vv] [files [files ...]]

参数说明

+ -h, --help	显示此帮助消息并退出
+ -v, --version	显示版本号并退出
+ -d, --diff	比较差异
+ -i, --in-place	对文件进行更改
+ -r, --recursive	以递归方式运行目录
+ -e, --exlude  排除的文件
+ --style, 样式名称，比如 pep8 或者 google，默认为pep8。或者样式配置文件，默认加载file所在目录
           或者file的一个父目录中的.style.yapf或者 setup.cfg 文件。
+ -p, 并行执行
+ -vv, --verbose 显示详细信息

~~~
yapf <python file>  #直接跟文件名（并不修改文件）
yapf -d <python file> #格式化前后对比
yapf -i <python file> #直接修改源文件
yapf -r <dir> # 递归格式化文件夹
yapf --style-help > .style.yapf #导出配置文件
~~~

> `autopep8 -aair src` 其实是和 `yapf -ri src` 很相似的
> 
> `pip install black` `black` 也可以，但是black可配置的选项不多


# Pyflakes

一个用于检查 Python 源文件错误的简单程序。Pyflakes 比 Pylint 和 Pychecker 也更快。 

Pyflakes 分析程序并且检查各种错误。它通过解析源文件实现，无需导入它，因此在模块中使用是安全的，
没有任何的副作用。

+ 不会检查代码风格
+ 由于它是单独检查各个文件，因此它也相当的快，当然检测范围也有一定的局限

## 安装使用

```
pip install pyflakes
pyflakes [ file name or directory name]
```



# Pylint

PyLint 是 Python 源代码分析器，可以分析 Python 代码中的错误，
查找不符合代码风格标准和有潜在问题的代码，是一个可以用于验证多个文件的模块和包的工具。

缺省情况下，PyLint 启用许多规则。它具有高度可配置性，从代码内部处理程序控制它。另外，编写插件添加到自己的检查中是可能的。

# 安装使用

```
pip install pylint
pylint [options] module_or_package
```


如果运行两次 Pylint，它会同时显示出当前和上次的运行结果，从而可以看出代码质量是否得到了改进。

错误代码含义
C：惯例，违反了编码风格标准
R：重构，代码非常糟糕
W：警告，某些 Python 特定的问题
E：错误，很可能是代码中的错误
F：致命错误，阻止 Pylint 进一步运行的错误
