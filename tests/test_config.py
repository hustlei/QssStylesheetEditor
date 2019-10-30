# -*- coding: utf-8 -*-
"""
test for qsst module.

Copyright (c) 2019 lileilei <hustlei@sina.cn>
"""

import os
import sys
from pytest import fixture
from config import Config

sys.path.append(os.path.abspath('..'))


@fixture
def conf():
    obj = Config()
    filesec = obj._getSec("file")
    obj.listNodeAppend("recent", "eeee", filesec)
    fontsec = obj._getSubSec(obj._getSec("editor"), "font")
    fontsec["size"] = 12
    obj.rmSec("editor0")
    return obj


def test_sec(conf):
    conf.getSec("xx")
    assert "xx" in conf.dict
    conf.dict["xx"] = "aa"
    assert "aa" == conf.dict["xx"]
    
def test_rmsec(conf):
    conf.getSec("xx")
    assert "xx" in conf.dict
    conf.rmSec("xx")
    assert "xx" not in conf.dict
    
def test_list(conf):
    conf.listNodeAppend("node","child1")
    conf.listNodeAppend("node","child2")
    assert "child1" == conf.dict["node"][0]
    assert "child2" == conf.dict["node"][1]
    conf.listNodeInsert("node","ccc")
    assert "ccc" == conf.dict["node"][0]
