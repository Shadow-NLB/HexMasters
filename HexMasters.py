import pygame
import HMLib.Frame
import HMLib.Hexagon
import HMLib.HexMap
import HMLib.BasicUnits as Units
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


# Establish frames
# Top Level Frame
worldFrame = HMLib.Frame.Frame(None, (0,0), screen)
worldFrame.color = (0,100, 100)
# HUD FRAME
hudFrame = HMLib.Frame.Frame(worldFrame, (10, 10), screen.subsurface((10,10, 100, 100)))
hudFrame.color = (100,100,100)

#blank the screen
screen.fill(0)

# Create the logical game board
hexMap = HMLib.HexMap.HexMap(10,10)
hexMap.insert(Units.Swordsmen(), (0,1))

#establish the hexagon dimensions
standard_hex = HMLib.Hexagon.Hexagon(45)
gameBoardFrame = HMLib.HexBoard.HexGameBoard(hexMap, standard_hex, worldFrame, (0,0), screen.subsurface(0,0, 300,300))
gameBoardFrame.gridColor = (240, 0, 240)
frameList = [gameBoardFrame, hudFrame, worldFrame]

def input (events) :
	for event in events :
		if (event.type == pygame.QUIT) :
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

fontThing = pygame.font.Font(None,45)

loop = True
while loop :
	loop = input(pygame.event.get())
	renderFrames(screen, frameList)
	mouseHandler(frameList)
	screen.blit(fontThing.render('This is text', True, (0,0,0)), (10,10))
	pygame.display.flip()
	#raw_input("Press enter to continue")


raw_input("Press enter to continue")
