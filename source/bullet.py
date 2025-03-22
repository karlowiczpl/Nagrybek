import pygame

from const import bullet

from .hp import HitBox
from .singleton import gl_player, enemies

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
        self._vel = 40
        self._hide = False

    def draw(self) -> bool:
        if gl_player[0]._hitbox.isTouching(self._hitbox):
            self._hide = True

        if not self._hide:
            self._win.blit(self._bullet_model, (self._x, self._y))
            self._hitbox.update(self._x+40, self._y+ 10)
            self._hitbox.draw()

        if self._left:
            self._x += self._vel
        else:
            self._x -= self._vel

    def hide(self):
        self._hide = True

class EnemyBullet(Bullet):
    def __init__(self, x, y, win, left):
        super().__init__(x, y, win, left)
        self._vel = 20

