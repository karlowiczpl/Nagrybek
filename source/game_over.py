import pygame

from const import (
    bg,
    main_font,
)
from .singleton import gl_player

class GameOver:
    def __init__(self, window):
        self._win = window
        self._info = pygame.display.Info()
        self._player = gl_player[0]
        self._dialog_on = False
        self._dialog_count = 0
        self._counter = 48
        self._stop = False

    def draw(self):
        if self._counter < 100 or self._stop:
            self._win.fill((0x00,0x00,0x00))
        else:
            self._counter += 4

        if self._stop:
            self._counter = 48

        if self._counter > 200:
            self._counter += 1
        if self._counter > 300:
            self._counter += 1
        if self._counter > 350:
            self._counter += 1


        self._player._live = False
        # background = pygame.transform.scale(bg, (self._info.current_w,self._info.current_h))
        # self._win.blit(background, (0,0))
        main_font = pygame.font.Font("./font/main/Tektur-Bold.ttf", self._counter)

        dialog_x = (self._win.get_width() - 100) // 2
        dialog_y = self._win.get_height() // 2 - 200

        who_surface = main_font.render("GAME OVER", True, (255, 255, 255))
        who_rect = who_surface.get_rect(center=(dialog_x, dialog_y))  
        self._win.blit(who_surface, who_rect)
        if self._counter < 400:
            self._counter += 1
        else:
            self._stop = True

        return True

    def key(self, key):
        pass

    def handle_event(self, event):
        pass
