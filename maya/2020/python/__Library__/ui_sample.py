# -*- coding: utf-8 -*-

from __future__ import absolute_import as _absolute_import
from __future__ import unicode_literals as _unicode_literals
from __future__ import division as _division
from __future__ import print_function as _print_function

import os
from functools import partial

import sys
sys.path.append("../")
from __Library__ import tk_pylib as tpl

from PySide2 import QtWidgets
from PySide2 import QtCore
from PySide2.QtUiTools import QUiLoader
from maya.app.general.mayaMixin import MayaQWidgetBaseMixin

import pymel.core as pm
import maya.mel as mel

from logging import getLogger
logger_name = __file__.replace("\\", "/").split("/")[-1]
logger = getLogger(logger_name)


class QtWindow(MayaQWidgetBaseMixin, QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(QtWindow, self).__init__(*args, **kwargs)

        # const
        self.PROJECT_CODE = "project_env"
        self.CURRENT_FILE = os.path.normpath(__file__)
        self.PATH, self.PY_EXTENTION = os.path.splitext(self.CURRENT_FILE)
        self.UI_FILE = "{0}{1}{2}".format("ui_", self.PATH, ".ui")
        self.WINDOW_TITLE = "Title sample"

        # self.sample_create_ui()

    def sample_create_ui(self):
        u"""
        create ui
        """

        logger.info("【Create GUI】: start proccess")

        # main window settings
        self.widget = QUiLoader().load(self.UI_FILE)
        self.setCentralWidget(self.widget)
        self.setWindowTitle(self.WINDOW_TITLE)

        # connect ui to function

        # Line Edit
        # self.widget.le_line_edit.setText("text")
        # self.widget.le_line_edit.returnPressed(partial("func", id))

        # Push Button
        # self.widget.pb_push_button.clicked.connect(partial(self.clicked_push_button, "id"))

        # Check Box
        # self.widget.cb_check_box.clicked.connect(partial(self.clicked_cb_check_box, "id"))

        # Horizontal Slider
        # self.widget.hs_horizontal_slider.valueChanged.connect(partial(changed_hs_horizontal_slider, "id"))

        logger.info("【Create GUI】: end proccess")

    # ===================================
    # sample functions
    # ===================================

    """
    def clicked_pb_push_button(self, id):
        "clicked push button"

        logger.info("clicked")
    """

    """
    def pressed_return_le_line_edit(self):
        "pressed return key in line edit"
        value = self.widget.le_line_edit.text()
        logger.info("yPressed Return Line Editz: value is {}".format(value))
    """

    """
    def clicked_cb_check_box(self, id):
        "clicked check box"
        value = self.widget.cb_check_box.isChecked()
        logger.info("yCheck Box Clickedz: {}".format(value))

        # result = True if value is True else False
        # return result
    """

    """
    def changed_hs_horizontal_slider(self, id):
        "change horizontal slider value"
        value = self.widget.hs_horizontal_slider.value()

        # when changed slider, change line edit value same time
        self.widget.le_line_edit.setValue(value)
    """

    """
    def update(self):
        "update gui"

        self.widget.update()
        logger.info("ui updated")
    """

    # ===================================
    # functions
    # ===================================


def main():
    ins_qt_window = QtWindow()
    ins_qt_window.show()
