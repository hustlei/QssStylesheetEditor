# -*- coding: utf-8 -*-
"""get .py source file list, and generate .ts file for translate.

translate step:

1. hehe.ui → hehe.py (用pyuic)
2. hehe.py → hehe.ts (用pylupdate)
3. hehe.ts → hehe.qm (用Qt Linguist)

Copyright (c) 2019 lileilei <hustlei@sina.cn>
"""

import os
import re

srcroot = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src"))

excludedir = (".git", ".github", ".idea", "__pycache__", "data", "dist", "font", "img", "font", "installer")

p = re.compile(r'_[vV][0-9.\-_]+[.]py$$|[.]old[.]py$')


def getsrclist(folder=None):
    """get .py source code file list, the list is used for pylupdate to generate ts file"""
    if folder is None:
        folder = srcroot
    rst = []
    lst = os.listdir(folder)
    for f in lst:
        if f in excludedir:
            continue
        file = os.path.join(folder, f)
        if os.path.isfile(file):
            if f.endswith(".py"):
                if p.search(f) is None:
                    rst.append(os.path.relpath(file, srcroot))
        elif os.path.isdir(file):
            subdir = file
            rst.extend(getsrclist(subdir))
    return rst


fs = getsrclist()
os.chdir(srcroot)
print(fs)
s = "pylupdate5 {} -ts {}".format(" ".join(fs), os.path.join(os.path.dirname(__file__), "English.ts"))
os.system(s)
