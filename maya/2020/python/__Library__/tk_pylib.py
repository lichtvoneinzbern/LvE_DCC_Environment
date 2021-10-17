# -*- coding: utf-8 -*-

# for python 2.x
from __future__ import absolute_import as _absolute_import
from __future__ import unicode_literals as _unicode_literals
from __future__ import division as _division
from __future__ import print_function as _print_function

import os

import pymel.core as pm
import maya.cmds as mc

from logging import getLogger
logger_name = "__Library__"
logger = getLogger(logger_name)


class General(object):
    @classmethod
    def get_platform_type(cls):
        u"""
        実行しているプラットフォームの種類を取得

        Returns:
            integer: 判定結果
        """

        import platform

        pf = platform.system()
        if pf == 'Windows':
            logger.info("【Platform Type】: Windows")
            return 0
        elif pf == 'Darwin':
            logger.info("【Platform Type】: Mac")
            return 1
        elif pf == 'Linux':
            logger.info("【Platform Type】: Linux")
            return 2

    @classmethod
    def open_file_dialog(cls):
        """ファイル名を含むパスを返却

        Returns:
            string: 選択したパス
        """

        path = pm.fileDialog()
        return path

    @classmethod
    def open_folder_dialog(cls):
        """ディレクトリのみのパスを返却

        Returns:
            string: 選択したパス
        """

        path = pm.fileDialog2(fileMode=3)
        return path


class Node(object):
    @classmethod
    def get_selection_node_name_list(cls):
        u"""
        選択されたオブジェクトのリストを返却（Unicode型）
        Returns:
            list(string): 選択されているノードのリスト
        """
        selections = pm.ls(os=1)
        # print(selection)
        return selections
    # get_selection_node_name_list()

    @classmethod
    def select_node_from_name(cls, *node_names):
        """
        文字列からノードを選択

        Args:
            *node_names (string): 選択したいノードの名前
        """
        for node_name in node_names: pm.select(node_name, replace=True)
    # l = ["lightLinker1", "shaderGlow1"]
    # select_node_from_name(l)


class Environment(object):
    @classmethod
    def get_script_folder(cls):
        """
        Mayaの環境変数からスクリプトパスを返却する

        Returns:
            list(string): mayaのスクリプトパス
        """
        import os
        path = os.getenv('MAYA_SCRIPT_PATH').split(';')
        return path
    # path = get.env_script_folder()
    # print(path)


class Plugin(object):
    @classmethod
    def delete_unknown_plugin(cls):
        '''
        シーン内の不明なプラグインを削除する
        https://qiita.com/UnPySide/items/b91fe203ccf587e8cf99
        '''
        # シーン内の不明なプラグインをリストします。
        unknown_plugins = pm.unknownPlugin(q=True, l=True)
        # print(unknown_plugins)

        if unknown_plugins is not None:
            for unk_plugin in unknown_plugins:
                # 指定された不明なプラグインをシーンから除去します  pm.unknownPlugin(unp, r=True)
                logger.info('{} is Removed.'.format(unk_plugin))
        else:
            logger.info('There are not Unknown Plugin.')
    # unknown_plugin()


class SaveAndLoad(object):

    @classmethod
    def save_scene_as(cls, file_name="fn", folder_path="", file_type=0):
        u"""
        シーンの保存

        Args:
            file_name (str, optional): 拡張子なしのファイル名. Defaults to "fn".
            folder_path (str, optional): 保存対象になるパス 存在することが前提. Defaults to "".
            file_type (int, optional): 拡張子の設定 0=ma 1=mb. Defaults to 0.
        """
        mc.file(rename="{0}{1}".format(folder_path, file_name))
        if file_type == 0:
            mc.file(save=True, type="mayaAscii")
        else:
            mc.file(save=True, type="mayaBinary")


class Project(object):
    @classmethod
    def set_project(cls, path):
        u"""プロジェクトを作成

        Args:
            path (string)): プロジェクトを設定したいパスを指定

        Returns:
            bool: 処理結果　渡されたパスが存在しなければFalse
        """
        SEPARATOR = ["\\", "/"]

        # win環境ならセパレータの置き換え
        platform_type = General().get_platform_type()
        if platform_type == 0:
            path.replace("/", "\\")

        # パスが存在しなければ設定しない
        if os.path.exists(path) is False:
            logger.error("project path not exist")
            return False

        # パスが存在し、ワークスペースがなければ作成
        if os.path.exists(path + "{}workspace.mel".format(SEPARATOR[platform_type])) is False:
            try:
                print(path + "{}workspace.mel".format(SEPARATOR[platform_type]))
                pm.workspace(path, saveWorkspace=True)
            except(RuntimeError):
                logger.error("【Unknown Work Space】: {0}".format(path))

            return True
    # set_project(scene_path)


class Editor(object):
    @classmethod
    def create_confirm_dialog(cls, title="title", message="message", confirm="Yes", decline="No"):
        """
        ダイアログを作成

        Args:
            title (string): ダイアログのタイトルに使用されるメッセージ
            message (string)): ダイアログ内に表示するメッセージ
            confirm (string): ツール実行に対して確認をした際にクリックするボタンのテキスト
            decline (string): ツール実行に対して拒絶をする際にクリックするボタンのテキスト

        Returns:
            unicode(string): ユーザーが同意したかどうかの結果を返す。返却されるのはボタンに割り振ったテキスト
        """
        result = pm.confirmDialog(title=title,
                                    message=message,
                                    button=[confirm, decline],
                                    defaultButton=confirm,
                                    cancelButton=decline,
                                    dismissString=decline)
        return result
    # result = confirm_dialog("たいとる", "メッセージ", "同意する", "同意しない")
    # print (result)

    @classmethod
    def create_progress_window(cls, func, title, width, value):
        """
        プログレスウィンドウを作成
        Args:
            title(string):メニューのタイトル
            width(int):ウィンドウの幅
            value (int): バーのマックス値・処理を行う対象の数
        """

        # プログレスバーの表示
        progress_window = pm.window(title, minimizeButton=False, maximizeButton=False)
        pm.columnLayout()
        progress_control = pm.progressBar(maxValue=value, width=width, step=1)
        pm.showWindow(progress_window)

        for i in range(value):

            # ここに処理を実行
            func()

            # プログレスバーの更新
            pm.progressBar(progress_control, edit=True, isInterruptable=True, step=1)
    """
    @classmethod
    def say_hoge(cls):
        print("hoge")
    @classmethod
    def prg_win_execte(cls):
        cls.create_progress_window(cls.say_hoge, "title", 10)
    """

"""
def main():
    inst_editor = Editor()
    inst_editor.prg_win_execte()

if __name__ == "__main__":
    main()
"""