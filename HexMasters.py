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
worldFrame = HMLib.Frame.Frame(None, (0,0), screen)
worldFrame.color = (0,100, 100)
menuFrame = HMLib.Frame.Frame(worldFrame, (10, 10), screen.subsurface((10,10, 100, 100)))
#blank the screen
screen.fill(0)
grid = HMLib.HexBoard.HexGameBoard(45, worldFrame, (60,60), screen.subsurface(60,60, 200, 200))
grid2 = HMLib.HexBoard.HexGameBoard(45, worldFrame, (400,400), screen.subsurface(400,400, 200, 200))
grid2.gridColor = (240, 0, 240)
frameList = [menuFrame, grid2, grid, worldFrame]

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
			frame.handleMouse(mp)
			break

def renderFrames(surface, frameList):
	surface.fill(0)
	# Go through framelist in reverse order to render
	for frame in reversed(frameList) :
		frame.renderFrame()

loop = True
while loop :
	loop = input(pygame.event.get())
	renderFrames(screen, frameList)
	mouseHandler(frameList)
	pygame.display.flip()
	raw_input("Press enter to continue")

raw_input("Press enter to continue")
pygame.quit()
