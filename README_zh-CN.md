简体中文 | [English](readme.md)

# preimport

[![Build Status](https://travis-ci.com/hustlei/preimport.svg?branch=master)](https://travis-ci.com/hustlei/preimport)
[![Coverage Status](https://coveralls.io/repos/github/hustlei/preimport/badge.svg?branch=master)](https://coveralls.io/github/hustlei/preimport?branch=master)
[![Platform:win|osx|linux](https://hustlei.github.io/assets/badge/platform.svg)](https://travis-ci.com/hustlei/preimport)

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