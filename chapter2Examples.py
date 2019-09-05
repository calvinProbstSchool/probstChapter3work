import pygame
import sys

from pygame.locals import *

pygame.init()

DISPLAYSURF = pygame.display.set_mode((500, 500))
alphaSurf = DISPLAYSURF.convert_alpha()
pygame.display.set_caption("Calvin's Bangin' Example Window")

TEAL_TRANSPARENT = (0, 255, 100, 128)
ORANGE_SOLID = (255, 165, 0)
HOTPINK_TRANSPARENT = (255, 105, 180, 200)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


pygame.draw.polygon(DISPLAYSURF, ORANGE_SOLID, ((200, 200), (100, 200), (200, 100)))
pygame.draw.line(DISPLAYSURF, RED, (0, 0), (350, 300), 3)
pygame.draw.ellipse(DISPLAYSURF, BLUE, pygame.Rect(300, 300, 200, 100))
#A fully transparent rect covering the alphaSurf
pygame.draw.rect(alphaSurf, (255, 255, 255, 0), pygame.Rect(0, 0, 500, 500))
pygame.draw.rect(alphaSurf, TEAL_TRANSPARENT, pygame.Rect(100, 100, 100, 50))
pygame.draw.circle(alphaSurf, HOTPINK_TRANSPARENT, (200, 200), 50)
DISPLAYSURF.blit(alphaSurf, (0, 0))
DANNYBOY = pygame.image.load('daniels4Head.png')
DISPLAYSURF.blit(DANNYBOY, (400, 0))
pygame.mixer_music.load("Alcazar.mp3")
pygame.mixer_music.play(-1, 0.0)

while True:
    for event in pygame.event.get():
        print(str(event))
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
