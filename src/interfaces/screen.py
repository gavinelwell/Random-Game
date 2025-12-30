import pygame

class Screen:
    def __init__(self, res=None, border_th=None, disp=None):
        
        # Default variables
        if res==None: res = (1280, 720)
        if border_th==None: border_th = 10
        if disp==None: disp = pygame.display.set_mode(res)

        self.res = res
        self.border_th = border_th
        self.disp = disp