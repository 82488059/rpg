#!/usr/bin/python
# -*- coding:utf-8 -*-
# ## 
import pygame 


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
