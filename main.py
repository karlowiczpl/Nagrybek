import pygame
from const import(
    CONF_WIDTH,
    CONF_HEIGHT,
)

pygame.init()

window = pygame.display.set_mode((CONF_WIDTH,CONF_HEIGHT))

isRun = True
while isRun:
    pygame.time.delay(23)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRun = False

    

    pygame.display.update()
