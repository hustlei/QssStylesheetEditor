# -*- coding: utf-8 -*-
"""setup for TomlConfig

| author: lileilei  email: <hustlei@sina.cn>  @2019, wuhan
"""
from setuptools import setup

with open("README.md", encoding="utf-8") as f:
    long_desc=f.read()

ver="1.2.1"

setup(
    name="tomlconfig",
    author="lileilei",
    author_email="hustlei@sina.cn",
    keywords="toml config parser",
    desciption="Toml config parser made (stupidly) simple",
    long_description=long_desc,
    long_description_content_type="text/markdown",
    url="https://github.com/hustlei/tomlconfig",
    project_urls={"Source Code": "https://github.com/hustlei/tomlconfig"},
    classifiers=[
        "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
        "Programming Language :: Python :: 3", "Operating System :: OS Independent"
    ],

    version=ver,
    packages=["tomlconfig"],
    install_requires=['toml'],
)
