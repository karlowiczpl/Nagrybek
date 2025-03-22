import pygame
from .hp import HitBox
from .movment import Movment
from .motion_animation import PlatformaAnimation

class Platform(Movment, PlatformaAnimation):
    def __init__(self, x, y, width, height, window, model, is_moving=False, speed=5,):
        self._x = x
        self._y = y
        self._hitbox = HitBox(width, height, window)
        self._hitbox.update(x, y)
        self._window = window
        self.is_moving = is_moving
        self.model = model
        self.speed = speed
        self.direction = 1  

    def draw(self):
        self._hitbox.draw()
        
    
        
