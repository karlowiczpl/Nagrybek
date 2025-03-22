import pygame
from hp import HitBox
from movment import Movment



class Platform(Movment):
    def __init__(self, x, y, width, height, window, model, is_moving=False, speed=5,):
        self._hitbox = HitBox(width, height, window)
        self._hitbox.update(x, y)
        self._window = window
        self.is_moving = is_moving
        self.model = model
        self.speed = speed
        self.direction = 1  # 1 = right, -1 = left

    def update(self):
        return 

    def draw(self):
        return
        
