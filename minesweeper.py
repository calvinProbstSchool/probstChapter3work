# Minesweeper
# By Calvin Probst calvin.probst@gmail.com
# insert git project page here
#

import random
import pygame
import sys
from pygame.locals import *

FPS = 30
WINDOWWIDTH = 0
WINDOWHEIGHT = 0
EXPLOSIONSPEED = 10

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

    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
