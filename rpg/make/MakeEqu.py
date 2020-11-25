#!/usr/bin/python
# -*- coding:utf-8 -*-
# ## 

import pygame
import GlobalVar

from dialog.Dialog import Dialog
import random
from equ import Equ
from ctrl.Button import Button
from ctrl.Button import ButtonRgb
from ctrl.TextCtrl import TextCtrl

upimage="src/bt.png"
downimage="src/bt.png"
#background = pygame.image.load(bgimage)
#backgroundrect = background.get_rect()
        

class MakeScreen(Dialog):
    def __init__(self, pos=(0,0)):
        
        self.bgimage="src/铁匠铺.png"
        bgimage = pygame.image.load(self.bgimage).convert_alpha()
        f=GlobalVar
        Dialog.__init__(self, pos=((1024-703)/2, (768-535)/2), size=(703, 535), bkimage=bgimage,
                       font_family=GlobalVar.font_family, font_size=30)
        #self.cursor_surface.set_alpha(128)
        self.select=Equ.EquBase()
        x=self.pos[0]
        y=self.pos[1]
        #
        self.textColor=(0,0,0)

        self.title=TextCtrl(pos=(512-50, 133), text="装备炼化", size=(100, 30), width=1)
        # bt
        #self.btMake=Button(upimage, downimage, (x+120, y+400))
        #self.btReplace=Button(upimage, downimage, (x+420, y+400))
        # 
        self.btMake=ButtonRgb(pos=(x+150, y+350), text="炼化")
        self.btReplace=ButtonRgb(pos=(x+300, y+350), text="替换")
        self.btExit=ButtonRgb(pos=(x+450, y+350), text="退出")
        self.buttons=[]
        self.buttons.append(self.btMake)
        self.buttons.append(self.btReplace)
        self.buttons.append(self.btExit)
        # old
        self.showleft=[]
        self.showleft.append(TextCtrl(pos=(x+50, y+50), size=(150, 30), width=1))
        self.showleft.append(TextCtrl(pos=(x+50, y+100), size=(150, 30), width=1))
        self.showleft.append(TextCtrl(pos=(x+50, y+150), size=(150, 30), width=1))
        self.showleft.append(TextCtrl(pos=(x+50, y+200), size=(150, 30), width=1))
        self.showleft.append(TextCtrl(pos=(x+50, y+250), size=(150, 30), width=1))
        # new
        self.showright=[]
        self.showright.append(TextCtrl(pos=(x+512, y+50), size=(150, 30), width=1))
        self.showright.append(TextCtrl(pos=(x+512, y+100), size=(150, 30), width=1))
        self.showright.append(TextCtrl(pos=(x+512, y+150), size=(150, 30), width=1))
        self.showright.append(TextCtrl(pos=(x+512, y+200), size=(150, 30), width=1))
        self.showright.append(TextCtrl(pos=(x+512, y+250), size=(150, 30), width=1))
        # 
        # draw
        self.Draw()


    def Draw(self):
        return 0

    def Render(self, screen):
        
        Dialog.Render(self, screen)

        self.title.Render(screen)
        
        self.btMake.Render(screen)

        self.btReplace.Render(screen)

        # bt 
        for bt in self.buttons:
            bt.Render(screen)

        for ctrl in self.showleft:
            ctrl.Render(screen)
        for ctrl in self.showright:
            ctrl.Render(screen)
        #self.cursor_surface.set_alpha(128)
        return 0

    def OnMake(self):
        for ctrl in self.showright:
            r1 = str(random.randint(1, 100))
            ctrl.SetText(r1)

        return 0

    def OnExit(self):
        if GlobalVar.ScreenSelectedBack:
            GlobalVar.ScreenSelected=GlobalVar.ScreenSelectedBack[-1]
            GlobalVar.ScreenSelectedBack.pop()
        return 0

    def Events(self, events):
        
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                #if self.btMake.isOver():
                #    self.OnMake()
                if self.btMake.isOver():
                    self.OnMake()
                if self.btExit.isOver():
                    self.OnExit()
        return 0


