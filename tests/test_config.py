# -*- coding: utf-8 -*-
"""test for TomlConfig class"""


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
