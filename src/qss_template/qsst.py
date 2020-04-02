# -*- coding: utf-8 -*-
"""var operate for qss file

Copyright (c) 2019 lileilei <hustlei@sina.cn>
"""

import re


class Qsst():
    """qss template"""
    def __init__(self, qssFile=None):
        if qssFile is None:
            self.srctext = ''  # qss template，qss with vars
        else:
            with open(qssFile, 'r') as f:
                self.srctext = f.read()
        self.qss = ''  # translated qss
        self.varDict = {}  # defined vars Union used vars
        self.varUsed = []  # var used in qss
        self.varUndefined = []  # var used but not defined，these vars will be assign to ''
        self.codeBlocks = []

        # 嵌入代码定义
        self.reCodeBlock = re.compile(r'~{3}.*[\r\n]+(.*)[\r\n]+~{3}|`{3}.*[\r\n]+(.*)[\r\n]+`{3}', re.DOTALL)

    def loadVars(self, qssStr=None):
        """扫描qsst模板文件中的所有变量定义，引用的变量；
        把引用的变量放到varUsed列表中；
        把引用但未定义变量赋值为''放在varDict中；
        把定义的变量放到varDict中
        """
        if qssStr is None:
            qssStr = self.srctext
        self.varUsed = re.findall(r':[ \t\w,.:()]*[$]([\w]+)', qssStr)
        varsDefined = re.findall(r'[$](\w+)\s*=[ \t]*([#(),.\w]*)[\t ]*[\r\n;\/]+', qssStr)
        self.varDict = {}
        for var, val in varsDefined:
            self.varDict[var] = val
        self.varUndefined = []
        for varused in self.varUsed:
            if varused not in self.varDict.keys():
                self.varDict[varused] = ''
                self.varUndefined.append(varused)

    def runCodeBlocks(self):
        """代码块中可以放QPalette的定义，如果有Qpalette定义，在预览的时候需要先运行代码块中的定义"""
        self.codeBlocks = self.reCodeBlock.findall(self.srctext)
        if self.codeBlocks:
            try:
                eval("from PyQt5.QtGui import QPalette")
                for code in self.codeBlocks:
                    exec(code)
            except:
                print("warning: codeblock in qsst exec error.")

    def convertQss(self):
        """根据varDict中变量的值，把模板文件中引用的变量用值替换，转换为qss文件。
        """

        qssStr = self.srctext
        varDict = self.varDict
        self.loadVars()
        # 删除变量定义
        varsDefined = re.compile(r'[$](\w+)\s*=[ \t]*([#(),.\w]*)[ \t;]*[\r\n]{0,2}')
        qssStr = varsDefined.sub("", qssStr)

        for v in self.varDict:
            if v in varDict.keys():
                # qssStr = qssStr.replace("$" + v, varDict[v])
                qssStr = re.sub(r'[$](\w+)([\s;]*)', lambda m:'{}{}'.format(varDict[m.group(1)], m.group(2)), qssStr)
            else:
                self.varUndefined.append(v)
                # qssStr = qssStr.replace("$" + v, ' ')
                qssStr = re.sub(r'[$](\w+)([\s;]*)', lambda m:'{}{}'.format(" ", m.group(2)), qssStr)
        # 删除代码块
        qssStr = self.reCodeBlock.sub("", qssStr)
        self.qss = qssStr

    # def replaceVarsInQss(self,val):
    #     """
    #     把转换后的qss文件中，若还存在引用的变量（$开头）都赋值为val
    #     本方法暂时存在问题，qss和表达式需要+u
    #     """
    #     re.sub(r'(?<:[\s]*)\$([a-zA-Z_\u4e00-\u9fa5][0-9a-zA-Z_\u4e00-\u9fa5]*)',val,self.qss)

    def writeVars(self):
        varDictNew = self.varDict
        self.loadVars()
        if self.varDict:  # 如果文件中变量不为空，更新变量值
            self.srctext = re.sub(r'[$](\w+)\s*=[ \t]*([#(),.\w]*)[\t ]*[;]?',
                                  lambda m: '${} = {};'.format(m.group(1), varDictNew.get(m.group(1), "")),
                                  self.srctext)
            if self.varUndefined:  # 在第一的变量处插入多出来的变量,引用比定义的变量多的时候回出现这种情况
                s = ''
                for var, val in varDictNew.items():
                    if var in self.varUndefined:
                        s += "$" + var + " = " + val + ";\n"
                self.srctext = re.sub(r'[$](\w+)\s*=[ \t]*([#(),.\w]*)[\t ]*[;]?', r'{}$\1 = \2;\n'.format(s),
                                      self.srctext, 1)
        else:
            s = ''
            for var, val in varDictNew.items():
                s += "$" + var + " = " + val + ";\n"
            s += '\n'
            self.srctext = s + self.srctext
        self.loadVars()


if __name__ == "__main__":
    import os
    os.chdir(os.path.dirname(__file__))
    qssT = Qsst('default.qsst')
    qssT.loadVars()
    print(qssT.varDict)
    print(qssT.varUsed)
    print(qssT.varUndefined)
    qssT.convertQss()
    print(qssT.qss[100:200])
