import pygame.draw

INVALID_POSITION = (-1, -1)

def pointInBox(point, boxDim) :
	if (point[0] < 0 or point[0] > boxDim[0] or point[1] < 0 or point[1] > boxDim[1]) :
		return False
	else :
		return True
		
class Frame :
	color = (40,40,40)
	""" Defines an interface for frame objects
	
	Frames are used to hierarchically sub-divide the display area.
	Frames contain a surface upon which things may draw.
	Frames are able to normalize world coordinates to their own dimensions.
	Frames provide a general way to create regions in the display area,
	for things such as the game board, the HUD, and menus.
	"""
	def __init__(self, parentFrame, parentPosition, surface) :
		self.surface = surface
		self.pFrame = parentFrame
		self.pPos = parentPosition
				
		## logical checks
		## The length of the frame plus the frames offset in its parent
		## Cannot exceed the length of the parent
		#if (self.pFrame != None) :
		#	if ((parentFrame.xSize < (self.xSize + self.pPos[0])) or (parentFrame.ySize < (self.ySize + self.pPos[1]))) :
		#		raise Exception("Invalid Frame Size")

	def getRenderBox(self) :
		x,y = self.getWorldCoords((0,0))
		return (x, y, self.xSize, self.ySize)
	 
	def getWorldCoords(self, frameCoords) :
		# If the frame has no parent it must be the world frame
		# Therefore is coordinates are the world coordinates
		if (self.pFrame == None) :
			return frameCoords
		else :
			return self.pFrame.getWorldCoords([sum(a) for a in zip(frameCoords, self.pPos)])

	def getRelativePos(self, worldCoords) :
		# If we have a parent frame
		if (self.pFrame != None) :
			worldFramePos = tuple(self.pFrame.getWorldCoords(self.pPos))
			relPos = (worldCoords[0] - worldFramePos[0], worldCoords[1] - worldFramePos[1] )
			if (pointInBox(relPos, self.surface.get_size())) :
				return relPos
			else :
				return INVALID_POSITION
		else :
			return worldCoords

	def pointInFrame(self, point) :
		if (self.getRelativePos(point) == INVALID_POSITION) :
			return False
		else :
			return True

	def renderFrame(self) :
		pygame.draw.rect(self.surface, self.color, (0,0) + self.surface.get_size())

	def handleMouse(self, mousePos):
		print "I got the the mouse"
		print self

