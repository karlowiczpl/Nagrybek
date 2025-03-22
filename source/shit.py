import pygame

from const import bullet

from .hp import HitBox
from .singleton import gl_player, enemies

class Shit:
    def __init__(self, x, y, win):
        self._x = x
        self._y = y
        self._win = win
        self._bullets = []
        self._bullet_model = pygame.transform.scale(bullet, (50,100))
        self._hitbox = HitBox(50,40, self._win)
        self._vel = 40
        self._hide = False

    def draw(self) -> bool:
        if gl_player[0]._hitbox.isTouching(self._hitbox):
            self._hide = True

        if not self._hide:
            image = pygame.image.load("images/shit.png")
            transformed = pygame.transform.scale(image, (100,50))
            self._win.blit(transformed, (self._x, self._y))
            self._hitbox.update(self._x, self._y)
            self._hitbox.update(self._x, self._y)
            self._hitbox.draw()
        
        self._y += 10

    def hide(self):
        self._hide = True

class EnemyShit(Shit):
    def __init__(self, x, y, win):
        super().__init__(x, y, win)
        self._vel = 20

