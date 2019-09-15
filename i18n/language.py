from PyQt5.QtCore import QTranslator, QLibraryInfo, QLocale
from PyQt5.QtWidgets import QApplication
from config import Config
import os

class Language():
    lang="English"
    trans = QTranslator()
    trans_sys = QTranslator()

    @classmethod
    def getConfigLang(cls):
        configfile=os.path.join(os.path.dirname(__file__),"../config/config.toml")
        config=Config(configfile)
        Language.lang=config.getSec("general").get("language","English")

    @classmethod
    def setLang(cls):
        try:
            if Language.lang.lower()=="english":
                # qApp.removeTranslator(self.trans)
                # qApp.removeTranslator(self.trans_sys)
                pass
            else:
                lang="i18n/i18n-"+Language.lang+".qm"
                if(os.path.exists(lang)):
                    Language.trans.load(lang)
                    QApplication.installTranslator(Language.trans)

            if Language.trans_sys.load("qt_" + QLocale.system().name(),
                                   QLibraryInfo.location(QLibraryInfo.TranslationsPath)):
                QApplication.installTranslator(Language.trans_sys)
        except Exception as Argument:
            print(Argument)