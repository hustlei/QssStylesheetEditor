# -*- coding: utf-8 -*-
"""Test for TomlConfig class

Copyright (c) 2019 lileilei. <hustlei@sina.cn>
"""

from tomlconfig import TomlConfig


def test_tomlconfig(configfile):
    """Test for TomlConfig class
    """
    # readfile
    config = TomlConfig()
    config.read(configfile)
    assert "sec1" in config

    # readstring
    tomlstr = "[sec]\n"
    config.readString(tomlstr)
    assert "sec" in config
    assert "sec1" not in config

    # update dict to tomlconfig
    tomldict = {'sec3': {'v31': 31}}
    config.update(tomldict)
    assert "sec" in config
    assert config["sec3.v31"] == 31

    # test for clear
    config.clear()
    config["v2"] = 2
    assert config == {"v2": 2}

    # test for save
    config.save()
    config.read(configfile)
    assert "v2" in config
    assert "sec1" not in config

    # test for version
    import tomlconfig
    ver = tomlconfig.__version__
    assert int(ver[0]) >= 1
