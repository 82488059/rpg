#!/usr/bin/python
# -*- coding:utf-8 -*-
# ## hero

# 
import pygame 
from ctrl.Progress import Progress


class HeroBase(object):
    def __init__(self):
        #
        self.pos 
        self.image
        self.hpProgress=Progress()
        self.mpProgress=Progress()

        self.hpBase
        self.mpBase

        # 最高血
        self.hpMax=0
        # 最高法
        self.mpMax=0
        # 等级
        self.level=1
        # 经验
        self.exp=0
        # 当前血
        self.hp=0
        # 当前法
        self.mp=0

        # 装备
        self.wuqi=None
        self.maozi=None
        self.yifu=None
        self.xiezi=None

        # 攻防
        self.defJin=0
        self.defMu=0
        self.defShui=0
        self.defHuo=0
        self.defTu=0
        self.defWuli=0
        self.atkJin=0
        self.atkMu=0
        self.atkShui=0
        self.atkHuo=0
        self.atkTu=0
        self.atkWuli=0

    def load(self, savejson):

        return 0

    
    def Render(self, screen):
        screen.blit(self.image, self.pos)


        return 0


    def Events(self, events):
        return 0