# -*- coding: utf-8 -*-
"""preload modules before using
"""

import sys
from importlib import import_module
from time import time
from typing import Iterable
from warnings import warn


def preimport(*moduleNames):
    preload(moduleNames)


def preload(moduleNames: Iterable[str]):
    """Import modules before software starting, so that software run quickly.

    Should be called at the very start of the program.

    :param moduleNames:  For example ("PyQt5", "PyQt5.QtCore").
    """
    for module_name in moduleNames:
        if module_name not in sys.modules:
            print(" - {:16}... ".format(module_name), end="", flush=True)
            t0 = time()
            import_module(module_name)
            print("ok ({:.2}s)".format(time() - t0))  # ✓
        else:
            warn(f'Module "{module_name}" has already been imported. Make sure to call "preload"'
                 f'before any other import statements.')
