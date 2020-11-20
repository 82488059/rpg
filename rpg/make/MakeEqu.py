#!/usr/bin/python
# -*- coding:utf-8 -*-
# ## 

import pygame

import random
import GlobalVar
from equ import Equ
from Button import Button
from Button import ButtonRgb

upimage="src/bt.png"
downimage="src/bt.png"
bgimage="src/main.jpg"

#background = pygame.image.load(bgimage)
#backgroundrect = background.get_rect()
        

class MakeScreen(object):
    def __init__(self):
        self.x=0
        self.y=0
        self.sss=1
        self.bgimage="src/make.jpg"
        x=750
        y=90
        d=120
        self.btMake=Button(upimage, downimage, (650, 550))
        #self.btConf=Button(upimage, downimage, (x, 210))
        #self.btLoad=Button(upimage, downimage, (x, 330))
        #self.btExit=Button(upimage, downimage, (x, 450))
        self.bbtmake=ButtonRgb(pos=(50,50))
        
        self.select=Equ.EquBase()

        self.bg = pygame.image.load(self.bgimage).convert_alpha()
        self.myfont=pygame.font.Font(GlobalVar.font_family,20)
        self.cursor_surface = pygame.Surface((512, 768/2))
        
        

    def Render(self, screen):
        textImage=self.myfont.render("Hello Pygame",True, (0,255,0))

        self.cursor_surface.blit(textImage, (100,100))
        
        self.btMake.Render(self.cursor_surface)

        self.bbtmake.Render(self.cursor_surface)

        screen.blit(self.cursor_surface, (self.x, self.y))


       

        return 0

    def OnMake(self):

        textImage=self.myfont.render("Hello Pygame",True, (0,255,0))

        self.cursor_surface.blit(textImage, (100,100))


        return 0


    def Events(self, events):
        
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                if self.btMake.isOver():
                    self.OnMake()

        return 0


