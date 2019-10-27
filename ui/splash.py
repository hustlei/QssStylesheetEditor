# -*- coding: utf-8 -*-
"""
Copyright (c) 2019 lileilei <hustlei@sina.cn>
"""
import time

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QSplashScreen


class SplashScreen(QSplashScreen):
    def __init__(self, picfile):
        pixmap = QPixmap(picfile)
        # , Qt.WindowStaysOnTopHint)
        super(SplashScreen, self).__init__(pixmap)
        # self.setMask(splash_pix.mask())
        # self.raise_()
        self.labelAlignment = Qt.Alignment(
            Qt.AlignBottom | Qt.AlignHCenter | Qt.AlignAbsolute)
        self.show()
        QApplication.flush()

    def showMessage(self, msg):
        super(SplashScreen, self).showMessage(msg,
                                              self.labelAlignment,
                                              Qt.white)
        QApplication.processEvents()

    def clearMessage(self):
        super(SplashScreen, self).clearMessage()
        QApplication.processEvents()

    def setProgressText(self, percent, delay=0.1):
        time.sleep(delay)  # 延时，给查看splashscreen更新数值
        self.showMessage(self.tr("Loading... {0}%").format(percent))

    def loadProgress(self):
        self.setProgressText(0, 0)
        # QtCore QtGui 常用组件
        import PyQt5
        from PyQt5.QtCore import QDate, QDateTime
        from PyQt5.QtGui import (
            QBrush,
            QColor,
            QBitmap,
            QIcon,
            QImage,
            QPicture,
            QCursor,
            QPainter,
            QKeySequence,
            QFont,
            QPen,
            QMovie,
            qGray)
        #(Base64, Base64url,Bigfloat,DateTimeString,Decimal,QDir,QRegExp,QRegularExpression,QTimer,QUrl)
        self.setProgressText(10)
        import res.img_rc
        from res.img_rc import qt_resource_data
        # QtWidgets 常用控件
        from PyQt5.QtWidgets import (
            QAction,
            QActionGroup,
            QApplication,
            QBoxLayout,
            QCalendarWidget,
            QCheckBox,
            QColorDialog,
            QComboBox,
            QDesktopWidget,
            QDialog,
            QDockWidget,
            QDoubleSpinBox,
            QFileDialog,
            QFontComboBox,
            QFontDialog,
            QFormLayout,
            QFrame,
            QGesture,
            QGraphicsView,
            QGraphicsWidget,
            QGridLayout,
            QGroupBox,
            QHBoxLayout,
            QHeaderView,
            QInputDialog,
            QItemDelegate,
            QKeySequenceEdit,
            QLCDNumber,
            QLabel,
            QLineEdit,
            QListView,
            QListWidget,
            QListWidgetItem,
            QMainWindow,
            QMdiArea,
            QMdiSubWindow,
            QMenu,
            QMenuBar,
            QMessageBox,
            QOpenGLWidget,
            QProgressBar,
            QProgressDialog,
            QPushButton,
            QRadioButton,
            QRubberBand,
            QScrollArea,
            QScrollBar,
            QShortcut,
            QSizeGrip,
            QSlider,
            QSpacerItem,
            QSpinBox,
            QSplashScreen,
            QSplitter,
            QSplitterHandle,
            QStackedLayout,
            QStackedWidget,
            QStatusBar,
            QStyle,
            QStyleFactory,
            QSystemTrayIcon,
            QTabBar,
            QTabWidget,
            QTableView,
            QTableWidget,
            QTableWidgetItem,
            QTableWidgetSelectionRange,
            QTextBrowser,
            QTextEdit,
            QTimeEdit,
            QToolBar,
            QToolBox,
            QToolButton,
            QToolTip,
            QTreeView,
            QTreeWidget,
            QTreeWidgetItem,
            QUndoCommand,
            QUndoGroup,
            QUndoStack,
            QUndoView,
            QVBoxLayout,
            QWhatsThis,
            QWidget,
            QWidgetAction,
            QWidgetItem,
            qApp)
        self.setProgressText(30)
        # QtSci 所有组件
        from PyQt5 import Qsci
        from PyQt5.Qsci import (
            QsciLexer,
            QsciLexerAVS,
            QsciLexerBash,
            QsciLexerBatch,
            QsciLexerCMake,
            QsciLexerCPP,
            QsciLexerCSS,
            QsciLexerCSharp,
            QsciLexerCoffeeScript,
            QsciLexerCustom,
            QsciLexerD,
            QsciLexerDiff,
            QsciLexerFortran,
            QsciLexerFortran77,
            QsciLexerHTML,
            QsciLexerIDL,
            QsciLexerJSON,
            QsciLexerJava,
            QsciLexerJavaScript,
            QsciLexerLua,
            QsciLexerMakefile,
            QsciLexerMarkdown,
            QsciLexerMatlab,
            QsciLexerOctave,
            QsciLexerPO,
            QsciLexerPOV,
            QsciLexerPascal,
            QsciLexerPerl,
            QsciLexerPostScript,
            QsciLexerProperties,
            QsciLexerPython,
            QsciLexerRuby,
            QsciLexerSQL,
            QsciLexerSpice,
            QsciLexerTCL,
            QsciLexerTeX,
            QsciLexerVHDL,
            QsciLexerVerilog,
            QsciLexerXML,
            QsciLexerYAML,
            QsciMacro,
            QsciPrinter,
            QsciScintilla,
            QsciScintillaBase,
            QsciStyle,
            QsciStyledText,
            QsciAPIs)
        self.setProgressText(50)
        # ui preload
        import ui
        ui.preload()
        # 自定义控件preload
        import ui.editor
        ui.editor.preload()
        self.setProgressText(70)
        self.setProgressText(90)
        # 逻辑code preload
        import qss_template
        qss_template.preload()
        self.setProgressText(100)
