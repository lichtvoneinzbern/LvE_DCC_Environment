# -*- coding: utf-8 -*-

from shiboken2 import wrapInstance
from PySide2.QtWidgets import*
from PySide2.QtCore import*
from PySide2 import QtGui
from PySide2.QtGui import QSyntaxHighlighter, QColor, QTextCharFormat, QFont

from maya.OpenMayaUI import MQtUtil

from logging import getLogger
logger_name = "Syntax Highlighter"
logger = getLogger(logger_name)


class Rule():
    def __init__(self, fg_color, pattern='', bg_color=None, bold=False, italic=False, font='Courier New'):
        self.pattern = QRegExp(pattern)
        self.form = QTextCharFormat()
        self.form.setForeground(QColor(*fg_color))
        if bg_color:
            self.form.setBackground(QColor(*bg_color))
        font = QFont(font)
        # font = QFont(font, 10) size
        font.setBold(bold)
        font.setItalic(italic)
        self.form.setFont(font)


class SyntaxDecorator(QSyntaxHighlighter):
    def __init__(self, parent, rules):
        super(SyntaxDecorator, self).__init__(parent)
        self.parent = parent
        self.rules = rules

    def highlightBlock(self, text):
        for rule in self.rules:
            pattern = rule.pattern
            index = pattern.indexIn(text)
            while index >= 0:
                len = pattern.matchedLength()
                self.setFormat(index, len, rule.form)
                index = pattern.indexIn(text, index + len)
            self.setCurrentBlockState(0)
        return


def execute():
    i = 1
    while i:
        try:
            reporter = wrapInstance(long(MQtUtil.findControl('cmdScrollFieldReporter%i' % i)),
                                                            QTextEdit)
            assert reporter.findChild(QSyntaxHighlighter).deleteLater()
        except TypeError:
            i += 1
        except (AttributeError, AssertionError):
            break

    rules = [Rule((0, 191, 255), r'^(#|//).+$', bold=True),
             Rule((255, 255, 0), r'^(#|//).*(warning|Warning).+$', bold=True),
             Rule((255, 50, 50), r'^(#|//).*(error:|Error:).+$', bold=True)]

    ins_syntax_decorator = SyntaxDecorator(reporter, rules)
    return ins_syntax_decorator


if __name__ == '__main__':
    logger.info("info")
    logger.warning("warning")
    logger.error("error")