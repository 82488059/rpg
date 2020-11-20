#!/usr/bin/python
# -*- coding:utf-8 -*-
# ## 

import pygame
import GlobalVar

from Button import Button

upimage="src/bt.png"
downimage="src/bt.png"
bgimage="src/main.jpg"

#background = pygame.image.load(bgimage)
#backgroundrect = background.get_rect()
        

class StartScreen(object):
    def __init__(self):
        self.sss=1
        self.bgimage="src/main.jpg"
        x=750
        y=90
        d=120
        self.btStart=Button(upimage, downimage, (x, 90))
        self.btConf=Button(upimage, downimage, (x, 210))
        self.btLoad=Button(upimage, downimage, (x, 330))
        self.btExit=Button(upimage, downimage, (x, 450))
        
        #self.buttons.append(self.btStart)
        #self.buttons.append(self.btConf)
        #self.buttons.append(self.btLoad)
        #self.buttons.append(self.btExit)
        
        self.bg = pygame.image.load(self.bgimage).convert_alpha()


    def Render(self, screen):
        screen.blit(self.bg, (0, 0))

        self.btStart.Render(screen)
        self.btConf.Render(screen)
        self.btLoad.Render(screen)
        self.btExit.Render(screen)

        return 0

    def OnStart(self):

        return 0
    def OnConf(self):

        return 0
    def OnLoad(self):

        return 0

    def OnExit(self):
        GlobalVar.ScreenSelected=GlobalVar.SCREENMAKE
        return 0


    def Events(self, events):

        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                if self.btStart.isOver():
                    self.OnStart()
                if self.btConf.isOver():
                    self.OnConf()
                if self.btLoad.isOver():
                    self.OnLoad()
                if self.btExit.isOver():
                    self.OnExit()
        return 0

