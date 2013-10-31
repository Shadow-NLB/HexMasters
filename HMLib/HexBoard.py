import HMLib.Frame as Frame
from HMLib.Hexagon import Hexagon
import HMLib.GameBoard as GameBoard
import HMLib.Map.HexMap as HexMap
import pygame.image

#MODULE CONSTANTS
sinThirty = .5
cosThirty = .866
grassFlat = pygame.image.load(r'Q:\HexMasters\Resource\Tiles\GrassHex.png')
dirtTile = pygame.image.load(r'Q:\HexMasters\Resource\Tiles\DirtHex.png')
waterTile = pygame.image.load(r'Q:\HexMasters\Resource\Tiles\WaterHex.png')

def makeHexTile(surface, hex, offset) :
	maskSurface = surface.copy()
	maskSurface.fill((0,0,0,255))
	tile = surface.copy()
	pygame.draw.polygon(maskSurface, pygame.Color(255, 0, 0, 0),  hex.points())
	tile.blit(maskSurface, (0,0), None, pygame.BLEND_RGBA_SUB)
	return tile


		
# This class represents a hexagonal game board
class HexGameBoard(Frame.Frame):
	#__doc__
	""" This class represents a hexagonal game board.
	At the moment it is just a container a configuration.
	"""
	def __init__(self, hexSideLength, parentFrame, parentPosition, surface) :
		# Call base class initialize
		super(HexGameBoard,self).__init__(parentFrame, parentPosition, surface)
		rows, columns = self.surface.get_size()
		self.hex = Hexagon(hexSideLength)

		# get a row and column count front the surface dimensions
		self.rows = rows / (self.hex.height() - self.hex.tileOffset()[1])
		self.columns = columns / self.hex.width()
		self.tiles = [[grassFlat for x in xrange(columns)] for y in xrange(rows)]
		self.gridColor = (40, 40, 40, 40)

	def renderFrame(self):
      # Draw background tiles (this should be be rendered to a surface, then re-blitted, this will be much faster)
      # Draw space-occupying units/objects 
      # Draw grid
		self.drawGrid()
	
	def handleMouse(self, mousePos) :
		self.highlightHex(self.getMouseHexLocation(mousePos))
	
	def drawRow(self, surface, count, rowNumber) :
		grassTile = makeHexTile(grassFlat, self.hex, (0,0))
		# Get the hex width
		width = self.hex.width()
		# If this is an odd row then we need to use an offset
		xOffset = self.hex.tileOffset()[0] if (rowNumber % 2 == 1) else 0
		yOffset = self.hex.tileOffset()[1] * rowNumber
		# Draw each hex in the row
		for i in range(count) :
			pygame.draw.lines(surface, self.gridColor, True, self.hex.points((xOffset, yOffset)))
			self.surface.blit(makeHexTile(self.tiles[rowNumber][i],self.hex, (xOffset, yOffset)),(xOffset, yOffset))
			xOffset = xOffset + width

	def drawGrid(self) :
		for r in range(self.rows) :
			self.drawRow(self.surface, self.columns, r)
		return self.surface

	def highlightHex(self, loc) :
		row, col = loc
		#if (row < 0 or row > self.rows or col < 0 or col > self.columns) :
		#	raise IndexError('Row/Col not valid')
		#figure out where to drop hex highlight
		xOffset = self.hex.tileOffset()[0] if (row % 2 == 1) else 0
		xOffset = xOffset + col * self.hex.width()
		yOffset = self.hex.tileOffset()[1] * row
		pygame.draw.polygon(self.surface, (0, 255, 0), self.hex.points((xOffset, yOffset)))

	# This is essentially a debug method
	def drawSectors(self) :
		# Sector size for mouse detection
		# yDim is the yTileOffset
		sectorHeight = self.hex.tileOffset()[1]
		# xDim is width of hex, 
		sectorWidth = self.hex.width()

		rows, cols = self.surface.get_size()
		rows = rows / sectorHeight
		cols = cols / sectorWidth

		for i in xrange(rows) :
			pygame.draw.line(self.surface, (255, 255, 0), (0, i * sectorHeight), (self.surface.get_size()[0],i * sectorHeight))
		for i  in xrange(cols) :
			pygame.draw.line(self.surface, (255, 255, 0), (i * sectorWidth, 0), ((i) * sectorWidth, self.surface.get_size()[1]))
		
	def getMouseHexLocation(self, mousePosition) :
		
		# normalize mouse position to frame reference
		mX, mY = self.getRelativePos(mousePosition)

		# Sector size for mouse detection
		# yDim is the yTileOffset
		sectorHeight = self.hex.tileOffset()[1]
		# xDim is width of hex, 
		sectorWidth = self.hex.width()

		#First figure out which sector the mouse is in
		sectorC = mX / sectorWidth
		sectorR = mY / sectorHeight

		# Normalze coordinates to sector
		mX = mX % sectorWidth
		mY = mY % sectorHeight

		# functions that define the diagonal lines in the sector
		def nfx(u) : self.hex.tSideA() - (u % (sectorWidth / 2)) / 2
		def pfx(u) : (u % (sectorWidth / 2)) / 2 

		midPoint = self.hex.tSideB()
		oddRow = (sectorR % 2 == 1)

		hexR = 0 
		hexC = 0
		if (oddRow) :
			# If the mouse is above either line
			if (mY < nfx(mX) or mY < pfx(mX)) :
				#We're in the top hex
				hexR = sectorR - 1
				hexC = sectorC

			# The mouse is left of the midpoint
			elif (mX < midPoint) :
				hexC = sectorC - 1
				hexR = sectorR

			# The mouse is on or to the right of the midpoint	
			else :
				hexC = sectorC
				hexR = sectorR
		else :
			if (mX < midPoint and mY < nfx(mX)) :
				# we're in the top left  hex
				hexR = sectorR - 1
				hexC = sectorC - 1
			elif (mX > midPoint and mY < pfx(mX)) :
				#we're in the top right hex
				hexR = sectorR -1
				hexC = sectorC 			
			else :
				# We're in the main hex
				hexR = sectorR
				hexC = sectorC
		return (hexR, hexC)
