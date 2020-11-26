
#!/usr/bin/python
# -*- coding:utf-8 -*-
# ## 
import pygame

class Dialog(object):
    def __init__(self, pos=(0,0), size=(1024,768), bkimage=None, 
                 font_family=None,font_size=30):

        self.pos=pos
        self.size=size
        self.bkimage=bkimage
        self.font_family=font_family
        self.font=pygame.font.Font(font_family, 20)
        self.cursor_surface = pygame.Surface(size).convert_alpha()

    def Render(self, screen):
        screen.blit(self.bkimage, self.pos)
        return 0


    def Events(self, events):
        
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                if self.btMake.isOver():
                    self.OnMake()

        return 0


    def OnExit(self):
        if GlobalVar.ScreenSelectedBack:
            GlobalVar.ScreenSelected=GlobalVar.ScreenSelectedBack[-1]
            GlobalVar.ScreenSelectedBack.pop()
        return 0

    