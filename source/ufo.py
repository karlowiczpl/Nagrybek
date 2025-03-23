import pygame
import random
from .movment import Movment
from .singleton import shits,blasts
from .shit import Shit
from .blast import Blast

from const import(
    bird,
)
from .singleton import gl_player, time_freeze
from .hp import HitBox






class UFO(Movment):
    _vel = 20
    def __init__(self, x, y, win):
        self._y = y
        self._x = x
        self._win = win
        self._animation_counter = 0
        self._bullet_counter = 0
        self.model = pygame.transform.scale(pygame.image.load("images/alien.png"), (150,100))
        self._hitbox = HitBox(150,100, win)
        
    def draw(self):
        
        self._bullet_counter += 1
        
        if self._bullet_counter == 40:
            blasts.append(Blast(self._x, self._y, self._win))
            self._bullet_counter = 0
            
        
        self._hitbox.update(self._x, self._y)
        self._win.blit(self.model, (self._x, self._y))

        if gl_player[0]._hitbox.isTouching(self._hitbox):
            gl_player[0].hit()

        if time_freeze[0]:
            self._vel = 10
        else:
            self._vel = 20
        self._animation_counter += 1
        
        



