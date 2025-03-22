import pygame

from const import bullet

from .hp import HitBox

class Bullet:
    def __init__(self, x, y, win, left):
        self._win = win
        self._left = not left
        self._bullets = []
        self._bullet_model = pygame.transform.scale(bullet, (50,100))
        if self._left:
            self._bullet_model = pygame.transform.rotate(self._bullet_model, 270)
            self._x = x + 130
            self._y = y + 100
        else:
            self._bullet_model = pygame.transform.rotate(self._bullet_model, 90)
            self._x = x
            self._y = y + 100
        self._hitbox = HitBox(50,40, self._win)

    def draw(self) -> bool:
        self._win.blit(self._bullet_model, (self._x, self._y))

        if self._left:
            self._x += 40
        else:
            self._x -= 40

        self._hitbox.update(self._x-10, self._y+ 10)
        self._hitbox.draw()
