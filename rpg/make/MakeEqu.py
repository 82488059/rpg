#!/usr/bin/python
# -*- coding:utf-8 -*-
# ## 

import pygame
import GlobalVar

from dialog.Dialog import Dialog
import random
from equ import Equ
from Button import Button
from Button import ButtonRgb

upimage="src/bt.png"
downimage="src/bt.png"
#background = pygame.image.load(bgimage)
#backgroundrect = background.get_rect()
        

class MakeScreen(Dialog):
    def __init__(self):
        self.bgimage="src/铁匠铺.png"
        bgimage = pygame.image.load(self.bgimage).convert_alpha()
        f=GlobalVar
        GlobalVar.font_family = pygame.font.match_font("SIMYOU.TTF")

        Dialog.__init__(self, pos=(0,0), size=(1024,768), bkimage=bgimage,
                       font_family=GlobalVar.font_family, font_size=30)
        
        GlobalVar.font_family = pygame.font.match_font("./SIMYOU.TTF")

        self.x=0
        self.y=0
        self.sss=1
        x=750
        y=90
        d=120
        self.btMake=Button(upimage, downimage, (120, 400))
        self.btReplace=Button(upimage, downimage, (420, 400))
        
        self.select=Equ.EquBase()

        self.cursor_surface.set_alpha(128)

        
        self.textColor=(255,0,255)
        self.lineColor=(255,0,255)

        # draw
        self.Draw()


    def Draw(self):
        self.DrawBg()
        
        return 0

    def Render(self, screen):
        
        # Dialog.Render(self, screen)

        textImage=self.font.render("Hello Pygame", True, self.textColor)

        self.cursor_surface.blit(textImage, (100,100))
        
        self.btMake.Render(self.cursor_surface)

        self.btReplace.Render(self.cursor_surface)

        self.cursor_surface.set_alpha(128)

        screen.blit(self.cursor_surface, (self.x, self.y))

        return 0

    def OnMake(self):

        textImage=self.font.render("Hello Pygame",True, (0,255,0))

        self.cursor_surface.blit(textImage, (100,100))


        return 0


    def Events(self, events):
        
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                if self.btMake.isOver():
                    self.OnMake()

        return 0


