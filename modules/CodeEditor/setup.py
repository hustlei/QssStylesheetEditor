# -*- coding: utf-8 -*-
"""setup for CodeEditor

| author: lileilei  email: <hustlei@sina.cn>  @2019, wuhan
"""
from setuptools import setup

with open("README.md", encoding="utf-8") as f:
    long_desc=f.read()

ver="1.1.0"

setup(
    name="CodeEditor",
    author="lileilei",
    author_email="hustlei@sina.cn",
    keywords="editor highlight",
    desciption="Syntax highlighting code editor.",
    long_description=long_desc,
    long_description_content_type="text/markdown",
    url="https://github.com/hustlei/CodeEditor",
    project_urls={"Source Code": "https://github.com/hustlei/CodeEditor"},
    classifiers=[
        "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
        "Programming Language :: Python :: 3", "Operating System :: OS Independent"
    ],

    version=ver,
    packages=["CodeEditor", "CodeEditor.lexers"],
    install_requires=['chardet', 'Qscintilla'],
)
