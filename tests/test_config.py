# -*- coding: utf-8 -*-
"""test for qsst module.

Copyright (c) 2019 lileilei <hustlei@sina.cn>
"""

from pytest import fixture, raises
# from config import Config
from config.base import Section, Error


@fixture(scope="function")
def section():
    """Fixture: create a TomlConfigParser object
    """
    return Section()

def test_section_child(section):
    """Test child operation for Section"""
    section['sec1'] = Section()
    section['sec1']['sec11'] = Section()
    section['sec1']['sec12'] = Section()
    section['sec1']['sec11']['v111'] = 111
    section['sec1']['sec11']['v112'] = 112
    section['sec1']['sec12']['v121'] = 121
    section['sec1']['sec12']['v122'] = 122
    # test for hasChild
    assert section.hasChild("sec1")
    assert not section.hasChild("sec2")
    assert section.hasChild("sec1.sec11")
    assert section.hasChild("sec1.sec12")
    assert not section.hasChild("sec1.sec13")
    assert not section.hasChild("sec1.sec13.sec")
    assert section.hasChild("sec1.sec11.v111")
    # test for addChild
    add21 = section.addChild("sec2.sec21")
    assert section.hasChild("sec2.sec21")
    assert add21 == ""
    assert section.addChild(".") is None
    section.addChild("sec3")
    assert section.hasChild("sec3")
    section.addChild("sec3.sec31")
    assert section.hasChild("sec3.sec31")
    # test for rmChild
    section.rmChild("sec3.sec31")
    assert not section.hasChild("sec3.sec31")
    assert section.hasChild("sec3")
    rm1 = section.rmChild("sec3")
    assert not section.hasChild("sec3")
    assert rm1 == {}
    assert section.rmChild("sec3") is None
    # test for getChild
    assert section.getChild('sec1.sec12.v122') == 122
    assert 'v121' in section.getChild('sec1.sec12')
    assert section.getChild('sec1').hasChild('sec12')
    assert section.getChild('sec1').hasChild('sec12.v122')
    assert 'v121' in section.getChild('sec1.sec12')
    assert section.getChild('') is None
    assert section.getChild('sec4') == ""
    assert section.getChild('sec5', False) is None
    # test for setChild
    section.setChild("sec1.sec11.v111", 1112)
    assert section.getChild("sec1.sec11.v111") == 1112
    assert not section.setChild("sec1.sec11.v1113", 123, addifnochild=False)


def test_section_sec(section):
    """Test method for Section"""
    section['sec1'] = Section()
    section['sec1']['sec11'] = Section()
    section['sec1']['sec12'] = Section()
    section['sec1']['sec11']['v111'] = 111
    section['sec1']['sec11']['v112'] = 112
    section['sec1']['sec12']['v121'] = 121
    section['sec1']['sec12']['v122'] = 122
    # test for hasSec
    assert section.hasSec("sec1")
    assert not section.hasSec("sec2")
    assert section.hasSec("sec1.sec11")
    assert section.hasSec("sec1.sec12")
    assert not section.hasSec("sec1.sec13")
    assert not section.hasSec("sec1.sec13.sec")
    assert not section.hasSec("sec1.sec11.v111")
    # test for addSec
    add21 = section.addSec("sec2.sec21")
    assert isinstance(add21, Section)
    assert section.hasSec("sec2.sec21")
    assert section.addSec(".") is None
    # test for getSec
    assert section.getSec("sec2.sec21") == {}
    with raises(Error):
        section.getSec("sec2.sec11.v122", False)
    assert section.getSec("sec2.sec11.v122") == {}
    assert section.getSec(". ") is section
    # test for rmSec
    assert section.rmSec("sec2.sec21") == {}
    assert not section.hasSec("sec2.sec21")
    assert section.hasSec("sec2")
    # test for hasChild
    assert section.hasChild("sec1.sec11.v111")
    assert section.hasChild("sec1")
    assert not section.hasChild(".")
    assert not section.hasChild("...  ")
    assert not section.hasChild("sec22")
    # test for list oprations
    section.insertToChild("sec1.sec11.v111", 0, 1112)
    section.insertToChild("sec1.sec11.v111", 0, 1113)
    assert isinstance(section.getChild("sec1.sec11.v111"), list)
    assert 1112 in section.getChild("sec1.sec11.v111")
    assert not section.appendToChild("sec1", "sec1xx")

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
