import pygame
import CONSTANTS
import time
import random
import Inscriptions
from PyGameVars import DISPLAY

appleSpawn = 0
fastPlaceSpawn = 0
stonePlaceSpawn = 0

frame = 0
appleSet = set()
fastPlace = []
stonePlace = []


def getColor(row, column):
    return CONSTANTS.CHOOSE_COLOR[CONSTANTS.chosen[row][column]][0]


def mapInit():
    global appleSpawn
    global fastPlaceSpawn
    global stonePlaceSpawn

    appleSpawn = 0
    fastPlaceSpawn = 0
    stonePlaceSpawn = 0
    appleSet.clear()
    fastPlace.clear()


def drawMap(xCount, yCount):
    mapInit()
    for row in range(xCount):
        for column in range(yCount):
            pygame.draw.rect(DISPLAY, getColor(row, column),
                             (CONSTANTS.xIndent + row * CONSTANTS.sizeOfBlock,
                              CONSTANTS.yIndent + column * CONSTANTS.sizeOfBlock,
                              CONSTANTS.sizeOfBlock,
                              CONSTANTS.sizeOfBlock))


def getRect(row, column):
    return (CONSTANTS.xIndent + row * CONSTANTS.sizeOfBlock,
            CONSTANTS.yIndent + column * CONSTANTS.sizeOfBlock,
            CONSTANTS.sizeOfBlock,
            CONSTANTS.sizeOfBlock)


def drawRect(row, column, color):
    return pygame.draw.rect(DISPLAY, color, getRect(row, column))


def nonZeroCount(*args, point):
    for item in args:
        if item.count(point) > 0:
            return True

    return False


def createApple(snakeTale):
    global appleSpawn
    if time.time() - appleSpawn > CONSTANTS.appleSpawnTime:
        appleSpawn = time.time()
        xApple = random.randint(0, CONSTANTS.xCount - 1)
        yApple = random.randint(0, CONSTANTS.yCount - 1)
        if nonZeroCount(snakeTale, point=(xApple, yApple)):
            createApple(snakeTale)
        else:
            appleSet.add((xApple, yApple))
            drawRect(xApple, yApple, CONSTANTS.RED)


def randomFastPlaceInit(snakeTale):
    xFastPlace = random.randint(0, CONSTANTS.xCount - 1)
    yFastPlace = random.randint(0, CONSTANTS.yCount - 1)

    if nonZeroCount(fastPlace, snakeTale, point=(xFastPlace, yFastPlace)):
        randomFastPlaceInit(snakeTale)
    else:
        fastPlace.append((xFastPlace, yFastPlace))
        drawRect(xFastPlace, yFastPlace, CONSTANTS.BLACK)


def createFastPlace(snakeTale):
    global fastPlaceSpawn
    if time.time() - fastPlaceSpawn > CONSTANTS.fastPlaceSpawnTime:
        fastPlaceSpawn = time.time()
        for cell in fastPlace:
            drawRect(cell[0], cell[1], getColor(cell[0], cell[1]))
        fastPlace.clear()
        for i in range(CONSTANTS.fastPlaceCount):
            randomFastPlaceInit(snakeTale)


def randomStonePlaceInit(snakeTale):
    xStonePlace = random.randint(0, CONSTANTS.xCount - 1)
    yStonePlace = random.randint(0, CONSTANTS.yCount - 1)

    if nonZeroCount(fastPlace, snakeTale, stonePlace, point=(xStonePlace, yStonePlace)):
        randomFastPlaceInit(snakeTale)
    else:
        stonePlace.append((xStonePlace, yStonePlace))
        drawRect(xStonePlace, yStonePlace, CONSTANTS.GREY)


def createStonePlace(snakeTale):
    global stonePlaceSpawn
    if time.time() - stonePlaceSpawn > CONSTANTS.stonePlaceSpawnTime:
        stonePlaceSpawn = time.time()
        for cell in stonePlace:
            drawRect(cell[0], cell[1], getColor(cell[0], cell[1]))
        stonePlace.clear()
        for i in range(CONSTANTS.stonePlaceCount):
            randomStonePlaceInit(snakeTale)


def updateMap(SnakeTale):
    createApple(SnakeTale)
    createFastPlace(SnakeTale)
    createStonePlace(SnakeTale)
    Inscriptions.drawMapHotKeys()


def SnakeAnimation(frame, direct, color, row, column):
    if direct == 'w':
        pygame.draw.rect(DISPLAY, color,
                         (CONSTANTS.xIndent + row * CONSTANTS.sizeOfBlock,
                          CONSTANTS.yIndent + (column + ((CONSTANTS.SnakeMoveDelay - frame - 1) / (
                                  CONSTANTS.SnakeMoveDelay - 1))) * CONSTANTS.sizeOfBlock,
                          CONSTANTS.sizeOfBlock,
                          CONSTANTS.sizeOfBlock / (CONSTANTS.SnakeMoveDelay - 1)))
    elif direct == 's':
        pygame.draw.rect(DISPLAY, color,
                         (CONSTANTS.xIndent + row * CONSTANTS.sizeOfBlock,
                          CONSTANTS.yIndent + (
                                  column + (frame - 1) / (CONSTANTS.SnakeMoveDelay - 1)) * CONSTANTS.sizeOfBlock,
                          CONSTANTS.sizeOfBlock,
                          (CONSTANTS.sizeOfBlock) / (CONSTANTS.SnakeMoveDelay - 1)))
    elif direct == 'a':
        pygame.draw.rect(DISPLAY, color,
                         (CONSTANTS.xIndent + (row + (CONSTANTS.SnakeMoveDelay - frame - 1) / (
                                 CONSTANTS.SnakeMoveDelay - 1)) * CONSTANTS.sizeOfBlock,
                          CONSTANTS.yIndent + column * CONSTANTS.sizeOfBlock,
                          (CONSTANTS.sizeOfBlock) / (CONSTANTS.SnakeMoveDelay - 1),
                          CONSTANTS.sizeOfBlock))
    elif direct == 'd':
        pygame.draw.rect(DISPLAY, color,
                         (CONSTANTS.xIndent + (
                                 row + (frame - 1) / (CONSTANTS.SnakeMoveDelay - 1)) * CONSTANTS.sizeOfBlock,
                          CONSTANTS.yIndent + column * CONSTANTS.sizeOfBlock,
                          (CONSTANTS.sizeOfBlock) / (CONSTANTS.SnakeMoveDelay - 1),
                          CONSTANTS.sizeOfBlock))


def getDirect(cell1, cell2):
    if cell1[0] - cell2[0] == -1:
        return 'a'
    elif cell1[0] - cell2[0] == 1:
        return 'd'
    elif cell1[1] - cell2[1] == -1:
        return 'w'
    elif cell1[1] - cell2[1] == 1:
        return 's'

