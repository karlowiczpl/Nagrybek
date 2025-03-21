import pygame

class Hp:
    def __init__(self, window, max_hp, current_hp):
        self._win = window
        self.max_hp = max_hp  
        self.current_hp = current_hp  
        self.hp_bar_size = 30  
        self.hp_bar_gap = 5  
        self.x = 10 
        self.y = 10  
        self._hp_count = 10 

    def draw(self):
        hp_percentage = self.current_hp / self.max_hp
        full_blocks = int(hp_percentage * 10)  

        for i in range(self._hp_count):
            color = (50, 50, 50)  
            if i < full_blocks:  
                color = (0, 255, 0)
            
            pygame.draw.rect(self._win, color, (self.x + (self.hp_bar_size + self.hp_bar_gap) * i, self.y, self.hp_bar_size, self.hp_bar_size), border_radius=7)

    def hp_down(self, hp_count):
        self._hp_count -= hp_count

        if self._hp_count < 1:
            return False

        return True

