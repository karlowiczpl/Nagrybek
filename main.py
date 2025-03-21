import pygame
from const import(
    CONF_WIDTH,
    CONF_HEIGHT,
)
from source.start import Start
from source.player import Player

pygame.init()

# window = pygame.display.set_mode((CONF_WIDTH,CONF_HEIGHT))
window = pygame.display.set_mode()
start = Start(window)
player = Player(window)

isRun = True
while isRun:
    pygame.time.delay(23)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRun = False

    start.draw()
    player.draw()

    pygame.display.update()
