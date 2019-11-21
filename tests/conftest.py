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
def sharedapp():
    app = App()
    app.run(pytest=True)
    yield app
    app.quit()


@fixture(scope="function")
def sharedwin(sharedapp):
    print("@fixture: shared mainwin load...")
    app = sharedapp
    app.windows["main"].newFromTemplate()
    app.windows["main"].show()
    yield app.windows
    app.windows["main"].editor.setModified(False)
    app.windows["main"].close()
    print("@fixture: shared mainwin end.")
