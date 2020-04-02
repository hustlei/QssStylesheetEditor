简体中文 | [English](README.md)

# preimport

[![Build Status](https://travis-ci.com/hustlei/preimport.svg?branch=master)](https://travis-ci.com/hustlei/preimport)
[![Coverage Status](https://coveralls.io/repos/github/hustlei/preimport/badge.svg?branch=master)](https://coveralls.io/github/hustlei/preimport?branch=master)
[![Platform:win|osx|linux](https://hustlei.github.io/assets/badge/platform.svg)](https://travis-ci.com/hustlei/preimport)
[![PyPI](https://img.shields.io/pypi/v/preimport)](https://pypi.org/project/preimport/)

<br>

预加载(preimport) python 模块，加快 python 程序运行时的速度，消除程序运行的时候，因为加载模块导致的“停顿”。

# 安装

~~~shell
pip install preimport
~~~

# 使用

~~~python
from preimport import preimport

preimport('numpy', 'PyQt5')
preimport(['sys', 'os'])
~~~


使用 preimport 会在命令行中输出预加载情况信息，显示是否加载成功，是否出错等。

~~~
>>> # examples
>>> preimport('numpy')
>>> Preimporting 'numpy'       ...   successfully in 0.202s.
>>>
>>> # 如果模块已经导入了的情况
>>> preimport('os')
>>> Preimporting 'os'        ...   [Note]:os already imported.
>>>
>>> # 如果系统未安装模块
>>> preimport('PyQt5')
>>> Preimporting 'PyQt5'   ...   [Failed]:ModuleNotFound.
>>>
>>> # 模块名称错误
>>> preimport(1)
>>> [Error]: preimport error, moduleName must be str or Iterable.
~~~