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
    print("\n@fixture: shared session Application load...")
    app = App()
    app.run(pytest=True)
    yield app
    app.quit()
    del app
    print("\n@fixture: shared session Application quited.")


@fixture(scope="function")
def sharedwin(sharedapp):
    print("@fixture: shared mainwin load...")
    app = sharedapp
    app.windows["main"].newFromTemplate()
    app.windows["main"].show()
    yield app.windows
    app.windows["main"].editor.setModified(False)
    app.windows["main"].close()
    print("@fixture: shared mainwin closed.")


# @fixture(scope="function")
# def sharedwin():
#     print("@fixture: shared mainwin load...")
#     app = App()
#     app.run(pytest=True)
#     app.windows["main"].newFromTemplate()
#     app.windows["main"].show()
#     yield app.windows
#     app.windows["main"].editor.setModified(False)
#     app.windows["main"].close()
#     app.quit()
#     del app.windows
#     del app
#     print("@fixture: shared mainwin closed.")
