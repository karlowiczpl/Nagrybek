import pygame
from source.start import Start
from source.player import Player
from source.fight import Fight
from source.enemy import Enemy
import source.singleton as singleton
from source.platform import Platform

pygame.init()

window = pygame.display.set_mode()
player = Player(window)

singleton.gl_player.append(player)
singleton.timer_delay.append(23)

singleton.ptr.append(None)

start = Start(window, player, singleton.ptr[0])
enemy1 = Enemy(window, 100, 200)
enemy2 = Enemy(window, 150, 200)
enemy3 = Enemy(window, 80, 200)
enemies = [enemy1, enemy2, enemy3]


start = Start(window, player, enemies)
fight = Fight(window, player)

singleton.ptr[0] = fight

isRun = True
while isRun:
    pygame.time.delay(singleton.timer_delay[0])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRun = False

        start.handle_event(event)

    key = pygame.key.get_pressed()
    singleton.ptr[0].key(key)
    
    if not singleton.ptr[0].draw():
        selected_object = Fight(window, player)

    pygame.display.update()
