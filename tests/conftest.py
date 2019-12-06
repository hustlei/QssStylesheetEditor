# -*- coding: utf-8 -*-
"""shared fixtures for test

copyright (c) 2019, lileilei
"""

from pytest import fixture
from tomlconfig import TomlSection


@fixture(scope="function")
def section():
    """Fiture for pytest: return a tomlsection object"""
    tomldit = {'sec1': {'sec11': {'v111': 111, 'v112': 112}},
               'sec2': {'sec21': {'v211': 211, 'v212': 212}}
               }
    return TomlSection(tomldit)
