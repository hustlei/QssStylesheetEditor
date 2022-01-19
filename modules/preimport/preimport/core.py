# -*- coding: utf-8 -*-
"""Implementation functions for preimport
"""

import sys
from collections.abc import Iterable
from importlib import import_module
from time import time


def preimport(*moduleNames):
    """Import python modules. And print the status.

    :param moduleNames: module name to be imported. Can be multi names or name list.
    :return: no return
    """

    for moduleName in moduleNames:
        if isinstance(moduleName, str):
            print(
                "  Preimporting {:9}   ...".format("'" + moduleName + "'"),
                end="",
                flush=True,
            )
            if moduleName in sys.modules:
                print("   [Note]:{} already imported.".format(moduleName))
            else:
                timeStart = time()
                try:
                    import_module(moduleName)
                except ModuleNotFoundError:
                    print("   [Failed]:ModuleNotFound.")
                except:
                    print("   [Error]:Unexpected error happened")
                else:
                    print("   successfully in {:.2}s.".format(time() - timeStart))
        elif isinstance(moduleName, Iterable):
            preimport(*moduleName)
        else:
            print("  [Error]: preimport error, moduleName must be str or Iterable.")
