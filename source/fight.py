import pygame

from const import (
    bg
)
from .dialogue import Dialog

dl1 = "Nie wiem, kim jesteś, ale jeśli myślisz, że mnie pokonasz, to się grubo mylisz. Twoje dni są policzone."
dl2 = "Ha! Tylko ty to widzisz. Myślisz, że jeden człowiek może powstrzymać całą armię? Zobaczymy, jak długo wytrzymasz."
dl3 = "Nie jestem sam. Moje serce bije dla tych, których chronię. A ty? Jesteś tylko pionkiem w grze, której nie rozumiesz."

class Fight:
    def __init__(self, window, player):
        self._win = window
        self._info = pygame.display.Info()
        self._player = player
        self._dialog = [
            Dialog("testyasdgsad", "RIPPER", window),
            Dialog(dl2, "RIPPER", self._win),
            Dialog(dl3, "RIPPER", self._win),
        ]
        self._active_dialog = True
        self._keys_en = False
        self._dialog_counter = 0
        self._dialog_time = True

    def draw(self):
        if self._dialog_time:
            # if self._dialog_counter >= len(self._dialog):
            #     return False
            #
            # background = pygame.transform.scale(bg, (self._info.current_w,self._info.current_h))
            # self._win.blit(background, (0,0))
            # if not self._dialog[self._dialog_counter].draw():
            #     self._dialog_count += 1
            # self._player.draw()
            self._dialog[0].draw()
        else:
            print("test")
            background = pygame.transform.scale(bg, (self._info.current_w,self._info.current_h))
            self._win.blit(background, (0,0))
            self._player.draw()
        
    def key(self, key):
        # if self._keys_en:
            if key[pygame.K_w]:
                self._player.jump()
            if key[pygame.K_d]:
                self._player.walk_left()
            elif key[pygame.K_a]:
                self._player.walk_right()
            else:
                self._player.stand()

