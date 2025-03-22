import pygame

from const import (
    bg,
)
from .singleton import gl_player

class GameOver:
    def __init__(self, window):
        self._win = window
        self._info = pygame.display.Info()
        self._player = gl_player[0]
        self._dialog_on = False
        self._dialog_count = 0

    def draw(self):
        self._player._live = False
        background = pygame.transform.scale(bg, (self._info.current_w,self._info.current_h))
        self._win.blit(background, (0,0))

        return True

    def key(self, key):
        pass

    def handle_event(self, event):
        pass
