import pygame
import CONSTANTS
import Inscriptions
from PyGameVars import DISPLAY
import Map
import SnakeClass
import Records

gameOver = False
isPause = False


def gameStart():
    global gameOver
    global isPause

    gameOver = False
    CONSTANTS.constStandard()
    clock = pygame.time.Clock()
    SnakeClass.SnakeInit()
    CONSTANTS.constStandard()
    DISPLAY.fill(CONSTANTS.FRAME_COLOR)
    Map.drawMap(CONSTANTS.xCount, CONSTANTS.yCount)
    while not gameOver:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause()
                if event.key == pygame.K_m:
                    gameOver = True
            SnakeClass.changeDirect(event)

        if SnakeClass.checkDeath():
            gameOver = True
        gameOverMenu()
        SnakeClass.SnakeUpdate()
        pygame.display.flip()
        clock.tick(CONSTANTS.gameSpeed)
        Map.updateMap(SnakeClass.Snake)
    pass


def pause():
    global isPause
    global gameOver

    isPause = True
    clock = pygame.time.Clock()
    while isPause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    isPause = False
                if event.key == pygame.K_m:
                    isPause = False
                    gameOver = True
        pygame.display.flip()
        clock.tick(CONSTANTS.gameSpeed)


def gameOverMenu():
    global gameOver

    if gameOver:
        Records.rewriteRecords(CONSTANTS.name, SnakeClass.totalScore)
        print(CONSTANTS.name)
        clock = pygame.time.Clock()
        backToMainMenu = False
        DISPLAY.fill(CONSTANTS.FRAME_COLOR)
        Inscriptions.gameOverInscription(SnakeClass.totalScore)
        while not backToMainMenu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        backToMainMenu = True
                    if event.key == pygame.K_r:
                        backToMainMenu = True
                        gameStart()

            pygame.display.flip()
            clock.tick(CONSTANTS.gameSpeed)