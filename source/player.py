import pygame

from const import(
    CONF_PLAYER_HEIGHT,
    CONF_PLAYER_WIDTH,
)

class Bullet:
    def __init__(self, x, y, win, left):
        self._win = win
        self._x = x + 40
        self._y = y + 25
        self._left = not left
        self._bullets = []

    def draw(self) -> bool:
        pygame.draw.circle(self._win, (0, 0, 0), (self._x, self._y), 7)

        if self._left:
            self._x += 20
        else:
            self._x -= 20


class Player:
    walkLeftx = [
        pygame.image.load("images/L1.png"),
        pygame.image.load("images/L2.png"),
        pygame.image.load("images/L3.png"),
        pygame.image.load("images/L4.png"),
        pygame.image.load("images/L5.png"),
        pygame.image.load("images/L6.png"),
        pygame.image.load("images/L7.png"),
        pygame.image.load("images/L8.png"),
        pygame.image.load("images/L9.png"),
    ]
    walkRightx = [
        pygame.image.load("images/R1.png"),
        pygame.image.load("images/R2.png"),
        pygame.image.load("images/R3.png"),
        pygame.image.load("images/R4.png"),
        pygame.image.load("images/R5.png"),
        pygame.image.load("images/R6.png"),
        pygame.image.load("images/R7.png"),
        pygame.image.load("images/R8.png"),
        pygame.image.load("images/R9.png"),
    ]
    standing = pygame.image.load("images/standing.png")
    walkLeft = []
    walkRight = []

    def __init__(self, window):
        self._x = 50
        self._y = 400
        self._win = window
        self._left = False
        self._right = False
        self._motion_counter = 0
        self._jump = False
        self._jump_counter = -10
        self._after_jump = 0
        self._bullets = []
        self._bullet_delay = 0
        self._hitbox = (self._x + 20 , self._y, 28, 60)
        for item in self.walkLeftx:
            self.walkLeft.append(pygame.transform.scale(item, (CONF_PLAYER_WIDTH,CONF_PLAYER_HEIGHT)))
        for item in self.walkRightx:
            self.walkRight.append(pygame.transform.scale(item, (CONF_PLAYER_WIDTH,CONF_PLAYER_HEIGHT)))
        self.standing = pygame.transform.scale(self.standing, (CONF_PLAYER_WIDTH,CONF_PLAYER_HEIGHT))

    def walk_left(self):
        if self._x > 0:
            self._left = True
            self._right = False

            self._x -= 5
            self._motion_counter += 1

    def walk_right(self):
        if self._x < 450:
            self._left = False
            self._right = True

            self._x += 5
            self._motion_counter += 1

    def stand(self):
        self._left = False
        self._right = False

    def jump(self):
        if self._after_jump > 40:
            self._jump = True
            self._after_jump = 0

    def bullet(self, enemy):
        if self._bullet_delay > 10:
            self._bullets.append(Bullet(self._x, self._y, self._win, self._left))
            self._bullet_delay = 0
            self._enemy = enemy

    def draw(self):
        if self._jump:
            if self._jump_counter > 0:
                self._y += (self._jump_counter**2) / 2
            else:
                self._y -= (self._jump_counter**2) / 2

            self._jump_counter += 1
            if self._jump_counter == 11:
                self._jump = False
                self._jump_counter = -10

        if self._left:
            self._win.blit(self.walkLeft[self._motion_counter // 3], (self._x, self._y))
        elif self._right:
            self._win.blit(
                self.walkRight[self._motion_counter // 3], (self._x, self._y)
            )
        else:
            self._win.blit(self.standing, (self._x, self._y))

        if self._motion_counter == 26:
            self._motion_counter = 0

        for bullet in self._bullets:
            if bullet._y - 5 < self._enemy._hitbox[1] + self._enemy._hitbox[3] and bullet._y + 5  > self._enemy._hitbox[1]:
                if bullet._x + 5 > self._enemy._hitbox[0] and bullet._x  - 5> self._enemy._hitbox[0] + self._enemy._hitbox[2]:
                    self._enemy.hit()
                    self._bullets.pop(self._bullets.index(bullet))

            bullet.draw()

        self._after_jump += 1
        self._bullet_delay += 1

        self._hitbox = (self._x + 20, self._y,  28, 60)
        pygame.draw.rect(self._win , (255,0,0), self._hitbox, 2)
