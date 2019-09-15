# Minesweeper
# By Calvin Probst calvin.probst@gmail.com
# insert git project page here
#

import random
import pygame
import sys
import time
from pygame.locals import *

FPS = 30
BOARDWIDTH = 20
BOARDHEIGHT = 20
BOXSIZE = 30
GAPSIZE = 5
WINDOWWIDTH = BOXSIZE * BOARDWIDTH + GAPSIZE * (BOARDWIDTH + 1)
WINDOWHEIGHT = BOXSIZE * BOARDHEIGHT + GAPSIZE * (BOARDHEIGHT + 1)
EXPLOSIONSPEED = 10
BOMBCOUNT = int((BOARDHEIGHT * BOARDWIDTH) * 3 / 20)

assert BOMBCOUNT < BOARDHEIGHT * BOARDWIDTH, "Bomb count is larger than square count"

# Colors
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

BGCOLOR = RED


def main():
    global DISPLAYSURF, FPSCLOCK
    pygame.init()
    pygame.mixer_music.load("Alcazar.mp3")
    pygame.mixer_music.play(-1, 0.0)
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption("Minesweeper")

    mousex = 0
    mousey = 0
    gameBoard = makeNewBoard(BOARDWIDTH, BOARDHEIGHT)
    flags = [[False] * BOARDHEIGHT] * BOARDWIDTH

    revealed = flags

    gamePlaying = True

    while True:
        mouseClicked = False

        if gamePlaying:
            drawGameBoard(revealed)
        pygame.display.update()
        FPSCLOCK.tick(FPS)
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True

        boxX, boxY = getBoxPos(mousex, mousey)
        if mouseClicked and gamePlaying:
            if not boxY == -1 and not boxX == -1:
                if not revealed[boxX][boxY]:
                    if gameBoard[boxX][boxY]:
                        gameOver()
                        gamePlaying = False
                    else:
                        revealBox(gameBoard, revealed, boxX, boxY)


def makeNewBoard(width, height):
    board = [[False] * BOARDHEIGHT] * BOARDWIDTH
    bombsPlaced = 0
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
    return boxXPos, boxYPos

def revealBox(board,revealedBoxes, x, y):
    if not revealedBoxes[x][y]:
        # draw the revealed square
        revealedBoxes[x][y] = True
        bombsTouchingBox = getBombsNear(board, x, y)
        # draw the font version of the number
        if bombsTouchingBox = 0
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
            for xTemp in range(xMin, xMax + 1):
                for yTemp in range(yMin, yMax + 1):
                    if not xTemp == x and not yTemp == y:
                        revealedBoxes = revealBox(board, revealedBoxes, x, y)
    return revealedBoxes
    
    
def getBombsNear(board, x, y):
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
    bombsTouching = 0
    for xTemp in range(xMin, xMax + 1):
        for yTemp in range(yMin, yMax + 1):
            if board[xTemp][yTemp]:
                bombsTouching = bombsTouching + 1
    return bombsTouching
            

def gameOver(board):
    for x in range(0, BOARDWIDTH):
        for y in range(0, BOARDHEIGHT):
            if board[x][y]:
                # draw the bombs exploded


def drawGameBoard(board):
    for x in range(0, BOARDWIDTH):
        for y in range(0, BOARDHEIGHT):
            # Draw a rectangle for the box
            # fix with math
            if not board[x][y]:
                pygame.draw.rect(DISPLAYSURF, BLUE, pygame.Rect((GAPSIZE + (GAPSIZE + BOXSIZE) * x), (GAPSIZE + (GAPSIZE + BOXSIZE) * y), BOXSIZE, BOXSIZE))
            # if flagBoard[x][y]:
            # Replace with drawing actual flag at position
            # pygame.draw.polygon(DISPLAYSURF, RED, ((1, 0), (1, 1), (2, 2)))

main()
