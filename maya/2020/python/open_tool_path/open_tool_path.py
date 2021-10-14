# -*- coding: utf-8 -*-

from __future__ import absolute_import as _absolute_import
from __future__ import unicode_literals as _unicode_literals
from __future__ import division as _division
from __future__ import print_function as _print_function

import pymel.core as pm

import sys
sys.path.append("../")
from __Library__ import tk_pylib as tpl

import os
import subprocess

from logging import getLogger
logger_name = os.path.basename(__file__)
logger = getLogger(logger_name)


class OpenToolPath(object):
    def __init__(self):
        logger.info("initialized")
        return

    @classmethod
    def get_tool_path(cls):
        p = os.path.dirname(__file__).replace("\\", "/").split("/")[:-4]
        p = "\\".join(p)
        return p

    @classmethod
    def execute(cls):
        path = cls.get_tool_path()
        pf_type = tpl.General.get_platform_type()
        logger.info("【Platform】: {}".format(pf_type))
        logger.info("【Path】: {}".format(path))

        if pf_type == 0:
            subprocess.Popen(["explorer", path], shell=True)
        elif pf_type == 1:
            subprocess.call(["open", path])
        else:
            logger.warning("not support")


def main():
    OpenToolPath.execute()
