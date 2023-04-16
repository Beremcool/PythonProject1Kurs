import pygame
import CONSTANTS
import time
import random
import Inscriptions
from PyGameVars import DISPLAY

class MapClass():

    def __init__(self):
        self.appleSpawn = 0
        self.fastPlaceSpawn = 0
        self.stonePlaceSpawn = 0

        self.frame = 0
        self.appleSet = set()
        self.fastPlace = []
        self.stonePlace = []

    @staticmethod
    def getColor(row, column):
        return CONSTANTS.CHOOSE_COLOR[CONSTANTS.chosen[row][column]][0]

    @staticmethod
    def drawMap(xCount, yCount):
        for row in range(xCount):
            for column in range(yCount):
                pygame.draw.rect(DISPLAY, MapClass.getColor(row, column),
                                 (CONSTANTS.xIndent + row * CONSTANTS.sizeOfBlock,
                                  CONSTANTS.yIndent + column * CONSTANTS.sizeOfBlock,
                                  CONSTANTS.sizeOfBlock,
                                  CONSTANTS.sizeOfBlock))

    @staticmethod
    def getRect(row, column):
        return (CONSTANTS.xIndent + row * CONSTANTS.sizeOfBlock,
                CONSTANTS.yIndent + column * CONSTANTS.sizeOfBlock,
                CONSTANTS.sizeOfBlock,
                CONSTANTS.sizeOfBlock)

    @staticmethod
    def drawRect(row, column, color):
        return pygame.draw.rect(DISPLAY, color, MapClass.getRect(row, column))

    @staticmethod
    def nonZeroCount(*args, point):
        for item in args:
            if item.count(point) > 0:
                return True

        return False

    def createApple(self, snakeTale):

        if time.time() - self.appleSpawn > CONSTANTS.appleSpawnTime:
            self.appleSpawn = time.time()
            xApple = random.randint(0, CONSTANTS.xCount - 1)
            yApple = random.randint(0, CONSTANTS.yCount - 1)
            if self.nonZeroCount(snakeTale, point=(xApple, yApple)):
                self.createApple(snakeTale)
            else:
                self.appleSet.add((xApple, yApple))
                self.drawRect(xApple, yApple, CONSTANTS.RED)

    def randomFastPlaceInit(self, snakeTale):
        xFastPlace = random.randint(0, CONSTANTS.xCount - 1)
        yFastPlace = random.randint(0, CONSTANTS.yCount - 1)

        if self.nonZeroCount(self.fastPlace, snakeTale, point=(xFastPlace, yFastPlace)):
            self.randomFastPlaceInit(snakeTale)
        else:
            self.fastPlace.append((xFastPlace, yFastPlace))
            self.drawRect(xFastPlace, yFastPlace, CONSTANTS.BLACK)

    def createFastPlace(self, snakeTale):
        if time.time() - self.fastPlaceSpawn > CONSTANTS.fastPlaceSpawnTime:
            self.fastPlaceSpawn = time.time()
            for cell in self.fastPlace:
                self.drawRect(cell[0], cell[1], self.getColor(cell[0], cell[1]))
            self.fastPlace.clear()
            for i in range(CONSTANTS.fastPlaceCount):
                self.randomFastPlaceInit(snakeTale)

    def randomStonePlaceInit(self, snakeTale):
        xStonePlace = random.randint(0, CONSTANTS.xCount - 1)
        yStonePlace = random.randint(0, CONSTANTS.yCount - 1)

        if self.nonZeroCount(self.fastPlace, snakeTale, self.stonePlace, point=(xStonePlace, yStonePlace)):
            self.randomFastPlaceInit(snakeTale)
        else:
            self.stonePlace.append((xStonePlace, yStonePlace))
            self.drawRect(xStonePlace, yStonePlace, CONSTANTS.GREY)

    def createStonePlace(self, snakeTale):
        if time.time() - self.stonePlaceSpawn > CONSTANTS.stonePlaceSpawnTime:
            self.stonePlaceSpawn = time.time()
            for cell in self.stonePlace:
                self.drawRect(cell[0], cell[1], self.getColor(cell[0], cell[1]))
            self.stonePlace.clear()
            for i in range(CONSTANTS.stonePlaceCount):
                self.randomStonePlaceInit(snakeTale)

    def updateMap(self, SnakeTale):
        self.createApple(SnakeTale)
        self.createFastPlace(SnakeTale)
        self.createStonePlace(SnakeTale)
        Inscriptions.drawMapHotKeys()

    @staticmethod
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

    @staticmethod
    def getDirect(cell1, cell2):
        if cell1[0] - cell2[0] == -1:
            return 'a'
        elif cell1[0] - cell2[0] == 1:
            return 'd'
        elif cell1[1] - cell2[1] == -1:
            return 'w'
        elif cell1[1] - cell2[1] == 1:
            return 's'

