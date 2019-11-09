#!usr/bin/python
# -*- coding: utf-8 -*-
"""test for app module.

Copyright (c) 2019 lileilei <hustlei@sina.cn>
"""

from app import App


def test_mainwin(qtbot):
    app = App()
    app.run(pytest=True)
    qtbot.waitForWindowShown(app.windows["main"])
