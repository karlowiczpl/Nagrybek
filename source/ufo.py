import pygame
import random
from .movment import Movment
from .singleton import shits
from .shit import Shit

from const import(
    bird,
)
from .singleton import gl_player, time_freeze
from .hp import HitBox

class UFO(Movment):
    _vel = 20
    def __init__(self, y, win):
        self._y = y
        self._x = 1500
        self._win = win
        self._animation_counter = 0
        model = pygame.transform.scale(pygame.image.load("images/ufo.png"), (150,100))
        self._hitbox = HitBox(150,100, win)
        
    def draw(self):
        self._hitbox.update(self._x, self._y)

        if gl_player[0]._hitbox.isTouching(self._hitbox):
            gl_player[0].hit()

        if time_freeze[0]:
            self._vel = 10
        else:
            self._vel = 20

        self._x -= self._vel
        self._animation_counter += 1