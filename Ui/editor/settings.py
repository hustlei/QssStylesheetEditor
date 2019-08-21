# Language lexers and their file extensions
# (Name, extensions) tuples, where <Name> must match
# QsciLexer<Name>
language_extensions = (
    ('None', '.txt'),
    #('Custom', ''),
    ('Bash', '.sh .bashrc .bash_history'),
    ('Batch', '.bat .cmd'),
    ('CMake', '.cmake'),
    ('CPP', '.c++ .cpp .cxx .cc .hh .hxx .hpp .c .h'),
    ('CSharp', '.cs'),
    ('CSS', '.css .qss .qsst'),
    ('CoffeeScript','.coffee'),
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

_settings = {
    # Boolean settings
    'tabIndents': {
        'label': 'Tab indents',
        'type': 'bool',
        'help': 'Use the tab key to indent text',
    },
    'backspaceUnindents': {
        'label': 'Backspace unindents',
        'type': 'bool',
        'help': 'Backspace will unindent a line instead of just deleting a character',
    },
    'autoIndent': {
        'label': 'Auto-indent',
        'type': 'bool',
        'help': 'Automatically indent text to match the preceding line',
    },
    'indentationGuides': {
        'label': 'Indentation guides',
        'type': 'bool',
        'help': 'Display visible guidelines to help keep indentation consistent',
    },
    'indentationsUseTabs': {
        'label': 'Use tab character',
        'type': 'bool',
        'help': 'Tab key inserts an actual tab character instead of spaces',
    },
    'eolVisibility': {
        'label': 'Show CR/LF',
        'type': 'bool',
        'help': 'Display a visible icon for carriage return and line feeds',
    },

    # Color settings
    'color': {
        'label': 'Text color',
        'type': 'color',
    },
    'paper': {
        'label': 'Paper color',
        'type': 'color',
    },

    # Numeric settings
    'edgeColumn': {
        'label': 'Text width',
        'type': 'number',
        'help': 'Number of characters per line before wrapping occurs',
    },
    'tabWidth': {
        'label': 'Tab width',
        'type': 'number',
        'help': 'Width of tabs in characters, or the number of'
            ' spaces to insert when tab is pressed',
    },

    # Multiple-selection settings
    'braceMatching': {
        'label': 'Brace Matching',
        'type': 'combo',
        'help': 'Whether and how to highlight matching {} [] () braces',
        'values': (
            ('None', 'NoBraceMatch'),
            ('Strict', 'StrictBraceMatch'),
            ('Sloppy', 'SloppyBraceMatch'),
        ),
    },
    'edgeMode': {
        'label': 'Edge Mode',
        'type': 'combo',
        'help': 'How the edge of the text width is indicated',
        'values': (
            ('None', 'EdgeNone'),
            ('Line', 'EdgeLine'),
            ('Background', 'EdgeBackground'),
        ),
    },
    'eolMode': {
        'label': 'Line Endings',
        'type': 'combo',
        'help': 'End lines with carriage return and/or line feed',
        'values': (
            ('Windows', 'EolWindows'),
            ('Unix', 'EolUnix'),
            ('Mac', 'EolMac'),
        ),
    },
    'folding': {
        'label': 'Folding',
        'type': 'combo',
        'help': 'What kind of icons to display for code-folding',
        'values': (
            ('None', 'NoFoldStyle'),
            ('Plain','PlainFoldStyle'),
            ('Circled', 'CircledFoldStyle'),
            ('Boxed', 'BoxedFoldStyle'),
            ('Circled Tree', 'CircledTreeFoldStyle'),
            ('Boxed Tree', 'BoxedTreeFoldStyle'),
        ),
    },
    'whitespaceVisibility': {
        'label': 'Whitespace',
        'type': 'combo',
        'help': 'Whether whitespace is indicated with visible markers',
        'values': (
            ('Invisible', 'WsInvisible'),
            ('Visible', 'WsVisible'),
            ('Visible After Indent', 'WsVisibleAfterIndent'),
        ),
    },
    'wrapMode': {
        'label': 'Wrap Mode',
        'type': 'combo',
        'help': 'How to wrap text when it reaches the text width',
        'values': (
            ('None', 'WrapNone'),
            ('Word', 'WrapWord'),
            ('Character', 'WrapCharacter'),
        ),
    },
    'language': {
        'label': 'Language',
        'type': 'combo',
        'help': 'Syntax highlighting language',
        'values': [
            (lang, lang) for (lang, ext) in language_extensions
        ],
    },

    # TODO: Need a getter for this
    # 'caretWidth': {
        #'label': 'Caret width (pixels)',
    #},

    # Stuff the user probably doesn't care about configuring
    # (or do you?)
    # 'annotationDisplay': {
        #'label': 'Annotation Display',
        #'type': 'combo',
        #'values': (
            #('Hidden', 'AnnotationHidden'),
            #('Standard', 'AnnotationStandard'),
            #('Boxed', 'AnnotationBoxed'),
        #),
    #},
    # 'autoCompletionSource': {
        #'label': 'Auto Completion Source',
        #'type': 'combo',
        #'values': (
            #('None', 'AcsNone'),
            #('All', 'AcsAll'),
            #('Document', 'AcsDocument'),
            #('APIs', 'AcsAPIs'),
        #),
    #},
    # 'callTipsStyle': {
        #'label': 'Call Tips Style',
        #'type': 'combo',
        #'values': (
            #('None', 'CallTipsNone'),
            #('No Context', 'CallTipsNoContext'),
            #('No Auto-completion Context', 'CallTipsNoAutoCompletionContext'),
            #('Context', 'CallTipsContext'),
        #),
    #},

}

# Setting groups
_setting_groups = (
    ('Colors',
        (
            'color',
            'paper',
        )
    ),

    ('Indentation',
        (
            'tabWidth',
            'tabIndents',
            'backspaceUnindents',
            'autoIndent',
            'indentationGuides',
            'indentationsUseTabs',
        )
    ),

    ('Wrapping',
        (
            'edgeMode',
            'wrapMode',
            'edgeColumn',
        )
    ),

    ('Formatting',
        (
            'whitespaceVisibility',
            'eolMode',
            'eolVisibility',
        )
    ),

    ('Coding aids',
        (
            'language',
            'folding',
            'braceMatching',
        )
    ),
)


# Write-only color settings.
# FIXME: Can't effectively include these until getters are written.
_other_color_settings = (
    # Selection
    'selectionForegroundColor',
    'selectionBackgroundColor',
    # Caret (current line)
    'caretForegroundColor',
    'caretLineBackgroundColor',
    # Edge marker
    'edgeColor',
    # Indentation guides
    'indentationGuidesForegroundColor',
    'indentationGuidesBackgroundColor',
    # Brace matching
    'matchedBraceForegroundColor',
    'matchedBraceBackgroundColor',
    'unmatchedBraceForegroundColor',
    'unmatchedBraceBackgroundColor',
    # Marker colors
    'markerForegroundColor',
    'markerBackgroundColor',
    # Margins
    'marginsForegroundColor',
    'marginsBackgroundColor',
    # CallTips
    'callTipsForegroundColor',
    'callTipsBackgroundColor',
    'callTipsHighlightColor',
)

import os
from PyQt5 import QtGui
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import  Qt,QVariant

class EditorSettings (QDialog):
    """A dialog window for configuring a QsciScintilla editor.
    """
    def __init__(self, editor):
        QDialog.__init__(self, editor)
        self.editor = editor

        layout = self._create_layout()
        self.setLayout(layout)

    def guess_language(cls, filename):
        """Guess the language based on the given filename's extension, and return
        the name of the language, or the string 'None' if no extension matches.
        """
        # Get the file's extension
        root, ext = os.path.splitext(filename)
        # See if any known language extensions match
        for language, extensions in language_extensions:
            if ext in extensions.split(' '):
                return language

        # No match -- asume plain text
        return 'None'


    def _create_layout(self):
        """Create and return the main layout for the dialog widget.
        """
        # Indexed group boxes, for easier rearrangement
        groups = {}

        # Create and populate each group
        for label, names in _setting_groups:
            groups[label] = QGroupBox(label)
            group_layout = QVBoxLayout()
            for name in names:
                group_layout.addLayout(self._create_widget(name))
            groups[label].setLayout(group_layout)
            groups[label].setFlat(False)

        # Create two columns
        left_column = QVBoxLayout()
        left_column.addWidget(groups['Indentation'])
        left_column.addWidget(groups['Wrapping'])
        left_column.addStretch(1)
        right_column = QVBoxLayout()
        right_column.addWidget(groups['Formatting'])
        right_column.addWidget(groups['Colors'])
        right_column.addWidget(groups['Coding aids'])
        right_column.addStretch(1)

        # Arrange both columns side-by-side in the middle
        columns_layout = QHBoxLayout()
        columns_layout.addLayout(left_column)
        columns_layout.addLayout(right_column)

        # Layout columns section and OK button vertically
        main_layout = QVBoxLayout()
        main_layout.addLayout(columns_layout)

        # OK button at the bottom
        ok = QPushButton('OK', self)
        ok.clicked.connect(self.accept)
        main_layout.addWidget(ok)

        return main_layout


    def _create_widget(self, name):
        """Return an appropriate widget for the given configuration setting.
        """
        setting = _settings[name]
        type_ = setting['type']

        # Get the appropriate widget type
        if type_ == 'bool':
            widget = self._create_checkbox(name)
        elif type_ == 'number':
            widget = self._create_number_box(name)
        elif type_ == 'combo':
            widget = self._create_combobox(name)
        elif type_ == 'color':
            widget = self._create_color_picker(name)


        # Label with possible tooltip
        label = QLabel(setting['label'])

        # Add tooltip to widget
        if 'help' in setting:
            widget.setToolTip(setting['help'])

        # Add label and widget
        layout = QHBoxLayout()
        layout.addWidget(label)
        layout.addStretch(1)
        layout.addWidget(widget)

        return layout


    def _create_checkbox(self, name):
        """Return a ``QCheckBox`` for the given setting.
        """
        checkbox = QCheckBox(self)

        def checkbox_changed(state):
            """Event handler for the given setting.
            """
            if state == Qt.Checked:
                self.editor.set_config(name, True)
            elif state == Qt.Unchecked:
                self.editor.set_config(name, False)

        checkbox.stateChanged[int].connect(checkbox_changed)

        # Set the initial checkbox state based on current getValue
        if self.editor.get_config(name):
            checkbox.setCheckState(Qt.Checked)
        else:
            checkbox.setCheckState(Qt.Unchecked)

        return checkbox


    def _create_combobox(self, name):
        """Return a combobox for modifying a multiple-getValue setting.
        """
        setting = _settings[name]
        # Create the combobox and populate it
        combo = QComboBox(self)
        for label, value in setting['values']:
            data = QVariant(value)
            combo.addItem(label, data)

        # Set the initial getValue, if any
        current = self.editor.get_config(name)
        index = combo.findData(current)
        combo.setCurrentIndex(index)

        # Ugly event handler!
        def combo_changed(index):
            data = combo.itemData(index)
            value = str(data.toString())
            self.editor.set_config(name, value)

        # Connect event handler
        combo.currentIndexChanged[int].connect(combo_changed)

        return combo


    def _create_color_picker(self, name):
        """Return a color-picker widget for a color-based setting.
        """
        # Button with colored background
        button = QPushButton()

        # Event handler
        def button_pressed():
            current_color = self.editor.get_config(name)
            color = QColorDialog.getColor(current_color)
            button.setStyleSheet("background-color: %s" % color.getName())
            self.editor.set_config(name, color)

        # Connect event handler
        button.pressed.connect(button_pressed)

        # Set default background color
        color = self.editor.get_config(name)
        button.setStyleSheet("background-color: %s" % color.getName())

        return button


    def _create_number_box(self, name):
        """Return a numeric entry widget for a numeric setting.
        """
        spinbox = QSpinBox()

        # Set initial getValue
        spinbox.setValue(self.editor.get_config(name))

        def spinbox_changed(value):
            self.editor.set_config(name, value)

        # Connect event handler
        spinbox.valueChanged[int].connect(spinbox_changed)

        return spinbox


    def _create_line_number_checkbox(self):
        """Return a widget for enabling/disabling line numbers.
        """
        # Line numbers
        def checkbox_changed(state):
            """Event handler for the given setting.
            """
            if state == Qt.Checked:
                self.editor.set_config('marginLineNumbers', (0, True))
            elif state == Qt.Unchecked:
                self.editor.set_config('marginLineNumbers', (0, False))

        # Create the checkbox and connect the event handler
        checkbox = QCheckBox('Line numbers', self)
        checkbox.stateChanged[int].connect(checkbox_changed)

        # Set the initial checkbox state based on current getValue
        if self.editor.get_config('marginLineNumbers', 0):
            checkbox.setCheckState(Qt.Checked)
        else:
            checkbox.setCheckState(Qt.Unchecked)

        return checkbox

if __name__=="__main__":
    from PyQt5.QtWidgets import *
    import sys
    
    from Editor import CodeEditor
    app=QApplication(sys.argv)
    win=QWidget()
    ed=CodeEditor()
    layout=QVBoxLayout()
    d=EditorSettings(ed)
    layout.addWidget(d)
    d.show()
    win.show()
    sys.exit(app.exec_())