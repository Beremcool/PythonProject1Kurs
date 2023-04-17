import pygame
import pygame_menu
import CONSTANTS
import ChangeMap
import GameProcess
import Records
import Tutorial
from PyGameVars import DISPLAY

CONSTANTS.StandardMap()


def StartGame():
    mainGame = GameProcess.GameProcess()
    mainGame.gameStart()


def StartChangeMap():
    mapChanger = ChangeMap.ChangeMapClass()
    mapChanger.ChangeMap()


mainMenu = pygame_menu.Menu('THE SNAKE GAME 2000', CONSTANTS.sizeX, CONSTANTS.sizeY,
                       theme=pygame_menu.themes.THEME_GREEN)

mainMenu.add.text_input('Name :', default=CONSTANTS.name, onchange=CONSTANTS.nameChange)
mainMenu.add.selector('Difficulty :', [('Super Chill', 1),
                                   ('Easy', 2),
                                   ('Normal', 3),
                                   ('Hard', 4),
                                   ('Импосибле', 5)],
                                    onchange=CONSTANTS.Difficult)
mainMenu.add.selector('Snake color:', [('Green', 1),
                                    ('Pink', 2),
                                    ('Violet', 3),
                                    ('Yellow', 4)],
                                    onchange=CONSTANTS.SnakeColorChange)
mainMenu.add.button('Play', StartGame)
mainMenu.add.button('Change Map', StartChangeMap)
mainMenu.add.button('Records', Records.showRecords)
mainMenu.add.button('Tutorial', Tutorial.tutorial)
mainMenu.add.button('Quit', pygame_menu.events.EXIT)

mainMenu.mainloop(DISPLAY)

pygame.quit()