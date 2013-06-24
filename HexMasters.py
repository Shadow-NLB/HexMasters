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
grid = HMLib.HexBoard.HexGameBoard(45, gray, (SCREEN_X, SCREEN_Y))
grid.drawGrid()
grid.highlightHex((0,0))
grid.highlightHex((5,5))
screen.blit(grid.surface, (0,0))


## draw the hex grid
#count = SCREEN_Y / (2 * HEX_SIDE)
#isOdd = False
#for y in range(SCREEN_Y / (2 * HEX_SIDE)) :
#	drawRow(screen, isOdd, y * (2 * HEX_SIDE - HEX_SIDE / 2))
#	isOdd = False if isOdd else True

def input (events) :
	for event in events :
		if (event.type == QUIT) :
			return False
	return True

loop = True
while loop :
	loop = input(pygame.event.get())
	mp = pygame.mouse.get_pos()

	print mp
	print grid.getMouseHexPosition(mp)
	grid.highlightHex(grid.getMouseHexPosition(mp))
	grid.drawSectors()
	screen.blit(grid.surface, (0,0))
	pygame.display.flip()
	raw_input("Press enter to continue")
print grid.hex.width()
print grid.hex.height()
raw_input("Press enter to continue")
pygame.quit()
