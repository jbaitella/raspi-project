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
        # Score auf Null setzen 
        self.score = 0
        self.font = pygame.font.Font(None, 35)
        # Erstellen des Menu, Players, Blöcke, Umfeld 
        self.menu = Menu(("Start", "About", "Exit"), fontColor = Const.WHITE, font_size = 80)
        self.player = Player(32, 128, "Pictures/player.png")
        self.horizontalBlocks = pygame.sprite.Group()
        self.verticalBlocks = pygame.sprite.Group()
        self.dotsGroup = pygame.sprite.Group()
 
        for i, row in enumerate(enviroment()):
            for j, item in enumerate(row):
                if item == 1: 
                    self.horizontalBlocks.add(Block(j * 32 + 8, i * 32 + 8, Const.BLACK, 16, 16))
                elif item == 2:
                    self.verticalBlocks.add(Block(j * 32 + 8, i * 32 + 8, Const.BLACK, 16, 16))

        # Monster kreiren 
        self.enemies = pygame.sprite.Group()
        self.enemies.add(Slime(288, 96, 0, 2))
        self.enemies.add(Slime(288, 320, 0, -2))
        self.enemies.add(Slime(544, 128, 0, 2))
        self.enemies.add(Slime(32, 224, 0, 2))
        self.enemies.add(Slime(160, 64, 2, 0))
        self.enemies.add(Slime(448, 64, -2,0))
        self.enemies.add(Slime(640, 448, 2, 0))
        self.enemies.add(Slime(448, 320, 2, 0))

        # Punkte hinzufügen 
        for i, row in enumerate(enviroment()):
            for j, item in enumerate(row):
                if item != 0:
                    self.dotsGroup.add(Ellipse(j * 32 + 12, i * 32 + 12, Const.WHITE, 8, 8))

        # Sounds laden
        self.pacmanSound = pygame.mixer.Sound("Sounds/pacmanSound.ogg")
        self.gameOverSound = pygame.mixer.Sound("Sounds/gameOverSound.ogg")

    def processGestures(self) -> bool:
        gest = g.return_gesture()
        if gest in [2, 7, 8, 9]: 
            gest = 0
        print("Gesture:", gest)

        event = pygame.event.get()
        if len(event) > 0 and event[0].type == pygame.QUIT: 
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
                self.menu.state -= 1

            elif gest == g.DOWN:
                self.player.move_down()
                print ("Down")
                self.menu.state += 1 

            elif len(event) > 0 and event[0].key == pygame.K_ESCAPE:
                self.gameOver = True
                self.about = False
                
        return False

    def runLogic(self) -> None:
        if not self.gameOver:
            self.player.update(self.horizontalBlocks, self.verticalBlocks)
            block_hit_list = pygame.sprite.spritecollide(self.player, self.dotsGroup, True)

            if len(block_hit_list) > 0:
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
        screen.fill(Const.BLACK)
        # --- Drawing code should go here
        if self.gameOver:
            if self.about:
                self.displayMessage(screen, "Try to control Pacman with Gestures! Good Luck!")
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

    def displayMessage(self, screen, message, color = (255, 0, 0)):
        label = self.font.render(message, True, color)
        width = label.get_width()
        height = label.get_height()
        posX = (Const.SCREEN_WIDTH / 2) - (width / 2)
        posY = (Const.SCREEN_HEIGHT / 2) - (height / 2)
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
            t_h = len(self.items) * height
            posY = (Const.SCREEN_HEIGHT / 2) - (t_h / 2) + (index * height)
            screen.blit(label, (posX, posY))

    def event_handler(self, gest: int) -> None:
        if gest == g.UP:
            if self.state > 0:
                self.state -= 1
            if self.state == 0:
                self.state =2

        elif gest == g.DOWN:
            if self.state < len(self.items) - 1:
                self.state += 1
            else: 
                self.state = 1 
