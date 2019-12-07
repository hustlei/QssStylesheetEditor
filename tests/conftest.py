# -*- coding: utf-8 -*-
"""Shared fixtures for pytest

Copyright (c) 2019 lileilei. <hustlei@sina.cn>
"""

from pytest import fixture
from tomlconfig import TomlSection


@fixture(scope="function")
def section():
    """Fiture for pytest: return a tomlsection object"""
    tomldit = {'sec1': {'sec11': {'v111': 111, 'v112': 112}}, 'sec2': {'sec21': {'v211': 211, 'v212': 212}}}
    return TomlSection(tomldit)


@fixture(scope="function")
def configfile(tmpdir):
    """fixure for pytest: return tmp toml files for read and write"""
    configfile = tmpdir.join("config.toml").ensure()
    configfile.write("""
    [sec1.sec11]
    v111 = 111
    v112 = 112
    [sec2.sec21]
    v211 = 211
    v212 = 212
    """)
    return str(configfile)
