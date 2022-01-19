# -*- coding: utf-8 -*-
"""Tests for auxilary"""


from CodeEditor.auxilary import *

def test_bgr():
    assert BGR2RGB(4227327) == (255, 128, 64)

def test_isBin():
    bytes=b"123456789\x00\x00\x00\x00"
    assert isBin(bytes)
    str="一段中文，莫名其妙，阿斯蒂芬(^_−)☆ψ(*｀ー´)ψ"
    bytes=str.encode("utf8")
    assert not isBin(bytes)
    bytes=str.encode("utf16")
    assert not isBin(bytes)
    # bytes=str.encode("utf32")
    # assert not isBin(bytes)
    bytes=str.encode("GB18030")
    assert not isBin(bytes)