import pygame

from .hp import Hp
from .movment import Movment
from .bullet import Bullet
from .motion_animation import PlayerAnimation
from .hp import HitBox
from .singleton import enemies, ptr
from .game_over import GameOver
from .platform import Platform
from .singleton import enemies,platforms

from const import(
    CONF_PLAYER_HEIGHT,
    CONF_PLAYER_WIDTH,
)

class Player(Movment, PlayerAnimation):
    def __init__(self, window):
        self._x = 50
        self._y = 750
        self._win = window
        self._left = False
        self._right = False
        self._motion_counter = 0
        self._dodge_counter = 0
        self._jump = False
        self._dodge = False
        self._jump_counter = -10
        self._dodge = False
        self._after_jump = 40
        self._bullets = []
        self._bullet_delay = 0
        self._hitbox = HitBox(100, 197, self._win)
        self._live = True
        self._fall_counter = 0
        self._disable = False

        for item in self.walkLeftx:
            self.walkLeft.append(pygame.transform.scale(item, (CONF_PLAYER_WIDTH,CONF_PLAYER_HEIGHT)))
        for item in self.walkRightx:
            self.walkRight.append(pygame.transform.scale(item, (CONF_PLAYER_WIDTH,CONF_PLAYER_HEIGHT)))

        self.standing = pygame.transform.scale(self.standing, (CONF_PLAYER_WIDTH,CONF_PLAYER_HEIGHT))
        self._hp = Hp(window, 100, 100)
        self._last_postion = True

    def hit(self):
        if not self._hp.hp_down(1):
            ptr[0] = GameOver(self._win)

    def hp_up(self):
        self._hp.hp_down(-1)

    def bullet(self):
        if self._bullet_delay > 10:
            if not self._left and not self._right:
                self._bullets.append(Bullet(self._x, self._y, self._win, not self._last_postion))
                self._bullet_delay = 0
            else:
                self._bullets.append(Bullet(self._x, self._y, self._win, self._left))
                self._bullet_delay = 0

    def move_y(self):
        for platform in platforms:
            if self._hitbox.isTouching(platform._hitbox) and not self._disable:
                self._disable = True
                self._jump = False
                self._jump_counter = -10
                x1, y1, w1, h1 = self._hitbox._hitbox
                # self._y = y1 
        
        if self._jump:
            if self._jump_counter > 0:
                self._y += (self._jump_counter**2)  
            else:
                self._y -= int((self._jump_counter**2) )
                self._disable = False

            if self._jump_counter == 11:
                self._jump = False  
                if self._y >= 650:
                    if self._y + int((self._jump_counter**2)) <= 650:
                        self._y += int((self._jump_counter**2) )
                    else:
                        self._y = 650
                        self._jump_counter = -10
                        self._jump = False
                else:
                    self._y += int((self._jump_counter**2) )
            else:
                self._jump_counter += 1
    def draw(self):
        if self._live:
            self._hp.draw()
            self.move_y()

            if self._left:
                self._win.blit(self.walkLeft[self._motion_counter // 1], (self._x, self._y))
            elif self._right:
                self._win.blit(self.walkRight[self._motion_counter // 1], (self._x, self._y))
            else:
                self._win.blit(self.standing, (self._x, self._y))

            if self._motion_counter == 8:
                self._motion_counter = 0

            self._hitbox.update(self._x + 50, self._y + 53)
            self._hitbox.draw()

            for bullet in self._bullets:
                bullet.draw()  

                for enemy in enemies:
                    if bullet._hitbox.isTouching(enemy._hitbox):
                        enemy.kill()  

            self._after_jump += 1  
            self._bullet_delay += 1  

            if self._dodge is True:
                self._dodge_counter += 1

            if self._dodge_counter == 5 and self._dodge is True:
                self._dodge = False  
                self._dodge_counter = 0  
                
