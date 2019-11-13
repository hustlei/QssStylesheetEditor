# -*- coding: utf-8 -*-
"""
create a qrc file including all png/jpg/ico/icon resouce.
and compile qrc file to .py file.

Copyright (c) 2019 lileilei <hustlei@sina.cn>
"""

import os
dir = os.path.dirname(__file__) + "/img"
os.chdir(os.path.dirname(__file__))

s = '<!DOCTYPE RCC>\n<RCC version="1.0">\n<qresource prefix="appres.img">\n'

for f in os.listdir(dir):
    if (f.endswith(".png") or f.endswith(".jpg") or f.endswith(".ico") or f.endswith(".icon")):
        imgqrc = '    <file alias="{0}">img/{0}</file>\n'.format(f)
        s += imgqrc
        print("added " + f)

s += "</qresource>\n</RCC>\n"
print("\ncreate qrcfile")
with open("img.qrc", "w", newline="") as out:
    out.write(s)

print("\ncompile qrc to py")

os.system("pyrcc5 img.qrc -o ../src/res/img_rc.py")

input()
