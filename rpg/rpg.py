#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import re
import os
import pygame
import StartScreen
import save 
import GlobalVar
from make import MakeEqu


pygame.init()  # 初始化pygame

infoObject = pygame.display.Info()
# full screen
screensize=(infoObject.current_w, infoObject.current_h)
screenflags=flags=pygame.FULLSCREEN | pygame.HWSURFACE | pygame.DOUBLEBUF
# window
screensize=(1024, 768)
screenflags=pygame.HWSURFACE | pygame.DOUBLEBUF
# 
screen = pygame.display.set_mode(size=screensize, flags=screenflags)



def load():



    return 0



def run():
    clock = pygame.time.Clock()

    sc = StartScreen.StartScreen()
    scmake = MakeEqu.MakeScreen()

    GlobalVar.ScreenSelected=GlobalVar.SCREENMAKE
    #GlobalVar.ScreenSelected=GlobalVar.SCREENMAIN

     
    while True:
        events = pygame.event.get()

        if GlobalVar.SCREENCONF == GlobalVar.ScreenSelected:
            print("conf screen")
        elif GlobalVar.SCREENLOAD == GlobalVar.ScreenSelected:
            print("load screen")
        elif GlobalVar.SCREENGAME == GlobalVar.ScreenSelected:
            print("game screen")
        elif GlobalVar.SCREENMAIN == GlobalVar.ScreenSelected:
            # print("one screen")
            sc.Events(events)
            sc.Render(screen)
        elif GlobalVar.SCREENMAKE == GlobalVar.ScreenSelected:
            # print("one screen")
            scmake.Events(events)
            scmake.Render(screen)

        for event in events:   
            if event.type == pygame.QUIT:  
                exit(0)
        
        pygame.display.update()  # 更新显示
        clock.tick(30)

    return 0

if __name__ == "__main__":
    GlobalVar.font_family = pygame.font.match_font("./SIMYOU.TTF")

    if run():
        print('make done!')
    else:
        print('make rc error!')

