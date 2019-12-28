# -*- coding: utf-8 -*-
""" Language lexers and their file extensions

(Name, extensions) tuples, where <Name> must match QsciLexer<Name>

Copyright (c) 2019 lileilei <hustlei@sina.cn>
"""

import os
from PyQt5.QtCore import Qt, QVariant, QCoreApplication
from PyQt5.QtGui import QColor, QPalette, QFont
from PyQt5.QtWidgets import (QWidget, QGroupBox, QVBoxLayout, QPushButton, QLabel, QHBoxLayout, QSpinBox, QCheckBox,
                             QComboBox, QColorDialog, QFontComboBox)
from PyQt5.Qsci import QsciScintilla
from .setting_enums import EnumError, SettingEnums


class EditorSettings():
    """A dialog window for configuring a QsciScintilla editor."""
    settingItems = {
        # Boolean settings
        'tabIndents': {
            'type': 'bool',
            'label': QCoreApplication.translate('EditorSettings', 'Tab indents'),
            'help': QCoreApplication.translate('EditorSettings', 'Use the tab key to indent text'),
        },
        'backspaceUnindents': {
            'type': 'bool',
            'label': QCoreApplication.translate('EditorSettings', 'Backspace unindents'),
            'help': QCoreApplication.translate('EditorSettings',
                                               'Backspace will unindent a line instead of just deleting a character'),
        },
        'autoIndent': {
            'type': 'bool',
            'label': QCoreApplication.translate('EditorSettings', 'Auto-indent'),
            'help': QCoreApplication.translate('EditorSettings',
                                               'Automatically indent text to match the preceding line'),
        },
        'indentationGuides': {
            'type': 'bool',
            'label': QCoreApplication.translate('EditorSettings', 'Indentation guides'),
            'help': QCoreApplication.translate('EditorSettings',
                                               'Display visible guidelines to help keep indentation consistent'),
        },
        'indentationsUseTabs': {
            'type': 'bool',
            'label': QCoreApplication.translate('EditorSettings', 'Use tab character'),
            'help': QCoreApplication.translate('EditorSettings',
                                               'Tab key inserts an actual tab character instead of spaces'),
        },
        'eolVisibility': {
            'type': 'bool',
            'label': QCoreApplication.translate('EditorSettings', 'Show CR/LF'),
            'help': QCoreApplication.translate('EditorSettings',
                                               'Display a visible icon for carriage return and line feeds'),
        },

        # Color settings
        'color': {
            'type': 'color',
            'label': QCoreApplication.translate('EditorSettings', 'Text color'),
            'help': QCoreApplication.translate('EditorSettings',
                                               'Default text color'),
        },
        'paper': {
            'type': 'color',
            'label': QCoreApplication.translate('EditorSettings', 'Paper color'),
            'help': QCoreApplication.translate('EditorSettings',
                                               'Default background color'),
        },
        'fontFamily': {
            'type': 'fontfamily',
            'label': QCoreApplication.translate('EditorSettings', 'Font Family'),
            'help': QCoreApplication.translate('EditorSettings',
                                               'Default font family'),
        },
        'fontSize': {
            'type': 'number',
            'label': QCoreApplication.translate('EditorSettings', 'Font Size'),
            'help': QCoreApplication.translate('EditorSettings',
                                               'Default font size'),
        },
        # Numeric settings
        'edgeColumn': {
            'type': 'number',
            'label': QCoreApplication.translate('EditorSettings', 'Text width'),
            'help': QCoreApplication.translate('EditorSettings',
                                               'Number of characters per line before wrapping occurs'),
        },
        'tabWidth': {
            'type': 'number',
            'label': QCoreApplication.translate('EditorSettings', 'Tab width'),
            'help': QCoreApplication.translate('EditorSettings',
                                               'Width of tabs in characters, or the number of spaces to insert when tab is pressed'),
        },

        # Multiple-selection settings
        'braceMatching': {
            'type': 'combo',
            'valuetype': QsciScintilla.BraceMatch,
            'label': QCoreApplication.translate('EditorSettings', 'Brace Matching'),
            'help': QCoreApplication.translate('EditorSettings',
                                               'Whether and how to highlight matching {} [] () braces'),
        },
        'edgeMode': {
            'type': 'combo',
            'valuetype': QsciScintilla.EdgeMode,
            'label': QCoreApplication.translate('EditorSettings', 'Edge Mode'),
            'help': QCoreApplication.translate('EditorSettings', 'How the edge of the text width is indicated'),
        },
        'eolMode': {
            'type': 'combo',
            'valuetype': QsciScintilla.EolMode,
            'label': QCoreApplication.translate('EditorSettings', 'Line Endings'),
            'help': QCoreApplication.translate('EditorSettings', 'End lines with carriage return and/or line feed'),
        },
        'folding': {
            'type': 'combo',
            'valuetype': QsciScintilla.FoldStyle,
            'label': QCoreApplication.translate('EditorSettings', 'Folding'),
            'help': QCoreApplication.translate('EditorSettings', 'What kind of icons to display for code-folding')
        },
        'whitespaceVisibility': {
            'type': 'combo',
            'valuetype': QsciScintilla.WhitespaceVisibility,
            'label': QCoreApplication.translate('EditorSettings', 'Whitespace'),
            'help': QCoreApplication.translate('EditorSettings', 'Whether whitespace is indicated with visible markers')
        },
        'wrapMode': {
            'type': 'combo',
            'valuetype': QsciScintilla.WrapMode,
            'label': QCoreApplication.translate('EditorSettings', 'Wrap Mode'),
            'help': QCoreApplication.translate('EditorSettings', 'How to wrap text when it reaches the text width')
        },
        'language': {
            'type': 'combo',
            'valuetype': 'language',
            'label': QCoreApplication.translate('EditorSettings', 'Language'),
            'help': QCoreApplication.translate('EditorSettings', 'Syntax highlighting language'),
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
    settingGroups = {
        'Colors': {'label': QCoreApplication.translate('EditorSettings', 'Colors'),
                   'items': {'color', 'paper', }},
        'Text':{'label': QCoreApplication.translate('EditorSettings', 'Text'),
                   'items': {'fontFamily', 'fontSize', }},
        'Indentation': {'label': QCoreApplication.translate('EditorSettings', 'Indentation'),
                        'items': {'tabWidth', 'tabIndents', 'backspaceUnindents', 'autoIndent', 'indentationGuides',
                                  'indentationsUseTabs', }},
        'Wrapping': {'label': QCoreApplication.translate('EditorSettings', 'Wrapping'),
                     'items': {'edgeMode', 'wrapMode', 'edgeColumn', }},
        'Formatting': {'label': QCoreApplication.translate('EditorSettings', 'Formatting'),
                       'items': {'whitespaceVisibility', 'eolMode', 'eolVisibility', }},
        'Coding aids': {'label': QCoreApplication.translate('EditorSettings', 'Coding aids'),
                        'items': {'language', 'folding', 'braceMatching', }},
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

    def __init__(self, editor=None):
        self.currentSettings = {}  # settings exist
        self.changedSettings = {}  # settings changed to be applied
        self.updateActions = {}
        # all setting group widgets
        self.groupWidgets = {}
        self.editor = editor

    def loadFromEditor(self):
        for item in self.settingItems:
            self.currentSettings[item] = self.editor.getConfig(item)

        self.updateUi(self.currentSettings)

    def loadFromTomlDict(self, tomldict):
        """
        :param tomldict: settings dict load form toml config file, all colors and enums are using name string insteaded in tomldict
        """
        for name, value in tomldict:
            self.currentSettings[name] = value
            if isinstance(value, str) and name in self.settingItems:
                if self.settingItems[name][type] == 'color':
                    self.currentSettings[name] = QColor(value)
                elif self.settingItems[name][type] == 'combo':
                    self.currentSettings[name] = SettingEnums.getFromName(self.settingItems[name]['valuetype'], name)
        self.updateUi(self.currentSettings)

    def defaultLayout(self):
        """Create and return the main layout for the dialog widget.
        """
        # Indexed group boxes, for easier rearrangement

        self.createWidgets()
        layout = QVBoxLayout()
        for g in self.groupWidgets.values():
            layout.addWidget(g)
        self.loadFromEditor()
        return layout

    def createWidgets(self):
        """Create widgets for setting and save them into self.settingWidgets, each widget is a QGroup"""
        for values in self.settingGroups.values():
            label = values['label']
            names = values['items']
            self.groupWidgets[label] = QGroupBox(label)
            group_layout = QVBoxLayout()
            for name in names:
                group_layout.addLayout(self._create_widget(name))
            self.groupWidgets[label].setLayout(group_layout)
            self.groupWidgets[label].setFlat(False)

    def _create_widget(self, name):
        """Return an appropriate widget for the given configuration setting.
        """
        setting = self.settingItems[name]
        type_ = setting['type']

        # Get the appropriate widget type
        if type_ == 'bool':
            widget = self._create_checkbox(name)
        elif type_ == 'number':
            widget = self._create_number_box(name)
        elif type_ == 'combo':
            widget = self._create_combobox(name)
        elif type_ == 'fontfamily':
            widget = self._create_fontcombobox(name)
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
            if state == Qt.Checked:
                self.changedSettings[name] = True
            elif state == Qt.Unchecked:
                self.changedSettings[name] = False

        checkbox.stateChanged[int].connect(checkbox_changed)

        def checkbox_update(value):
            if value:
                checkbox.setChecked(True)  # checkbox.setCheckState(Qt.Checked)
            else:
                checkbox.setChecked(False)  # checkbox.setCheckState(Qt.Unchecked)

        self.updateActions[name] = checkbox_update

        # Set the initial checkbox state based on current getValue
        # checkbox_update(self.currentSettings.get(name, True))
        return checkbox

    def _create_number_box(self, name):
        """Return a numeric entry widget for a numeric setting.
        """
        spinbox = QSpinBox()
        spinbox.setMaximumWidth(120)

        def spinbox_changed(value):
            self.changedSettings[name] = value

        spinbox.valueChanged[int].connect(spinbox_changed)

        def spinbox_update(value):
            spinbox.setValue(value)

        self.updateActions[name] = spinbox_update
        # Set initial getValue
        # spinbox.setValue(self.currentSettings.get(name, 5))
        return spinbox

    def _create_combobox(self, name):
        """Return a combobox for modifying a multiple-getValue setting."""
        setting = self.settingItems[name]
        valuetype = setting['valuetype']
        # Create the combobox and populate it
        combo = QComboBox()
        combo.setMinimumWidth(100)
        for value, valueinfo in SettingEnums.enums[valuetype].items():
            data = QVariant(value)
            combo.addItem(valueinfo["display"], data)

        # Ugly event handler!
        def combo_changed(index):
            data = combo.itemData(index)
            self.changedSettings[name] = data

        combo.currentIndexChanged[int].connect(combo_changed)

        # Set the initial getValue, if any
        def combo_update(value):
            index = combo.findData(value)
            combo.setCurrentIndex(index)

        self.updateActions[name] = combo_update
        # combo_update(self.currentSettings.get(name, list(SettingEnums.enums[valuetype].values())[0]))
        return combo

    def _create_fontcombobox(self, name):
        """Return a combobox for modifying a multiple-getValue setting."""
        setting = self.settingItems[name]
        # Create the combobox and populate it
        combo = QFontComboBox()
        combo.setMinimumWidth(100)
        combo.setFontFilters(QFontComboBox.AllFonts) #设置过滤器

        # Ugly event handler!
        def combo_changed(index):
            self.changedSettings[name] = combo.currentFont().family()

        combo.currentFontChanged.connect(combo_changed)

        # Set the initial getValue, if any
        def combo_update(value):
            combo.setCurrentFont(QFont(value))

        self.updateActions[name] = combo_update
        # combo_update(self.currentSettings.get(name, list(SettingEnums.enums[valuetype].values())[0]))
        return combo

    def _create_color_picker(self, name):
        """Return a color-picker widget for a color-based setting."""
        # Button with colored background
        button = QPushButton()
        button.setMinimumWidth(80)

        # Event handler
        def button_pressed():
            color = QColorDialog.getColor(
                self.currentSettings.get(name, Qt.white))  # button.palette().color(QPalette.Background))
            if color.isValid():
                button.setStyleSheet("background-color: %s" % color.name())
                self.changedSettings[name] = color

        # Connect event handler
        button.pressed.connect(button_pressed)

        def button_update(value):
            button.setStyleSheet("background-color: %s" % value.name())

        self.updateActions[name] = button_update
        # button.setStyleSheet("background-color: %s" % current_color)
        return button

    def updateUi(self, settingdict):
        if self.editor:
            for name, value in settingdict.items():
                try:
                    self.updateActions[name](value)
                except:
                    print("Can't update {} setting to config dialog.".format(name))

    def cancel(self):
        self.changedSettings.clear()
        self.updateUi(self.currentSettings)

    def apply(self):
        self.currentSettings.update(self.changedSettings)
        if self.editor:
            try:
                self.editor.configure(**self.changedSettings)
            except Exception as e:
                print(e)
        self.changedSettings.clear()