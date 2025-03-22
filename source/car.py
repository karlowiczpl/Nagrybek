import pygame

from const import car
from .singleton import gl_player
from .hp import HitBox

class Car:
    def __init__(self, window):
        self._win = window
        self._x = -1000
        self._y = 750
        self._car_img = []
        self._hitbox = HitBox(300,150,window)
        self._counter = 0
        for c in car:
            self._car_img.append(pygame.transform.scale(c, (300,150)))

    def draw(self):
        self._counter += 1
        self._win.blit(self._car_img[self._counter], (self._x, self._y))
        self._x += 40

        if self._counter == 3:
            self._counter = 0

        if self._x > 5000:
            self._x = -1000

        if gl_player[0]._hitbox.isTouching(self._hitbox):
            gl_player[0].hit()

        self._hitbox.update(self._x , self._y)

