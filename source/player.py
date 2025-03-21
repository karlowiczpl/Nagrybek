import pygame

from .hp import Hp
from .movment import Movment
from .bullet import Bullet

from const import(
    CONF_PLAYER_HEIGHT,
    CONF_PLAYER_WIDTH,
)

class Player(Movment):
    def __init__(self, window):
        self._x = 50
        self._y = 600
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
        self._hitbox = (self._x + 20 , self._y, 28, 60)
        for item in self.walkLeftx:
            self.walkLeft.append(pygame.transform.scale(item, (CONF_PLAYER_WIDTH,CONF_PLAYER_HEIGHT)))
        for item in self.walkRightx:
            self.walkRight.append(pygame.transform.scale(item, (CONF_PLAYER_WIDTH,CONF_PLAYER_HEIGHT)))
        self.standing = pygame.transform.scale(self.standing, (CONF_PLAYER_WIDTH,CONF_PLAYER_HEIGHT))
        self._hp = Hp(window, 100, 100)

    def bullet(self, enemy):
        if self._bullet_delay > 10:
            self._bullets.append(Bullet(self._x, self._y, self._win, self._left))
            self._bullet_delay = 0
            self._enemy = enemy

    def draw(self):
        self._hp.draw()
        if self._jump:
            if self._jump_counter > 0:
                self._y += (self._jump_counter**2) 
            else:
                self._y -= (self._jump_counter**2)

            self._jump_counter += 1
            if self._jump_counter == 11:
                self._jump = False
                self._jump_counter = -10

        if self._left:
            self._win.blit(self.walkLeft[self._motion_counter // 1], (self._x, self._y))
        elif self._right:
            self._win.blit(
                self.walkRight[self._motion_counter // 1], (self._x, self._y)
            )
        else:
            self._win.blit(self.standing, (self._x, self._y))

        if self._motion_counter == 8:
            self._motion_counter = 0

        for bullet in self._bullets:
            if bullet._y - 5 < self._enemy._hitbox[1] + self._enemy._hitbox[3] and bullet._y + 5  > self._enemy._hitbox[1]:
                if bullet._x + 5 > self._enemy._hitbox[0] and bullet._x  - 5> self._enemy._hitbox[0] + self._enemy._hitbox[2]:
                    self._enemy.hit()
                    self._bullets.pop(self._bullets.index(bullet))

            bullet.draw()

        self._after_jump += 1
        self._bullet_delay += 1
        
        if self._dodge is True:
            print("dodging")
            self._dodge_counter += 1
        
        if self._dodge_counter == 5 and self._dodge is True:
            self._dodge = False
            self._dodge_counter = 0
            
        
            
