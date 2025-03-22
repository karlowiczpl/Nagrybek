import pygame
from .singleton import gl_player
from const import(
    hp_bar,
)

class Hp:
    def __init__(self, window, max_hp, current_hp):
        self._win = window
        self.max_hp = max_hp  
        self.current_hp = current_hp  
        self.hp_bar_size = 30  
        self.hp_bar_gap = 5  
        self.x = -40 
        self.y = -50  
        self._hp_count = 10 
        self._hp_delay = 0

    def draw(self):
        hp = self._hp_count
        hp -= 1
        if self._hp_count > 9:
            hp = 9

        self._win.blit(pygame.transform.scale(hp_bar[hp], (500,170)), (self.x, self.y))

        self._hp_delay += 1

    def hp_down(self, hp_count):
        if self._hp_delay > 10:
            self._hp_count -= hp_count
            self._hp_delay = 0

        if self._hp_count < 1:
            return False
        
        return True

class HitBox:
    def __init__(self, width, height, window):
        self._width = width
        self._height = height
        self._window = window
        self._hitbox = (0,0,width,height)
        self._win = window

    def update(self, x, y):
        self._hitbox = (x, y, self._width, self._height)

    def draw(self):
        pygame.draw.rect(self._win , (255,0,0), self._hitbox, 2)

    def isTouching(self, hitbox):
        x1, y1, w1, h1 = hitbox._hitbox
        x2, y2, w2, h2 = self._hitbox
        
        return not (x1 + w1 <= x2 or x2 + w2 <= x1 or y1 + h1 <= y2 or y2 + h2 <= y1)       

    def isTouchingFromBottom(self, hitbox):
        x1, y1, w1, h1 = hitbox._hitbox
        x2, y2, w2, h2 = self._hitbox

        if y1 >= y2 + h2 and x1 + w1 > x2 and x1 < x2 + w2:
            return True
        return False

    def isTouchingFromSides(self, hitbox):
        x1, y1, w1, h1 = self._hitbox
        x2, y2, w2, h2 = hitbox._hitbox

        if (y1 + h1 > y2 and y1 < y2 + h2) and (x1 + w1 > x2 and x1 < x2 + w2):
            return True
        return False
    

    def isTouchingFromTop(self, hitbox, tolerance=2):
        # Załóżmy, że hitbox przekazany jako argument to obiekt gracza
        x1, y1, w1, h1 = hitbox._hitbox  # hitbox gracza
        x2, y2, w2, h2 = self._hitbox      # hitbox platformy
        
        # Sprawdź, czy dolna krawędź gracza jest blisko górnej krawędzi platformy
        if abs((y1 + h1) - y2) <= tolerance and x1 + w1 > x2 and x1 < x2 + w2:
            return True
        return False

    
        
