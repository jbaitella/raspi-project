import pygame
import random

import Programms.constants as Const

class Block(pygame.sprite.Sprite):
    def __init__(self, x, y, color, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)


class Ellipse(pygame.sprite.Sprite):
    def __init__(self, x, y, color, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill(Const.BLACK)
        self.image.set_colorkey(Const.BLACK)
        pygame.draw.ellipse(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        
class Slime(pygame.sprite.Sprite):
    def __init__(self, x, y, change_x, change_y):
        pygame.sprite.Sprite.__init__(self)
        self.change_x = change_x
        self.change_y = change_y
        self.image = pygame.image.load("Pictures/slime.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
 

    def update(self, horizontal_blocks, vertical_blocks):
        self.rect.x += self.change_x
        self.rect.y += self.change_y

        if self.rect.right < 0:
            self.rect.left = Const.SCREEN_WIDTH

        elif self.rect.left > Const.SCREEN_WIDTH:
            self.rect.right = 0

        if self.rect.bottom < 0:
            self.rect.top = Const.SCREEN_HEIGHT

        elif self.rect.top > Const.SCREEN_HEIGHT:
            self.rect.bottom = 0

        #Bewegungen des PacMans
        if self.rect.topleft in self.get_intersection_position():
            direction = random.choice(("left", "right", "up", "down"))

            if direction == "left" and self.change_x == 0:
                self.change_x = -2
                self.change_y = 0

            elif direction == "right" and self.change_x == 0:
                self.change_x = 2
                self.change_y = 0

            elif direction == "up" and self.change_y == 0:
                self.change_x = 0
                self.change_y = -2

            elif direction == "down" and self.change_y == 0:
                self.change_x = 0
                self.change_y = 2
                

    def get_intersection_position(self):
        items = []
        for i, row in enumerate(enviroment()):
            for j, item in enumerate(row):
                if item == 3:
                    items.append((j * 32, i * 32))

        return items
    
 #Spielfeld Linien       
def enviroment():
    grid = ((0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0),
            (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0),
            (1,3,1,1,1,1,1,1,1,3,1,1,1,1,1,1,1,3,1,1,1,1,1,3,1),
            (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0),
            (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0),
            (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0),
            (1,3,1,1,1,1,1,1,1,3,1,1,1,1,1,1,1,3,1,1,1,1,1,3,1),
            (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0),
            (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0),
            (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0),
            (1,3,1,1,1,1,1,1,1,3,1,1,1,1,1,1,1,3,1,1,1,1,1,3,1),
            (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0),
            (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0),
            (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0),
            (1,3,1,1,1,1,1,1,1,3,1,1,1,1,1,1,1,3,1,1,1,1,1,3,1),
            (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0),
            (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0),
            (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0))

    return grid

#Zahlen definieren, was sie für Linien haben: Wie sich Pacman bewegen kann
def drawEnviroment(screen):
    for i, row in enumerate(enviroment()):
        for j,item in enumerate(row):
            if item == 1:
                pygame.draw.line(screen, Const.BLUE, [j * 32, i * 32], [j * 32 + 32, i * 32], 3)
                pygame.draw.line(screen, Const.BLUE, [j * 32, i * 32 + 32], [j * 32 + 32, i * 32 + 32], 3)

            elif item == 2:
                pygame.draw.line(screen, Const.BLUE, [j * 32, i * 32], [j * 32, i * 32 + 32], 3)
                pygame.draw.line(screen, Const.BLUE, [j * 32 + 32, i * 32], [j * 32 + 32 ,i * 32 + 32], 3)
