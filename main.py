import pygame
from source.start import Start
from source.player import Player
from source.fight import Fight
from source.enemy import Enemy
from source.dialogue import Dialog

pygame.init()

window = pygame.display.set_mode()
player = Player(window)

selected_object = None

start = Start(window, player, selected_object)
enemy1 = Enemy(window, 100, 200)
enemy2 = Enemy(window, 150, 200)
enemy3 = Enemy(window, 80, 200)
enemies = [enemy1, enemy2, enemy3]

# start = Start(window, player, enemies)
fight = Fight(window, player)

selected_object = fight
dialog = Dialog("sdjadkjhsa djsahjd jdsahkjd", "shadjh", window)

isRun = True
while isRun:
    pygame.time.delay(23)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRun = False

        start.handle_event(event)

    key = pygame.key.get_pressed()
    selected_object.key(key)
    
    if not selected_object.draw():
        selected_object = Fight(window, player)


    pygame.display.update()

