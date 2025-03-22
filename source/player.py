import pygame

from .hp import Hp
from .movment import Movment
from .bullet import Bullet
from .motion_animation import PlayerAnimation
from .hp import HitBox
from .singleton import enemies

from const import(
    CONF_PLAYER_HEIGHT,
    CONF_PLAYER_WIDTH,
)

class Player(Movment, PlayerAnimation):
    def __init__(self, window):
        self._x = 50
        self._y = 600
        self._win = window
        self._left = False
        self._right = False
        self._motion_counter = 0
        self._dodge_counter = 0
        self._jump = False
        self._dodge = False
        self._jump_counter = -10
        self._dodge = False
        self._after_jump = 40
        self._bullets = []
        self._bullet_delay = 0
        self._hitbox = HitBox(100, 197, self._win)

        for item in self.walkLeftx:
            self.walkLeft.append(pygame.transform.scale(item, (CONF_PLAYER_WIDTH,CONF_PLAYER_HEIGHT)))
        for item in self.walkRightx:
            self.walkRight.append(pygame.transform.scale(item, (CONF_PLAYER_WIDTH,CONF_PLAYER_HEIGHT)))

        self.standing = pygame.transform.scale(self.standing, (CONF_PLAYER_WIDTH,CONF_PLAYER_HEIGHT))
        self._hp = Hp(window, 100, 100)
        self._last_postion = True

    def bullet(self):
        if self._bullet_delay > 10:
            if not self._left and not self._right:
                self._bullets.append(Bullet(self._x, self._y, self._win, not self._last_postion))
                self._bullet_delay = 0
            else:
                self._bullets.append(Bullet(self._x, self._y, self._win, self._left))
                self._bullet_delay = 0

    def draw(self):
        # Rysowanie paska zdrowia postaci
        self._hp.draw()

        # Sprawdzenie, czy postać skacze
        if self._jump:
            # Jeśli licznik skoku jest większy niż 0, postać porusza się w górę
            if self._jump_counter > 0:
                self._y += (self._jump_counter**2)  # Ruch w górę - efekt paraboliczny
            else:
                self._y -= (self._jump_counter**2)  # Ruch w dół po osiągnięciu szczytu skoku (spadanie)

            # Zwiększanie licznika skoku (prędkość skoku)
            self._jump_counter += 1

            # Kiedy licznik skoku osiągnie wartość 11, kończymy skok
            if self._jump_counter == 11:
                self._jump = False  # Ustawienie, że skok się zakończył
                self._jump_counter = -10  # Reset licznika skoku, by zacząć opadać

        # Sprawdzenie, czy postać porusza się w lewo
        if self._left:
            # Rysowanie postaci idącej w lewo
            self._win.blit(self.walkLeft[self._motion_counter // 1], (self._x, self._y))
        # Sprawdzenie, czy postać porusza się w prawo
        elif self._right:
            # Rysowanie postaci idącej w prawo
            self._win.blit(self.walkRight[self._motion_counter // 1], (self._x, self._y))
        else:
            # Rysowanie postaci, gdy nie porusza się (stojąc)
            self._win.blit(self.standing, (self._x, self._y))

        # Reset licznika animacji ruchu po osiągnięciu wartości 8
        if self._motion_counter == 8:
            self._motion_counter = 0

        # Aktualizacja hitboxa postaci (czyli miejsca, w którym postać może kolidować)
        self._hitbox.update(self._x + 50, self._y + 53)

        # Rysowanie hitboxa (niewidoczny obszar detekcji kolizji)
        self._hitbox.draw()

        # Rysowanie pocisków (jeśli postać ma jakieś wystrzelone pociski)
        for bullet in self._bullets:
            bullet.draw()  # Rysowanie każdego pocisku

            # Sprawdzenie kolizji między pociskiem a wrogami
            for enemy in enemies:
                # Jeśli pocisk trafia w wroga, ten umiera
                if bullet._hitbox.isTouching(enemy._hitbox):
                    enemy.kill()  # Zabicie wroga

        # Zwiększanie liczników dla dalszych akcji
        self._after_jump += 1  # Licznik po skoku
        self._bullet_delay += 1  # Opóźnienie dla strzałów (zapobiega ciągłemu strzelaniu)

        # Jeśli postać wykonuje unik, licznik uniku rośnie
        if self._dodge is True:
            self._dodge_counter += 1

        # Kiedy licznik uniku osiągnie 5, koniec uniku
        if self._dodge_counter == 5 and self._dodge is True:
            self._dodge = False  # Zakończenie uniku
            self._dodge_counter = 0  # Reset licznika uniku
            
