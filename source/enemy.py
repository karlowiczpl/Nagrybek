import pygame
import random

from .hp import Hp, HitBox
from .movment import Movment
from .bullet import EnemyBullet
from .motion_animation import EnemyAnimation
from .singleton import gl_player, time_freeze

from const import(
    CONF_PLAYER_HEIGHT,
    CONF_PLAYER_WIDTH,
)

class Enemy(Movment, EnemyAnimation):
    def __init__(self, window, x, y):
        self._x = x
        self._y = 650
        self._win = window
        self._left = False
        self._right = False
        self._motion_counter = 0
        self._dodge_counter = 0
        self._jump = False
        self._dodge = False
        self._jump_counter = -10
        self._dodge = False
        self._after_jump = 0
        self._bullets = []
        self._bullet_delay = 0
        self._hide = False
        self._hitbox = HitBox(97, 200, window)
        self._freeze = True
        for item in self.walkLeftx:
            self.walkLeft.append(pygame.transform.scale(item, (CONF_PLAYER_WIDTH,CONF_PLAYER_HEIGHT)))
        for item in self.walkRightx:
            self.walkRight.append(pygame.transform.scale(item, (CONF_PLAYER_WIDTH,CONF_PLAYER_HEIGHT)))
        self.standing = pygame.transform.scale(self.standing, (CONF_PLAYER_WIDTH,CONF_PLAYER_HEIGHT))
        self._kill = False
        self._bullet_counter = 0
        self._vel = 7
        self._time_frezze_timer = 0
        self._rand = 100
        self._hp = 25

    def kill(self):
        self._hp -= 1
        if self._hp < 0:
            self._kill = True

    def update(self):
        self._bullet_counter += 1
        if self._bullet_counter == self._rand:
            self.bullet(not (gl_player[0]._x > self._x))
            self._bullet_counter = 0

        if (gl_player[0]._x > self._x):
            self.walk_left()
        else:
            self.walk_right()

    def bullet(self, left=None):
            if left:
                self._bullets.append(EnemyBullet(self._x , self._y, self._win, left))
            else:
                self._bullets.append(EnemyBullet(self._x, self._y, self._win, self._left))
            self._bullet_delay = 0
            self._rand = random.randint(0, 70)
            print("bullet")

    def move_towards_target(self, target_x, target_y):
        if self.x < target_x:
            self.walk_right()
        elif self.x > target_x:
            self.walk_left()

    def draw(self):
        if time_freeze[0]:
            self._vel = 3
        else:
            self._vel = 7

        if not self._kill:
            self.update()
            if self._jump:
                if self._jump_counter > 0:
                    self._y += (self._jump_counter**2) / 2
                else:
                    self._y -= (self._jump_counter**2) / 2

                self._jump_counter += 1
                if self._jump_counter == 11:
                    self._jump = False
                    self._jump_counter = -10
            if not self._hide:
                if time_freeze[0]:
                    if self._left:
                        self._win.blit(self.walkLeft[self._time_frezze_timer // 5], (self._x, self._y))
                    elif self._right:
                        self._win.blit(
                            self.walkRight[self._time_frezze_timer// 5], (self._x, self._y)
                        )
                    else:
                        self._win.blit(self.standing, (self._x, self._y))
                else:
                    if self._left:
                        self._win.blit(self.walkLeft[self._motion_counter // 3], (self._x, self._y))
                    elif self._right:
                        self._win.blit(
                            self.walkRight[self._motion_counter // 3], (self._x, self._y)
                        )
                    else:
                        self._win.blit(self.standing, (self._x, self._y))

            if self._motion_counter == 26:
                self._motion_counter = 0

            if self._time_frezze_timer == 52:
                self._time_frezze_timer = 0

            for bullet in self._bullets:
                bullet.draw()
                if gl_player[0]._hitbox.isTouching(bullet._hitbox):
                    gl_player[0].hit()
                    # bullet._hide()

            if gl_player[0]._hitbox.isTouching(self._hitbox) and not self._hide:
                gl_player[0].hit()

            self._time_frezze_timer += 1
            self._after_jump += 1
            self._bullet_delay += 1
            self._hitbox.update(self._x + 50, self._y + 53)
            self._hitbox.draw()
