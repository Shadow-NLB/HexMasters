import pygame, sys,os
import HMLib.HexBoard
from pygame.locals import * 
import itertools

# Constants
SCREEN_X = 800
SCREEN_Y = 800
WINDOW_BUFFER = 50
GRID_AREA = (WINDOW_BUFFER, WINDOW_BUFFER, SCREEN_X - 2 * WINDOW_BUFFER, SCREEN_Y - 2 * WINDOW_BUFFER)
# A color for our hexagon
red =(255, 0 , 0)
green = (50, 255, 50)
gray = (240, 240, 240, 2)

#initlaize pygame
pygame.init()

#get the screen
window = pygame.display.set_mode((SCREEN_X,SCREEN_Y))
screen = pygame.display.get_surface()

#blank the screen
screen.fill(0)
grid = HMLib.HexBoard.HexGameBoard(40, gray)
grid.drawGrid(screen.subsurface(GRID_AREA))


## draw the hex grid
#count = SCREEN_Y / (2 * HEX_SIDE)
#isOdd = False
#for y in range(SCREEN_Y / (2 * HEX_SIDE)) :
#	drawRow(screen, isOdd, y * (2 * HEX_SIDE - HEX_SIDE / 2))
#	isOdd = False if isOdd else True


pygame.display.flip()


def input (events) :
	for event in events :
		if (event.type == QUIT) :
			return False
	return True

loop = True
while loop :
	loop = input(pygame.event.get())

pygame.quit()
