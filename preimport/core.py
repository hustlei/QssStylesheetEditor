# -*- coding: utf-8 -*-
"""

:author: lileilei
:email: hustlei@sina.cn
"""

import sys
from collections.abc import Iterable
from importlib import import_module
from time import time


def preimport(*moduleNames):
    """
    """
    for moduleName in moduleNames:
        if isinstance(moduleName, str):
            if moduleName in sys.modules:
                print("  [Note]: {} already imported.".format(moduleName))
            else:
                print("  Preimporting {:18}...".format(moduleName), end="", flush=True)
                timeStart = time()
                try:
                    import_module(moduleName)
                except ModuleNotFoundError:
                    print("  failed, ModuleNotFound.")
                except:
                    print("  failed, error happened.")
                else:
                    print(" successfully in {:.2}s".format(time() - timeStart))
        elif isinstance(moduleName, Iterable):
            for name in moduleName:
                preimport(name)
        else:
            print("  [Error]: preimport failed, please check the moduleName")
