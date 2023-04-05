import pygame
from PyGameVars import DISPLAY
import CONSTANTS

changeMapFont = pygame.font.SysFont('courier', 25)
mapHotkeyFont = pygame.font.SysFont('courier', 20)
gameOverFont = pygame.font.SysFont('courier', 30)
tutorialInstructionFont = pygame.font.SysFont('courier', 25)
totalScoreFont = pygame.font.SysFont('courier', 36)
recordFont = pygame.font.SysFont('courier', 27)

def drawChangeMapInstruction():
    pressEscToGoBack(changeMapFont)

    howToStandardMap = changeMapFont.render("Press P to make map standard", False, CONSTANTS.BRIGHT_RED)
    DISPLAY.blit(howToStandardMap, CONSTANTS.writeP)

    pushToChangeColor = changeMapFont.render("Press number key to change color", False, CONSTANTS.BRIGHT_RED)
    DISPLAY.blit(pushToChangeColor, CONSTANTS.writeChange)


def drawMapHotKeys():
    pauseHotKey = mapHotkeyFont.render("Press ESC to PAUSE and UNPAUSE", False, CONSTANTS.BRIGHT_RED)
    quitGame = mapHotkeyFont.render("Press M to QUIT", False, CONSTANTS.BRIGHT_RED)

    DISPLAY.blit(pauseHotKey, CONSTANTS.writePause)
    DISPLAY.blit(quitGame, CONSTANTS.writeQuit)


def gameOverInscription(total):
    yourScore = gameOverFont.render(f"YOUR SCORE: {total}", False, CONSTANTS.BRIGHT_RED)
    escToMainMenu = gameOverFont.render("PRESS ESC TO GET BACK TO MENU", False, CONSTANTS.BRIGHT_RED)
    pressRToRestart = gameOverFont.render("PRESS R TO RESTART", False, CONSTANTS.BRIGHT_RED)

    DISPLAY.blit(yourScore, CONSTANTS.writeYourScore)
    DISPLAY.blit(escToMainMenu, CONSTANTS.writeEscToMainMenu)
    DISPLAY.blit(pressRToRestart, CONSTANTS.writeRToRestart)

def tutorialInscription():
    backHotKey = tutorialInstructionFont.render("Press ESC to back to menu", False, CONSTANTS.BRIGHT_RED)
    DISPLAY.blit(backHotKey, CONSTANTS.writeGoBackTutorialInscription)


def totalShow(totalScore):
    score = totalScoreFont.render(f"Total: {totalScore}", False, CONSTANTS.BRIGHT_RED)
    DISPLAY.blit(score, (CONSTANTS.xScore, CONSTANTS.yScore))


def showRecord(recordData, position):
    record = recordFont.render(f"{recordData[1]}: {recordData[0]}", False, CONSTANTS.BRIGHT_RED)
    DISPLAY.blit(record, position)


def pressEscToGoBack(font):
    howToGoBack = font.render("Press ESC to go back", False, CONSTANTS.BRIGHT_RED)
    DISPLAY.blit(howToGoBack, CONSTANTS.writeESC)