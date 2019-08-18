# enums.py

"""Wrapper for Qsci.QsciScintilla enumerations.
"""
from PyQt5.Qsci import QsciScintilla


QsciTypes = {
    # annotation display styles
    QsciScintilla.AnnotationDisplay: (
        ('AnnotationHidden', QsciScintilla.AnnotationHidden),
        ('AnnotationStandard', QsciScintilla.AnnotationStandard),
        ('AnnotationBoxed', QsciScintilla.AnnotationBoxed),
    ),

    # sources for auto-completion lists.
    QsciScintilla.AutoCompletionSource: (
        ('AcsNone', QsciScintilla.AcsNone),
        ('AcsAll', QsciScintilla.AcsAll),
        ('AcsDocument', QsciScintilla.AcsDocument),
        ('AcsAPIs', QsciScintilla.AcsAPIs),
    ),

    # brace matching modes. The character pairs (), [] and () are treated as
    # braces. The Python lexer will also match a : with the end of the
    # corresponding indented block.
    QsciScintilla.BraceMatch: (
        ('NoBraceMatch', QsciScintilla.NoBraceMatch),
        ('StrictBraceMatch', QsciScintilla.StrictBraceMatch),
        ('SloppyBraceMatch', QsciScintilla.SloppyBraceMatch),
    ),

    # call tip styles
    QsciScintilla.CallTipsStyle: (
        ('CallTipsNone', QsciScintilla.CallTipsNone),
        ('CallTipsNoContext', QsciScintilla.CallTipsNoContext),
        ('CallTipsNoAutoCompletionContext', QsciScintilla.CallTipsNoAutoCompletionContext),
        ('CallTipsContext', QsciScintilla.CallTipsContext),
    ),

    # edge modes for long lines
    QsciScintilla.EdgeMode: (
        ('EdgeNone', QsciScintilla.EdgeNone),
        ('EdgeLine', QsciScintilla.EdgeLine),
        ('EdgeBackground', QsciScintilla.EdgeBackground),
    ),

    # end-of-line modes
    QsciScintilla.EolMode: (
        ('EolWindows', QsciScintilla.EolWindows),
        ('EolUnix', QsciScintilla.EolUnix),
        ('EolMac', QsciScintilla.EolMac),
    ),

    # styles for the folding margin
    QsciScintilla.FoldStyle: (
        ('NoFoldStyle', QsciScintilla.NoFoldStyle),
        ('PlainFoldStyle', QsciScintilla.PlainFoldStyle),
        ('CircledFoldStyle', QsciScintilla.CircledFoldStyle),
        ('BoxedFoldStyle', QsciScintilla.BoxedFoldStyle),
        ('CircledTreeFoldStyle', QsciScintilla.CircledTreeFoldStyle),
        ('BoxedTreeFoldStyle', QsciScintilla.BoxedTreeFoldStyle),
    ),

    # margin types
    QsciScintilla.MarginType: (
        ('SymbolMargin', QsciScintilla.SymbolMargin),
        ('SymbolMarginDefaultForegroundColor', QsciScintilla.SymbolMarginDefaultForegroundColor),
        ('SymbolMarginDefaultBackgroundColor', QsciScintilla.SymbolMarginDefaultBackgroundColor),
        ('NumberMargin', QsciScintilla.NumberMargin),
        ('TextMargin', QsciScintilla.TextMargin),
        ('TextMarginRightJustified', QsciScintilla.TextMarginRightJustified),
    ),

    # pre-defined marker symbols
    QsciScintilla.MarkerSymbol: (
        ('Circle', QsciScintilla.Circle),
        ('Rectangle', QsciScintilla.Rectangle),
        ('RightTriangle', QsciScintilla.RightTriangle),
        ('SmallRectangle', QsciScintilla.SmallRectangle),
        ('RightArrow', QsciScintilla.RightArrow),
        ('Invisible', QsciScintilla.Invisible),
        ('DownTriangle', QsciScintilla.DownTriangle),
        ('Minus', QsciScintilla.Minus),
        ('Plus', QsciScintilla.Plus),
        ('VerticalLine', QsciScintilla.VerticalLine),
        ('BottomLeftCorner', QsciScintilla.BottomLeftCorner),
        ('LeftSideSplitter', QsciScintilla.LeftSideSplitter),
        ('BoxedPlus', QsciScintilla.BoxedPlus),
        ('BoxedPlusConnected', QsciScintilla.BoxedPlusConnected),
        ('BoxedMinus', QsciScintilla.BoxedMinus),
        ('BoxedMinusConnected', QsciScintilla.BoxedMinusConnected),
        ('RoundedBottomLeftCorner', QsciScintilla.RoundedBottomLeftCorner),
        ('LeftSideRoundedSplitter', QsciScintilla.LeftSideRoundedSplitter),
        ('CircledPlus', QsciScintilla.CircledPlus),
        ('CircledPlusConnected', QsciScintilla.CircledPlusConnected),
        ('CircledMinus', QsciScintilla.CircledMinus),
        ('CircledMinusConnected', QsciScintilla.CircledMinusConnected),
        ('Background', QsciScintilla.Background),
        ('ThreeDots', QsciScintilla.ThreeDots),
        ('ThreeRightArrows', QsciScintilla.ThreeRightArrows),
        #('FullRectangle', QsciScintilla.FullRectangle),
        #('LeftRectangle', QsciScintilla.LeftRectangle),
        #('Underline', QsciScintilla.Underline),
    ),

    # whitespace visibility modes. When whitespace is visible spaces are
    # displayed as small centred dots and tabs are displayed as light arrows
    # pointing to the right.
    QsciScintilla.WhitespaceVisibility: (
        ('WsInvisible', QsciScintilla.WsInvisible),
        ('WsVisible', QsciScintilla.WsVisible),
        ('WsVisibleAfterIndent', QsciScintilla.WsVisibleAfterIndent),
    ),

    # line wrap modes
    QsciScintilla.WrapMode: (
        ('WrapNone', QsciScintilla.WrapNone),
        ('WrapWord', QsciScintilla.WrapWord),
        ('WrapCharacter', QsciScintilla.WrapCharacter),
    ),

    # line wrap visual flags
    QsciScintilla.WrapVisualFlag: (
        ('WrapFlagNone', QsciScintilla.WrapFlagNone),
        ('WrapFlagByText', QsciScintilla.WrapFlagByText),
        ('WrapFlagByBorder', QsciScintilla.WrapFlagByBorder),
    ),
}

# Just the enumeration names (strings)
QsciEnumDict = dict(
    (name, value)
    for name_values in QsciTypes.values()
    for (name, value) in name_values
)

class BadQsciEnum (Exception):
    """Bad (unknown or failed) enumeration name.
    """
    def __init__(self, name):
        super(BadQsciEnum, self).__init__("Enumeration unknown: '%s'" % name)


def enum_value(enum_name):
    """Return the Qsci.QsciScintilla value for the given enumeration name.
    """
    if enum_name not in QsciEnumDict:
        raise BadQsciEnum(enum_name)
    else:
        return QsciEnumDict[enum_name]


def enum_string(enum_value):
    """Return the string version of the given enumeration value,
    or raise `BadEnum` if there's no such enumeration value.
    """
    enum_type = type(enum_value)

    # Invalid enum type?
    if enum_type not in QsciTypes:
        raise BadQsciEnum(enum_value)

    # Construct a lookup table indexed by enumeration value
    lookup = dict((value, name) for (name, value) in QsciTypes[enum_type])

    # Invalid enum value?
    if enum_value not in lookup:
        raise BadQsciEnum(enum_value)

    return lookup[enum_value]