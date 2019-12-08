# -*- coding: utf-8 -*-
"""test for qsst module.

Copyright (c) 2019 lileilei <hustlei@sina.cn>
"""

from pytest import fixture
# from config import Config
from config import Config


@fixture(scope="function")
def config():
    """Fixture: create a TomlConfigParser object
    """
    return Config.current()


def test_configparser(config):
    """Test for TomlConfigParser
    """
    assert config.hasSec("general")
