# -*- coding: utf-8 -*-

from __future__ import absolute_import as _absolute_import
from __future__ import unicode_literals as _unicode_literals
from __future__ import division as _division
from __future__ import print_function as _print_function

# 対策：Error: NameError: file  line 1: name 'reload' is not defined #
# Python3.3
# import imp
# Python3.4
# import importlib

import pymel.core as pm
import maya.mel as mel

import os


class CustomMayaMenu(object):
    menu_name = "CustomTools"

    @classmethod
    def set_items(cls):
        # デザイナー向け
        cls.set_tools()

        # 開発者向け
        cls.set_developer_tools()

    @classmethod
    def set_tools(cls):
        """
        デザイナーの使用するツール群を追加
        """

        pm.menuItem(label=u'Tools',
                    subMenu=True,
                    tearOff=True,
                    parent=cls.menu_name
                    )

        pm.menuItem(divider=True, label=u'【共用】')

        pm.menuItem(label=u'シーンパスを開く',
                    image="open_scene_path.png",
                    command='from open_scene_path import open_scene_path; reload(open_scene_path); open_scene_path.main()')

        pm.menuItem(label=u'プロジェクトフォルダを作成',
                    image="create_project.png",
                    command='from create_project import create_project; reload(create_project); create_project.main()')

        pm.menuItem(label=u'アウトライナーを着彩',
            image="",
            command='from outliner_coloring import outliner_coloring; reload(outliner_coloring); outliner_coloring.main()')

        pm.menuItem(divider=True, label=u'【造形者用】')

        pm.menuItem(label=u'テクスチャセット用のマテリアルを割り当て',
                    image="set_textureset_material.png",
                    command='from set_textureset_material import set_textureset_material; reload(set_textureset_material); set_textureset_material.main()')

        pm.menuItem(label=u'FBXをエクスポート',
                    image="export_model_fbx.png",
                    command='from export_fbx import export_fbx; reload(export_fbx); export_fbx.main(0)')

        pm.menuItem(divider=True, label=u'【アニメーター用】')

        pm.menuItem(label=u'FBXをエクスポート',
                image="export_animation_fbx.png",
                command='from export_fbx import export_fbx; reload(export_fbx); export_fbx.main(1)')

    @classmethod
    def set_developer_tools(cls):
        """
        開発用のツール群を追加
        """

        pm.menuItem(label=u'Develop',
                    subMenu=True,
                    tearOff=True,
                    parent=cls.menu_name
                    )

        pm.menuItem(divider=True, label=u'【実行環境】: {}'.format(cls.get_tool_path_name()))

        pm.menuItem(label=u'ツールフォルダを開く',
                    image="",
                    command='from open_tool_path import open_tool_path; reload(open_tool_path); open_tool_path.main()')

        pm.menuItem(label=u'ログをハイライト',
            image="",
            command='from syntax_highlighter import command as syntax_highlighter; reload(syntax_highlighter); syntax_highlighter.execute()')

    @classmethod
    def get_tool_path_name(cls):
        """ツール実行環境のフォルダ名を取得

        Returns:
            string: ツールの設置された最上位のパス
        """
        p = os.path.dirname(__file__).replace("\\", "/").split("/")[:-3]
        return p[-1]

    @classmethod
    def main(cls):
        g_main_window = mel.eval('$temp=$gMainWindow')
        if pm.menu(cls.menu_name, q=True, ex=True):
            cls.menu = pm.menu(cls.menu_name, e=True, dai=True, tearOff=True)
        else:
            cls.menu = pm.menu(cls.menu_name,
                               label=cls.menu_name.capitalize(),
                               parent=g_main_window,
                               tearOff=True
                               )

        """
        pm.menu(label=cls.menu_name,
                parent='MayaWindow',
                tearOff=True)
        """

        cls.set_items()

        pm.setParent('..', menu=True)
        pm.setParent('..')
        pm.setParent(cls.menu_name, menu=True)
