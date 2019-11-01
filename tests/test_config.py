#!usr/bin/python
# -*- coding: utf-8 -*-
"""test for qsst module.

Copyright (c) 2019 lileilei <hustlei@sina.cn>
"""

from pytest import fixture
from config import Config


@fixture
def conf():
    obj = Config()
    return obj


def test_sec(conf):
    conf.getSec("xx")
    assert "xx" in conf.dict
    conf.dict["xx"] = "aa"
    assert conf.dict["xx"] == "aa"


def test_rmsec(conf):
    conf.getSec("xx")
    assert "xx" in conf.dict
    conf.rmSec("xx")
    assert "xx" not in conf.dict


def test_list(conf):
    conf.listNodeAppend("node", "child1")
    conf.listNodeAppend("node", "child2")
    assert conf.dict["node"][0] == "child1"
    assert conf.dict["node"][1] == "child2"
    conf.listNodeInsert("node", "ccc")
    assert conf.dict["node"][0] == "ccc"
