# -*- coding: utf-8 -*-
"""Auxilary functions for color convert, file type detect etc."""

def BGR2RGB(bgrInt):
    """Convert an integer in BGR format to an ``(r, g, b)`` tuple.

    ``bgr_int`` is an integer representation of an RGB color, where the R, G,
    and B values are in the range (0, 255), and the three channels are comined
    into ``bgr_int`` by a bitwise ``red | (green << 8) | (blue << 16)``. This
    leaves the red channel in the least-significant bits, making a direct
    translation to a QColor difficult (the QColor constructor accepts an
    integer form, but it assumes the *blue* channel is in the least-significant
    bits).

    Examples:

        >>> BGR2RGB(4227327)
        (255, 128, 64)

    """
    red, green, blue = (
        bgrInt & 0xFF,
        (bgrInt >> 8) & 0xFF,
        (bgrInt >> 16) & 0xFF,
    )
    return (red, green, blue)


def isBin(strbytes):
    ctl_list = [b for b in strbytes if (b < 0x20 and b not in (9, 10, 13))]
    # ctl_list = [b for b in strbytes if (b < 0x20 and b not in (9, 10, 13)) or 127<b<160]
    count = len(ctl_list)
    f = count / len(strbytes)
    return f > 0.3

# 二进制文件基本上都会有char(0)，注意，是“基本上” 。#
# 我尝试通过这个方式来判断，发现判断正确率很高，我手头的二进制STL文件都能够判断正确，但是总觉得这种方式不够保险，如果刚好某个二进制文件没有char(0)怎么办？？？
# 纯文本中间是不会含有\0\0\0\0(四个连续的0)的,
# 细点分就是:
# ucs-4/utf-32中不会含有\0\0\0\0
# ucs-2/utf-8/utf-16中不会含有\0\0
# ascii中不会含有\0

# 逐字节读取，然后满足以下任何一个条件那么就是二进制文件：
# 1）所读取字节大于127并且小于160；
# 2）所读取字节大于等于160并且不成对出现；(注：大于等于160并成对出现的是汉字，其他UNICODE字符集编码格式不是很清楚)
# 3）所读取字节小于32并且不等于9(TAB)、10(换行) (注： 10 是UNIX格式文本换行)
# 4）所读取字节小于32并且等于13(回车)但是之后的字节并不是10(换行) (注：13 10 是DOS格式文本换行)

def byte2str(strbytes, echoescape=True):
    s = ""
    if echoescape and len(strbytes) < 11 * 1024:
        for b in strbytes:  # ord(chr(b))
            if b < 0x20 and b not in (9, 10, 13):  # >= 0x80 or c.isalnum() or c == "-" or c == "_":
                s += " NUL "
            else:
                c = chr(b)
                s += c
    else:
        str_list = [chr(b) for b in strbytes if b > 0x30]
        s = "".join(str_list)
    return s
