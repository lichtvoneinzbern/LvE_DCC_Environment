#!/bin/sh

# =============================
# date  :2021/10/13
# Author:Licht von Einzbern
# =============================

# 現在のディレクトリをバッチファイルの場所に移動
cd `dirname $0`

# ファイル名を除いたパスを取得
cd ..
MAYA_VER=`pwd`

# Mayaのバージョンを取得
cd ..
MAYA_VER=${MAYA_VER#`pwd`}
MAYA_VER=${MAYA_VER#"/"}

# -------------
# 環境変数の設定
# -------------
cd `dirname $0`
cd ..
INHOUSE_DIR=`pwd`

# プロジェクト外で作成されたスクリプト・プラグインの格納場所
# ToDo:未デバッグ
# THIRD_DIR=%INHOUSE_DIR:inhouse=thirdparty%

# export MAYA_UI_LANGUAGE=ja_JP
export MAYA_UI_LANGUAGE=en_US
# export MAYA_ENABLE_LEGACY_VIEWPORT=1
# export MAYA_MODULE_PATH=$MAYA_MODULE_PATH;$INHOUSE_DIR/modules
# export MAYA_PLUG_IN_PATH=$MAYA_PLUG_IN_PATH;$INHOUSE_DIR/plug-ins
# export MAYA_SCRIPT_PATH=$MAYA_SCRIPT_PATH;$INHOUSE_DIR/scripts
# export MAYA_PRESET_PATH=$MAYA_PRESET_PATH;$INHOUSE_DIR/presets
export XBMLANGPATH=$XBMLANGPATH:$INHOUSE_DIR/icons/icon-assets
# export MAYA_MODULE_PATH=$MAYA_MODULE_PATH;$INHOUSE_DIR/modules

export PYTHONPATH=$PYTHONPATH:$INHOUSE_DIR/python
# site-packageが必要な場合
# export PYTHONPATH=$PYTHONPATH:$INHOUSE_DIR/python:$INHOUSE_DIR/python/site-packages

#read -p "Hit enter: "

# Maya起動
/Applications/Autodesk/maya2020/Maya.app/Contents/bin/maya
