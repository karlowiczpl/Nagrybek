import pygame
from const import(
    CONF_WIDTH,
    CONF_HEIGHT,
)
from source.start import Start
from source.player import Player
from source.enemy import Enemy

pygame.init()

# window = pygame.display.set_mode((CONF_WIDTH,CONF_HEIGHT))
window = pygame.display.set_mode()
player = Player(window)
enemy1 = Enemy(window, 100, 200)
enemy2 = Enemy(window, 150, 200)
enemy3 = Enemy(window, 80, 200)
enemies = [enemy1, enemy2, enemy3]
start = Start(window, player, enemies)

selected_object = start


isRun = True
while isRun:
    pygame.time.delay(23)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRun = False

    key = pygame.key.get_pressed()
    selected_object.key(key)

    selected_object.draw()
    
    

    pygame.display.update()
