import pygame

from const import (
    bg,
    main_font,
)
from .dialogue import Dialog

class Button:
    def __init__(self, x, y, text, color, window, border_radius=10):
        self._x = x
        self._y = y
        self._width = 500
        self._height = 100
        self._text = text
        self._font = main_font
        self._color = color
        self._window = window
        self._rect = pygame.Rect(x, y, self._width, self._height)
        self._border_radius = border_radius
        self._original_color = color
        self._clicked = False
        self._click_timer = 0  
        factor = 0.2
        self._color_2 = (int(color[0] * factor), int(color[1] * factor), int(color[2] * factor))

    
    def draw(self):
        self.update()
        if self._clicked:
            pygame.draw.rect(self._window, self._color_2, self._rect, border_radius=self._border_radius) 
        else:
            pygame.draw.rect(self._window, self._color, self._rect, border_radius=self._border_radius)  
        
        text_surface = self._font.render(self._text, True, (255, 255, 255))  
        self._window.blit(text_surface, (self._x + (self._width - text_surface.get_width()) / 2,
                                        self._y + (self._height - text_surface.get_height()) / 2))

    def is_pressed(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self._rect.collidepoint(event.pos):
            self._clicked = True
            self._click_timer = pygame.time.get_ticks()
            return True
        return False

    def update(self):
        if self._clicked and pygame.time.get_ticks() - self._click_timer > 150:
            self._clicked = False

class Start:
    def __init__(self, window, player):
        self._win = window
        self._info = pygame.display.Info()
        self._player = player
        self._button = [
            Button(230, 450, "START", (0xfd, 0x5a, 0x46),window),
            Button(230, 590, "MENU", (0x55, 0x2c, 0xb7),window),
        ]
        self._dialog_on = False
        self._dialog_count = 0
        self._dialog = [
            Dialog("Jesteś gotów na to starcie?", "RIPPER", self._win),
            Dialog("Heh… gotów? Ja się urodziłem, by walczyć!", "PRZECIWNIK", self._win),
            Dialog("Zobaczymy, czy twoje słowa mają pokrycie w czynach.", "RIPPER", self._win),
        ]

    def draw(self):
        if not self._dialog_on:
            background = pygame.transform.scale(bg, (self._info.current_w,self._info.current_h))
            self._win.blit(background, (0,0))
            for button in self._button:
                button.draw()
        else:
            if self._dialog_count > len(self._dialog):
                stop_start()

            background = pygame.transform.scale(bg, (self._info.current_w,self._info.current_h))
            self._win.blit(background, (0,0))
            if not self._dialog[self._dialog_count].draw():
                self._dialog_count += 1

        return True

    def key(self, key):
        pass

    def handle_event(self, event):
        for button in self._button:
            if button.is_pressed(event):
                if button._text == "START":
                    self._dialog_on = True
