# -*- coding: utf-8 -*-
"""get tranlations and set language for the app.

Copyright (c) 2019 lileilei <hustlei@sina.cn>
"""
import os
from PyQt5.QtCore import QTranslator, QLibraryInfo, QLocale
from PyQt5.QtWidgets import QApplication
from config import Config


class Language():
    """i18n setting class"""
    trans = QTranslator()  # 必须定义为Language的变量，定义为局部变量不起作用
    systrans = QTranslator()
    __inited = False
    __listInToml = []
    lang = "en"

    @classmethod
    def loadList(cls):
        """加载list.toml中的内容
        :return: 返回一个列表，列表的每个元素是一个包含name,systrans,trans,englishname的字典。
                systrans,trans,分别是qtbase_xx.qm文件和当前语言的qm文件
        """
        Language.__listInToml = []
        try:
            conf = Config(os.path.join(os.path.dirname(__file__), "list.toml"))
            languages = conf.getSec("languages")
            for k, v in languages.items():
                langitem = {}
                langitem["lang"] = v[0]
                langitem["qmfile"] = v[1]
                langitem["nativename"] = v[2]
                langitem["englishname"] = k
                if not langitem["nativename"]:
                    langitem["nativename"] = QLocale(langitem["name"]).nativeLanguageName()
                if langitem["lang"]:
                    Language.__listInToml.append(langitem)
        except Exception:
            Language.__listInToml = [
                {
                    "lang": "en",
                    "qmfile": "",
                    "nativename": "English",
                    "englishname": "English"
                },
            ]
        Language.__inited = True
        return Language.__listInToml

    @staticmethod
    def getLangs():
        """load avaiable languages
        :return: 可用的语言包列表
        """
        if not Language.__inited:
            Language.loadList()
        # qmfiles = []
        # dir = os.path.join(os.path.dirname(__file__), "../i18n")
        # for f in os.listdir(dir):
        #     if (f.startswith("i18n_") and f.endswith(".qm")):  # os.path.isfile(file) and
        #         qmfiles.append(f)  # f[5:-3])
        langs = Language.__listInToml.copy()
        for lang in Language.__listInToml:
            p = os.path.join(os.path.dirname(__file__), lang["qmfile"])
            if not os.path.exists(p) and not lang["lang"].startswith("en"):
                langs.remove(lang)
        return langs

    @classmethod
    def getLang(cls):
        """根据配置文件读取语言配置，如果没有找到当前系统配置
        :return:
        """
        config = Config.current()
        Language.lang = config["general.language"]

        if not Language.lang.strip():
            # import locale
            # lang,country=locale.getdefaultlocale()
            Language.lang = QLocale.system().name()  # 语言_国家”形式形成的字符串，比如zh_CN。
            # QLocale.languageToString(QLocale.system().language()) #语言英文名称，比如English，Chinese
            # QLocale.system().nativeLanguageName() #语言自身的写法比如：中文(简体)
        return Language.lang

    @classmethod
    def setTrans(cls):
        """根据配置文件(如果没有就根据当前系统语言)设置当前语言包
        """
        langs = Language.getLangs()
        lang = Language.getLang()
        qmfile = None
        for l in langs:
            if lang in (l["lang"], l["lang"].replace("-", "_")):
                qmfile = l["qmfile"]
                break
        if qmfile is None:
            lang = "en"
        try:
            if lang == "en":
                # qApp.removeTranslator(self.qmfile)
                # qApp.removeTranslator(self.trans_sys)
                pass
            else:
                transdir = os.path.dirname(__file__)
                if os.path.exists(os.path.join(transdir, qmfile)):
                    Language.trans.load(qmfile, transdir)
                    QApplication.installTranslator(Language.trans)
        except Exception as Argument:
            print(Argument)

        systransdir = QLibraryInfo.location(QLibraryInfo.TranslationsPath)
        try:
            if Language.systrans.load("qt_" + QLocale(lang).name(), systransdir):
                QApplication.installTranslator(Language.systrans)
            if Language.systrans.load("qscintilla_" + QLocale(lang).name(), systransdir):
                QApplication.installTranslator(Language.systrans)
        except Exception:
            Language.systrans.load("qt_" + QLocale.system().name(), systransdir)
            QApplication.installTranslator(Language.systrans)


if __name__ == "__main__":
    print(Language.getLangs())
