import pygame

from .motion_animation import Animation, PlayerAnimation

class Movment:
    _vel = 20

    def walk_right(self):
        if self._x > 0:
            self._left = True
            self._right = False

            self._x -= self._vel
            self._last_postion = False
            self._motion_counter += 1

    def walk_left(self):
        if self._x < 1700:
            self._left = False
            self._right = True

            self._x += self._vel
            self._motion_counter += 1
            self._last_postion = True


    def stand(self):
        self._left = False
        self._right = False

    def jump(self):
        # if self._after_jump > 40:
            self._jump = True
            self._after_jump = 0

    def dodge(self):
        print(self._dodge)
        if self._dodge is False:
            self._hitbox = (0,0,0,0)
            self._dodge = True
            print("B")
        else:
            self._hitbox = (self._x + 20 , self._y, 28, 60)
            print("C")
            
