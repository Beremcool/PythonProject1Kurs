import pygame
import CONSTANTS
import Inscriptions
from PyGameVars import DISPLAY
import Map

colorNumberFont = pygame.font.SysFont('courier', 25)
cursor = [CONSTANTS.xStart, CONSTANTS.yStart]


def ChangeMap():
    clock = pygame.time.Clock()
    DISPLAY.fill(CONSTANTS.FRAME_COLOR)
    goBack = False
    Map.drawMap(CONSTANTS.xCount, CONSTANTS.yCount)
    Inscriptions.drawChangeMapInstruction()
    drawPanel()
    while not goBack:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                goBack = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                goBack = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                CONSTANTS.StandardMap()
                Map.drawMap(CONSTANTS.xCount, CONSTANTS.yCount)
            changeCell(event)
            changeColor(cursor[0], cursor[1], event)

        clock.tick(CONSTANTS.gameSpeed)
        pygame.display.flip()
    pass


def chooseCell(row, column):
    Map.drawRect(row, column, CONSTANTS.CHOOSE_COLOR[CONSTANTS.chosen[row][column]][1])


def unchooseCell(row, column):
    Map.drawRect(row, column, CONSTANTS.CHOOSE_COLOR[CONSTANTS.chosen[row][column]][0])


def changeColor(row, column, event):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_1:
            CONSTANTS.chosen[row][column] = 0
            chooseCell(row, column)
        if event.key == pygame.K_2:
            CONSTANTS.chosen[row][column] = 1
            chooseCell(row, column)
        if event.key == pygame.K_3:
            CONSTANTS.chosen[row][column] = 2
            chooseCell(row, column)
        if event.key == pygame.K_4:
            CONSTANTS.chosen[row][column] = 3
            chooseCell(row, column)


def changeCell(event):
    if event.type == pygame.KEYDOWN:
        if (event.key == pygame.K_a or event.key == pygame.K_LEFT) and cursor[0] != 0:
            unchooseCell(cursor[0], cursor[1])
            cursor[0] -= 1
            chooseCell(cursor[0], cursor[1])
        if (event.key == pygame.K_w or event.key == pygame.K_UP) and cursor[1] != 0:
            unchooseCell(cursor[0], cursor[1])
            cursor[1] -= 1
            chooseCell(cursor[0], cursor[1])
        if (event.key == pygame.K_s or event.key == pygame.K_DOWN) and cursor[1] != CONSTANTS.yCount - 1:
            unchooseCell(cursor[0], cursor[1])
            cursor[1] += 1
            chooseCell(cursor[0], cursor[1])
        if (event.key == pygame.K_d or event.key == pygame.K_RIGHT) and cursor[1] != CONSTANTS.xCount - 1:
            unchooseCell(cursor[0], cursor[1])
            cursor[0] += 1
            chooseCell(cursor[0], cursor[1])


def drawPanel():
    for row in range(CONSTANTS.CHOOSE_COLOR_COUNT):
        pygame.draw.rect(DISPLAY, CONSTANTS.CHOOSE_COLOR[row][0],
                         (CONSTANTS.xPanel + row * CONSTANTS.sizeOfColorBlock,
                          CONSTANTS.yPanel,
                          CONSTANTS.sizeOfColorBlock,
                          CONSTANTS.sizeOfColorBlock))

    for row in range(CONSTANTS.CHOOSE_COLOR_COUNT):
        numberOfColor = colorNumberFont.render(str(row + 1), False, CONSTANTS.BLACK)
        DISPLAY.blit(numberOfColor,
                     (CONSTANTS.xWriteNumberOfColor + row * CONSTANTS.sizeOfColorBlock,
                      CONSTANTS.yWriteNumberOfCOlor))