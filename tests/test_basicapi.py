# -*- coding: utf-8 -*-
"""Test basic api of tomlsection

Copyright (c) 2019 lileilei. <hustlei@sina.cn>
"""

from pytest import raises
from tomlconfig import TomlSection, Error


def test_child_basicapi(section):
    """Test child operation for Section"""
    # test for hasChild
    assert section.hasChild("sec1")
    assert not section.hasChild("sec3")
    assert section.hasChild("sec1.sec11")
    assert section.hasChild("sec1.sec11.v111")
    assert not section.hasChild("sec1.sec13")
    assert not section.hasChild("sec1.sec13.sec")
    # test for addChild
    add21 = section.addChild("sec3.sec31")
    assert section.hasChild("sec3.sec31")
    assert add21 == ""
    assert section.addChild(".") is None
    section.addChild("sec3")
    assert section.hasChild("sec3")
    section.addChild("sec3.sec31", TomlSection())
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
    assert section.getChild('sec1.sec11.v111') == 111
    assert 'v111' in section.getChild('sec1.sec11')
    assert section.getChild('sec1').hasChild('sec11')
    assert section.getChild('sec1').hasChild('sec11.v111')
    assert section.getChild('') is None
    assert section.getChild('sec4') == ""
    assert section.getChild('sec5', False) is None
    # test for setChild
    section.setChild("sec1.sec11.v111", 1112)
    assert section.getChild("sec1.sec11.v111") == 1112
    assert not section.setChild("sec1.sec11.v1113", 123, addifnochild=False)


def test_sec_basicapi(section):
    """Test method for Section"""
    # test for hasSec
    assert section.hasSec("sec1")
    assert not section.hasSec("sec3")
    assert section.hasSec("sec1.sec11")
    assert not section.hasSec("sec1.sec13")
    assert not section.hasSec("sec1.sec13.sec")
    assert not section.hasSec("sec1.sec11.v111")
    # test for addSec
    add21 = section.addSec("sec2.sec21")
    assert isinstance(add21, TomlSection)
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
