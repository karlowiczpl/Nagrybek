import pygame

from const import (
    bg
)
from .dialogue import Dialog

sample_dialog = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electroni"

class button:
    def __init__(self, x, y, window):
        self._x = x
        self._y = y
        self._win = window

    def draw(self):
        pass

class Start:
    def __init__(self, window, player):
        self._win = window
        self._info = pygame.display.Info()
        self._player = player
        self._dialog = Dialog(sample_dialog, "jan", self._win)
        self._active_dialog = True

    def draw(self):
        background = pygame.transform.scale(bg, (self._info.current_w,self._info.current_h))
        self._win.blit(background, (0,0))
        self._player.draw()
        if self._active_dialog:
            self._active_dialog = self._dialog.draw()

    def key(self, key):
        if key[pygame.K_w]:
            self._player.jump()
        if key[pygame.K_d]:
            self._player.walk_left()
        if key[pygame.K_a]:
            self._player.walk_right()
