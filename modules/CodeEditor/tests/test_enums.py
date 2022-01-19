from PyQt5.Qsci import QsciScintilla
from setting_enums import SettingEnums

def test_basic():
    # test enums
    assert SettingEnums.enums[QsciScintilla.AnnotationDisplay][QsciScintilla.AnnotationHidden]['name'] == "AnnotationHidden"
    assert type(SettingEnums.enums[QsciScintilla.AnnotationDisplay][QsciScintilla.AnnotationHidden]['display']) == str
    # test lookup
    assert SettingEnums.lookup[QsciScintilla.AnnotationDisplay]['AnnotationHidden'] == QsciScintilla.AnnotationHidden
    # test getName
    assert SettingEnums.getName(QsciScintilla.AutoCompletionSource,QsciScintilla.AcsNone) == "AcsNone"
    # test getDisplay
    assert SettingEnums.getDisplayString(QsciScintilla.AutoCompletionSource, QsciScintilla.AcsNone) == "None"
    # test getFromName
    assert SettingEnums.getFromName(QsciScintilla.AutoCompletionSource,"AcsNone") == QsciScintilla.AcsNone

    # test for language
    assert SettingEnums.getName('language',"Python") == 'Python'
    assert SettingEnums.getFromName('language',"Python") == 'Python'
    assert SettingEnums.getDisplayString('language',"Python") == 'Python'
