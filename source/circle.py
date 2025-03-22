import pygame


class Circle:
    def __init__(self, x, y, radius, color, alpha=255):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.alpha = alpha
        

        self.surface = pygame.Surface((self.radius * 2, self.radius * 2),  pygame.SRCALPHA)
        

        pygame.draw.circle(self.surface, self.color, (self.radius, self.radius), self.radius)
        

        self.surface.set_alpha(self.alpha)

    def draw(self, screen):

        screen.blit(self.surface, (self.x - self.radius, self.y - self.radius))