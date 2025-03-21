import pygame

class Movment:
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

    def walk_right(self):
        if self._x > 0:
            self._left = True
            self._right = False

            self._x -= 20
            self._motion_counter += 1

    def walk_left(self):
        if self._x < 1700:
            self._left = False
            self._right = True

            self._x += 20
            self._motion_counter += 1

    def dodge(self):
        if self.dodge is False: 
            self._hitbox = (0,0,0,0)
            self.dodge = True
        else:
            self._hitbox = (self._x + 20 , self._y, 28, 60)

    def stand(self):
        self._left = False
        self._right = False

    def jump(self):
        if self._after_jump > 40:
            self._jump = True
            self._after_jump = 0

    def dodge(self):
        print(self._dodge)
        if self._dodge is False:
            self._hitbox = (0,0,0,0)
            self._dodge = True
            print("B")
        else:
            self._hitbox = (self._x + 20 , self._y, 28, 60)
            print("C")
            
