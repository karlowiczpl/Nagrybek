import pygame

from const import (
    bg
)

class button:
    def __init__(self, x, y, window):
        self._x = x
        self._y = y
        self._win = window

    def draw(self):
        pass


class Start:
    def __init__(self, window):
        self._win = window
        self._info = pygame.display.Info()

    def draw(self):
        
        background = pygame.transform.scale(bg, (self._info.current_w,self._info.current_h))
        self._win.blit(background, (0,0))
        
