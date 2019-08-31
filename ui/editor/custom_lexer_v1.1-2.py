# -*- coding: utf-8 -*-

# Copyright (c) 2005 - 2019 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing a QSS lexer with some additional methods.
"""

from __future__ import unicode_literals

from PyQt5.Qsci import QsciLexerCSS



class QsciLexerQSS( QsciLexerCSS):
    """
    Subclass to implement some additional lexer dependent methods.
    """

    def __init__(self, parent=None):
        """
        Constructor

        @param parent parent widget of this lexer
        """
        QsciLexerCSS.__init__(self, parent)

        self.commentString = "#"
        self.streamCommentString = {
            'start': '/* ',
            'end': ' */'
        }

        self.keywordSetDescriptions = [
            self.tr("CSS1 Properties"),
            self.tr("Pseudo-Classes"),
            self.tr("CSS2 Properties"),
            self.tr("CSS3 Properties"),
            self.tr("Pseudo-Elements"),
            self.tr("Browser-Specific CSS Properties"),
            self.tr("Browser-Specific Pseudo-Classes"),
            self.tr("Browser-Specific Pseudo-Elements"),
        ]



    def isCommentStyle(self, style):
        """
        Public method to check, if a style is a comment style.

        @param style style to check (integer)
        @return flag indicating a comment style (boolean)
        """
        return style in [QsciLexerCSS.Comment]

    def isStringStyle(self, style):
        """
        Public method to check, if a style is a string style.

        @param style style to check (integer)
        @return flag indicating a string style (boolean)
        """
        return style in [QsciLexerCSS.DoubleQuotedString,
                         QsciLexerCSS.SingleQuotedString]

    def defaultKeywords(self, kwSet):
        """
        Public method to get the default keywords.

        @param kwSet number of the keyword set (integer)
        @return string giving the keywords (string) or None
        """
        if kwSet == 1:
            return "alternate-background-color background background-color" \
                   " background-image background-repeat background-position" \
                   " background-attachment background-clip background-origin" \
                   " border border-top border-right border-bottom border-left" \
                   " border-color border-top-color border-right-color" \
                   " border-bottom-color border-left-color border-image" \
                   " border-radius border-top-left-radius" \
                   " border-top-right-radius border-bottom-right-radius" \
                   " border-bottom-left-radius border-style border-top-style" \
                   " border-right-style border-bottom-style border-left-style" \
                   " border-width border-top-width border-right-width" \
                   " border-bottom-width border-left-width bottom button-layout" \
                   " color dialogbuttonbox-buttons-have-icons font font-family" \
                   " font-size font-style font-weight gridline-color" \
                   " height icon-size image image-position left" \
                   " lineedit-password-character margin margin-top margin-right" \
                   " margin-bottom margin-left max-height max-width" \
                   " messagebox-text-interaction-flags min-height min-width" \
                   " opacity outline padding padding-top padding-right" \
                   " padding-bottom padding-left" \
                   " paint-alternating-row-colors-for-empty-area" \
                   " position right selection-background-color selection-color" \
                   " show-decoration-selected spacing subcontrol-origin" \
                   " subcontrol-position text-align text-decoration" \
                   " top width" \
                   "" \
                   " backward-icon cd-icon computer-icon desktop-icon" \
                   " dialog-apply-icon dialog-cancel-icon dialog-close-icon" \
                   " dialog-discard-icon dialog-help-icon dialog-no-icon" \
                   " dialog-ok-icon dialog-open-icon dialog-reset-icon" \
                   " dialog-save-icon dialog-yes-icon directory-closed-icon" \
                   " directory-icon directory-link-icon directory-open-icon" \
                   " dockwidget-close-icon downarrow-icon dvd-icon file-icon" \
                   " file-link-icon filedialog-contentsview-icon" \
                   " filedialog-detailedview-icon filedialog-end-icon" \
                   " filedialog-infoview-icon filedialog-listview-icon" \
                   " filedialog-new-directory-icon" \
                   " filedialog-parent-directory-icon filedialog-start-icon" \
                   " floppy-icon forward-icon harddisk-icon home-icon" \
                   " leftarrow-icon messagebox-critical-icon" \
                   " messagebox-information-icon messagebox-question-icon" \
                   " messagebox-warning-icon network-icon rightarrow-icon" \
                   " titlebar-contexthelp-icon titlebar-maximize-icon" \
                   " titlebar-menu-icon titlebar-minimize-icon" \
                   " titlebar-normal-icon titlebar-shade-icon" \
                   " titlebar-unshade-icon trash-icon uparrow-icon"
        elif kwSet == 2:
            return "active adjoins-item alternate bottom checked closable" \
                   " closed default disabled editable edit-focus enabled" \
                   " exclusive first flat floatable focus has-children" \
                   " has-siblings horizontal hover indeterminate last left" \
                   " maximized middle minimized movable no-frame" \
                   " non-exclusive off on only-one open next-selected" \
                   " pressed previous-selected read-only right selected top" \
                   " unchecked vertical window" \
                   "" \
                   " add-line add-page branch chunk close-button corner" \
                   " down-arrow down-button drop-down float-button groove" \
                   " indicator handle icon item left-arrow left-corner" \
                   " menu-arrow menu-button menu-indicator right-arrow" \
                   " pane right-corner scroller section separator sub-line" \
                   " sub-page tab tab-bar tear tearoff text title up-arrow" \
                   " up-button"

        return None

    def language(self):
        """
        Public method to return the lexer language.

        @return lexer language (string)
        """
        return "QSS"

    def lexerName(self):
        """
        Public method to return the lexer name.

        @return lexer name (string)
        """
        return "QSS"
