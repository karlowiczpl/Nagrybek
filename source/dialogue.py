import pygame

class Dialog:
    def __init__(self, dialog_text, who, window):
        self._who = who
        self._words = dialog_text.split()  # Podziel tekst na słowa
        self._win = window
        self.dialog_width = 1000
        self.dialog_height = 100
        self.font = pygame.font.Font(None, 36)
        self._current_text = ""
        self._index = 0  
        self._last_update = pygame.time.get_ticks()  
        self._speed = 100  
        self._wait = False
        self._wait_counter = 0

    def update(self):
        now = pygame.time.get_ticks()
        if not self._wait:
            if self._index < len(self._words) and now - self._last_update > self._speed:
                self._current_text += " " + self._words[self._index]  
                self._index += 1
                self._last_update = now  
        else:
            self._wait_counter = self._wait_counter + 1
            print(f"waiting, {self._wait_counter}")

            if self._wait_counter > 40:
                self._wait = False
                self._current_text = ""

        if len(self._current_text) > 60:
            self._wait = True
            self._wait_counter = 0

    def draw(self):
        self.update()

        dialog_x = (self._win.get_width() - self.dialog_width) // 2
        dialog_y = self._win.get_height() - 200

        pygame.draw.rect(self._win, (50, 50, 50), (dialog_x, dialog_y, self.dialog_width, self.dialog_height), border_radius=10)
        pygame.draw.rect(self._win, (255, 255, 255), (dialog_x, dialog_y, self.dialog_width, self.dialog_height), 3, border_radius=10)

        text_surface = self.font.render(self._current_text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(self._win.get_width() // 2, dialog_y + self.dialog_height // 2))
        self._win.blit(text_surface, text_rect)

