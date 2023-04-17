import CONSTANTS
import pygame

import Inscriptions
from PyGameVars import DISPLAY

recordArray = []


def rewriteRecords(username, totalScore):
    global recordArray
    fillRecordArray()
    recordArray.append(tuple([totalScore, username]))
    recordArray.sort()
    recordArray.reverse()
    if len(recordArray) > CONSTANTS.recordCount:
        recordArray = recordArray[:-1]
    newRecordFile = open("Records", 'w')
    for record in recordArray:
        print(record[1], record[0], file=newRecordFile)


def fillRecordArray():
    global recordArray
    file = open("Records", 'r')
    recordArray.clear()
    for line in file:
        line.strip()
        record = line.split()
        record.reverse()
        recordArray.append(tuple([int(record[0]), record[1]]))
    file.close()


def showRecords():
    clock = pygame.time.Clock()
    DISPLAY.fill(CONSTANTS.FRAME_COLOR)
    fillRecordArray()
    backToMainMenu = False
    Inscriptions.pressEscToGoBack(Inscriptions.recordFont)
    for i in range(CONSTANTS.recordCount):
        Inscriptions.showRecord(recordArray[i], CONSTANTS.recordPos[i])
    while not backToMainMenu:
        for event in pygame.event.get():
            if event.type == pygame.quit:
                quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                backToMainMenu = True
        clock.tick(CONSTANTS.gameSpeed)
        pygame.display.flip()