import pygame
import random

from .hp import HitBox
from .singleton import gl_player, items, isplaying
from const import xdskajdksa

class Item:
    def __init__(self, x, y, window, player):
        self._x = x
        self._y = y
        self._win = window
        self._vel = (1500 - y) / 100 
        self._hitbox = HitBox(100, 100, window)
        self._player = player
        self._img = []
        for item in xdskajdksa:
            self._img.append(pygame.transform.scale(item, (100,100)))

        self._animation_count = 0
        self._animation = True
        self._hide = False
        self._number = random.randint(0,2)

    def draw(self):
        if self._animation:
            if self._animation_count == 50:
                self._animation = False
            self._y += self._vel

            self._animation_count += 1

        if self._hitbox.isTouching(gl_player[0]._hitbox):
            isplaying[0] = False
            self._hide = True
            rand1 = random.randint(100, 1500)
            rand2 = random.randint(100, 100)
            items[0] = (Item(rand1, rand2, self._win, self._player))
            self._player.hp_up()

        if not self._hide:
            self._win.blit(self._img[self._number], (self._x-50, self._y-50))
            self._hitbox.update(self._x -50, self._y-50)
 
            if  not isplaying[0] and not isplaying[2]:
                isplaying[0] = True
                channel = pygame.mixer.Channel(0)
                gl_player[0]._score.update(250)
                if self._number==0:
                    sound = pygame.mixer.Sound("images/sounds/6zer.mp3")
                    channel.play(sound)
                elif self._number==1:
                    sound = pygame.mixer.Sound("images/sounds/redbull.mp3")
                    channel.play(sound)
                elif self._number==2:
                    sound = pygame.mixer.Sound("images/sounds/szlugi.mp3")
                    channel.play(sound)
                
                
            # self._hitbox.draw()
