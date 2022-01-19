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

# def byte2str(strbytes, echoescape=True):
#     s = ""
#     if echoescape and len(strbytes) < 11 * 1024:
#         for b in strbytes:  # ord(chr(b))
#             if b < 0x20 and b not in (9, 10, 13):  # >= 0x80 or c.isalnum() or c == "-" or c == "_":
#                 s += " NUL "
#             else:
#                 c = chr(b)
#                 s += c
#     else:
#         str_list = [chr(b) for b in strbytes if b > 0x30]
#         s = "".join(str_list)
#     return s

fontFamilies = {
    "宋体": "SimSun",
    "黑体": "SimHei",
    "微软雅黑": "Microsoft YaHei",
    "微软雅黑体": "Microsoft YaHei",
    "微软正黑体": "Microsoft JhengHei",
    "新宋体": "NSimSun",
    "新细明体": "PMingLiU",
    "细明体": "MingLiU",
    "标楷体": "DFKai-SB",
    "仿宋": "FangSong",
    "楷体": "KaiTi",
    "隶书": "LiSu",
    "幼圆": "YouYuan",
    "仿宋_GB2312": "FangSong_GB2312",
    "楷体_GB2312": "KaiTi_GB2312",
    "华文黑体": "STHeiti",
    "华文细黑": "STXihei",
    "华文楷体": "STKaiti",
    "华文宋体": "STSong",
    "华文中宋": "STZhongsong",
    "华文仿宋": "STFangsong",
    "方正舒体": "FZShuTi",
    "方正姚体": "FZYaoti",
    "华文彩云": "STCaiyun",
    "华文琥珀": "STHupo",
    "华文隶书": "STLiti",
    "华文行楷": "STXingkai",
    "华文新魏": "STXinwei",
    "儷黑 Pro": "LiHei Pro Medium",
    "儷宋 Pro": "LiSong Pro Light",
    "蘋果儷中黑": "Apple LiGothic Medium",
    "蘋果儷細宋": "Apple LiSung Light",
    "新細明體": "PMingLiU",
    "細明體": "MingLiU",
    "微軟正黑體": "Microsoft JhengHei"
}

# 支持文件类型
# 用16进制字符串的目的是可以知道文件头是多少字节
# 各种文件头的长度不一样，少半2字符，长则8字符
typeList = {
    "68746D6C3E": 'html',  #
    "d0cf11e0a1b11ae10000": 'xls',
    "44656C69766572792D64": 'eml',
    'ffd8ffe000104a464946': 'jpg',
    '89504e470d0a1a0a0000': 'png',
    '47494638396126026f01': 'gif',
    '49492a00227105008037': 'tif',
    '424d228c010000000000': 'bmp',
    '424d8240090000000000': 'bmp',
    '424d8e1b030000000000': 'bmp',
    '41433130313500000000': 'dwg',
    '3c21444f435459504520': 'html',  #
    '3c21646f637479706520': 'htm',  #
    '48544d4c207b0d0a0942': 'css',  #
    '696b2e71623d696b2e71': 'js',  #
    '7b5c727466315c616e73': 'rtf',  #
    '38425053000100000000': 'psd',
    '46726f6d3a203d3f6762': 'eml',
    'd0cf11e0a1b11ae10000': 'doc',
    'd0cf11e0a1b11ae10000': 'vsd',
    '5374616E64617264204A': 'mdb',
    '252150532D41646F6265': 'ps',
    '255044462d312e350d0a': 'pdf',
    '2e524d46000000120001': 'rmvb',
    '464c5601050000000900': 'flv',
    '00000020667479706d70': 'mp4',
    '49443303000000002176': 'mp3',
    '000001ba210001000180': 'mpg',
    '3026b2758e66cf11a6d9': 'wmv',
    '52494646e27807005741': 'wav',
    '52494646d07d60074156': 'avi',
    '4d546864000000060001': 'mid',
    '504b0304140000080044': 'zip',
    '504b03040a0000080000': 'zip',
    '504b03040a0000000000': 'zip',
    '526172211a0700cf9073': 'rar',
    '235468697320636f6e66': 'ini',  #
    '504b03040a0000000000': 'jar',
    '4d5a9000030000000400': 'exe',
    '3c25402070616765206c': 'jsp',  #
    '4d616e69666573742d56': 'mf',  #
    '3c3f786d6c2076657273': 'xml',  #
    '494e5345525420494e54': 'sql',  #
    '7061636b616765207765': 'java',  #
    '406563686f206f66660d': 'bat',  #
    '1f8b0800000000000000': 'gz',
    '6c6f67346a2e726f6f74': 'properties',  #
    'cafebabe0000002e0041': 'class',
    '49545346030000006000': 'chm',
    '04000000010000001300': 'mxp',
    '504b0304140006000800': 'docx',
    'd0cf11e0a1b11ae10000': 'wps',
    '6431303a637265617465': 'torrent',  #
}
binfiletypes = {
    'xls', 'eml', 'jpg', 'png', 'gif', 'tif', 'bmp', 'bmp', 'bmp', 'dwg', 'psd', 'eml', 'doc', 'vsd', 'mdb', 'ps',
    'pdf', 'rmvb', 'flv', 'mp4', 'mp3', 'mpg', 'wmv', 'wav', 'avi', 'mid', 'zip', 'zip', 'zip', 'rar', 'jar', 'exe',
    'gz', 'class', 'chm', 'mxp', 'docx', 'wps'
}
textfiletypes = {
    "html": "HTML",
    "htm": "HTML",
    "css": "CSS",
    "js": "JavaScript",
    "rtf": "Text",
    "ini": "Text",
    "jsp": 'Text',
    "mf": "Text",
    "xml": "XML",
    "sql": "SQL",
    "java": "Java",
    "bat": "Batch",
    "properties": "Text",
    "torrent": "XML"
}


# 字节码转16进制字符串
def bytes2hex(bytes):
    num = len(bytes)
    hexstr = u""
    for i in range(num):
        t = u"%x" % bytes[i]
        if len(t) % 2:
            hexstr += u"0"
        hexstr += t
    return hexstr.upper()


# 获取文件类型
def getFileType(filename):
    binfile = open(filename, 'rb')  # 必需二制字读取
    bins = binfile.read(20)  # 提取20个字符
    binfile.close()  # 关闭文件流
    bins = bytes2hex(bins)  # 转码
    bins = bins.lower()  # 小写
    tl = typeList  # 文件类型
    ftype = 'unknown'
    for hcode in tl.keys():
        lens = len(hcode)  # 需要的长度
        if bins[0:lens] == hcode:
            ftype = tl[hcode]
            break
    if ftype == 'unknown':  # 全码未找到，优化处理，码表取5位验证
        bins = bins[0:5]
        for hcode in tl.keys():
            if len(hcode) > 5 and bins == hcode[0:5]:
                ftype = tl[hcode]
                break
    return ftype
