# -*- coding: utf-8 -*-
"""Basic for load save and add item for toml config file

Copyright (c) 2019 lileilei <hustlei@sina.cn>
"""

import os,sys
sys.path.append(os.path.dirname(__file__))
import toml

class ConfBase:
    def __init__(self):
        self.dict={}

    def read(self,cfgFile=None):
        """ read a toml config file
        :param cfgFile:  config file path
        :return:  true if read success
        """
        if cfgFile!=None:
            if not os.path.exists(cfgFile):
                print("config cfgFile"+ os.path.basename(cfgFile) + ' not found')
                return False
            with open(cfgFile, mode='rb') as f:
                content = f.read()
            if content.startswith(b'\xef\xbb\xbf'):  # 去掉 utf8 bom 头 #TOML要求使用UTF-8 编码
                content = content[3:]
            self.dict = toml.loads(content.decode('utf8'))
            return True
        return False

    def _save(self,cfgFile=None):
        if cfgFile!=None:
            with open(cfgFile, 'w', newline='', encoding='utf-8') as outfile:
                # 不指定newline，则换行符自动转换为各系统默认的换行符(\n, \r, or \r\n,)
                # newline=''表示不转换
                s=toml.dumps(self.dict)
                outfile.write(s)
                print("config file saved.")

    # def addSec(self, secName, dict={}):
    #     if (secName not in self.dict or type(self.dict[secName])!=dict):
    #         conf.dict[secName] = {}
    #     self.dict[secName].update(dict)
    #     return self.dict[secName]
    #
    # def addSubSec(self, sec, subName):
    #     if(type(sec)==dict):
    #         if (subName not in sec or type(sec[subName])!=dict):
    #             sec[subName]={}
    #         return sec[subName]

    def _getSec(self, secName=None):
        if secName==None:
            return  self.dict
        if(secName not in self.dict):
            self.dict[secName]={}
        return self.dict[secName]

    def _getSubSec(self, sec, subName):
        if(type(sec)==dict):
            if(subName not in sec):
                sec[subName]={}
            return sec[subName]

    def getSec(self,secString):
        s=secString.strip()
        secs=s.split(".")
        if(len(secs)==1):
            return self._getSec(secs[0])
        else:
            sec=self._getSec(secs[0])
            for i in range(1,len(secs)):
                sec=self._getSubSec(sec,secs[i])
            return sec

    def rmSec(self,secName):
        if(secName in self.dict):
            self.dict.pop(secName)

    def rmSubSec(self,sec,subName):
        if(type(sec)==dict and subName in sec):
            sec.pop(subName)

    def listNodeAppend(self, node, child, sec=None):
        if(sec==None):
            sec=self.dict
        if (node not in sec or type(sec[node])!=list):
            sec[node] = []
        if(child in sec[node]):
            for _ in range(sec[node].count(child)):
                sec[node].remove(child)
        sec[node].append(child)

    def listNodeInset(self, node, child, sec=None):
        if(sec==None):
            sec=self.dict
        if (node not in sec or type(sec[node])!=list):
            sec[node] = []
        if(child in sec[node]):
            for _ in range(sec[node].count(child)):
                sec[node].remove(child)
        sec[node].insert(0,child)


if __name__=="__main__":
    cfgfile="config.toml"
    conf=ConfBase()
    if(conf.read(cfgfile)):
        filesec=conf._getSec("file")
        conf.listNodeAppend("recent","eeee",filesec)
        fontsec=conf._getSubSec(conf._getSec("editor"), "font")
        fontsec["size"]=12
        conf.rmSec("editor0")
        conf.save()