import pygame
import CONSTANTS
import Inscriptions
from PyGameVars import DISPLAY
import Map

class ChangeMapClass():

    def __init__(self):
        self.colorNumberFont = pygame.font.SysFont('courier', 25)
        self.cursor = [CONSTANTS.xStart, CONSTANTS.yStart]

    def ChangeMap(self):
        clock = pygame.time.Clock()
        DISPLAY.fill(CONSTANTS.FRAME_COLOR)
        goBack = False
        Map.MapClass.drawMap(CONSTANTS.xCount, CONSTANTS.yCount)
        Inscriptions.drawChangeMapInstruction()
        self.drawPanel()
        while not goBack:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    goBack = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    goBack = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                    CONSTANTS.StandardMap()
                    Map.MapClass.drawMap(CONSTANTS.xCount, CONSTANTS.yCount)
                self.changeCell(event)
                self.changeColor(self.cursor[0], self.cursor[1], event)

            clock.tick(CONSTANTS.gameSpeed)
            pygame.display.flip()
        pass

    @staticmethod
    def chooseCell(row, column):
        Map.MapClass.drawRect(row, column, CONSTANTS.CHOOSE_COLOR[CONSTANTS.chosen[row][column]][1])

    @staticmethod
    def unchooseCell(row, column):
        Map.MapClass.drawRect(row, column, CONSTANTS.CHOOSE_COLOR[CONSTANTS.chosen[row][column]][0])


    def changeColor(self, row, column, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                CONSTANTS.chosen[row][column] = 0
                self.chooseCell(row, column)
            if event.key == pygame.K_2:
                CONSTANTS.chosen[row][column] = 1
                self.chooseCell(row, column)
            if event.key == pygame.K_3:
                CONSTANTS.chosen[row][column] = 2
                self.chooseCell(row, column)
            if event.key == pygame.K_4:
                CONSTANTS.chosen[row][column] = 3
                self.chooseCell(row, column)

    def changeCell(self, event):
        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_a or event.key == pygame.K_LEFT) and self.cursor[0] != 0:
                self.unchooseCell(self.cursor[0], self.cursor[1])
                self.cursor[0] -= 1
                self.chooseCell(self.cursor[0], self.cursor[1])
            if (event.key == pygame.K_w or event.key == pygame.K_UP) and self.cursor[1] != 0:
                self.unchooseCell(self.cursor[0], self.cursor[1])
                self.cursor[1] -= 1
                self.chooseCell(self.cursor[0], self.cursor[1])
            if (event.key == pygame.K_s or event.key == pygame.K_DOWN) and self.cursor[1] != CONSTANTS.yCount - 1:
                self.unchooseCell(self.cursor[0], self.cursor[1])
                self.cursor[1] += 1
                self.chooseCell(self.cursor[0], self.cursor[1])
            if (event.key == pygame.K_d or event.key == pygame.K_RIGHT) and self.cursor[1] != CONSTANTS.xCount - 1:
                self.unchooseCell(self.cursor[0], self.cursor[1])
                self.cursor[0] += 1
                self.chooseCell(self.cursor[0], self.cursor[1])


    def drawPanel(self):
        for row in range(CONSTANTS.CHOOSE_COLOR_COUNT):
            pygame.draw.rect(DISPLAY, CONSTANTS.CHOOSE_COLOR[row][0],
                             (CONSTANTS.xPanel + row * CONSTANTS.sizeOfColorBlock,
                              CONSTANTS.yPanel,
                              CONSTANTS.sizeOfColorBlock,
                              CONSTANTS.sizeOfColorBlock))

        for row in range(CONSTANTS.CHOOSE_COLOR_COUNT):
            numberOfColor = self.colorNumberFont.render(str(row + 1), False, CONSTANTS.BLACK)
            DISPLAY.blit(numberOfColor,
                         (CONSTANTS.xWriteNumberOfColor + row * CONSTANTS.sizeOfColorBlock,
                          CONSTANTS.yWriteNumberOfCOlor))