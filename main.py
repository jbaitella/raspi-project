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
    # Initialize all imported pygame modules
    pygame.init()
    # Set the width and height of the screen [width, height]
    screen = pygame.display.set_mode((Const.SCREEN_WIDTH, Const.SCREEN_HEIGHT))
    # Set the current window caption
    pygame.display.set_caption("PACMAN")
    #Loop until the user clicks the close button.
    done = False
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    # Create a game object
    game = Game()
    # -------- Main Program Loop -----------

    while not done:
        # --- Process events (keystrokes, mouse clicks, etc)
        done = game.processGestures()
        # --- Game logic should go here
        game.runLogic()
        # --- Draw the current frame
        game.displayFrame(screen)
        # --- Limit to 30 frames per second
        clock.tick(20)
        #tkMessageBox.showinfo("GAME OVER!","Final Score = "+(str)(GAME.score))
    # Close the window and quit.
    # If you forget this line, the program will 'hang'
    # on exit if running from IDLE.
    
    pygame.quit()
    
if __name__ == '__main__':
    main()
