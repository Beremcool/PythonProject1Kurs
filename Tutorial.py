import pygame
from PyGameVars import DISPLAY
import CONSTANTS
import Inscriptions

tutorialFont = pygame.font.SysFont('courier', 30)


def tutorial():
    clock = pygame.time.Clock()
    DISPLAY.fill(CONSTANTS.FRAME_COLOR)
    drawGameThings()
    writeDescription()
    Inscriptions.tutorialInscription()
    backToMainMenu = False
    while not backToMainMenu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    backToMainMenu = True
        clock.tick(CONSTANTS.gameSpeed)
        pygame.display.flip()


def drawGameThings():
    pygame.draw.rect(DISPLAY, CONSTANTS.RED, CONSTANTS.appleTutorial)
    pygame.draw.rect(DISPLAY, CONSTANTS.BLACK, CONSTANTS.fastPlaceTutorial)
    pygame.draw.rect(DISPLAY, CONSTANTS.GREY, CONSTANTS.stonePlaceTutorial)

def writeDescription():
    appleDescription = tutorialFont.render("Increase your speed, give you score", False, CONSTANTS.BRIGHT_RED)
    DISPLAY.blit(appleDescription, CONSTANTS.writeAppleDescription)

    fastPlaceDescription = tutorialFont.render("Strongly increase your speed, doesn't give you score",
                                               False, CONSTANTS.BRIGHT_RED)
    DISPLAY.blit(fastPlaceDescription, CONSTANTS.writeFastPlaceDescription)

    stonePlaceDescription = tutorialFont.render("If you eat it you will die", False, CONSTANTS.BRIGHT_RED)
    DISPLAY.blit(stonePlaceDescription, CONSTANTS.writeStonePlaceDescription)