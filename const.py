import pygame

CONF_WIDTH = 1000
CONF_HEIGHT = 500

CONF_PLAYER_WIDTH = 200
CONF_PLAYER_HEIGHT = 250
CONF_FLOR_LEVEL = 200

pygame.font.init()

button1 = pygame.image.load("images/Play_button.png")
button2 = pygame.image.load("images/Credits_button.png")
bg = pygame.image.load("images/bg.png")
fight_bg = pygame.image.load("images/fight_bg.png")
bullet = pygame.image.load("images/bullet.png")
ground = pygame.image.load("images/ground1.png")

main_font = pygame.font.Font("font/main/Tektur-Bold.ttf", 48)
# button = [
#     [pygame.image.load("img/button_clicked1.jpg"),pygame.image.load("img/button_unclicked1.jpg")],
#     [pygame.image.load("img/button_clicked2.jpg"),pygame.image.load("img/button_unclicked2.jpg")],
#     [pygame.image.load("img/button_clicked3.jpg"),pygame.image.load("img/button_unclicked3.jpg")],
# ]
hp_bar = [
    pygame.image.load("images/piwo1.png"),
    pygame.image.load("images/piwo2.png"),
    pygame.image.load("images/piwo3.png"),
    pygame.image.load("images/piwo4.png"),
    pygame.image.load("images/piwo5.png"),
    pygame.image.load("images/piwo6.png"),
    pygame.image.load("images/piwo7.png"),
    pygame.image.load("images/piwo8.png"),
    pygame.image.load("images/piwo9.png"),
    pygame.image.load("images/piwo10.png"),
]
bird = [
    pygame.image.load("images/flappy_bird/skeleton-01_fly_00.png"),
    pygame.image.load("images/flappy_bird/skeleton-01_fly_01.png"),
    pygame.image.load("images/flappy_bird/skeleton-01_fly_02.png"),
    pygame.image.load("images/flappy_bird/skeleton-01_fly_03.png"),
    pygame.image.load("images/flappy_bird/skeleton-01_fly_04.png"),
    pygame.image.load("images/flappy_bird/skeleton-01_fly_05.png"),
    pygame.image.load("images/flappy_bird/skeleton-01_fly_06.png"),
    pygame.image.load("images/flappy_bird/skeleton-01_fly_07.png"),
    pygame.image.load("images/flappy_bird/skeleton-01_fly_08.png"),
    pygame.image.load("images/flappy_bird/skeleton-01_fly_09.png"),
    pygame.image.load("images/flappy_bird/skeleton-01_fly_10.png"),
    pygame.image.load("images/flappy_bird/skeleton-01_fly_11.png"),
    pygame.image.load("images/flappy_bird/skeleton-01_fly_12.png"),
    pygame.image.load("images/flappy_bird/skeleton-01_fly_13.png"),
    pygame.image.load("images/flappy_bird/skeleton-01_fly_14.png"),
    pygame.image.load("images/flappy_bird/skeleton-01_fly_15.png"),
]
