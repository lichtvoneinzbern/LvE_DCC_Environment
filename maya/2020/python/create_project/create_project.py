# -*- coding: utf-8 -*-

from __future__ import absolute_import as _absolute_import
from __future__ import unicode_literals as _unicode_literals
from __future__ import division as _division
from __future__ import print_function as _print_function

import os
import re
import subprocess
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


class CreateProject(MayaQWidgetBaseMixin, QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(CreateProject, self).__init__(*args, **kwargs)

        # const
        self.PROJECT_CODE = "ccc"
        self.CURRENT_FILE = os.path.normpath(__file__)
        self.PATH, self.PY_EXTENTION = os.path.splitext(self.CURRENT_FILE)
        self.UI_FILE = "{0}{1}".format(self.PATH, "_ui.ui")
        self.WINDOW_TITLE = "Create Project"
        self.ASSET_CATEGORY = ["Character", "Bg", "Prop"]
        self.MODEL_FOLDER_PATH = "/trunk/Work/3d/"
        self.SUB_FOLDERS = ["/Scene", "/Texture", "/Fbx"]

        # checking is project path correct
        self.PROJECT_ROOT_PATH = self.CURRENT_FILE.replace("\\", "/").split("/")[:-7]
        if not self.PROJECT_ROOT_PATH[-1] == self.PROJECT_CODE:
            logger.error("【Get Miss Match Project Code】: {}".format(self.PROJECT_ROOT_PATH))
            return

        self.PLATFORM_TYPE = tpl.General().get_platform_type()
        if self.PLATFORM_TYPE == 0:
            self.PROJECT_ROOT_PATH = "\\".join(self.PROJECT_ROOT_PATH)
        elif self.PLATFORM_TYPE == 1:
            self.PROJECT_ROOT_PATH = "/".join(self.PROJECT_ROOT_PATH)
        logger.info("【Match Project Code】: {}".format(self.PROJECT_ROOT_PATH))

        self.create_ui()

    def create_ui(self):
        """
        create ui
        """
        logger.info("【Create GUI】: start proccess")

        # main window settings
        self.widget = QUiLoader().load(self.UI_FILE)
        self.setCentralWidget(self.widget)
        self.setWindowTitle(self.WINDOW_TITLE)

        # connect ui to function

        # project path
        self.widget.le_ccc_path.setText(self.PROJECT_ROOT_PATH)

        # asset name
        self.widget.pb_set_asset_name.clicked.connect(partial(self.set_asset_type, 0))
        self.widget.le_asset_name.textChanged.connect(self.changed_le_asset_name)
        self.widget.le_asset_name.returnPressed.connect(partial(self.set_asset_type, 1))

        # execute create project
        self.widget.pb_create_project.clicked.connect(self.create_project)

        logger.info("【Create GUI】: end proccess")

    # ===================================
    # functions
    # ===================================

    def changed_le_asset_name(self):
        """
        check asset name
        """

        # get input
        name = self.widget.le_asset_name.text()
        if len(name) == 0:
            return

        # check category
        if name[0] in ["0", "1", "2"]:
            category = name[0]
            "miss match format"
            try:
                re.match("[0-9]{4}[A-Z][a-z]+", name).group(0)
                self.widget.le_asset_name.setText(name)
                self.widget.lbl_asset_type.setText(self.ASSET_CATEGORY[int(category)])

            except(AttributeError):
                self.widget.lbl_asset_type.setText("Unknown")

        else:
            self.widget.lbl_asset_type.setText("Unknown")

    def set_asset_type(self, id):
        """
        set asset name to line edit
        when click "Current Scene Name" or enter name into line edit
        """

        # check call type
        if id == 0:
            name = pm.sceneName().replace("\\", "/").split("/")[-1]
            name = name.split(".")[0]
        elif id == 1:
            name = self.widget.le_asset_name.text()
        if len(name) == 0:
            return

        category = name[0]

        # check category
        if name[0] in ["0", "1", "2"]:
            "miss match format"
            try:
                re.match("[0-9]{4}[A-Z][a-z]+", name).group(0)
                self.widget.le_asset_name.setText(name)
                self.widget.lbl_asset_type.setText(self.ASSET_CATEGORY[int(category)])
                logger.error("【Category Set】: {}".format(self.ASSET_CATEGORY[int(category)]))
            except(AttributeError):
                self.widget.le_asset_name.setText("")
                logger.error("【Format Error】: asset name format miss match")
        else:
            self.widget.le_asset_name.setText("")
            logger.error("【Category Error】: Category type miss match")

    def create_project(self):

        separator = ["\\", "/"]

        name = self.widget.le_asset_name.text()

        """
        print("{0}{1}{2}/{3}".format(self.PROJECT_ROOT_PATH,
                                 self.MODEL_FOLDER_PATH,
                                 self.ASSET_CATEGORY[int(name[0])],
                                 name))
        """

        # create export path
        path = "{0}{1}{2}/{3}".format(self.PROJECT_ROOT_PATH,
                                self.MODEL_FOLDER_PATH,
                                self.ASSET_CATEGORY[int(name[0])],
                                name)
        if not os.path.exists(path):
            os.mkdir(path)

        for sub_folder in self.SUB_FOLDERS:
            if self.PLATFORM_TYPE == 0:
                path = path.replace("/", "\\")

            if not os.path.exists("{0}{1}".format(path, sub_folder)):
                os.mkdir("{0}{1}".format(path, sub_folder))

            # save scene as asset name
            if sub_folder == "{}Scene".format(separator[self.PLATFORM_TYPE]) \
               and self.widget.cb_save_scene_as_asset_name.isChecked() is True:
                tpl.SaveAndLoad().save_scene_as("{0}{1}".format(separator[self.PLATFORM_TYPE], name),
                                                "{0}{1}".format(path, sub_folder),
                                                0)

        # set project
        if self.widget.cb_set_project.isChecked():
            tpl.Project().set_project(path)

        if self.widget.cb_open_project_folder.isChecked():
            self.open_path(path, self.PLATFORM_TYPE)

    def open_path(self, path, platform_type):
        """
        open path

        Args:
            path (string): wanted open path
            platform_type (int): is win or mac or linux
        """
        if platform_type == 0:
            subprocess.Popen(["explorer", path], shell=True)
        elif platform_type == 1:
            subprocess.call(["open", path])
        else:
            logger.warning("not support")

def main():
    ins_qt_window = CreateProject()
    ins_qt_window.show()
