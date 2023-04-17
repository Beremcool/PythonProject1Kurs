import pygame
import CONSTANTS
import Inscriptions
from PyGameVars import DISPLAY
import Map
import SnakeClass
import Records

class GameProcess():

    def __init__(self):
        self.gameOver = True
        self.isPause = False
        self.mainSnake = SnakeClass.SnakeClass()
        self.mainMap = Map.MapClass()

    def gameStart(self):
        self.gameOver = False
        CONSTANTS.constStandard()
        clock = pygame.time.Clock()
        self.mainSnake = SnakeClass.SnakeClass()
        CONSTANTS.constStandard()
        DISPLAY.fill(CONSTANTS.FRAME_COLOR)
        self.mainMap = Map.MapClass()
        Map.MapClass.drawMap(CONSTANTS.xCount, CONSTANTS.yCount)
        while not self.gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.pause()
                    if event.key == pygame.K_m:
                        self.gameOver = True
                self.mainSnake.changeDirect(event)

            if self.mainSnake.checkDeath():
                self.gameOver = True
            self.gameOverMenu()
            self.mainSnake.SnakeUpdate(self.mainMap)
            pygame.display.flip()
            clock.tick(CONSTANTS.gameSpeed)
            self.mainMap.updateMap(self.mainSnake.Snake)
        pass

    def pause(self):
        self.isPause = True
        clock = pygame.time.Clock()
        while self.isPause:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.isPause = False
                    if event.key == pygame.K_m:
                        self.isPause = False
                        self.gameOver = True
            pygame.display.flip()
            clock.tick(CONSTANTS.gameSpeed)


    def gameOverMenu(self):
        if self.gameOver:
            Records.rewriteRecords(CONSTANTS.name, self.mainSnake.totalScore)
            print(CONSTANTS.name)
            clock = pygame.time.Clock()
            backToMainMenu = False
            DISPLAY.fill(CONSTANTS.FRAME_COLOR)
            Inscriptions.gameOverInscription(self.mainSnake.totalScore)
            while not backToMainMenu:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            backToMainMenu = True
                        if event.key == pygame.K_r:
                            backToMainMenu = True
                            self.gameStart()

                pygame.display.flip()
                clock.tick(CONSTANTS.gameSpeed)