# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open("readme.md", "r", encoding='utf-8') as fh:
    long_desc = fh.read()

setup(
    name="QssStylesheetEditor", #ProjectName
    version="1.5",
    python_requires='>=3.0.*, <4', # python的依赖关系
    install_requires=[
        'PyQt5', 'Qscintilla'
    ],
    
    # Module
    package_dir = {'':'src'},  # # tell distutils packages are under src
    packages=find_packages(where='src', include=('*'), exclude=['*.bak',]), #
    py_modules=['app','bootstrapper'], #single file
    
    # data
    package_data={
        'config': ['*.toml'], # *.toml files found in config package
        'data': ['*.qss', '*.qsst'],
        'i18n': ['*.qm', '*.toml'],
        'res':['*'],
        '':['*.zip']
    },    
    exclude_package_data={'': ['*.ts','*.qrc',], # 'font' is not in package
                          'res':['img',]},
    
    # excutable
    # scripts=[],
    entry_points={
        "distutils.commands": [
            "QssStylesheetEditor = app",
        ],
    },
    
    
    # metadata to display on PyPI
    author='lileilei',
    author_email='hustlei@sina.cn',
    description="A Qt Stylesheet(QSS) editor",
    keywords="QSS",
    long_description=long_desc,
    long_description_content_type="text/markdown",
    url="https://github.com/hustlei/QssStylesheetEditor"   # project home page, if any
)


# <https://www.jianshu.com/p/e0e7420e3141>
# <https://www.cnblogs.com/yangwm/p/11243346.html>
# <https://www.cnblogs.com/ls-2018/p/10451393.html>
# install command
# 源码发布，使用python setup.py install安装
# python setup.py sdist  # 创建一个压缩包
# 创建二进制程序
# python setup.py bdist_wininst  # windows exe 应用程序,依赖本地安装的python，与py2exe不同
# python setup.py bdist_rpm # linux rpm
# 获取所有支持的平台
# python setup.py bdist --help-formats