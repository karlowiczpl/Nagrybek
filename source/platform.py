import pygame
from .hp import HitBox
from .movment import Movment
from .motion_animation import PlatformaAnimation
from const import ground

class Platform(Movment, PlatformaAnimation):
    def __init__(self, x, y, width, height, window, model, is_moving=False, speed=5):
        self._x = x
        self._y = y

        self._width = width
        self._height = height
        self._window = window
        self.is_moving = is_moving
        self.speed = speed
        self.direction = 1  

        self._hitbox = HitBox(width-300, height, window)
        self._hitbox.update(x, y)
        self.model = ground
        self.scaled_model = pygame.transform.scale(self.model, (self._width, self._height))
        self.set_size(width, height)


    def draw(self):
        self._window.blit(self.scaled_model, (self._x, self._y))

    def set_size(self, new_width, new_height):
        self._width = new_width
        self._height = new_height
        self.scaled_model = pygame.transform.scale(self.model, (self._width, self._height))
        self._hitbox.update(self._x+150, self._y+30)

