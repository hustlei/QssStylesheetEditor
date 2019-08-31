# -*- coding: utf-8 -*-   

import sys  
import re
  
class Qsst():        
    def __init__(self,qssFile=None):
        if qssFile is None:
            self.srctext=''#qss template，qss with vars
        else:
            with open(qssFile,'r') as f:
                self.srctext=f.read()
        self.qss=''#translated qss
        self.varDict={}#defined vars
        self.varsUsed=[]#var used in qss
        self.varUndefined=[]#var used but not defined，qss will not work
    
    def loadVarDict(self,qssStr=None):
        if qssStr is None:
            qssStr=self.srctext
        rst=re.findall(r'([^\s=;]+)\s*={1}[ \t]*([^\s=;]*)[\r\n;]+',qssStr)
        self.varDict={}
        for var,val in rst:
            self.varDict[var]=val
        return self.varDict
    
    def scanVarsUsed(self,qssStr=None):
        if qssStr is None:
            qssStr=self.srctext
        self.varsUsed=re.findall(r'[.\s]*\$+([^\$;]+)\s*;+[.\s]*',qssStr)
        return self.varsUsed
        
    def replaceVars(self,qssStr=None,varDict=None):
        if qssStr is None:
            qssStr=self.srctext
        if varDict is None:
            varDict=self.varDict
        self.varUndefined=[]
        vars=self.scanVarsUsed(qssStr)
        for v in vars:
            if(v in varDict.keys()):
                qssStr=qssStr.replace("$"+v,varDict[v])
            else:
                self.varUndefined.append(v)
                qssStr=qssStr.replace("$"+v,' ')
        self.qss=qssStr
        return self.varUndefined
        
    def writeVarList(self):
        varlist=self.varDict
        self.loadVarDict()
        if(self.varDict):
            self.srctext=re.sub(r'[\t ]*([^;\s=/*]+)\s*={1}[\t ]*([^;\s=/*]*)[\t ]*',
                        lambda m:r'{}={}'.format(m.group(1),varlist[m.group(1)]),
                        self.srctext)
            if(len(varlist)>len(self.varDict)):
                s=''
                for var,val in varlist.items():
                    if(var not in self.varDict.keys()):
                        s+=var+"="+val+"\n"
                self.srctext=re.sub(r'[\t ]*([^;\s=/*]+\s*={1}[\t ]*[^;\s=/*]*)[\t ]*',
                        r'{}\1'.format(s),
                        self.srctext,1)
        else:
            s='/*'
            for var,val in varlist.items():
                s+=var+"="+val+"\n"
            s+='*/\n'
            self.srctext=s+self.srctext
        return self.srctext
            
 
if __name__=="__main__":
    import os 
    os.chdir(os.path.dirname(__file__))
    qssT=Qsst('new.qsst')
    qssT.loadVarDict()
    print(qssT.varDict)