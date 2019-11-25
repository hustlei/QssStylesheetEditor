# -*- coding: utf-8 -*-
"""test for qsst module.

Copyright (c) 2019 lileilei <hustlei@sina.cn>
"""

from pytest import fixture
# from config import Config
from config.base import Section


@fixture(scope="function")
def section():
    """Fixture: create a TomlConfigParser object
    """
    return Section()


def test_section_base(section):
    """Test protect method of Section
    """
    # test for add section
    sec1 = Section._addChild(section, "sec1", None)
    assert 'sec1' in section
    assert sec1 is None
    # assert isinstance(sec1, Section)
    # sec1_1 = section._addSec("sec1")
    # assert sec1 is sec1_1
    # test for add sub section
    # sec11 = section._addChild(sec1, "sec11")
    # assert 'sec11' in sec1
    # assert isinstance(sec1, Section)
    # assert isinstance(sec1, dict)
    # sec11_1 = section._addChild(sec1, "sec11")
    # assert sec11 is sec11_1
    # assert sec11 == {}
    # assert sec11 == Section()
    # # test for get section
    # root = section._getSec() # get root
    # assert root is section
    # get1 = section._getSec("sec1")
    # assert isinstance(get1, Section)
    # get2 = section._getSec("sec2", addifnotfound=False)
    # assert get2 is None
    # get2 = section._getSec("sec2")
    # assert get2 == {}
    # assert get2 == Section()
    # # test for get subsection
    # get11 = section._getSubSec(sec1, "sec11")
    # assert get11 is not None
    # assert get11 == {}
    # get12 = section._getSubSec(sec1, "sec12", addifnotfound=False)
    # assert get12 is None
    # get12 = section._getSubSec(sec1, "sec12")
    # assert "sec12" in sec1
    # assert get12 == {}
    # assert isinstance(get12, Section)
    # # test for rmsec
    # assert section._rmSec('default') is None
    # assert section._rmSubSec(sec1, 'aaa') is None
    # rm1 = section._rmSubSec(sec1, "sec12")
    # assert "sec12" not in sec1
    # assert rm1 == {}
    # rm2 = section._rmSec('sec1')
    # assert 'sec1' not in section
    # assert 'sec11' in rm2

# def test_section(section):
#     """Test method for Section"""
#     section['sec1'] = Section()
#     section['sec1']['sec11'] = Section()
#     section['sec1']['sec12'] = Section()
#     section['sec1']['sec11']['v111'] = 111
#     section['sec1']['sec11']['v112'] = 112
#     section['sec1']['sec12']['v121'] = 121
#     section['sec1']['sec12']['v122'] = 122
#     # test for hasSec
#     assert section.hasSec("sec1")
#     assert not section.hasSec("sec2")
#     assert section.hasSec("sec1.sec11")
#     assert section.hasSec("sec1.sec12")
#     assert not section.hasSec("sec1.sec13")
#     assert not section.hasSec("sec1.sec13.sec")
#     assert not section.hasSec("sec1.sec11.v111")
#     # test for addSec
#     add21 = section.addSec("sec2.sec21")
#     assert isinstance(add21, Section)
#     assert section.hasSec("sec2.sec21")
#     assert section.addSec(".") is None
#     # test for getSec
#     assert section.getSec("sec2.sec21") == {}
#     assert section.getSec(". ")  is None
#     # test for rmSec
#     assert section.rmSec("sec2.sec21") == {}
#     assert not section.hasSec("sec2.sec21")
#     assert section.hasSec("sec2")
#     # test for hasChild
#     assert section.hasChild("sec1.sec11.v111")
#     assert section.hasChild("sec1")
#     assert not section.hasChild(".")
#     assert not section.hasChild("...  ")
#     assert not section.hasChild("sec22")

# def test_tomlparser(tomlparser):
#     """Test for TomlConfigParser
#     """
#     # test read
#     rst = section.read()
#     assert (not rst)
#     rst = section.read("config/config.toml")
#     assert rst
#     assert section["general"]
#     assert 'file' in section
#     assert 'editor' in section
#     assert 'default' not in section
#
#     root = tomlparser.getSec()
#     assert root == {}
#     tomlparser.add


# @fixture
# def conf():
#     obj = Config()
#     return obj
#
#
# def test_sec(conf):
#     conf.getSec("xx")
#     assert "xx" in conf.dict
#     conf.dict["xx"] = "aa"
#     assert conf.dict["xx"] == "aa"
#
#
# def test_rmsec(conf):
#     conf.getSec("xx")
#     assert "xx" in conf.dict
#     conf.rmSec("xx")
#     assert "xx" not in conf.dict
#
#
# def test_list(conf):
#     conf.listNodeAppend("node", "child1")
#     conf.listNodeAppend("node", "child2")
#     assert conf.dict["node"][0] == "child1"
#     assert conf.dict["node"][1] == "child2"
#     conf.listNodeInsert("node", "ccc")
#     assert conf.dict["node"][0] == "ccc"
