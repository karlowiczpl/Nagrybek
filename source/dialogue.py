import pygame

class Dialog:

    def __init__(self, dialog_text, who, window):

        self._who = who
        self._words = dialog_text.split()
        self._win = window
        self.dialog_width = 1000
        self.dialog_height = 100
        self.font = pygame.font.Font((0xff,0xff,0xff), 36)
        self._current_text = ""

    def draw(self):
        dialog_x = (self._win.get_width() - self.dialog_width) // 2
        dialog_y = self._win.get_height() - 200

        pygame.draw.rect(self._win, (50, 50, 50), (dialog_x, dialog_y, self.dialog_width, self.dialog_height), border_radius=10)
        pygame.draw.rect(self._win, (255, 255, 255), (dialog_x, dialog_y, self.dialog_width, self.dialog_height), 3, border_radius=10)

        text_surface = self.font.render(self._current_text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(self._win.get_width() // 2, dialog_y + self.dialog_height // 2))
        self._win.blit(text_surface, text_rect)

        

