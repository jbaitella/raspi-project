import pygame
from Programms.game import Game
import Programms.constants as Const

import time

def main():
    pygame.init()
    screen = pygame.display.set_mode((Const.SCREEN_WIDTH, Const.SCREEN_HEIGHT))
    pygame.display.set_caption("PACMAN THE GAME")
    done = False
    clock = pygame.time.Clock()
    game = Game()
    game.processGestures()

    while not done:
        done = game.processGestures()
        game.runLogic()
        game.displayFrame(screen)
        clock.tick(20)
    
    pygame.quit()
    
if __name__ == '__main__':
    main()
