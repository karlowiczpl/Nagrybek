import pygame
import time

from .singleton import gl_player


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)


class GameOver:
    def __init__(self, window):
        self._win = window
        self._player = gl_player[0]
        self._counter = 48  
        self._stop = False
        self._fade_alpha = 0  
        self._start_time = time.time()  
        self._action_taken = False  
        self._red_intensity = 0 

    def key(self, event):
        pass

    def draw(self):

        self._win.fill(BLACK)  

        elapsed_time = time.time() - self._start_time


        if elapsed_time < 0.3:
            self._counter += 20
        else:
    
            if self._fade_alpha < 255:
                self._fade_alpha += 3  
            if self._red_intensity < 200:
                self._red_intensity += 3  

  

        main_font = pygame.font.Font("./font/main/bytesize/pixel.ttf", self._counter) 


        text_surface = main_font.render("You died", True, (self._red_intensity, 0, 0))  

        text_surface.set_alpha(self._fade_alpha)


        text_rect = text_surface.get_rect(center=(self._win.get_width() // 2, self._win.get_height() // 3))
        self._win.blit(text_surface, text_rect)

        if self._fade_alpha >= 255:
            self._stop = True
