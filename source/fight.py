import pygame
from const import (
    fight_bg
)
from .dialogue import Dialog
from .enemy import Enemy
from .platform import Platform
from .singleton import timer_delay, enemies, time_freeze, platforms

dl1 = "Nie wiem, kim jesteś"
dl2 = "Ha! Tylko ty to widzisz"
dl3 = "Nie jestem sam. Moje "

class Fight:
    def __init__(self, window, player):
        self._win = window
        self._info = pygame.display.Info()
        self._player = player
        self._enemy = Enemy(self._win, 1000,600)
        platforms.append(Platform(0, 900, 2000, 100, window, pygame.image.load("images/platform/platform.png"))
)
        enemies.append(self._enemy)
        self._dialog = [
            Dialog(dl1, "RIPPER", window),
            Dialog(dl2, "ENEMY", self._win),
            Dialog(dl3, "RIPPER", self._win),
        ]
        # self._keys_en = False
        # self._dialog_time = True
        self._keys_en = True
        self._dialog_time = False
        self._dialog_counter = 0
        self._enemy_hit = False
        self._time_frezze_delay = 0
        self._time_frezze = False

    def draw(self):
        if time_freeze[0]:
            self._time_frezze_delay += 1

        if self._time_frezze_delay == 40:
            time_freeze[0] = False
            self._time_frezze_delay = 0

        if not self._dialog_time:
            background = pygame.transform.scale(fight_bg, (self._info.current_w,self._info.current_h))
            self._win.blit(background, (0,0))
            self._player.draw()
            self._enemy.draw()
            
            for i in platforms:
                i.draw()
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
                time_freeze[0] = True
                self._time_frezze = True

    def handle_event(self, event):
        pass
