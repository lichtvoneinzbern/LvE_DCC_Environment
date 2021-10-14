# -*- coding: utf-8 -*-

from __future__ import absolute_import as _absolute_import
from __future__ import unicode_literals as _unicode_literals
from __future__ import division as _division
from __future__ import print_function as _print_function

import os
import stat

import pymel.core as pm
import maya.mel as mel
from logging import getLogger

# logger template
# logger_title = ""
# logger = getLogger(logger_title)


class ExportFbx(object):

    @classmethod
    def remove_extention(cls, file_name):
        u"""付与されている拡張子を削除する

        Args:
            file_name (string): 拡張子のついたファイル名

        Returns:
            string: 拡張子を取り除いたファイル名　拡張子が見当たらなければそのまま返却
        """

        logger = getLogger(cls.remove_extention.__name__)

        without_extention = file_name.split(".")[:-1]

        # 拡張子が見当たらなかった場合ファイル名を変更せず文字列で返却
        if len(without_extention) == 0:
            logger.warning("has no extention")
            return str(file_name)
        return str(without_extention[0])
    # remove_extention("hoge.ma")

    @classmethod
    def check_fbx_plugin_exist(cls):
        u"""
        fbxのプラグインが存在するかをチェック

        Returns:
            bool: チェック結果　プラグインが存在しなければFalse
        """

        logger = getLogger(cls.check_fbx_plugin_exist.__name__)

        fbxPlugin = pm.pluginInfo('fbxmaya', query=True, loaded=True)
        if fbxPlugin is not True:
            try:
                pm.loadPlugin('fbxmaya.mll')
            except BaseException:
                logger.error('FBX Plugin not found')
                return False
        logger.info("FBX plugin found")
        return True
    # check_fbx_plugin_exist()

    @classmethod
    def get_scene_path(cls):
        u"""
        現在開いているシーンのパスを取得

        Returns:
            string: パスを文字列で返却(シーンが開かれていない場合は空白が帰る)
        """

        scene_path = pm.sceneName()
        return scene_path
    # get_scene_path()

    @classmethod
    def get_project_path(cls):
        u"""プロジェクトのパスを取得

        Returns:
            string: プロジェクトパスを文字列で返却
        """

        project_path = pm.workspace.path
        return project_path
    # get_project_path()

    @classmethod
    def set_project(cls, path):
        """プロジェクトを作成

        Args:
            path (string)): プロジェクトを設定したいパスを指定

        Returns:
            bool: 処理結果　渡されたパスが存在しなければFalse
        """

        logger = getLogger(cls.set_project.__name__)

        # パスが存在しなければ設定しない
        if os.path.exists(path) is False:
            logger.error("project path not exist")
            return False

        # パスが存在し、ワークスペースがなければ作成
        if os.path.exists(path + "/workspace.mel") is False:
            pm.workspace(path, saveWorkspace=True)
            return True
    # set_project(scene_path)

    @classmethod
    def create_fbx_folder(cls):
        u"""
        fbxフォルダを作成

        Returns:
            string: 作成したパスを返却　エラーが発生した場合”error”が返却される
        """

        logger = getLogger(cls.create_fbx_folder.__name__)

        # 作成されるフォルダ名
        fbx_folder_name = "Fbx"

        # fbxを格納するフォルダのディレクトリを作成
        scene_path = pm.sceneName()  # '/Users/von/Documents/ccc/trunk/Work/3d/Prop/2999Test/Scene/2999Test.ma'

        # シーンが設定されておらずuntitledの状態だとos errorになるためtry catchする
        try:
            # シーンパスから作成するfbxのフォルダパスを作成
            fbx_folder_path = scene_path.replace("\\", "/").split("/")[:-2]
            fbx_folder_path = "/".join(fbx_folder_path)
            fbx_folder_path = os.path.join(fbx_folder_path, fbx_folder_name).replace("\\", "/")
            # logger.info("{0}{1}".format("fbx_folder_path == ", fbx_folder_path))

            # パスが存在しなければ作成
            if not os.path.isdir(fbx_folder_path):
                os.mkdir(fbx_folder_path)
                logger.info("create fbx folder")
                return fbx_folder_path
            # あったら何もしない
            logger.warning("aleady exist fbx folder")
            return fbx_folder_path
        except(OSError):
            logger.error("os path error")
            return "error"
    # create_fbx_folder()

    @classmethod
    def export_fbx_selected_node(cls):
        u"""
        選択されたノードをfbx形式でエクスポート

        Returns:
            bool: 処理結果　最後まで走ればTrue
        """

        logger = getLogger(cls.export_fbx_selected_node.__name__)

        # init
        suffix = ""
        fbx_extention = ".fbx"
        fbx_folder_name = "Fbx"

        # fbxファイル名を作成
        scene_name = str(pm.sceneName().replace("\\", "/").split("/")[-1])
        scene_name = cls.remove_extention(scene_name)
        fbx_file_name = "{0}{1}{2}".format(scene_name, suffix, fbx_extention)
        logger.info("{0}{1}".format("export fbx name == ", fbx_file_name))

        # シーンパスから作成するfbxのフォルダパスを作成
        scene_path = pm.sceneName()
        fbx_folder_path = scene_path.replace("\\", "/").split("/")[:-2]
        fbx_folder_path = "/".join(fbx_folder_path)
        fbx_folder_path = os.path.join(fbx_folder_path, fbx_folder_name).replace("\\", "/")
        logger.info("{0}{1}".format("fbx folder path == ", fbx_folder_path))

        # FBX をエクスポート
        mel.eval('FBXExport -f ' + '"' + fbx_folder_path + "/" + fbx_file_name + '" -s')
        logger.info("Selected objects exported to " + fbx_folder_path)
        return True
    # export_fbx_selected_node()

    @classmethod
    def create_error_dialog(cls, title="title", message="", confirm="OK"):
        """
        エラー用のダイアログを作成

        Args:
            title (string): ダイアログのタイトルに使用されるメッセージ
            message (string)): ダイアログ内に表示するメッセージ
            confirm (string): ツール実行に対して確認をした際にクリックするボタンのテキスト

        Returns:
            unicode(string): ユーザーが同意したかどうかの結果を返す。返却されるのはボタンに割り振ったテキスト
        """

        result = pm.confirmDialog(title=title,
                                  message=message,
                                  button=[confirm],
                                  defaultButton=confirm)
        return result
    # create_error_dialog("title", "message", "OK")

    @classmethod
    def execute(cls):
        logger = getLogger(cls.execute.__name__)
        logger.info("==================start log=================")

        if cls.check_fbx_plugin_exist() == 0:
            return

        result = cls.create_fbx_folder()
        if result == "error":
            return

        result = cls.export_fbx_selected_node()
        if result is False:
            cls.create_error_dialog("エラー", "書き出しに失敗しました。")
        cls.create_error_dialog("export_fbx", "書き出しに成功しました。")

    """
    if __name__ == "__main__":
        main()
    """


def main():
    ExportFbx.execute()
