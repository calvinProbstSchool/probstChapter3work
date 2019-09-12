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
GAPSIZE = 1
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
    print("all vars init")
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


    while True:
        mouseClicked = False

        drawGameBoard()
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
        if mouseClicked:
            print("click" + str(boxX) + " " + str(boxY))


def makeNewBoard(width, height):
    board = []
    for x in range(width):
        column = []
        for y in range(height):
            column.append(False)
        board.append(column)
    bombsPlaced = 0
    while bombsPlaced < BOMBCOUNT:
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        if not board[x][y]:
            board[x][y] = True
            bombsPlaced = bombsPlaced + 1
            print(str(bombsPlaced))
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


def drawGameBoard():
    for x in range(0, BOARDWIDTH):
        for y in range(0, BOARDHEIGHT):
            # Draw a rectangle for the box
            # fix with math
            pygame.draw.rect(DISPLAYSURF, BLUE, pygame.Rect((GAPSIZE + (GAPSIZE + BOXSIZE) * x), (GAPSIZE + (GAPSIZE + BOXSIZE) * y), BOXSIZE, BOXSIZE), 1)
            # if flagBoard[x][y]:
            # Replace with drawing actual flag at position
            # pygame.draw.polygon(DISPLAYSURF, RED, ((1, 0), (1, 1), (2, 2)))

main()