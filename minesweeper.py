# Minesweeper
# By Calvin Probst calvin.probst@gmail.com
# insert git project page here
#

import random
import pygame
import sys
from pygame.locals import *

FPS = 30
BOARDWIDTH = 20
BOARDHEIGHT = 20
BOXSIZE = 30
GAPSIZE = 5
FONTSIZE = 26
WINDOWWIDTH = BOXSIZE * BOARDWIDTH + GAPSIZE * (BOARDWIDTH + 1)
WINDOWHEIGHT = BOXSIZE * BOARDHEIGHT + GAPSIZE * (BOARDHEIGHT + 1)
BOMBCOUNT = int((BOARDHEIGHT * BOARDWIDTH) * 3 / 20)

assert BOMBCOUNT < BOARDHEIGHT * BOARDWIDTH, "Bomb count is larger than square count"

# Colors
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 165, 0)

BGCOLOR = RED


# noinspection PyGlobalUndefined
def main():
    global DISPLAYSURF, FPSCLOCK, BOXFONT
    pygame.init()
    pygame.mixer_music.load("Alcazar.mp3")
    pygame.mixer_music.play(-1, 0.0)
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    BOXFONT = pygame.font.Font('./3Dventure.ttf', FONTSIZE)
    pygame.display.set_caption("Minesweeper")

    mousex = 0
    mousey = 0
    gameBoard = makeNewBoard(BOARDWIDTH, BOARDHEIGHT)
    flags = []
    for x in range(BOARDWIDTH):
        column = []
        for y in range(BOARDHEIGHT):
            column.append(False)
        flags.append(column)

    revealed = []
    for x in range(BOARDWIDTH):
        column = []
        for y in range(BOARDHEIGHT):
            column.append(False)
        revealed.append(column)

    gamePlaying = True
    firstClick = True
    while True:
        leftClicked = False
        rightClicked = False
        middleClicked = False
        if gamePlaying:
            drawGameBoard(revealed, flags)
        pygame.display.update()
        FPSCLOCK.tick(FPS)
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == MOUSEBUTTONUP:
                buttonPressed = event.button
                mousex, mousey = event.pos
                if buttonPressed == 1:
                    leftClicked = True
                elif buttonPressed == 2:
                    middleClicked = True
                elif buttonPressed == 3:
                    rightClicked = True

        boxX, boxY = getBoxPos(mousex, mousey)
        if firstClick and leftClicked and gamePlaying:
            if not boxY == -1 and not boxX == -1:
                print("first click at" + str(boxX) + " " + str(boxY))
                firstBombCount = getBombsNear(gameBoard, boxX, boxY)
                noBomb = False
                while not firstBombCount == 0 and not noBomb:
                    gameBoard = makeNewBoard(BOARDWIDTH, BOARDHEIGHT)
                    firstBombCount = getBombsNear(gameBoard, boxX, boxY)
                    noBomb = not gameBoard[boxX][boxY]
                firstClick = False
                revealBox(gameBoard, revealed, boxX, boxY)
        elif leftClicked and gamePlaying:
            if not boxY == -1 and not boxX == -1:
                print("click at" + str(boxX) + " " + str(boxY))
                if not revealed[boxX][boxY]:
                    if gameBoard[boxX][boxY]:
                        gameOver(gameBoard)
                        gamePlaying = False
                    else:
                        revealed = revealBox(gameBoard, revealed, boxX, boxY)
                        if gameWinCheck(gameBoard, revealed):
                            # draw a flower or something
                            print("winna")
                            gamePlaying = False
                            gameWinJoke()
        elif rightClicked and gamePlaying:
            if not boxY == -1 and not boxX == -1:
                if not revealed[boxX][boxY] or flags[boxX][boxY]:
                    flags[boxX][boxY] = not flags[boxX][boxY]
                    revealed[boxX][boxY] = not revealed[boxX][boxY]
                    if gameWinCheck(gameBoard, revealed):
                        # draw a flower or something
                        print("winna")
                        gamePlaying = False
                        gameWinJoke()
        elif middleClicked and gamePlaying:
            if not boxY == -1 and not boxX == -1:
                if revealed[boxX][boxY]:
                    boxList = getBoxesTouching(boxX, boxY)
                    correctFlags = 0
                    bombsNear = getBombsNear(gameBoard, boxX, boxY)
                    for coords in boxList:
                        nearX = coords[0]
                        nearY = coords[1]
                        if flags[nearX][nearY] and gameBoard[nearX][nearY]:
                            correctFlags += 1
                    if correctFlags == bombsNear:
                        for coords in boxList:
                            nearX = coords[0]
                            nearY = coords[1]
                            if not revealed[nearX][nearY] and not gameBoard[nearX][nearY]:
                                revealBox(gameBoard, revealed, nearX, nearY)
                                if gameWinCheck(gameBoard, revealed):
                                    # draw a flower or something
                                    print("winna")
                                    gamePlaying = False
                                    gameWinJoke()


def gameWinCheck(board, revealedBoxes):
    gameWon = True
    for x in range(0, BOARDWIDTH):
        for y in range(0, BOARDWIDTH):
            if board[x][y] == revealedBoxes[x][y] and not board[x][y]:
                gameWon = False
    return gameWon


def gameWinJoke():
    jokeSurf = pygame.image.load("pizzaJokeJPG.jpg")
    DISPLAYSURF.blit(jokeSurf, (0, 0))
    pygame.display.update()


def makeNewBoard(width, height):
    board = []
    for x in range(width):
        column = []
        for y in range(height):
            column.append(False)
        board.append(column)
    bombsPlaced = 1
    board[9][11] = True
    print("starting while loop")
    while bombsPlaced < BOMBCOUNT:
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        if not board[x][y]:
            board[x][y] = True
            bombsPlaced = bombsPlaced + 1
    return board


def getBoxPos(x, y):
    boxXOverlap = (x - GAPSIZE) % (BOXSIZE + GAPSIZE)
    boxXPos = (x - GAPSIZE - boxXOverlap) / (BOXSIZE + GAPSIZE)
    if not boxXOverlap < BOXSIZE:
        boxXPos = -1
    boxYOverlap = (y - GAPSIZE) % (BOXSIZE + GAPSIZE)
    boxYPos = (y - GAPSIZE - boxYOverlap) / (BOXSIZE + GAPSIZE)
    if not boxYOverlap < BOXSIZE:
        boxYPos = -1
    return int(boxXPos), int(boxYPos)


def revealBox(board, revealedBoxes, x, y):
    if not revealedBoxes[x][y]:
        print("revealing " + str(x) + ' ' + str(y))
        drawBoxAt(GREEN, x, y)
        # draw the revealed square
        revealedBoxes[x][y] = True
        bombsTouchingBox = getBombsNear(board, x, y)
        print("bombs touching " + str(x) + " " + str(y) + ": " + str(bombsTouchingBox))
        # draw the font version of the number
        if bombsTouchingBox == 0:
            for coords in getBoxesTouching(x, y):
                if not revealedBoxes[coords[0]][coords[1]]:
                    revealBox(board, revealedBoxes, coords[0], coords[1])
        else:
            drawText(bombsTouchingBox, x, y)
    return revealedBoxes


def boxToCoords(n):
    return int(GAPSIZE + (GAPSIZE + BOXSIZE) * n)


def drawText(num, x, y):
    textObj = BOXFONT.render(str(num), True, BLACK)
    textRect = textObj.get_rect()
    textRect.center = ((boxToCoords(x) + BOXSIZE / 2), (boxToCoords(y) + BOXSIZE / 2))
    DISPLAYSURF.blit(textObj, textRect)
    pygame.display.update()


def getBoxesTouching(x, y):
    xMin = x - 1
    if xMin < 0:
        xMin = 0
    yMin = y - 1
    if yMin < 0:
        yMin = 0
    xMax = x + 1
    if xMax > BOARDWIDTH - 1:
        xMax = x
    yMax = y + 1
    if yMax > BOARDWIDTH - 1:
        yMax = y
    boxList = []
    for xTemp in range(xMin, xMax + 1):
        for yTemp in range(yMin, yMax + 1):
            if not x == xTemp or not y == yTemp:
                boxList.append([xTemp, yTemp])
    return boxList


def getBombsNear(board, x, y):
    boxList = getBoxesTouching(x, y)
    bombsTouching = 0
    for coords in boxList:
        if board[coords[0]][coords[1]]:
            bombsTouching += 1
    return bombsTouching


def gameOver(board):
    for x in range(0, BOARDWIDTH):
        for y in range(0, BOARDHEIGHT):
            if board[x][y]:
                drawBoxAt(RED, x, y)


def drawBoxAt(boxColor, x, y):
    pygame.draw.rect(DISPLAYSURF, boxColor, (
        boxToCoords(x), boxToCoords(y), BOXSIZE, BOXSIZE))


def drawGameBoard(board, flagBoard):
    for x in range(0, BOARDWIDTH):
        for y in range(0, BOARDHEIGHT):
            # Draw a rectangle for the box
            # fix with math
            if not board[x][y]:
                drawBoxAt(BLUE, x, y)
            elif flagBoard[x][y]:
                drawBoxAt(ORANGE, x, y)


main()
