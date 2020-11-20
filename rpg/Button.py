#!/usr/bin/python
# -*- coding:utf-8 -*-
# ## 
import pygame 
import os


class Button(object):
    def __init__(self, upimage, downimage, position):
        self.imageUp = pygame.image.load(upimage).convert_alpha()
        self.imageDown = pygame.image.load(downimage).convert_alpha()
        self.position = position

    def isOver(self):
        point_x,point_y = pygame.mouse.get_pos()
        x, y = self. position
        w, h = self.imageUp.get_size()
        #in_x = x - w/2 < point_x < x + w/2
        #in_y = y - h/2 < point_y < y + h/2
        in_x = x < point_x < x + w
        in_y = y < point_y < y + h

        return in_x and in_y

    def Render(self,screen):
        w, h = self.imageUp.get_size()
        x, y = self.position
        
        if self.isOver():
            #screen.blit(self.imageDown, (x-w/2,y-h/2))
            screen.blit(self.imageDown, (x, y))
        else:
            #screen.blit(self.imageUp, (x-w/2, y-h/2))
            screen.blit(self.imageUp, (x, y))


class ButtonRgb(object):
    def __init__(self, 
                 pos=(0,0), 
                 size=(100,20),
                 color=(10,200,0), 
                 downcolor=(10,200,0),
                 textcolor=(0,0,0),
                 font_family="./",
                 font_size=35):
        self.position = pos
        self.size=size
        self.color=color
        self.downcolor=downcolor
        self.textcolor = textcolor

        self.font_size = font_size
        
        if not os.path.isfile(font_family):
            font_family = pygame.font.match_font(font_family)
        self.font_object = pygame.font.Font(font_family, font_size)



    def isOver(self):
        point_x,point_y = pygame.mouse.get_pos()
        x, y = self. position
        w, h = self.size
        #in_x = x - w/2 < point_x < x + w/2
        #in_y = y - h/2 < point_y < y + h/2
        in_x = x < point_x < x + w
        in_y = y < point_y < y + h

        return in_x and in_y

    def Render(self,screen):
        w, h = self.size
        x, y = self.position
        
        if self.isOver():
            #screen.blit(self.imageDown, (x, y))
            pygame.draw.rect(screen, self.color, (x,y,w,h))
        else:
            #screen.blit(self.imageUp, (x, y))
            pygame.draw.rect(screen, self.color, (x,y,w,h))