# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name="preimport",
    setup_requires=['setuptools_scm'],
    use_scm_version=True,  # version="1.0",
    python_requires='>=2.7.*',
    # install_requires=[''],
    package_dir={'': 'src'},  # tell distutils packages are under src
    packages=find_packages(where='src', include=('*'), exclude=[
        '*.bak',
    ]),
    # py_modules=['__main__'],  # single file

    # data
    package_data={'': ['README.md', 'LICENSE']},

    # metadata to display on PyPI
    author='lileilei',
    author_email='hustlei@sina.cn',
    description="Preimport python modules to accelerate running speed.",
    keywords="preimport",
    url="https://github.com/hustlei/preimport",
    project_urls={"Source Code": "https://github.com/hustlei/preimport"},
    classifiers=[
        "License :: OSI Approved :: GNU LESSER GENERAL PUBLIC LICENSE v2.1 (LGPLv2.1)",
        "Programming Language :: Python",
        "Operating System :: OS Independent",
    ],
)

# python setup.py build  # 编译
# python setup.py sdist  # zip格式包
# python setup.py --help-commands 显示相关可用命令
# python setup.py install #安装
