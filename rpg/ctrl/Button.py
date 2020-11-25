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
                 size=(100,30),
                 border_radius=3,
                 color=(10,200,0), 
                 downcolor=(10,200,0),
                 text="",
                 textcolor=(0,0,0),
                 font_family="./",
                 font_size=24):
        self.pos = pos
        self.size=size
        self.color=color
        self.downcolor=downcolor
        self.text=text
        self.textcolor = textcolor
        self.border_radius=border_radius
        self.font_size = font_size
        
        if not os.path.isfile(font_family):
            font_family = pygame.font.match_font(font_family)
        self.font_object = pygame.font.Font(font_family, font_size)

        self.textSurface=self.font_object.render(self.text, True, self.textcolor).convert_alpha()
        self.textrect = self.textSurface.get_rect()
        #self.textpos = self.pos
        self.textpos = (self.pos[0] + self.size[0]/2-self.textrect.w/2, self.pos[1] + self.size[1]/2-self.textrect.h/2 )
        self.btdown=False

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
        
        if self.isOver():
            #screen.blit(self.imageDown, (x, y))
            if self.btdown:
                pygame.draw.rect(screen, self.color, (x+1,y+1,w,h), border_radius=3)
                screen.blit(self.textSurface, (self.textpos[0]+1, self.textpos[1]+1))
            else:
                pygame.draw.rect(screen, self.color, (x-1,y-1,w,h), border_radius=3)
                screen.blit(self.textSurface, (self.textpos[0]-1, self.textpos[1]-1))
        else:
            #screen.blit(self.imageUp, (x, y))
            pygame.draw.rect(screen, self.color, (x,y,w,h), border_radius=3)
            screen.blit(self.textSurface, self.textpos)

    