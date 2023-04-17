import pygame

# DISPLAY PARAMETERS
sizeX = 1200
sizeY = 800
sizeOfWindow = (1200, 800)

# MAP PARAMETERS
sizeOfBlock = 30
xIndent = 100
yIndent = 100
xCount = 34
yCount = 20
xStart = 17
yStart = 10

# GAMEPLAY PARAMETERS
gameSpeedArray = (30, 35, 40, 45, 50)
gameSpeed = 30
gameSpeedStandard = 30

appleSpawnTimeArray = (3, 5, 6, 6, 6)
appleSpawnTime = 3

appleCost = 1

appleTimeHasteArray = (0.5, 0.5, 1, 1, 1)
appleTimeHaste = 0.5

fastPlaceSpawnTimeArray = (10000, 10, 9, 7, 5)
fastPlaceSpawnTime = 10000

fastPlaceTimeHasteArray = (0, 1, 3, 5, 10)
fastPlaceTimeHaste = 0

fastPlaceCountArray = (0, 2, 2, 4, 8)
fastPlaceCount = 0

stonePlaceCountArray = (0, 1, 2, 3, 4)
stonePlaceCount = 0

stonePlaceSpawnTimeArray = (10000, 13, 10, 9, 8)
stonePlaceSpawnTime = 10000

SnakeMoveDelay = 4

# HOTKEYS INSCRIPTION PARAMETER
xScore = 20
yScore = 20
xScoreClear = 300
yScoreClear = 100

writePause = (800, 20)
writeQuit = (800, 50)

# PAUSE MENU PARAMETERS
pauseSizeX = 400
pauseSizeY = 600

# GAMEOVER INSCRIPTION PARAMETERS
writeYourScore = (500, 300)
writeEscToMainMenu = (360, 350)
writeRToRestart = (470, 400)

# COLORS
WHITE = (255, 255, 255)
BLUE = (200, 200, 255)
HEADER_COLOR = (0, 204, 153)
FRAME_COLOR = (0, 255, 204)
RED = (255, 30, 30)
BRIGHT_RED = (255, 100, 100)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BRIGHT_GREEN = (100, 255, 100)
GREY = (150, 150, 150)

# MAPCHANGER PARAMETERS

CHOOSE_COLOR_COUNT = 4
CHOOSE_COLOR = ((WHITE, (200, 200, 200)),
                (BLUE, (150, 150, 230)),
                ((255, 170, 170), (255, 120, 120)),
                ((50, 140, 90), (10, 180, 20)))

# MAPCHANGER INSCRIPTIONS PARAMETERS
writeESC = (10, 10)
writeP = (10, 40)
writeChange = (500, 65)

xWriteNumberOfColor = 612
yWriteNumberOfCOlor = 30

sizeOfColorBlock = 40
xPanel = 600
yPanel = 20

# DEFAULT MAP
chosen = []


def StandardMap():
    chosen.clear()
    for i in range(xCount):
        chosen.append([])
        for j in range(yCount):
            if (i + j) % 2 == 0:
                chosen[i].append(1)
            else:
                chosen[i].append(0)


# TUTORIAL PARAMETERS
appleTutorial = (50, 200, 50, 50)
fastPlaceTutorial = (50, 400, 50, 50)
stonePlaceTutorial = (50, 600, 50, 50)

writeAppleDescription = (120, 220)
writeFastPlaceDescription = (120, 420)
writeStonePlaceDescription = (120, 620)
writeGoBackTutorialInscription = (700, 20)


def Difficult(selected, value):
    global gameSpeed
    global gameSpeedStandard
    gameSpeed = gameSpeedArray[value - 1]
    gameSpeedStandard = gameSpeed

    global appleSpawnTime
    appleSpawnTime = appleSpawnTimeArray[value - 1]

    global appleTimeHaste
    appleTimeHaste = appleTimeHasteArray[value - 1]

    global fastPlaceSpawnTime
    fastPlaceSpawnTime = fastPlaceSpawnTimeArray[value - 1]

    global fastPlaceTimeHaste
    fastPlaceTimeHaste = fastPlaceTimeHasteArray[value - 1]

    global fastPlaceCount
    fastPlaceCount = fastPlaceCountArray[value - 1]

    global stonePlaceCount
    stonePlaceCount = stonePlaceCountArray[value - 1]

    global stonePlaceSpawnTime
    stonePlaceSpawnTime = stonePlaceSpawnTimeArray[value - 1]


SNAKE_COLOR_ARRAY = ((0, 220, 80),
                     (255, 120, 120),
                     (240, 20, 240),
                     (240, 240, 0))
SNAKE_COLOR = (0, 220, 80)


def SnakeColorChange(selected, value):
    global SNAKE_COLOR
    SNAKE_COLOR = SNAKE_COLOR_ARRAY[value - 1]


# PLAYER NAME
name = 'Alanochka'

# RECORDS
recordCount = 3

recordPos = ((10, 200),
             (10, 400),
             (10, 600))

def nameChange(newName):
    global name
    name = newName



def constStandard():
    global gameSpeed
    gameSpeed = gameSpeedStandard
