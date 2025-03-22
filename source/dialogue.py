import pygame
from const import main_font

class Dialog:
    _wait_counter: int

    def __init__(self, dialog_text, who, window):
        self._who = who
        self._words = dialog_text.split()  
        self._win = window
        self.dialog_width = 1700
        self.dialog_height = 100
        self.font = main_font
        self._current_text = ""
        self._index = 0
        self._last_update = pygame.time.get_ticks()  
        self._speed = 100  
        self._wait = False
        self._wait_counter = 0
        self._counter = 0
        self._stop = False
        self._now = 0
        self._last_update = 0

    def update(self):
        now = pygame.time.get_ticks()

        if not self._stop:
            if not self._wait and not self._stop:
                if self._index < len(self._words) and now - self._last_update > self._speed:
                    self._current_text += " " + self._words[self._index]  
                    self._index += 1
                    self._last_update = now  
                if self._index == len(self._words):
                    self._stop = True
            else:
                self._counter += 1

                if self._counter > 100:
                    self._wait = False
                    self._counter = 0
                    self._current_text = ""

            if len(self._current_text) > 60:
                self._wait = True
                self._wait_counter = 0

            return True
        else:
            self._counter += 1

            if self._counter > 30:
                return False

            return True

    def draw(self):
        up = self.update()

        dialog_x = (self._win.get_width() - self.dialog_width) // 2
        dialog_y = self._win.get_height() - 200
        name_y = dialog_y - 30  
        name_x = dialog_x + 120

        pygame.draw.rect(self._win, (50, 50, 50), (dialog_x, dialog_y, self.dialog_width, self.dialog_height), border_radius=10)
        pygame.draw.rect(self._win, (255, 255, 255), (dialog_x, dialog_y, self.dialog_width, self.dialog_height), 3, border_radius=10)

        who_surface = self.font.render(self._who, True, (255, 255, 255))
        who_rect = who_surface.get_rect(center=(name_x , name_y))  
        self._win.blit(who_surface, who_rect)

        text_surface = self.font.render(self._current_text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(self._win.get_width() // 2, dialog_y + self.dialog_height // 2))
        self._win.blit(text_surface, text_rect)

        return up

