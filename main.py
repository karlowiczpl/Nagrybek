import pygame
from source.start import Start
from source.player import Player

pygame.init()

# window = pygame.display.set_mode((CONF_WIDTH,CONF_HEIGHT))
window = pygame.display.set_mode()
player = Player(window)

start = Start(window, player)

selected_object = start

isRun = True
while isRun:
    pygame.time.delay(23)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRun = False

        start.handle_event(event)

    key = pygame.key.get_pressed()
    selected_object.key(key)

    selected_object.draw()

    pygame.display.update()
