import pygame
import random
from .circle import Circle
from .bird import Bird
from const import (
    fight_bg
)
from .dialogue import Dialog
from .enemy import Enemy
from .platform import Platform
from .singleton import timer_delay, enemies, time_freeze, platforms, items
from .items import Item
from .car import Car

dl1 = "Nie wiem, kim jesteś"
dl2 = "Ha! Tylko ty to widzisz"
dl3 = "Nie jestem sam. Moje "

PURPLE = (128, 0, 128)


class Fight:
    def __init__(self, window, player):
        self._circle_radius = 0
        self._win = window
        self._info = pygame.display.Info()
        self._player = player
        self._enemy = Enemy(self._win, 1000,600)
        platforms.append(Platform(300, 600, 600, 40, window, pygame.image.load("images/platform/platform.png")))
        platforms.append(Platform(1300, 350, 600, 40, window, pygame.image.load("images/platform/platform.png")))
        enemies.append(self._enemy)
        self._birds = [Bird(400, self._win)]
        self._bird_spawn_time = 60
        self._dialog = [
            Dialog(dl1, "RIPPER", window),
            Dialog(dl2, "ENEMY", self._win),
            Dialog(dl3, "RIPPER", self._win),
        ]
        self._keys_en = True
        self._dialog_time = False
        self._dialog_counter = 0
        self._enemy_hit = False
        self._time_frezze_delay = 0
        self._time_frezze = False
        items.append(Item(50 , 50, self._win, self._player))
        self._bird_delay = 0
        self._time = Circle(self._player._x, self._player._y, (0,0,0), self._win, 80)
        self._time._off = True
        self._car = Car(window)

    def draw(self):
        if self._bird_delay > self._bird_spawn_time:
            postion = random.randint(200,650)
            self._bird_spawn_time = random.randint(20,120)
            self._birds.append(Bird(postion, self._win))
            self._bird_delay = 0

        self._bird_delay += 1

        if time_freeze[0]:
            self._time_frezze_delay += 1
        self.circleBack = False

        if time_freeze[0]:
        
            self._time_frezze_delay += 1
            
            if self._time_frezze_delay == 0:
                pygame.mixer.music.load("images/sounds/ticking.mp3")
                pygame.mixer.music.play(4, 0.0)
            
        if not self._dialog_time:
            background = pygame.transform.scale(fight_bg, (2000,1000))
            self._win.blit(background, (0,0))
            self._player.draw()
            self._enemy.draw()
            
            for i in platforms:
                i.draw()
            self._car.draw()
        else:
            if self._dialog_counter >= len(self._dialog):
                self._dialog_time = False
                self._keys_en = True
                return True
            
            background = pygame.transform.scale(fight_bg, (self._info.current_w,self._info.current_h))
            self._win.blit(background, (0,0))
            if not self._dialog[self._dialog_counter].draw():
                self._dialog_counter += 1

            self._player.draw()
            for enemy in enemies:
                enemy.draw()
            
            for i in platforms:
                i.draw()

        items[0].draw()
        for bird in self._birds:
            bird.draw()
                
        if self._time.draw(self._player._x, self._player._y):
            time_freeze[0] = False
        
        return True

    def key(self, key):
        if self._keys_en:
            if key[pygame.K_w]:
                self._player.jump()
            if key[pygame.K_d]:
                self._player.walk_left()
            elif key[pygame.K_a]:
                self._player.walk_right()
            else:
                self._player.stand()
            if key[pygame.K_SPACE]:
                self._player.bullet()
            if key[pygame.K_t]:
                self._time_frezze = True
                time_freeze[0] = True
                self._time = Circle(self._player._x, self._player._y, (0,0,0), self._win, 80)

    def handle_event(self, event):
        pass
