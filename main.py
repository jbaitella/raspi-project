import pygame

from Programms.game import Game
import Programms.constants as Const

import time

"""
TODO: Code lesen und verstehen
Überall schönheitsabstände einfügen
Variabel namen nach Python Standard bennen (z.B. kein _ wenn der Namen kleingeschrieben wird)
bei allen funktionen die Parameter definieren und dire Rückgabe werte definieren
Unnötige Komentare entfernen
Kommentare hinzufügen
main.py vereinfachen
imports ordnen und auf import wechseln
"""

def main():
    pygame.init()
    screen = pygame.display.set_mode((Const.SCREEN_WIDTH, Const.SCREEN_HEIGHT))
    pygame.display.set_caption("PACMAN")
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
