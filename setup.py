# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

# with open("readme.md", "r", encoding='utf-8') as fh:
# long_desc = fh.read()

# import os
# def clearpyc(srcpath):
# files = os.listdir(srcpath)
# for fd in files:
# cur_path = os.path.join(srcpath, fd)
# if os.path.isdir(cur_path):
# if fd == "__pycache__":
# print("rm %s -rf" % cur_path)
# os.system("rm %s -rf" % cur_path)
# else:
# clearpyc(cur_path)
# clearpyc(os.path.join(os.path.dirname(__file__),'src'))

setup(
    name="QssStylesheetEditor",  # ProjectName
    version="1.8",
    python_requires='>=3.0.*, <4',  # python的依赖关系
    install_requires=["requests>=2.0", "preimport>=1.1.0", "tomlconfig>=1.2.1", "CodeEditor>=1.1.0"],

    # Module
    package_dir={'': 'src'},  # tell distutils packages are under src
    packages=find_packages(where='src', include=('*'), exclude=[
        '*.__pycache__',
    ]),  #
    py_modules=['app'],  # , 'bootstrapper'],  # single file

    # data
    package_data={
        'config': ['*.toml'],  # *.toml files found in config package
        'config.skin': ['*.qss'],
        'data': ['*.qss', '*.qsst'],
        'i18n': ['*.qm', '*.toml'],
        'res': ['*'],
        '': ['*.zip']
    },
    exclude_package_data={
        '': [
            '*.ts',
            '*.qrc',
            '__pycache__/*.*',
        ],
        'res': [
            'img',
        ],
        # 'data': ['__init__.py']  # not work
    },

    # excutable
    # scripts=['src/app.py','src/__main__.py'],# 指定脚本会被安装到Python3x/Scripts下
    entry_points={
        "console_scripts": [
            'qsseditor = app:main',  # create qsseditor.exe in Python3x/Scripts
            'qssteditor = app:main',  # __main__
        ],
        "gui_scripts": [
            'QssStylesheetEditor = app:main',
        ]
    },

    # metadata to display on PyPI
    author='lileilei',
    author_email='hustlei@sina.cn',
    description="A Qt Stylesheet(QSS) CodeEditor",
    keywords="QSS",
    # long_description=long_desc,
    # long_description_content_type="text/markdown",
    url="https://github.com/hustlei/QssStylesheetEditor",  # project home page, if any
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)

# <https://www.jianshu.com/p/e0e7420e3141>
# <https://www.cnblogs.com/yangwm/p/11243346.html>
# <https://www.cnblogs.com/ls-2018/p/10451393.html>

# python setup.py build  # 编译
# python setup.py sdist  # zip格式包
# python setup.py bdist_wininst # exe格式包
# python setup.py bdist_rpm # rpm格式包  bdist_wheel wheel包
# python setup.py bdist --help-formats # 获取所有支持的平台
# python setup.py --help-commands 显示相关可用命令
# python setup.py install #安装
