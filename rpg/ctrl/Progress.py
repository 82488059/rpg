#!/usr/bin/python
# -*- coding:utf-8 -*-
# ## 
import pygame 
import os


class Progress(object):
    def __init__(self, 
                 pos=(0,0), 
                 size=(100,30),
                 border_radius=3,
                 color=(10,200,0), 
                 downcolor=(10,200,0),
                 now=95,
                 max=100,
                 text="",
                 textcolor=(0,0,0),
                 font_family="./SIMYOU.TTF",
                 font_size=24):
        self.pos = pos
        self.size=size
        self.color=color
        self.downcolor=downcolor
        self.text=text
        self.textcolor = textcolor
        self.border_radius=border_radius
        self.font_size = font_size
        self.now=now
        self.max=max
        if not os.path.isfile(font_family):
            font_family = pygame.font.match_font(font_family)
        self.font_object = pygame.font.Font(font_family, font_size)

        self.textSurface=self.font_object.render(self.text, True, self.textcolor).convert_alpha()
        self.textrect = self.textSurface.get_rect()
        #self.textpos = self.pos
        self.textpos = (self.pos[0] + self.size[0]/2-self.textrect.w/2, self.pos[1] + self.size[1]/2-self.textrect.h/2 )
        self.pro=self.now*1.0/self.max

    def isOver(self):
        point_x,point_y = pygame.mouse.get_pos()
        x, y = self. pos
        w, h = self.size
        #in_x = x - w/2 < point_x < x + w/2
        #in_y = y - h/2 < point_y < y + h/2
        in_x = x < point_x < x + w
        in_y = y < point_y < y + h
        return in_x and in_y

    def setNow(self, now):

        self.textSurface=self.font_object.render(self.text, True, self.textcolor).convert_alpha()
        self.textrect = self.textSurface.get_rect()
        self.textpos = (self.pos[0] + self.size[0]/2-self.textrect.w/2, self.pos[1] + self.size[1]/2-self.textrect.h/2 )
        
        self.now=now
        self.pro=self.now/self.max*0.01

        return 0
    
    def Render(self, screen):
        w, h = self.size
        x, y = self.pos
        
        if self.isOver():
            pygame.draw.rect(screen, self.downcolor, (x,y,w,h), border_radius=3)
            pygame.draw.rect(screen, self.color, (x+1,y+1,(w-2)*self.pro,h-2), border_radius=3)
            screen.blit(self.textSurface, self.textpos)
        else:
            pygame.draw.rect(screen, self.downcolor, (x,y,w,h), border_radius=3)
            pygame.draw.rect(screen, self.color, (x+1,y+1,(w-2)*self.pro,h-2), border_radius=3)
            screen.blit(self.textSurface, self.textpos)

    