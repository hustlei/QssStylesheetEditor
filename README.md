English | [简体中文](https://github.com/hustlei/preimport/blob/master/README_zh-CN.md)

# preimport

[![Build Status](https://travis-ci.com/hustlei/preimport.svg?branch=master)](https://travis-ci.com/hustlei/preimport)
[![Coverage Status](https://coveralls.io/repos/github/hustlei/preimport/badge.svg?branch=master)](https://coveralls.io/github/hustlei/preimport?branch=master)
[![Platform:win|osx|linux](https://hustlei.github.io/assets/badge/platform.svg)](https://travis-ci.com/hustlei/preimport)
[![PyPI](https://img.shields.io/pypi/v/preimport)](https://pypi.org/project/preimport/)

<br>

preimport python modules to accelerate running speed and avoid "hang" when invoke module.

# Installation

~~~shell
pip install preimport
~~~

# Usage

~~~python
from preimport import preimport

preimport('numpy', 'PyQt5')
preimport(['sys', 'os'])
~~~

It will be like following when using preimport in cli.

~~~
>>> # examples
>>> preimport('numpy')
>>> Preimporting 'numpy'       ...   successfully in 0.202s.
>>>
>>> # if module imported
>>> preimport('os')
>>> Preimporting 'os'        ...   [Note]:os already imported.
>>>
>>> # if module not installed
>>> preimport('PyQt5')
>>> Preimporting 'PyQt5'   ...   [Failed]:ModuleNotFound.
>>>
>>> # error module name
>>> preimport(1)
>>> [Error]: preimport error, moduleName must be str or Iterable.
~~~