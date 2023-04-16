import pygame
import CONSTANTS
import Map
import Inscriptions
from PyGameVars import DISPLAY


class SnakeClass:

    def __init__(self):
        self.headCoordinate = [CONSTANTS.xStart, CONSTANTS.yStart]
        self.frame = CONSTANTS.SnakeMoveDelay
        self.totalScore = 0
        self.isSnakeDead = False
        self.Snake = []
        self.direct = 'w'
        self.oldDirect = 'w'
        self.Snake.append(self.headCoordinate)

    def SnakeUpdate(self, mainMap):

        if self.frame != CONSTANTS.SnakeMoveDelay:
            if not tuple(self.headCoordinate) in mainMap.appleSet:
                Map.MapClass.SnakeAnimation(self.frame, Map.MapClass.getDirect(self.Snake[1], self.Snake[0]),
                                   Map.MapClass.getColor(self.Snake[0][0], self.Snake[0][1]),
                                   self.Snake[0][0], self.Snake[0][1])
            Map.MapClass.SnakeAnimation(self.frame, self.oldDirect, CONSTANTS.SNAKE_COLOR,
                               self.headCoordinate[0], self.headCoordinate[1])
            if self.frame == CONSTANTS.SnakeMoveDelay - 1:
                self.eatApple(mainMap)
                self.eatFastPlace(mainMap)
                self.eatStone(mainMap)
            self.frame += 1
            self.totalClear()
            Inscriptions.totalShow(self.totalScore)
        else:
            self.oldDirect = self.checkIsNewDirectCorrect()
            self.changeHeadCoordinate()
            self.Snake.append(tuple(self.headCoordinate))
            self.frame = 1


    def changeHeadCoordinate(self):

        if self.oldDirect == 'a':
            self.headCoordinate[0] -= 1
        elif self.oldDirect == 'w':
            self.headCoordinate[1] -= 1
        elif self.oldDirect == 'd':
            self.headCoordinate[0] += 1
        elif self.oldDirect == 's':
            self.headCoordinate[1] += 1
        if self.Snake.count(tuple(self.headCoordinate)) > 0 and len(self.Snake) > 1:
            self.isSnakeDead = True

    def changeDirect(self, event):

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                self.direct = 'a'
            elif event.key == pygame.K_w or event.key == pygame.K_UP:
                self.direct = 'w'
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                self.direct = 'd'
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                self.direct = 's'

    def checkIsNewDirectCorrect(self):

        if len(self.Snake) == 1:
            return self.direct

        if self.oldDirect == 'w' and self.direct == 's':
            return self.oldDirect
        elif self.oldDirect == 's' and self.direct == 'w':
            return self.oldDirect
        elif self.oldDirect == 'a' and self.direct == 'd':
            return self.oldDirect
        elif self.oldDirect == 'd' and self.direct == 'a':
            return self.oldDirect
        return self.direct

    def eatApple(self, mainMap):

        if tuple(self.headCoordinate) in mainMap.appleSet:
            mainMap.appleSet.remove(tuple(self.headCoordinate))
            self.totalScore += CONSTANTS.appleCost
            CONSTANTS.gameSpeed += CONSTANTS.appleTimeHaste
        else:
            self.Snake.pop(0)

    def eatFastPlace(self, mainMap):

        if mainMap.fastPlace.count(tuple(self.headCoordinate)) > 0:
            mainMap.fastPlace.remove(tuple(self.headCoordinate))
            CONSTANTS.gameSpeed += CONSTANTS.fastPlaceTimeHaste

    def eatStone(self, mainMap):

        if mainMap.stonePlace.count(tuple(self.headCoordinate)) > 0:
            self.isSnakeDead = True

    def checkDeath(self):
        return (self.headCoordinate[0] == -1 or self.headCoordinate[0] == CONSTANTS.xCount or
                self.headCoordinate[1] == -1 or self.headCoordinate[1] == CONSTANTS.yCount or
                self.isSnakeDead)

    @staticmethod
    def totalClear():
        pygame.draw.rect(DISPLAY, CONSTANTS.FRAME_COLOR,
                         (0, 0, CONSTANTS.xScoreClear, CONSTANTS.yScoreClear))

