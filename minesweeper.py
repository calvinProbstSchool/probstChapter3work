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
WINDOWWIDTH = 0
WINDOWHEIGHT = 0
EXPLOSIONSPEED = 10
BOMBCOUNT = 60

assert BOMBCOUNT > BOARDHEIGHT * BOARDWIDTH, "Bomb count is larger than square count"

# Colors
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

BGCOLOR = RED


# noinspection PyGlobalUndefined
def main():
    global FPSCLOCK
    global DISPLAYSURF
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

    firstSelection = None

    while True:
        mouseClicked = False

        drawGameBoard(flags)

        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True

        box = getBoxPos(mousex, mousey)
        if mouseClicked:
            print("click" + str(box))


def makeNewBoard(width, height):
    board = [[False] * height] * width
    bombsPlaced = 0
    while bombsPlaced < BOMBCOUNT:
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        if not board[x][y]:
            board[x][y] = True
            bombsPlaced += 1
    return board


def getBoxPos(x, y):
    return x, y


def drawGameBoard(flagBoard):
    DISPLAYSURF.fill(BGCOLOR)
    for x in flagBoard:
        for y in flagBoard[x]:
            # Draw a rectangle for the box
            # fix with math
            pygame.draw.rect(DISPLAYSURF, GREEN, (6, 7, 8, 9))
            if flagBoard[x][y]:
                # Replace with drawing actual flag at position
                pygame.draw.polygon(DISPLAYSURF, RED, ((1, 0), (1, 1), (2, 2)))
