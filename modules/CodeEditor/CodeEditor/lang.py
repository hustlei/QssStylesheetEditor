# -*- coding: utf-8 -*-
"""Language and code file extensions

language_extensions is (Name, extensions) tuples, where <Name> must match QsciLexer<Name>

"""

import os

language_extensions = (
    # ('None', '.txt .text'),
    ('Text', '.txt .text'),
    ('QSS', '.qss .qsst'),
    ('Bash', '.sh .bashrc .bash_history'),
    ('Batch', '.bat .cmd'),
    ('CMake', '.cmake'),
    ('CPP', '.c++ .cpp .cxx .cc .hh .hxx .hpp .c .h'),
    ('CSharp', '.cs'),
    ('CSS', '.css'),
    ('CoffeeScript', '.coffee'),
    ('D', '.d'),
    ('Diff', '.diff'),
    ('Fortran', '.f'),
    ('Fortran77', '.f77 .f90'),
    ('HTML', '.html'),
    ('IDL', '.idl'),
    ('JSON', '.json'),
    ('Java', '.java'),
    ('JavaScript', '.js'),
    ('Lua', '.lua'),
    ('Makefile', '.make .mk .makefile'),
    ('Markdown', '.md .markdown'),
    ('Matlab', '.m'),
    ('Pascal', '.pas'),
    ('Perl', '.pl'),
    ('PostScript', '.ps .eps .ai'),
    ('POV', '.pov'),
    ('Properties', '.properties'),
    ('Python', '.py .pyw'),
    ('Ruby', '.rb'),
    ('SQL', '.sql'),
    ('TCL', '.tcl'),
    ('TeX', '.tex .latex'),
    ('VHDL', '.vhd .vhdl'),
    ('Verilog', '.v'),
    ('XML', '.xml .svg'),
    ('YAML', '.yaml .yml'),
)


def guessLang(filename):
    """Guess the language based on the given filename's extension, and return name of the language,
     or the string 'None' if no extension matches.
    """
    _, ext = os.path.splitext(filename)

    for language, extensions in language_extensions:
        if ext in extensions.split(' '):
            return language

    # No match -- asume plain text
    return "None"
