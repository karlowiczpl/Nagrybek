import pygame
import random

from .hp import HitBox
from .singleton import gl_player, items

class Item:
    def __init__(self, x, y, window, player):
        self._x = x
        self._y = y
        self._win = window
        self._vel = (1500 - y) / 100 
        self._hitbox = HitBox(100, 100, window)
        self._player = player

        self._animation_count = 0
        self._animation = True
        self._hide = False

    def draw(self):
        if self._animation:
            if self._animation_count == 50:
                self._animation = False
            self._y += self._vel

            self._animation_count += 1

        if self._hitbox.isTouching(gl_player[0]._hitbox):
            self._hide = True
            rand1 = random.randint(100, 1500)
            rand2 = random.randint(100, 100)
            items[0] = (Item(rand1, rand2, self._win, self._player))
            self._player.hp_up()

        if not self._hide:
            pygame.draw.circle(self._win, (0x00,0x00,0x00), (self._x, self._y), 50)
            self._hitbox.update(self._x -50, self._y-50)
            self._hitbox.draw()
