"""Wrapper for Qsci.QsciScintilla enumerations.
"""
from PyQt5.Qsci import QsciScintilla
from PyQt5.QtCore import QCoreApplication, Qt
from CodeEditor.lang import language_extensions


class EnumError(Exception):
    """unknown enum name or get enum failed."""
    def __init__(self, name):
        super(EnumError, self).__init__("Unknown enumeration: {}".format(name))


class SettingEnums:
    enums = {
        # annotation display styles
        QsciScintilla.AnnotationDisplay: {
            QsciScintilla.AnnotationHidden: {
                'name': 'AnnotationHidden',
                'display': QCoreApplication.translate('SettingEnums', "Hidden")
            },
            QsciScintilla.AnnotationStandard: {
                'name': 'AnnotationStandard',
                'display': QCoreApplication.translate('SettingEnums', "Standard")
            },
            QsciScintilla.AnnotationBoxed: {
                'name': 'AnnotationBoxed',
                'display': QCoreApplication.translate('SettingEnums', "Boxed")
            },
        },
        # sources for auto-completion lists.
        QsciScintilla.AutoCompletionSource: {
            QsciScintilla.AcsNone: {
                'name': 'AcsNone',
                'display': QCoreApplication.translate('SettingEnums', "None")
            },
            QsciScintilla.AcsAll: {
                'name': 'AcsAll',
                'display': QCoreApplication.translate('SettingEnums', "All")
            },
            QsciScintilla.AcsDocument: {
                'name': 'AcsDocument',
                'display': QCoreApplication.translate('SettingEnums', "Document")
            },
            QsciScintilla.AcsAPIs: {
                'name': 'AcsAPIs',
                'display': QCoreApplication.translate('SettingEnums', "APIs")
            },
        },
        # brace matching modes. The character pairs (), [] and () are treated as
        # braces. The Python lexers will also match a : with the end of the
        # corresponding indented block.
        QsciScintilla.BraceMatch: {
            QsciScintilla.NoBraceMatch: {
                'name': 'NoBraceMatch',
                'display': QCoreApplication.translate('SettingEnums', "No")
            },
            QsciScintilla.StrictBraceMatch: {
                'name': 'StrictBraceMatch',
                'display': QCoreApplication.translate('SettingEnums', "Strict")
            },
            QsciScintilla.SloppyBraceMatch: {
                'name': 'SloppyBraceMatch',
                'display': QCoreApplication.translate('SettingEnums', "Sloppy")
            },
        },
        # call tip styles
        QsciScintilla.CallTipsStyle: {
            QsciScintilla.CallTipsNone: {
                'name': 'CallTipsNone',
                'display': QCoreApplication.translate('SettingEnums', "None")
            },
            QsciScintilla.CallTipsNoContext: {
                'name': 'CallTipsNoContext',
                'display': QCoreApplication.translate('SettingEnums', "NoContext")
            },
            QsciScintilla.CallTipsNoAutoCompletionContext: {
                'name': 'CallTipsNoAutoCompletionContext',
                'display': QCoreApplication.translate('SettingEnums', "NoAutoCompletionContext")
            },
            QsciScintilla.CallTipsContext: {
                'name': 'CallTipsContext',
                'display': QCoreApplication.translate('SettingEnums', "Context")
            },
        },
        # edge modes for long lines
        QsciScintilla.EdgeMode: {
            QsciScintilla.EdgeNone: {
                'name': 'EdgeNone',
                'display': 'None'
            },
            QsciScintilla.EdgeLine: {
                'name': 'EdgeLine',
                'display': 'Line'
            },
            QsciScintilla.EdgeBackground: {
                'name': 'EdgeBackground',
                'display': 'Background'
            }
        },
        # end-of-line modes
        QsciScintilla.EolMode: {
            QsciScintilla.EolWindows: {
                'name': 'EolWindows',
                'display': 'Windows'
            },
            QsciScintilla.EolUnix: {
                'name': 'Unix',
                'display': 'Unix'
            },
            QsciScintilla.EolMac: {
                'name': 'EolMac',
                'display': 'Mac'
            }
        },
        # styles for the folding margin
        QsciScintilla.FoldStyle: {
            QsciScintilla.NoFoldStyle: {
                'name': 'NoFoldStyle',
                'display': 'No'
            },
            QsciScintilla.PlainFoldStyle: {
                'name': 'PlainFoldStyle',
                'display': 'Plain'
            },
            QsciScintilla.CircledFoldStyle: {
                'name': 'CircledFoldStyle',
                'display': 'Circled'
            },
            QsciScintilla.BoxedFoldStyle: {
                'name': 'BoxedFoldStyle',
                'display': 'Boxed'
            },
            QsciScintilla.CircledTreeFoldStyle: {
                'name': 'CircledTreeFoldStyle',
                'display': 'CircledTree'
            },
            QsciScintilla.BoxedTreeFoldStyle: {
                'name': 'BoxedTreeFoldStyle',
                'display': 'BoxedTree'
            }
        },
        # margin types
        QsciScintilla.MarginType: {
            QsciScintilla.SymbolMargin: {
                'name': 'NoFoldStyle',
                'display': 'NoFoldStyle'
            },
            QsciScintilla.SymbolMarginDefaultForegroundColor: {
                'name': 'PlainFoldStyle',
                'display': 'PlainFoldStyle'
            },
            QsciScintilla.SymbolMarginDefaultBackgroundColor: {
                'name': 'CircledFoldStyle',
                'display': 'CircledFoldStyle'
            },
            QsciScintilla.NumberMargin: {
                'name': 'BoxedFoldStyle',
                'display': 'BoxedFoldStyle'
            },
            QsciScintilla.TextMargin: {
                'name': 'CircledTreeFoldStyle',
                'display': 'CircledTreeFoldStyle'
            },
            QsciScintilla.TextMarginRightJustified: {
                'name': 'BoxedTreeFoldStyle',
                'display': 'BoxedTreeFoldStyle'
            }
        },
        # pre-defined marker symbols   #25 28 tobe added
        QsciScintilla.MarkerSymbol: {
            QsciScintilla.Circle: {
                'name': 'Circle',
                'display': 'Circle'
            },
            QsciScintilla.Rectangle: {
                'name': 'Rectangle',
                'display': 'Rectangle'
            },
            QsciScintilla.RightTriangle: {
                'name': 'RightTriangle',
                'display': 'RightTriangle'
            },
            QsciScintilla.SmallRectangle: {
                'name': 'SmallRectangle',
                'display': 'SmallRectangle'
            },
            QsciScintilla.RightArrow: {
                'name': 'RightArrow',
                'display': 'RightArrow'
            },
            QsciScintilla.Invisible: {
                'name': 'Invisible',
                'display': 'Invisible'
            },
            QsciScintilla.DownTriangle: {
                'name': 'DownTriangle',
                'display': 'DownTriangle'
            },
            QsciScintilla.Minus: {
                'name': 'Minus',
                'display': 'Minus'
            },
            QsciScintilla.Plus: {
                'name': 'Plus',
                'display': 'Plus'
            },
            QsciScintilla.VerticalLine: {
                'name': 'VerticalLine',
                'display': 'VerticalLine'
            },
            QsciScintilla.BottomLeftCorner: {
                'name': 'BottomLeftCorner',
                'display': 'BottomLeftCorner'
            },
            QsciScintilla.LeftSideSplitter: {
                'name': 'LeftSideSplitter',
                'display': 'LeftSideSplitter'
            },
            QsciScintilla.BoxedPlus: {
                'name': 'BoxedPlus',
                'display': 'BoxedPlus'
            },
            QsciScintilla.BoxedPlusConnected: {
                'name': 'BoxedPlusConnected',
                'display': 'BoxedPlusConnected'
            },
            QsciScintilla.BoxedMinus: {
                'name': 'BoxedMinus',
                'display': 'BoxedMinus'
            },
            QsciScintilla.BoxedMinusConnected: {
                'name': 'BoxedMinusConnected',
                'display': 'BoxedMinusConnected'
            },
            QsciScintilla.RoundedBottomLeftCorner: {
                'name': 'RoundedBottomLeftCorner',
                'display': 'RoundedBottomLeftCorner'
            },
            QsciScintilla.LeftSideRoundedSplitter: {
                'name': 'LeftSideRoundedSplitter',
                'display': 'LeftSideRoundedSplitter'
            },
            QsciScintilla.CircledPlus: {
                'name': 'CircledPlus',
                'display': 'CircledPlus'
            },
            QsciScintilla.CircledPlusConnected: {
                'name': 'CircledPlusConnected',
                'display': 'CircledPlusConnected'
            },
            QsciScintilla.CircledMinus: {
                'name': 'CircledMinus',
                'display': 'CircledMinus'
            },
            QsciScintilla.CircledMinusConnected: {
                'name': 'CircledMinusConnected',
                'display': 'CircledMinusConnected'
            },
            QsciScintilla.Background: {
                'name': 'Background',
                'display': 'Background'
            },
            QsciScintilla.ThreeDots: {
                'name': 'ThreeDots',
                'display': 'ThreeDots'
            },
            QsciScintilla.ThreeRightArrows: {
                'name': 'ThreeRightArrows',
                'display': 'ThreeRightArrows'
            },
            QsciScintilla.FullRectangle: {
                'name': 'FullRectangle',
                'display': 'FullRectangle'
            },
            QsciScintilla.LeftRectangle: {
                'name': 'LeftRectangle',
                'display': 'LeftRectangle'
            },
            QsciScintilla.Underline: {
                'name': 'Underline',
                'display': 'Underline'
            }
        },
        # whitespace visibility modes. When whitespace is visible spaces are
        # displayed as small centred dots and tabs are displayed as light arrows
        # pointing to the right.
        QsciScintilla.WhitespaceVisibility: {
            QsciScintilla.WsInvisible: {
                'name': 'WsInvisible',
                'display': 'Invisible'
            },
            QsciScintilla.WsVisible: {
                'name': 'WsVisible',
                'display': 'Visible'
            },
            QsciScintilla.WsVisibleAfterIndent: {
                'name': 'WsVisibleAfterIndent',
                'display': 'VisibleAfterIndent'
            }
        },
        # line wrap modes
        QsciScintilla.WrapMode: {
            QsciScintilla.WrapNone: {
                'name': 'WrapNone',
                'display': 'None'
            },
            QsciScintilla.WrapWord: {
                'name': 'WrapWord',
                'display': 'Word'
            },
            QsciScintilla.WrapCharacter: {
                'name': 'WrapCharacter',
                'display': 'Character'
            }
        },
        # line wrap visual flags
        QsciScintilla.WrapVisualFlag: {
            QsciScintilla.WrapFlagNone: {
                'name': 'WrapFlagNone',
                'display': 'None'
            },
            QsciScintilla.WrapFlagByText: {
                'name': 'WrapFlagByText',
                'display': 'ByText'
            },
            QsciScintilla.WrapFlagByBorder: {
                'name': 'WrapFlagByBorder',
                'display': 'ByBorder'
            }
        },
        # custom list for language
        'language': dict([(lang, {
            'name': lang,
            'display': lang
        }) for (lang, ext) in language_extensions]),
    }
    lookup = dict([(enumtype, dict([(enuminfo['name'], enumvalue) for (enumvalue, enuminfo) in enumvalues.items()]))
                   for (enumtype, enumvalues) in enums.items()])

    @classmethod
    def getName(cls, enumType, enumValue):
        """Return the string version of the enumeration type,
        or raise `BadEnum` if there's no such enumeration type.
        """
        # Invalid enum type or value
        if enumType not in cls.enums:
            raise EnumError(enumType)
        if enumValue not in cls.enums[enumType]:
            raise EnumError(enumValue)
        return cls.enums[enumType][enumValue]['name']

    @classmethod
    def getDisplayString(cls, enumType, enumValue):
        """Return the string display on ui for the enumeration type,
        or raise `BadEnum` if there's no such enumeration type.
        """
        # Invalid enum type or value
        if enumType not in cls.enums:
            raise EnumError(enumType)
        if enumValue not in cls.enums[enumType]:
            raise EnumError(enumValue)
        return cls.enums[enumType][enumValue]['display']

    @classmethod
    def getFromName(cls, enumType, enumName):
        """Return the Qsci.QsciScintilla enum value for the given enume Name."""
        # Invalid enum type or value
        if enumType not in cls.lookup:
            raise EnumError(enumType)
        if enumName not in cls.lookup[enumType]:
            raise EnumError(enumName)
        return cls.lookup[enumType][enumName]
