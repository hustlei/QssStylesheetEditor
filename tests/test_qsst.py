# -*- coding: utf-8 -*-
"""test for qsst module.

Copyright (c) 2019 lileilei <hustlei@sina.cn>
"""

from pytest import fixture


@fixture
def qsst():
    from qss_template import Qsst
    obj = Qsst()
    obj.srctext = '''
    $text = black;
    QWidget{
        color: $text;
        background: $background;
    }
    '''
    return obj


def test_loadvars(qsst):
    qsst.loadVars()
    assert "text" in qsst.varDict
    assert "text" in qsst.varUsed
    assert "background" in qsst.varUndefined
    assert qsst.varDict["text"] == "black"


def test_writevars(qsst):
    qsst.loadVars()
    qsst.varDict['new'] = 'new'
    qsst.writeVars()
    assert "new" not in qsst.varDict
    assert '$new = new;' not in qsst.srctext


def test_convertqss(qsst):
    qsst.loadVars()
    qsst.convertQss()
    rst = '''
    QWidget{
        color: black;
        background: ;
    }
    '''
    assert qsst.qss.strip() == rst.strip()
