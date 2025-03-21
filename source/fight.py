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
        self._dialog = Dialog(dl1, "RIPPER", self._win)
        self._active_dialog = True

    def draw(self):
        background = pygame.transform.scale(bg, (self._info.current_w,self._info.current_h))
        self._win.blit(background, (0,0))
        self._player.draw()
        if self._active_dialog:
            self._active_dialog = self._dialog.draw()

    def key(self, key):
        if key[pygame.K_w]:
            self._player.jump()
        if key[pygame.K_d]:
            self._player.walk_left()
        elif key[pygame.K_a]:
            self._player.walk_right()
        else:
            self._player.stand()
