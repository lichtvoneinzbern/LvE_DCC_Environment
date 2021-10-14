# -*- coding: utf-8 -*-

from __future__ import absolute_import as _absolute_import
from __future__ import unicode_literals as _unicode_literals
from __future__ import division as _division
from __future__ import print_function as _print_function

import pymel.core as pm

import subprocess

from logging import getLogger


class OpenScenePath(object):

    @classmethod
    def get_scene_path(cls):
        u"""
        現在開いているシーンのパスを取得

        Returns:
            string: パスを文字列で返却(シーンが開かれていない場合は空白が帰る)
        """

        scene_path = pm.sceneName()
        return scene_path

    @classmethod
    def execute(cls):

        logger_name = "open_scene_path"
        logger = getLogger(logger_name)

        # パスを成形
        path = cls.get_scene_path()

        if path == "":
            logger.error("missing path")
            return

        path = path.replace("/", "\\").split("\\")
        path = "\\".join(path[:-1])

        logger.info("{0}{1}".format("target path: ", path))

        # パスを開く
        subprocess.Popen(["explorer", path], shell=True)


def main():
    open_scene_path = OpenScenePath()
    open_scene_path.execute()
