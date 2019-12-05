# -*- coding: utf-8 -*-
"""test for qsst module.

Copyright (c) 2019 lileilei <hustlei@sina.cn>
"""

import sys
sys.path.append(".")

from pytest import fixture, raises
# from config import Config
from tomlconfig import TomlSection, Error


@fixture(scope="function")
def section():
    """Fixture: create a TomlConfigParser object
    """
    return TomlSection()


def test_section(section):
    """Test child operation for Section"""
    section['sec1'] = TomlSection()
    section['sec2'] = TomlSection()
    section['sec1']['sec11'] = TomlSection()
    section['sec1']['sec12'] = TomlSection()
    section['sec1']['sec11']['v111'] = 111
    section['sec1']['sec11']['v112'] = 112
    section['sec1']['sec12']['v121'] = 121
    section['sec1']['sec12']['v122'] = 122
    # test for hasChild
    # assert section.hasChild("sec1")
    # assert not section.hasChild("sec2")
    # assert section.hasChild("sec1.sec11")
    # assert section.hasChild("sec1.sec12")
    # assert not section.hasChild("sec1.sec13")
    # assert not section.hasChild("sec1.sec13.sec")
    # assert section.hasChild("sec1.sec11.v111")
    # test for addChild
    assert "sec1" in section
    assert "sec3" not in section
    assert 'sec11' in section["sec1"]
    assert section["sec2"] == {}
    del section["sec2"]
    assert 'sec2' not in section
    # add21 = section.addChild("sec2.sec21")
    # assert section.hasChild("sec2.sec21")
    # assert add21 == ""
    # assert section.addChild(".") is None
    # section.addChild("sec3")
    # assert section.hasChild("sec3")
    # section.addChild("sec3.sec31")
    # assert section.hasChild("sec3.sec31")
    # # test for rmChild
    # section.rmChild("sec3.sec31")
    # assert not section.hasChild("sec3.sec31")
    # assert section.hasChild("sec3")
    # rm1 = section.rmChild("sec3")
    # assert not section.hasChild("sec3")
    # assert rm1 == {}
    # assert section.rmChild("sec3") is None
    # # test for getChild
    # assert section.getChild('sec1.sec12.v122') == 122
    # assert 'v121' in section.getChild('sec1.sec12')
    # assert section.getChild('sec1').hasChild('sec12')
    # assert section.getChild('sec1').hasChild('sec12.v122')
    # assert 'v121' in section.getChild('sec1.sec12')
    # assert section.getChild('') is None
    # assert section.getChild('sec4') == ""
    # assert section.getChild('sec5', False) is None
    # # test for setChild
    # section.setChild("sec1.sec11.v111", 1112)
    # assert section.getChild("sec1.sec11.v111") == 1112
    # assert not section.setChild("sec1.sec11.v1113", 123, addifnochild=False)
