# -*- coding: utf-8 -*-
""" Language lexers and their file extensions

(Name, extensions) tuples, where <Name> must match QsciLexer<Name>

Copyright (c) 2019 lileilei <hustlei@sina.cn>
"""

import os
from PyQt5.QtCore import Qt, QVariant
from PyQt5.QtWidgets import (QWidget, QGroupBox, QVBoxLayout, QPushButton, QLabel, QHBoxLayout, QSpinBox, QCheckBox,
                             QComboBox, QColorDialog)
from settingEnums import getEnum, getEnumName, BadEnum
from lang import language_extensions

settingItems = {
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
        'label':
            'Folding',
        'type':
            'combo',
        'help':
            'What kind of icons to display for code-folding',
        'values': (
            ('None', 'NoFoldStyle'),
            ('Plain', 'PlainFoldStyle'),
            ('Circled', 'CircledFoldStyle'),
            ('Boxed', 'BoxedFoldStyle'),
            ('Circled Tree', 'CircledTreeFoldStyle'),
            ('Boxed Tree', 'BoxedTreeFoldStyle'),
        ),
    },
    'whitespaceVisibility': {
        'label':
            'Whitespace',
        'type':
            'combo',
        'help':
            'Whether whitespace is indicated with visible markers',
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
        'values': [(lang, lang) for (lang, ext) in language_extensions],
    },

    # TODO: Need a getter for this
    # 'caretWidth': {
    # 'label': 'Caret width (pixels)',
    # },

    # Stuff the user probably doesn't care about configuring
    # (or do you?)
    # 'annotationDisplay': {
    # 'label': 'Annotation Display',
    # 'type': 'combo',
    # 'values': (
    # ('Hidden', 'AnnotationHidden'),
    # ('Standard', 'AnnotationStandard'),
    # ('Boxed', 'AnnotationBoxed'),
    # ),
    # },
    # 'autoCompletionSource': {
    # 'label': 'Auto Completion Source',
    # 'type': 'combo',
    # 'values': (
    # ('None', 'AcsNone'),
    # ('All', 'AcsAll'),
    # ('Document', 'AcsDocument'),
    # ('APIs', 'AcsAPIs'),
    # ),
    # },
    # 'callTipsStyle': {
    # 'label': 'Call Tips Style',
    # 'type': 'combo',
    # 'values': (
    # ('None', 'CallTipsNone'),
    # ('No Context', 'CallTipsNoContext'),
    # ('No Auto-completion Context', 'CallTipsNoAutoCompletionContext'),
    # ('Context', 'CallTipsContext'),
    # ),
    # },
}

# Setting groups
_settingGroups = {
    'Colors': {'color', 'paper', },
    'Indentation': {'tabWidth', 'tabIndents', 'backspaceUnindents', 'autoIndent', 'indentationGuides',
                    'indentationsUseTabs', },
    'Wrapping': {'edgeMode', 'wrapMode', 'edgeColumn', },
    'Formatting': {'whitespaceVisibility', 'eolMode', 'eolVisibility', },
    'Coding aids': {'language', 'folding', 'braceMatching', },
}

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

class EditorSettings():
    """A dialog window for configuring a QsciScintilla editor."""

    def __init__(self, editor=None):
        self.previousSettings = {} # settings exist
        self.nextSettings = {} # settings changed to be applied
        # settings in toml format (all enum using name intead)
        self.tomlDictSettings = {}
        # all setting group widgets
        self.groupWidgets = {}
        if editor:
            self.editor = editor


    def defaultLayout(self):
        """Create and return the main layout for the dialog widget.
        """
        # Indexed group boxes, for easier rearrangement

        self.createWidgets()
        layout = QVBoxLayout()
        for g in self.groupWidgets.values():
            layout.addWidget(g)

        # Layout columns section and OK button vertically

        # OK button at the bottom
        ok = QPushButton('OK')
        # ok.clicked.connect(self.accept)
        layout.addWidget(ok)

        return layout

    def createWidgets(self):
        """Create widgets for setting and save them into self.settingWidgets, each widget is a QGroup"""
        for label, names in _settingGroups.items():
            self.groupWidgets[label] = QGroupBox(label)
            group_layout = QVBoxLayout()
            for name in names:
                group_layout.addLayout(self._create_widget(name))
            self.groupWidgets[label].setLayout(group_layout)
            self.groupWidgets[label].setFlat(False)

    def _create_widget(self, name):
        """Return an appropriate widget for the given configuration setting.
        """
        setting = settingItems[name]
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
        hbox = QHBoxLayout()
        hbox.addWidget(label)
        hbox.addStretch(1)
        hbox.addWidget(widget)

        return hbox

    def _create_checkbox(self, name):
        """Return a ``QCheckBox`` for the given setting."""
        checkbox = QCheckBox()

        def checkbox_changed(state):
            """Event handler for the given setting.
            """
            if state == Qt.Checked:
                self.nextSettings[name] = True
            elif state == Qt.Unchecked:
                self.nextSettings[name] = False

        checkbox.stateChanged[int].connect(checkbox_changed)

        # Set the initial checkbox state based on current getValue
        if self.previousSettings.get(name, True):
            checkbox.setCheckState(Qt.Checked)
        else:
            checkbox.setCheckState(Qt.Unchecked)

        return checkbox

    def _create_combobox(self, name):
        """Return a combobox for modifying a multiple-getValue setting."""
        setting = settingItems[name]
        # Create the combobox and populate it
        combo = QComboBox()
        for label, value in setting['values']:
            data = QVariant(value)
            combo.addItem(label, data)

        # Set the initial getValue, if any
        current = self.previousSettings.get(name, setting['values'][0][1])
        index = combo.findData(current)
        combo.setCurrentIndex(index)

        # Ugly event handler!
        def combo_changed(index):
            data = combo.itemData(index)
            value = str(data)  # .toString())
            self.nextSettings[name] = value

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
            current_color = self.previousSettings.get(name, Qt.white)
            color = QColorDialog.getColor(current_color)
            button.setStyleSheet("background-color: %s" % color.name())
            self.nextSettings[name] = color

        # Connect event handler
        button.pressed.connect(button_pressed)

        # Set default background color
        color = self.previousSettings.get(name, Qt.white)
        button.setStyleSheet("background-color: %s" % color)

        return button

    def _create_number_box(self, name):
        """Return a numeric entry widget for a numeric setting.
        """
        spinbox = QSpinBox()

        # Set initial getValue
        spinbox.setValue(self.previousSettings.get(name, 5))

        def spinbox_changed(value):
            self.nextSettings[name] = value

        # Connect event handler
        spinbox.valueChanged[int].connect(spinbox_changed)

        return spinbox

    def _create_line_number_checkbox(self):
        """Return a widget for enabling/disabling line numbers."""

        # Line numbers
        def checkbox_changed(state):
            """Event handler for the given setting.
            """
            if state == Qt.Checked:
                self.nextSettings['marginLineNumbers'] = True
            elif state == Qt.Unchecked:
                self.nextSettings['marginLineNumbers'] = False

        # Create the checkbox and connect the event handler
        checkbox = QCheckBox('Line numbers', self)
        checkbox.stateChanged[int].connect(checkbox_changed)

        # Set the initial checkbox state based on current getValue
        if self.previousSettings['marginLineNumbers']:
            checkbox.setCheckState(Qt.Checked)
        else:
            checkbox.setCheckState(Qt.Unchecked)

        return checkbox


if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    import sys
    from editor import Editor

    app = QApplication(sys.argv)
    win = QWidget()
    layout=QHBoxLayout()
    win.setLayout(layout)
    ed = Editor()
    d = QWidget(win)
    d.setLayout(EditorSettings(ed).defaultLayout())
    layout.addWidget(ed)
    layout.addWidget(d)
    win.show()
    sys.exit(app.exec_())
