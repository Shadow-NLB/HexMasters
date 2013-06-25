import pygame, sys,os
import HMLib.HexBoard
import HMLib.IFrame
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

#frames
worldFrame = HMLib.IFrame.IFrame(None, (0,0), (SCREEN_X, SCREEN_Y), (100,100,0))
gridFrame = HMLib.IFrame.IFrame(worldFrame, (10, 10), (100,100), (255, 0, 255))

frameList = [gridFrame, worldFrame]



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

def mouseHandler(frameList) :
	mp = pygame.mouse.get_pos()

	# Go through framelist to figure out who gets the mouse pointer
	for frame in frameList :
		if frame.pointInFrame(mp) :
			print 'Point in frame'
			print frame
			break

def renderFrames(surface, frameList):
	# Go through framelist in reverse order to render
	for frame in reversed(frameList) :
		frame.renderFrame(surface.subsurface(frame.getRenderBox()))

loop = True
while loop :
	loop = input(pygame.event.get())
	mp = pygame.mouse.get_pos()
	grid.clearGrid()
	grid.drawGrid()
	grid.highlightHex(grid.getMouseHexPosition(mp))
	#grid.drawSectors()
	screen.blit(grid.surface, (0,0))
	renderFrames(screen, frameList)
	mouseHandler(frameList)
	pygame.display.flip()
	raw_input("Press enter to continue")

raw_input("Press enter to continue")
pygame.quit()
