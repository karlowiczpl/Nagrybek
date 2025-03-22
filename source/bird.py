import pygame

from const import(
    bird,
)
from .singleton import gl_player
from .hp import HitBox

class Bird:
    def __init__(self, y, win):
        self._y = y
        self._x = 1500
        self._win = win
        self._animation_counter = 0
        self._bird = []
        for item in bird:
            self._bird.append(pygame.transform.scale(item, (150,100)))
        self._hitbox = HitBox(150,100, win)
        
    def draw(self):
        if self._animation_counter == 15:
            self._animation_counter = 0

        self._win.blit(self._bird[self._animation_counter], (self._x, self._y))
        self._hitbox.update(self._x, self._y)

        if gl_player[0]._hitbox.isTouching(self._hitbox):
            gl_player[0].hit()

        self._x -= 20
        self._animation_counter += 1

