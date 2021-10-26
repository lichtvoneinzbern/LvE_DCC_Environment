# -*- coding: utf-8 -*-

from __future__ import absolute_import as _absolute_import
from __future__ import unicode_literals as _unicode_literals
from __future__ import division as _division
from __future__ import print_function as _print_function

from __Library__ import tk_pylib as tpl

import pymel.core as pm
import maya.mel as mel

import os
import subprocess

from logging import getLogger
logger_name = "Export FBX"
logger = getLogger(logger_name)


class ExportFbx(object):
    def __init__(self):
        self.CATEGORY_CHARACTER = "Character"
        self.CATEGORY_BG        = "Bg"
        self.CATEGORY_PROP      = "Prop"
        self.FOLDER_FBX         = "/Fbx"

        self.scene_path = ""
        self.fbx_folder_path = ""
        self.scene_name = ""
        self.export_path = ""

    def show_error_message(self, error_id=0):
        u"""エラーが起こったことを表示するダイアログを作成

        Args:
            error_id (int, optional): エラーIDを取得してメッセージを分岐. Defaults to 0.
        """
        mes = [u"原因不明のエラーが発生しました。\nテクニカルアーティストにお知らせください。",
               u"シーンが想定されたパスに存在しません。\n処理を中断します。",
               u"FBXのプラグインが存在しませんでした。\n処理を中断します。",
               u"選択されたノードが一つではありません。\n処理を中断します。"]

        pm.confirmDialog(title='Error',
                         message=mes[error_id],
                         button='OK')
        return

    def check_fbx_plugin(self):
        u"""FBXのプラグインが存在するか確認

        Returns:
            bool: 判定結果
        """

        fbxPlugin = pm.pluginInfo('fbxmaya', query=True, loaded=True)

        if fbxPlugin != True:
            try:
                pm.loadPlugin('fbxmaya.mll')
                logger.info('【Plugin Load】: fbxmaya.mll is not loaded. but load success now')
                return True
            except:
                logger.error('【Plugin Error】: FBX Plugin not found')
                return False
        else:
            logger.info('【Plugin Exist】: fbxmaya.mll')
            return True

    def get_scene_name(self):
        u"""シーン名を取得
        """

        self.scene_path = pm.sceneName()
        if self.scene_path == "":
            self.show_error_message(1)
            return

        self.scene_path = self.scene_path.replace("\\", "/")
        logger.info("【Scene Parh】: {}".format(self.scene_path))

        scene_name_w2_ext = self.scene_path[self.scene_path.rfind('/')+1:]
        self.scene_name = scene_name_w2_ext[0:scene_name_w2_ext.rfind(".")]

        logger.info("【Scene Name】: {}".format(self.scene_name))
        return

    def get_fbx_folder_path(self):
        u"""Fbxフォルダのパスを取得
        """
        base_path = self.scene_path.replace("\\", "/").split("/")[:-2]
        base_path = "/".join(base_path)
        self.fbx_folder_path = "{0}{1}".format(base_path, "/Fbx")

        logger.info("【Fbx Folder Path】: {}".format(self.fbx_folder_path))
        return

    def check_fbx_folder_path_exist(self):
        u"""Fbxフォルダのパスが存在するかチェック

        Returns:
            bool: 判定結果
        """

        if os.path.exists(self.fbx_folder_path):
            logger.info("【Fbx Folder】: Exist")
            return True
        logger.warning("【Fbx Folder】: Not Exist")
        return False

    def create_fbx_folder_path(self):
        u"""Fbxフォルダを作成
        """
        os.mkdir(self.fbx_folder_path)

        logger.info("【Created Fbx Directory】: {}".format(self.fbx_folder_path))
        return

    def get_export_path(self):
        u"""FBXの出力パスを作成
        """
        self.export_path = "{0}/{1}{2}".format(self.fbx_folder_path, self.scene_name, ".fbx")

        logger.info("【Export Path】: {}".format(self.export_path))
        return

    def export_model_fbx(self):
        u"""FBXモデルを出力
        """

        mel.eval('FBXExportUseSceneName -v true;')
        mel.eval('FBXExportTriangulate -v true;')
        mel.eval('FBXExportAnimationOnly -v false;')
        # logger.info("【FBXExportTriangulate】: {}".format(mel.eval('FBXExportTriangulate -q;')))
        mel.eval('FBXExportSmoothMesh -v true;')
        mel.eval('FBXExportSmoothingGroups -v true;')
        mel.eval('FBXExportInputConnections -v true;')
        mel.eval('FBXExportIncludeChildren -v true;')
        mel.eval('FBXExportFileVersion -v FBX202000;')
        pm.FBXExport(['-f',
                      '{}'.format(self.export_path),
                      '-s'])
        return

    def export_animation_fbx(self):
        u"""FBXアニメーションを出力
        """

        mel.eval('FBXExportUseSceneName -v true;')
        mel.eval('FBXExportAnimationOnly -v true;')
        mel.eval('FBXExportConstraints -v true;')
        mel.eval('FBXExportInputConnections -v true;')
        mel.eval('FBXExportIncludeChildren -v true;')
        mel.eval('FBXExportFileVersion -v FBX202000;')
        pm.FBXExport(['-f',
                      '{}'.format(self.export_path),
                      '-s'])
        return

    def bake_animation(self):
        """FBXアニメーション書き出しのためにアニメーションをベイク処理
        """

        # ノード名を取得
        node, type = pm.ls(selection=True, showType=True)

        # タイムスライダの時間を取得
        start = pm.Env().getMinTime()
        end = pm.Env().getMaxTime()

        # アニメーションをベイク
        pm.bakeResults(node, time=(start, end), simulation=True, hierarchy="below", shape=False)


    def open_fbx_folder(self):
        u"""Fbx フォルダのパスを開く
        """

        pl_type = tpl.General.get_platform_type()
        if pl_type == 0:
            self.fbx_folder_path = self.fbx_folder_path.replace("/", "\\")
            subprocess.Popen(["explorer", self.fbx_folder_path], shell=True)
        elif pl_type == 1:
            subprocess.call(["open", self.fbx_folder_path])
        else:
            logger.error("【Unexpected Platform Type】{}".format(pl_type))
            return

        logger.info("【Open FBX Folder】: {}".format(self.fbx_folder_path))
        return

    def execute(self, id):

        # 選択されたノードは一つか
        if tpl.Node.check_selected_node_is_single() is False:
            self.show_error_message(3)
            return

        # FBXのプラグインが存在するか
        result = self.check_fbx_plugin()
        if result is False:
            self.show_error_message(2)
            return

        # 使用するパスやファイル名の取得
        self.get_scene_name()
        # シーンが想定された場所に存在しなければ終了
        # ToDo: 例外処理を厳密に定義する必要がある?
        if self.scene_path == "":
            logger.error("【Missing Pass】: {}".format(self.scene_path))
            return
        elif self.scene_path.replace("\\", "/").split("/") < 4:
            logger.error("【Missing Pass】: {}".format(self.scene_path))
            self.show_error_message(1)
            return

        self.get_fbx_folder_path()
        self.get_export_path()

        # Fbxフォルダのパスが作成されており、パスが存在しなかった場合Fbxフォルダを作成
        if not self.fbx_folder_path == "" and self.check_fbx_folder_path_exist() == False:
            self.create_fbx_folder_path()

        # 渡されたIDごとに処理を分岐
        logger.info("【ID】: {}".format(id))
        if id == 0: # モデル
            self.export_model_fbx()
            self.open_fbx_folder()
        elif id == 1: # アニメーション
            self.bake_animation()
            self.export_animation_fbx()
            self.open_fbx_folder()
        else:
            self.show_error_message(1)

        logger.info("【End Process】: Executed")


def main(id):
    ins_export_model_fbx = ExportFbx()
    ins_export_model_fbx.execute(id)