#!/usr/bin/python
# -*- coding:utf-8 -*-
# ## 
import pygame 
import os

class TextCtrl(object):
    def __init__(self, 
                 pos=(0,0), 
                 size=(100,30),
                 width=0,
                 border_radius=3,
                 color=(111,0,0), 
                 text="",
                 textcolor=(0,0,0),
                 font_family="./SIMYOU.TTF",
                 font_size=24):
        self.pos = pos
        self.size=size
        self.color=color
        self.text=text
        self.textcolor = textcolor
        self.border_radius=border_radius
        self.font_size = font_size
        self.width=width
        if not os.path.isfile(font_family):
            font_family = pygame.font.match_font(font_family)
        self.font_object = pygame.font.Font(font_family, font_size)

        self.textSurface=self.font_object.render(self.text, True, self.textcolor).convert_alpha()
        self.textrect = self.textSurface.get_rect()

        self.textpos = (self.pos[0] + self.size[0]/2-self.textrect.w/2, self.pos[1] + self.size[1]/2-self.textrect.h/2 )

    def SetText(self, text):
        self.text = text
        self.textSurface=self.font_object.render(self.text, True, self.textcolor).convert_alpha()
        self.textrect = self.textSurface.get_rect()
        self.textpos = (self.pos[0] + self.size[0]/2-self.textrect.w/2, self.pos[1] + self.size[1]/2-self.textrect.h/2 )
        return 0;


    def isOver(self):
        point_x,point_y = pygame.mouse.get_pos()
        x, y = self. pos
        w, h = self.size
        #in_x = x - w/2 < point_x < x + w/2
        #in_y = y - h/2 < point_y < y + h/2
        in_x = x < point_x < x + w
        in_y = y < point_y < y + h

        return in_x and in_y

    def Render(self, screen):
        w, h = self.size
        x, y = self.pos
        #screen.blit(self.imageUp, (x, y))
        pygame.draw.rect(screen, self.color, (x,y,w,h),width=self.width, border_radius=3)
        screen.blit(self.textSurface, self.textpos)

    