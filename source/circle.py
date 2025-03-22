import pygame

class Circle:
    def __init__(self, x, y, color, window, alpha=255):
        self.x = x + 100
        self.y = y + 150
        self.rad = 10  
        self.color = color
        self.alpha = alpha
        self._win = window
        self.growing = True  
        self.waiting = False
        self.wait_time = 0
        self._off = False

    def draw(self, x, y):
        surface = pygame.Surface((self.rad * 2, self.rad * 2), pygame.SRCALPHA)
        pygame.draw.circle(surface, self.color, (self.rad, self.rad), self.rad)
        surface.set_alpha(self.alpha)

        self._win.blit(surface, (x - self.rad + 100, y - self.rad + 100))

        if self.rad < 50 and not self.growing:
            self._off = True
            return True

        if not self._off:
            if self.growing:
                self.rad += 90
                if self.rad >= 1000:  
                    self.growing = False
                    self.waiting = True
                    self.wait_time = 0
            elif self.waiting:
                self.wait_time += 1
                if self.wait_time >= 30:
                    self.waiting = False
            else:
                self.rad -= 90  
                if self.rad <= 0:  
                    self.growing = True

        return False

