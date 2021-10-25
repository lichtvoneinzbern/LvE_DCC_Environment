# -*- coding: utf-8 -*-

from __future__ import absolute_import as _absolute_import
from __future__ import unicode_literals as _unicode_literals
from __future__ import division as _division
from __future__ import print_function as _print_function

import syntax_highlighter.command as syntax_highlighter
from logging import getLogger
logger_name = "userSetup"
logger = getLogger(logger_name)


class UserSetup(object):

    @classmethod
    def set_preferences(cls):
        u"""
        プリファレンスを設定
        """

        # pymelにfileモジュールがないためcmdsで行う
        import maya.cmds as mc
        import maya.mel as mel

        logger.info("【Set Preferences】")

        # ユニット単位：cm
        mc.optionVar(sv=["workingUnitLinearDefault", "cm"])
        logger.info("【Unit】: cm")

        # FPS設定：30FPS
        mc.optionVar(sv=["workingUnitTimeDefault", "ntsc"])
        logger.info("【Time】: 30fps")

        # Maya終了時プリファレンスを保存しない
        mc.optionVar(iv=["saveActionsPreferences", False])
        logger.info("【Save Preferences When Close Maya】: False")

        # シーンへのレイアウト保存と復元を無効化
        # 行うことでシーン設定が反映される。
        save_layout = 0
        mc.optionVar(iv=["useSaveScenePanelConfig", save_layout])
        mc.file(uiConfiguration=save_layout)
        mel.eval("$gUseSaveScenePanelConfig=" + str(save_layout))
        logger.info("【Save Panel Layout】: Disable ")

        restore_layout = 0
        mc.optionVar(iv=["useScenePanelConfig", restore_layout])
        mc.file(uiConfiguration=restore_layout)
        mel.eval("$gUseScenePanelConfig=" + str(restore_layout))
        logger.info("【Restore Panel Layout】: Disable ")

    @classmethod
    def create_menu(cls):
        u"""
        ツールメニューを作成
        """

        import menu
        custom_maya_menu = menu.CustomMayaMenu()
        custom_maya_menu.main()

    @classmethod
    def main(cls):
        cls.set_preferences()
        cls.create_menu()

        # ログに色をつける
        # syntax_highlighter.execute()

# GUIが構築されてから実行
if __name__ == "__main__":
    import maya.utils as utl

    utl.executeDeferred(UserSetup.main)
