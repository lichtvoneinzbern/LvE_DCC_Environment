#!/bin/sh

# =============================
# date  :2021/10/13
# Author:Licht von Einzbern
# =============================

# ���݂̃f�B���N�g�����o�b�`�t�@�C���̏ꏊ�Ɉړ�
cd `dirname $0`

# �t�@�C�������������p�X���擾
cd ..
MAYA_VER=`pwd`

# Maya�̃o�[�W�������擾
cd ..
MAYA_VER=${MAYA_VER#`pwd`}
MAYA_VER=${MAYA_VER#"/"}

# -------------
# ���ϐ��̐ݒ�
# -------------
cd `dirname $0`
cd ..
INHOUSE_DIR=`pwd`

# �v���W�F�N�g�O�ō쐬���ꂽ�X�N���v�g�E�v���O�C���̊i�[�ꏊ
# ToDo:���f�o�b�O
# THIRD_DIR=%INHOUSE_DIR:inhouse=thirdparty%

# export MAYA_UI_LANGUAGE=ja_JP
export MAYA_UI_LANGUAGE=en_US
# export MAYA_ENABLE_LEGACY_VIEWPORT=1
# export MAYA_MODULE_PATH=$MAYA_MODULE_PATH;$INHOUSE_DIR/modules
# export MAYA_PLUG_IN_PATH=$MAYA_PLUG_IN_PATH;$INHOUSE_DIR/plug-ins
export MAYA_SCRIPT_PATH=$MAYA_SCRIPT_PATH:$INHOUSE_DIR/scripts
# export MAYA_PRESET_PATH=$MAYA_PRESET_PATH;$INHOUSE_DIR/presets
export XBMLANGPATH=$XBMLANGPATH:$INHOUSE_DIR/icons/icon-assets
# export MAYA_MODULE_PATH=$MAYA_MODULE_PATH;$INHOUSE_DIR/modules

export PYTHONPATH=$PYTHONPATH:$INHOUSE_DIR/python
# site-package���K�v�ȏꍇ
# export PYTHONPATH=$PYTHONPATH:$INHOUSE_DIR/python:$INHOUSE_DIR/python/site-packages

#read -p "Hit enter: "

# Maya�N��
/Applications/Autodesk/maya2020/Maya.app/Contents/bin/maya
