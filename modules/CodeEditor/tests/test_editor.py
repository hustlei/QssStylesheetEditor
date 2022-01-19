

def test_editor(editor):
    # test config
    editor.setConfig('edgeColumn', 10)
    assert editor.getConfig('edgeColumn') == 10
    editor.configure(EdgeColumn=20)
    assert editor.getConfig('EdgeColumn') == 20
    # test information
    editor.setText("first line\nsecond line.")
    assert editor.lines() == 2
    assert editor.count("line") == 2
    # test lang
    editor.setLanguage("QSS")
    assert editor.language() == "QSS"
    editor.setLanguage("Python")
    assert editor.language() == "Python"



