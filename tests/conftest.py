# -*- coding: utf-8 -*-
"""shared fixtures for tests

Copyright (c) 2019 lileilei <hustlei@sina.cn>
"""

from pytest import fixture
from app import App

# dir or module
collect_ignore = ["setup.py", "chardet", "flow_layout.py"]
collect_ignore_glob = ["*_v0.py", "*.old.py", "*_bak.py"]


@fixture(scope="session")
def sharedwin():
    app = App()
    app.run(pytest=True)
    yield app.windows
    app.exit()


@fixture(scope="function")
def mainwin():
    app = App()
    app.run(pytest=True)
    # windows["main"].newFromTemplate()
    yield app.windows["main"]
    app.windows["main"].editor.setModified(False)
    app.exit()
