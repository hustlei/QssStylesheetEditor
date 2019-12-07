# -*- coding: utf-8 -*-
"""test for TomlSection.

Copyright (c) 2019 lileilei. <hustlei@sina.cn>
"""

from tomlconfig import TomlSection


def test_section(section):
    """Test child operation for Section"""
    # test for in operation
    assert "sec1" in section
    assert "sec3" not in section
    assert "sec1.sec11.v111" in section
    assert 'sec11' in section["sec1"]

    # test for get
    assert section["sec1.sec11.v111"] == 111
    assert isinstance(section["sec1.sec11"], TomlSection)

    # test for add
    section["sec3.sec31.v311"] = 311
    assert section["sec3.sec31.v311"] == 311
    section["sec3.sec32"] = {}
    assert isinstance(section["sec3.sec32"], TomlSection)

    # test for del
    del section["sec3.sec32"]
    assert 'sec3.sec32' not in section

    # test for hassection
    assert section.hasSec("sec1.sec11")
    assert not section.hasSec("sec1.sec11.v111")

    # test for list
    section.insertToChild("sec1.sec11.v111", 0, 1110)
    assert section['sec1.sec11.v111'] == [1110, 111]
    section.appendToChild("sec1.sec11.v111", 1112)
    assert section['sec1.sec11.v111'] == [1110, 111, 1112]
