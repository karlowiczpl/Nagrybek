import pygame

CONF_WIDTH = 1000
CONF_HEIGHT = 500

CONF_PLAYER_WIDTH = 200
CONF_PLAYER_HEIGHT = 250
CONF_FLOR_LEVEL = 200

pygame.font.init()

bg = pygame.image.load("images/bg.png")
fight_bg = pygame.image.load("images/fight_bg.png")
bullet = pygame.image.load("images/bullet.png")
main_font = pygame.font.Font("font/main/Tektur-Bold.ttf", 48)
# button = [
#     [pygame.image.load("img/button_clicked1.jpg"),pygame.image.load("img/button_unclicked1.jpg")],
#     [pygame.image.load("img/button_clicked2.jpg"),pygame.image.load("img/button_unclicked2.jpg")],
#     [pygame.image.load("img/button_clicked3.jpg"),pygame.image.load("img/button_unclicked3.jpg")],
# ]
