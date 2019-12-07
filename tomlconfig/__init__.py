# -*- coding: utf-8 -*-
"""A easy-to-use toml config parser

| author: lileilei
| email <hustlei@sina.cn>
"""

__version__ = "1.2.0"

from .base import Error, NoSectionError, SectionTypeError, TomlSection
from .core import TomlConfig
