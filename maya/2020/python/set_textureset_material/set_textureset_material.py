# -*- coding: utf-8 -*-

# for python 2.x
from __future__ import absolute_import as _absolute_import
from __future__ import unicode_literals as _unicode_literals
from __future__ import division as _division
from __future__ import print_function as _print_function

import pymel.core as pm
import maya.mel as mel

import random

from __Library__ import tk_pylib as tpl

from logging  import getLogger
logger = getLogger("set_texture_set")

class SetTextureSet(object):

    def set_pbs_material(self, meshes):
        u"""マテリアルを割り当て

        Args:
            meshes (list(string)): マテリアルを割り当てる対象のトランスフォームノード名
        """

        for mesh in meshes:
            if "Shape" in mesh:
                mesh = mesh.replace("Shape", "")
            pm.select(None)
            pbs = pm.shadingNode("StingrayPBS", asShader=True, name=mesh)
            logger.info("【Created Material】: {}".format(pbs))

            pm.sets(name="{}SG".format(pbs), renderable=True, noSurfaceShader=True, empty=True)
            pm.setAttr("{}.initgraph".format(pbs), True)
            pm.connectAttr("{}.outColor".format(pbs), "{}SG.surfaceShader".format(pbs))
            pm.select(mesh)
            pm.sets("{}SG".format(pbs), forceElement=True)

            self.set_random_color(pbs)

    def set_random_color(self, material_name):
        u"""ベースカラーにランダムな色を設定

        Args:
            material_name (string): ベースカラーを割り当てるマテリアルの名前
        """
        pm.setAttr("{}.base_color".format(material_name), (random.uniform(0, 1),
                                                           random.uniform(0, 1),
                                                           random.uniform(0, 1)))

    def execute(self):
        # ノードが選択されているか確認
        sel = pm.ls(selection=True)
        if len(sel) == 0:
            logger.error("【Selection Error】: Notiong selected. processing omitted")
            return

        tpl.OptimizeScene.delete_unused_nodes()

        # 子のトランスフォームノードを全て取得
        meshes = tpl.Node.get_children_from_selections(t="mesh")
        logger.info("【Target is】: {}".format(meshes))

        self.set_pbs_material(meshes)

        tpl.OptimizeScene.delete_unused_nodes()
        logger.info("【Executed】: Success")

def main():
    ins_set_texture_set = SetTextureSet()
    ins_set_texture_set.execute()
