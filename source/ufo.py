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
        self._count = 4
        self._blast = []
        self._location_counter = 0
        
    def draw(self):
        
        self._bullet_counter += 1
        
        if self._bullet_counter == 40:
            print("leci sraka")
            for i in range(self._count):
                self._blast.append(Blast(self._x + (i * 200) , self._y+50, self._win))
                self._bullet_counter = 0

        if self._location_counter == 120:
            self._location_counter = 0
            rand = random.randint(0, 1500)
            self._x = rand
            
        self._hitbox.update(self._x, self._y)
        for i in range(self._count):
            self._win.blit(self.model, (self._x + (i * 200), self._y))

        if gl_player[0]._hitbox.isTouching(self._hitbox):
            gl_player[0].hit()

        for item in self._blast:
            item.draw()
            if gl_player[0]._hitbox.isTouching(item._hitbox):
                gl_player[0].hit()

        if time_freeze[0]:
            self._vel = 10
        else:
            self._vel = 20

        self._animation_counter += 1
        self._location_counter += 1



