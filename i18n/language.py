from PyQt5.QtCore import QTranslator, QLibraryInfo, QLocale
from PyQt5.QtWidgets import QApplication
from config import Config
import os
from config.base import ConfBase

class Language():
    lang="English"
    trans = QTranslator()
    systrans = QTranslator()
    transdir = os.path.dirname(__file__)
    systransdir = QLibraryInfo.location(QLibraryInfo.TranslationsPath)
    langs=[]
    
    @classmethod
    def getLangs(self):
        qmfiles=[]
        dir = os.path.join(os.path.dirname(__file__), "../i18n")
        for f in os.listdir(dir):
            if (f.startswith("i18n_") and f.endswith(".qm")):  # os.path.isfile(file) and
                qmfiles.append(f)#f[5:-3])
        langs = []
        conf=ConfBase()
        try:
            conf.read(os.path.join(os.path.dirname(__file__),"list.toml"))
            conflangs=conf.getSec("languages")
            for k,v in conflangs.items():
                l={}
                l["name"]=v[0]
                l["systrans"]="qtbase_"+v[1]+".qm"
                l["trans"]=v[2]
                l["englishname"]=k
                langs.append(l)
        except Exception as e:
            langs=[{"name":"English","systrans":"qtbase_en.qm","trans":"","englishname":"English"},]
        for lang in langs.copy():
            p1=os.path.join(Language.systransdir,lang["systrans"])
            p2=os.path.join(Language.transdir,lang["trans"])
            if not os.path.exists(p2) and lang["name"]!="English":
                langs.remove(lang)
            elif not os.path.exists(p1):
                l["systrans"]=""
        return langs

    @classmethod
    def getLang(cls):
        configfile=os.path.join(os.path.dirname(__file__),"../config/config.toml")
        config=Config(configfile)
        Language.lang=config.getSec("general").get("language","English")
        return Language.lang

    @classmethod
    def setTrans(cls):
        langs=Language.getLangs()
        lang=Language.getLang()
        trans=None
        for l in langs:
            if l["name"]==lang:
                trans=l["trans"]
                systrans=l["systrans"]
                break
        if trans==None:
            lang="English"
            systrans="qtbase_en.qm"
        try:
            if lang=="english":
                # qApp.removeTranslator(self.trans)
                # qApp.removeTranslator(self.trans_sys)
                pass
            else:
                if(os.path.exists(os.path.join(Language.transdir,trans))):
                    Language.trans.load(trans,Language.transdir)
                    QApplication.installTranslator(Language.trans)

            if Language.trans_sys.load(systrans,Language.systransdir):
                    #"qt_" + QLocale.system().name(),QLibraryInfo.location(QLibraryInfo.TranslationsPath)):
                QApplication.installTranslator(Language.systrans)
        except Exception as Argument:
            print(Argument)

if __name__=="__main__":
    print(Language.getLangs())