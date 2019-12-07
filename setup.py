# -*- coding: utf-8 -*-
"""setup for TomlConfig

| author: lileilei  email: <hustlei@sina.cn>  @2019, wuhan
"""
from setuptools import setup

with open("README.md") as f:
    long_desc=f.read()

ver="1.1.0"

setup(
    name="TomlConfig",
    author="lileilei",
    author_email="hustlei@sina.cn",
    keywords="toml config parser",
    desciption="Toml config parser made (stupidly) simple",
    long_description=long_desc,
    long_description_content_type="text/markdown",
    url="https://github.com/hustlei/TomlConfig",
    project_urls={"Source Code": "https://github.com/hustlei/TomlConfig"},
    classifiers=[
        "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
        "Programming Language :: Python :: 3", "Operating System :: OS Independent"
    ],

    version=ver,
    packages=["tomlconfig"],
    install_requires=['toml'],
)
