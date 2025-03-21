import pygame

class Bullet:
    def __init__(self, x, y, win, left):
        self._win = win
        self._x = x + 40
        self._y = y + 25
        self._left = not left
        self._bullets = []

    def draw(self) -> bool:
        pygame.draw.circle(self._win, (0, 0, 0), (self._x, self._y), 7)

        if self._left:
            self._x += 20
        else:
            self._x -= 20
