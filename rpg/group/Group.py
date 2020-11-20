#!/usr/bin/python
# -*- coding:utf-8 -*-
# ## hero

# 

from role.HeroBase import HeroBase

class Group(object):
    def __init__(self):
        self.A=HeroBase()
        self.B=HeroBase()
        self.C=HeroBase()
        self.D=HeroBase()
        self.E=HeroBase()



    def load(self, savejson):
        groupjson = savejson['group']
        


        return 0



