import pygame
import CONSTANTS
import Map
import Inscriptions
from PyGameVars import DISPLAY

totalScore = 0
headCoordinate = [CONSTANTS.xStart, CONSTANTS.yStart]
Snake = []
isSnakeDead = False
oldDirect = 'w'
direct = 'w'

def SnakeInit():
    global headCoordinate
    global frame
    global totalScore
    global isSnakeDead

    Snake.clear()
    headCoordinate = [CONSTANTS.xStart, CONSTANTS.yStart]
    Snake.append(headCoordinate)
    frame = CONSTANTS.SnakeMoveDelay
    totalScore = 0
    isSnakeDead = False


def SnakeUpdate():
    global oldDirect
    global frame
    global direct

    if frame != CONSTANTS.SnakeMoveDelay:
        if not tuple(headCoordinate) in Map.appleSet:
            Map.SnakeAnimation(frame, Map.getDirect(Snake[1], Snake[0]), Map.getColor(Snake[0][0], Snake[0][1]),
                           Snake[0][0], Snake[0][1])
        Map.SnakeAnimation(frame, oldDirect, CONSTANTS.SNAKE_COLOR, headCoordinate[0], headCoordinate[1])
        if frame == CONSTANTS.SnakeMoveDelay - 1:
            eatApple()
            eatFastPlace()
            eatStone()
        frame += 1
        totalClear()
        Inscriptions.totalShow(totalScore)
    else:
        oldDirect = checkIsNewDirectCorrect()
        changeHeadCoordinate()
        Snake.append(tuple(headCoordinate))
        frame = 1


def changeHeadCoordinate():
    global oldDirect
    global isSnakeDead

    if oldDirect == 'a':
        headCoordinate[0] -= 1
    elif oldDirect == 'w':
        headCoordinate[1] -= 1
    elif oldDirect == 'd':
        headCoordinate[0] += 1
    elif oldDirect == 's':
        headCoordinate[1] += 1
    if Snake.count(tuple(headCoordinate)) > 0 and len(Snake) > 1:
        isSnakeDead = True

def changeDirect(event):
    global direct

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_a or event.key == pygame.K_LEFT:
            direct = 'a'
        elif event.key == pygame.K_w or event.key == pygame.K_UP:
            direct = 'w'
        elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
            direct = 'd'
        elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
            direct = 's'

def checkIsNewDirectCorrect():
    global direct
    global oldDirect

    if len(Snake) == 1:
        return direct

    if oldDirect == 'w' and direct == 's':
        return oldDirect
    elif oldDirect == 's' and direct == 'w':
        return oldDirect
    elif oldDirect == 'a' and direct == 'd':
        return oldDirect
    elif oldDirect == 'd' and direct == 'a':
        return oldDirect
    return direct


def eatApple():
    global totalScore

    if tuple(headCoordinate) in Map.appleSet:
        Map.appleSet.remove(tuple(headCoordinate))
        totalScore += CONSTANTS.appleCost
        CONSTANTS.gameSpeed += CONSTANTS.appleTimeHaste
    else:
        Snake.pop(0)


def eatFastPlace():
    if Map.fastPlace.count(tuple(headCoordinate)) > 0:
        Map.fastPlace.remove(tuple(headCoordinate))
        CONSTANTS.gameSpeed += CONSTANTS.fastPlaceTimeHaste


def eatStone():
    global isSnakeDead

    if Map.stonePlace.count(tuple(headCoordinate)) > 0:
        isSnakeDead = True


def checkDeath():
    global isSnakeDead

    return (headCoordinate[0] == -1 or headCoordinate[0] == CONSTANTS.xCount or
            headCoordinate[1] == -1 or headCoordinate[1] == CONSTANTS.yCount or
            isSnakeDead)


def totalClear():
    pygame.draw.rect(DISPLAY, CONSTANTS.FRAME_COLOR,
                     (0, 0, CONSTANTS.xScoreClear, CONSTANTS.yScoreClear))