#!/usr/bin/python
# -*- coding:utf-8 -*-
# ## 

import pygame
import GlobalVar

from role.HeroBase import HeroBase


class Combat(object):
    def __init__(self):
        ""
    
        self.bgimage=None

        self.items=[]
        self.monsters=[]
        
        self.bgimage="src/combat.jpg"
        self.bg = pygame.image.load(self.bgimage).convert_alpha()

    
    def SetItems(self, items):
        self.items.clear()
        self.items.append(HeroBase(pos=(12, 640)))
        self.items.append(HeroBase(pos=(212, 640)))
        self.items.append(HeroBase(pos=(412, 640)))
        self.items.append(HeroBase(pos=(612, 640)))
        self.items.append(HeroBase(pos=(812, 640)))
        
        return 0

    def SetMonsters(self, monsters):

        self.monsters.clear()
        self.monsters.append(HeroBase(pos=(12, 20)))
        self.monsters.append(HeroBase(pos=(212, 20)))
        self.monsters.append(HeroBase(pos=(412, 20)))
        self.monsters.append(HeroBase(pos=(612, 20)))
        self.monsters.append(HeroBase(pos=(812, 20)))

        return 0

    def Render(self, screen):
        screen.blit(self.bg, (0, 0))

        for mon in self.monsters:
            mon.Render(screen)
        
        for hero in self.items:
            hero.Render(screen)

        return 0

    def Events(self, events):

        return 0


