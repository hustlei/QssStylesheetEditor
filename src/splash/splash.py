# -*- coding: utf-8 -*-
"""SplashScreen

Copyright (c) 2019 lileilei <hustlei@sina.cn>
"""

import time
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QSplashScreen
from preimport import preimport


class SplashScreen(QSplashScreen):
    """Custom SplashScreen"""
    def __init__(self, picfile):
        pixmap = QPixmap(picfile)
        # , Qt.WindowStaysOnTopHint)
        super(SplashScreen, self).__init__(pixmap)
        # self.setMask(splash_pix.mask())
        # self.raise_()
        self.labelAlignment = int(Qt.AlignBottom | Qt.AlignHCenter | Qt.AlignAbsolute)
        self.show()
        QApplication.flush()

    def showMessage(self, msg):
        """Show the progress message on the splash image"""
        super(SplashScreen, self).showMessage(msg, self.labelAlignment, Qt.white)
        QApplication.processEvents()

    def clearMessage(self):
        """Clear message on the splash image"""
        super(SplashScreen, self).clearMessage()
        QApplication.processEvents()

    def setProgressText(self, percent, delay=0.1):
        """Show load percent in format 'Loading ... xx%' by showMessage method"""
        time.sleep(delay)  # 延时，给查看splashscreen更新数值
        self.showMessage(self.tr("Loading... {0}%").format(percent))

    def loadProgress(self):
        """Preimport modules to improve start speed
        Following modules are imported before splash:
        PyQt5, PyQt5.QtCore, PyQt5.QtGui, PyQt5.QtWidgets are imported before Splash.
        i18n is imported before Splash, for Splash using i18n.
        config is imported before i18n, for i18n using config.
        """
        self.setProgressText(0, 0)
        time.sleep(0.1)
        self.setProgressText(5)
        time.sleep(0.1)
        self.setProgressText(10)
        time.sleep(0.1)
        self.setProgressText(15)
        time.sleep(0.1)
        self.setProgressText(20)  # PyQt5, i18n are loaded, so before 20% do nothing
        preimport(["PyQt5.Qsci"])
        self.setProgressText(40)
        preimport(["res", "res.img_rc"])
        self.setProgressText(60)
        preimport(["ui"])
        self.setProgressText(80)
        preimport(["qss_template"])
        self.setProgressText(100)


# from PyQt5.QtCore import QDate, QDateTime
#         from PyQt5.QtGui import (QBrush, QColor, QBitmap, QIcon, QImage, QPicture, QCursor, QPainter, QKeySequence,
#                                  QFont, QPen, QMovie, qGray)
#         # (Base64, Base64url,Bigfloat,DateTimeString,Decimal,QDir,QRegExp,QRegularExpression,QTimer,QUrl)
# # QtWidgets 常用控件
# from PyQt5.QtWidgets import (
#     QAction, QActionGroup, QApplication, QBoxLayout, QCalendarWidget, QCheckBox, QColorDialog, QComboBox,
#     QDesktopWidget, QDialog, QDockWidget, QDoubleSpinBox, QFileDialog, QFontComboBox, QFontDialog, QFormLayout,
#     QFrame, QGesture, QGraphicsView, QGraphicsWidget, QGridLayout, QGroupBox, QHBoxLayout, QHeaderView,
#     QInputDialog, QItemDelegate, QKeySequenceEdit, QLCDNumber, QLabel, QLineEdit, QListView, QListWidget,
#     QListWidgetItem, QMainWindow, QMdiArea, QMdiSubWindow, QMenu, QMenuBar, QMessageBox, QOpenGLWidget,
#     QProgressBar, QProgressDialog, QPushButton, QRadioButton, QRubberBand, QScrollArea, QScrollBar, QShortcut,
#     QSizeGrip, QSlider, QSpacerItem, QSpinBox, QSplashScreen, QSplitter, QSplitterHandle, QStackedLayout,
#     QStackedWidget, QStatusBar, QStyle, QStyleFactory, QSystemTrayIcon, QTabBar, QTabWidget, QTableView,
#     QTableWidget, QTableWidgetItem, QTableWidgetSelectionRange, QTextBrowser, QTextEdit, QTimeEdit, QToolBar,
#     QToolBox, QToolButton, QToolTip, QTreeView, QTreeWidget, QTreeWidgetItem, QUndoCommand, QUndoGroup,
#     QUndoStack, QUndoView, QVBoxLayout, QWhatsThis, QWidget, QWidgetAction, QWidgetItem, qApp)

# # QtSci 所有组件
# from PyQt5 import Qsci
# from PyQt5.Qsci import (QsciLexer, QsciLexerAVS, QsciLexerBash, QsciLexerBatch, QsciLexerCMake, QsciLexerCPP,
#                         QsciLexerCSS, QsciLexerCSharp, QsciLexerCoffeeScript, QsciLexerCustom, QsciLexerD,
#                         QsciLexerDiff, QsciLexerFortran, QsciLexerFortran77, QsciLexerHTML, QsciLexerIDL,
#                         QsciLexerJSON, QsciLexerJava, QsciLexerJavaScript, QsciLexerLua, QsciLexerMakefile,
#                         QsciLexerMarkdown, QsciLexerMatlab, QsciLexerOctave, QsciLexerPO, QsciLexerPOV,
#                         QsciLexerPascal, QsciLexerPerl, QsciLexerPostScript, QsciLexerProperties,
#                         QsciLexerPython, QsciLexerRuby, QsciLexerSQL, QsciLexerSpice, QsciLexerTCL,
#                         QsciLexerTeX, QsciLexerVHDL, QsciLexerVerilog, QsciLexerXML, QsciLexerYAML, QsciMacro,
#                         QsciPrinter, QsciScintilla, QsciScintillaBase, QsciStyle, QsciStyledText, QsciAPIs)
