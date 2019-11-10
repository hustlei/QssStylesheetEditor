# -*- coding: utf-8 -*-
"""shared fixtures for tests

Copyright (c) 2019 lileilei <hustlei@sina.cn>
"""

from pytest import fixture
from app import App


@fixture(scope="session")
def windows():
    app = App()
    app.run(pytest=True)
    yield app.windows
    app.exit()
