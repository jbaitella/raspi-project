import pygame
import tkinter
from tkinter import messagebox
import grove_gesture_sensor


from Programms.enemies import *
from Programms.player import Player
import Programms.constants as Const

# Gesturesensor Begriffe
g = grove_gesture_sensor.gesture()
g.init()

class Game(object):
    def __init__(self) -> None:
        self.font = pygame.font.Font(None, 40)
        self.about = False
        self.gameOver = True
        # Create the variable for the score
        self.score = 0
        # Create the font for displaying the score on the screen
        self.font = pygame.font.Font(None, 35)
        # Create the menu of the game
        self.menu = Menu(("Start", "About", "Exit"), fontColor = Const.WHITE, font_size = 80)
        # Create the player 
        self.player = Player(32, 128, "Pictures/player.png")
        # Create the blocks that will set the paths where the player can go
        self.horizontalBlocks = pygame.sprite.Group()
        self.verticalBlocks = pygame.sprite.Group()
        # Create a group for the dots on the screen
        self.dotsGroup = pygame.sprite.Group()
        # Set the enviroment:
        for i, row in enumerate(enviroment()):
            for j, item in enumerate(row):
                if item == 1: 
                    self.horizontalBlocks.add(Block(j * 32 + 8, i * 32 + 8, Const.BLACK, 16, 16))
                elif item == 2:
                    self.verticalBlocks.add(Block(j * 32 + 8, i * 32 + 8, Const.BLACK, 16, 16))

        # Create the enemies
        self.enemies = pygame.sprite.Group()
        self.enemies.add(Slime(288, 96, 0, 2))
        self.enemies.add(Slime(288, 320, 0, -2))
        self.enemies.add(Slime(544, 128, 0, 2))
        self.enemies.add(Slime(32, 224, 0, 2))
        self.enemies.add(Slime(160, 64, 2, 0))
        self.enemies.add(Slime(448, 64, -2,0))
        self.enemies.add(Slime(640, 448, 2, 0))
        self.enemies.add(Slime(448, 320, 2, 0))

        # Add the dots inside the game
        for i, row in enumerate(enviroment()):
            for j, item in enumerate(row):
                if item != 0:
                    self.dotsGroup.add(Ellipse(j * 32 + 12, i * 32 + 12, Const.WHITE, 8, 8))

        # Load the sound effects
        self.pacmanSound = pygame.mixer.Sound("Sounds/pacmanSound.ogg")
        self.gameOverSound = pygame.mixer.Sound("Sounds/gameOverSound.ogg")

    def processGestures(self) -> bool:
        gest = g.return_gesture()
        if gest in [2, 7, 8, 9]: 
            gest = 0

        print("Gesture:", gest)
        event = pygame.event.get() #this is a List
        if len(event) > 0 and event[0].type == pygame.QUIT: # If user clicked close
            return True

        if gest != 0:
            #self.menu.event_handler(gest)
            if gest == g.FORWARD:
                if self.gameOver and not self.about:
                    if self.menu.state == 0:
                        # ---- START ------
                        self.__init__()
                        self.gameOver = False

                    if self.menu.state == 1:
                        # --- ABOUT ------
                        self.about = True

                    elif self.menu.state == 2:
                        # --- EXIT -------
                        # User clicked exit
                        return True
    
            elif gest == g.RIGHT:
                self.player.move_right()
                print ("Right")

            elif gest == g.LEFT:
                self.player.move_left()
                print ("Left")

            elif gest == g.UP:
                self.player.move_up()
                print ("Up")

            elif gest == g.DOWN:
                self.player.move_down()
                print ("Down")

            elif len(event) > 0 and event[0].key == pygame.K_ESCAPE:
                self.gameOver = True
                self.about = False
                
        return False

    def runLogic(self) -> None:
        if not self.gameOver:
            self.player.update(self.horizontalBlocks, self.verticalBlocks)
            block_hit_list = pygame.sprite.spritecollide(self.player, self.dotsGroup, True)
            # When the block_hit_list contains one sprite that means that player hit a dot

            if len(block_hit_list) > 0:
                # Here will be the sound effect
                self.pacmanSound.play()
                self.score += 1

            block_hit_list = pygame.sprite.spritecollide(self.player, self.enemies, True)

            if len(block_hit_list) > 0:
                self.player.explosion = True
                self.gameOverSound.play()

            self.gameOver = self.player.gameOver
            self.enemies.update(self.horizontalBlocks, self.verticalBlocks)
           # tkMessageBox.showinfo("GAME OVER!","Final Score = "+(str)(GAME.score)) 
              
    def displayFrame(self, screen: pygame.Surface) -> None:
        # First, clear the screen to white. Don't put other drawing commands
        screen.fill(Const.BLACK)
        # --- Drawing code should go here
        if self.gameOver:
            if self.about:
                self.displayMessage(screen, "It is an arcade Game, changed by Julia Baitella")
                #"a maze containing various dots,\n"
                #known as Pac-Dots, and four ghosts.\n"
                #"The four ghosts roam the maze, trying to kill Pac-Man.\n"
                #"If any of the ghosts hit Pac-Man, he loses a life;\n"
                #"the game is over.\n")
            else:
                self.menu.displayFrame(screen)

        else:
            # --- Draw the game here ---
            self.horizontalBlocks.draw(screen)
            self.verticalBlocks.draw(screen)
            drawEnviroment(screen)
            self.dotsGroup.draw(screen)
            self.enemies.draw(screen)
            screen.blit(self.player.image, self.player.rect)
            #text=self.font.render("Score: "+(str)(self.score), 1,self.RED)
            #screen.blit(text, (30, 650))
            # Render the text for the score
            text = self.font.render("Your score: " + str(self.score), True, Const.GREEN)
            # Put the text on the screen
            screen.blit(text, [120, 20])
        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    def displayMessage(self, screen, message, color=(255, 0, 0)):
        label = self.font.render(message, True, color)
        # Get the width and height of the label
        width = label.get_width()
        height = label.get_height()
        # Determine the position of the label
        posX = (Const.SCREEN_WIDTH / 2) - (width / 2)
        posY = (Const.SCREEN_HEIGHT / 2) - (height / 2)
        # Draw the label onto the screen
        screen.blit(label, (posX, posY))

class Menu(object):
    state = 0
    def __init__(self, items: tuple, fontColor: tuple = (0, 0, 0), selectColor: tuple = (255, 0, 0), ttf_font = None, font_size: int = 25):
        self.fontColor = fontColor
        self.selectColor = selectColor
        self.items = items
        self.font = pygame.font.Font(ttf_font, font_size)

    def displayFrame(self, screen):
        for index, item in enumerate(self.items):
            if self.state == index:
                label = self.font.render(item, True, self.selectColor)
            else:
                label = self.font.render(item, True, self.fontColor)
            width = label.get_width()
            height = label.get_height()
            posX = (Const.SCREEN_WIDTH / 2) - (width / 2)
            # t_h: total height of text block
            t_h = len(self.items) * height
            posY = (Const.SCREEN_HEIGHT / 2) - (t_h / 2) + (index * height)
            screen.blit(label, (posX, posY))

    def event_handler(self, gest: int) -> None:
        if gest == g.UP:
            if self.state > 0:
                self.state -= 1

        elif gest == g.DOWN:
            if self.state < len(self.items) - 1:
                self.state += 1
