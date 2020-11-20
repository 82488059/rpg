#!/usr/bin/python
# -*- coding:utf-8 -*-
# ## 装备

# type 
# 1 hp
# 2 mp
# 3 atk
# 4 def 
# 4 jin
# 5 mu
TYPE_HP=1
TYPE_MP=2
TYPE_ATK=3
TYPE_DEF=4
TYPE_ATKJIN=5
TYPE_ATKMU=6
TYPE_ATKTU=7
TYPE_ATKSHUI=8
TYPE_ATKHUO=9
TYPE_DEFJIN=10
TYPE_DEFMU=11
TYPE_DEFTU=12
TYPE_DEFSHUI=13
TYPE_DEFHUO=14


class EquBase (object):
    def __init(self):
        self.name=""
        # 原始属性
        self.base={}
        # 额外属性
        self.ext={}


    def load(self, savejson):
        savejson={}
        #
        savejson['base1']={}
        savejson['base2']={}
        savejson['base3']={}
        #
        savejson['ext1']={}
        
        savejson['ext2']={}
        
        savejson['ext3']={}


        return 0