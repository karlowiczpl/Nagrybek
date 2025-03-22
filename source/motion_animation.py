import pygame

class Animation:
    pass

class EnemyAnimation(Animation):
    walkRightx = [
        pygame.image.load("images/enemy1.png"),
        pygame.image.load("images/enemy2.png"),
        pygame.image.load("images/enemy3.png"),
        pygame.image.load("images/enemy4.png"),
    ]
    walkLeftx = [
        pygame.image.load("images/enemy1_r.png"),
        pygame.image.load("images/enemy2_r.png"),
        pygame.image.load("images/enemy3_r.png"),
        pygame.image.load("images/enemy4_r.png"),
    ]
    standing = pygame.image.load("images/standing.png")
    walkLeft = []
    walkRight = []

class PlayerAnimation(Animation):
    walkLeftx = [
        pygame.image.load("images/L1.png"),
        pygame.image.load("images/L2.png"),
        pygame.image.load("images/L3.png"),
        pygame.image.load("images/L4.png"),
        pygame.image.load("images/L5.png"),
        pygame.image.load("images/L6.png"),
        pygame.image.load("images/L7.png"),
        pygame.image.load("images/L8.png"),
        pygame.image.load("images/L9.png"),
    ]
    walkRightx = [
        pygame.image.load("images/R1.png"),
        pygame.image.load("images/R2.png"),
        pygame.image.load("images/R3.png"),
        pygame.image.load("images/R4.png"),
        pygame.image.load("images/R5.png"),
        pygame.image.load("images/R6.png"),
        pygame.image.load("images/R7.png"),
        pygame.image.load("images/R8.png"),
        pygame.image.load("images/R9.png"),
    ]
    standing = pygame.image.load("images/standing.png")
    walkLeft = []
    walkRight = []


class PlatformaAnimation:
    normal = pygame.image.load("images/platform/platform.png")
