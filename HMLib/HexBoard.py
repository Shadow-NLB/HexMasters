import pygame.draw
import pygame.surface
#MODULE CONTANTS
sinThirty = .5
cosThirty = .866
grassFlat = pygame.image.load('Q:\\python\\HexMasters\\Resource\\Tiles\\GrassHex.png')
dirtTile = pygame.image.load('Q:\\python\\HexMasters\\Resource\\Tiles\\DirtHex.png')
waterTile = pygame.image.load('Q:\\python\\HexMasters\\Resource\\Tiles\\WaterHex.png')
 
def makeHexTile(surface, hex, offset) :
	maskSurface = surface.copy()
	maskSurface.fill((0,0,0,255))
	tile = surface.copy()
	pygame.draw.polygon(maskSurface, pygame.Color(255, 0, 0, 0),  hex.points())
	tile.blit(maskSurface, (0,0), None, pygame.BLEND_RGBA_SUB)
	return tile


def makeHexPoints(sideLength, offset) :
	"""Generates a tuple of (x,y) vertices for a regular hexagon with [sideLength]

	@param sideLength - a number of side length
	@param offset - a tuple (x,y) which will be applied to all points created

	NOTE: (0,0) represents top-left corner of space.
	"""
	C = sideLength
	B = C * sinSixty 
	A = C / 2
	return (
		   (int(0 + offset[0]), int(A + C + offset[1])),
		   (int(0 + offset[0]), int(A + offset[1])),
		   (int(B + offset[0]), int(0 + offset[1])),
		   (int(2*B + offset[0]), int(A + offset[1])),
		   (int(2*B + offset[0]), int(A + C + offset[1])),
		   (int(B + offset[0]), int(2 * C + offset[1])))


class Hexagon :
	""" A container for regular hexagon dimensions (pointy side up)"""
	def __init__(self, sideLength) :
		# The length of one side
		# Also the hypotenuse of the triangle which is part of the hexagon
		self.sideLength = sideLength
	def height(self) :
		"""The height of the hexagon at its tips"""
		return self.sideLength + 2 * self.tSideA()
	def width(self) :
		"""The width of the hexagon"""
		return 2 * self.tSideB()
	def tSideA(self) :
		"""Vertical side of inscribed triangle"""
		return int(self.sideLength * sinThirty)
	def tSideB(self) :
		"""Horizontal side of inscribed triable"""
		return int(self.sideLength * cosThirty)	
	def tileOffset(self) :
		"""The tiling offset needed in order to tile multiples of this hexagon"""
		return (self.tSideB(), self.sideLength + self.tSideA())
	def points(self, offset = (0,0)) :
		"""Generates a tuple of (x,y) vertices for a regular hexagon with [sideLength]

		@param sideLength - a number of side length
		@param offset - a tuple (x,y) which will be applied to all points created

		NOTE: (0,0) represents top-left corner of space.
		"""
		return (
				(int(0 + offset[0]), int(self.tSideA() + self.sideLength+ offset[1])),
				(int(0 + offset[0]), int(self.tSideA() + offset[1])),
				(int(self.tSideB() + offset[0]), int(0 + offset[1])),
				(int(2 * self.tSideB() + offset[0]), int(self.tSideA() + offset[1])),
				(int(2 * self.tSideB() + offset[0]), int(self.tSideA() + self.sideLength + offset[1])),
				(int(self.tSideB() + offset[0]), int(2 * self.sideLength + offset[1])))

		
# This class represents a hexagonal game board
# At the moment it is just a container for parameters
class HexGameBoard :
	#__doc__
	""" This class represents a hexagonal game board.
	At the moment it is just a container a configuration.
	"""
	def __init__(self, hexSideLength, gridColor, boardSpaceDim	) :

		self.surface = pygame.Surface(boardSpaceDim)
		rows, columns = self.surface.get_size()
		self.hex = Hexagon(hexSideLength)

		# get a row and column count front the surface dimensions
		self.rows = rows / (self.hex.height() - self.hex.tileOffset()[1])
		self.columns = columns / self.hex.width()
		
		self.gridColor = gridColor
	
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
			xOffset = xOffset + width

	def drawGrid(self) :
		for r in range(self.rows) :
			self.drawRow(self.surface, self.columns, r)
		return self.surface

	def highlightHex(self, loc) :
		row, col = loc
		if (row < 0 or row > self.rows or col < 0 or col > self.columns) :
			raise IndexError('Row/Col not valid')
		#figure out where to drop hex highlight
		xOffset = self.hex.tileOffset()[0] if (row % 2 == 1) else 0
		xOffset = xOffset + col * self.hex.width()
		yOffset = self.hex.tileOffset()[1] * row
		pygame.draw.lines(self.surface, (0, 255, 0), True, self.hex.points((xOffset, yOffset)), 2)

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
		


	def getMouseHexPosition(self, mousePosition) :
		
		# Sector size for mouse detection
		# yDim is the yTileOffset
		sectorHeight = self.hex.tileOffset()[1]
		# xDim is width of hex, 
		sectorWidth = self.hex.width()

		mX, mY = mousePosition

		#First figure out which sector the mouse is in
		sectorC = mX / sectorWidth
		sectorR = mY / sectorHeight

		# Normalze coordinates to sector
		mX = mX % sectorWidth
		mY = mY % sectorHeight

		# functions that define the diagonal lines in the sector
		nfx = lambda u: self.hex.tSideA() - (u % (sectorWidth / 2)) / 2
		pfx = lambda u: (u % (sectorWidth / 2)) / 2 

		midPoint = self.hex.tSideB()
		oddRow = (sectorR % 2 == 1)

		hexR = 0 
		hexC = 0
		print 'mY = {0} nfx(mX) = {1})'.format(mY, nfx(mX))
		print 'mY = {0} pfx(mX) = {1})'.format(mY, pfx(mX))

		if (oddRow) :
			# If the mouse is above either line
			if (mY < nfx(mX) or mY < pfx(mX)) :
				#We're in the top hex
				hexR = sectorR - 1
				hexC = sectorC
				print 'top'
			# The mouse is left of the midpoint
			elif (mX < midPoint) :
				hexC = sectorC - 1
				hexR = sectorR
				print 'left'
			# The mouse is on or to the right of the midpoint	
			else :
				hexC = sectorC
				hexR = sectorR
				print 'right'
		else :
			if (mX < midPoint and mY < nfx(mX)) :
				# we're in the top left  hex
				hexR = sectorR - 1
				hexC = sectorC - 1
				print 'top left'
			elif (mX > midPoint and mY < pfx(mX)) :
				#we're in the top right hex
				hexR = sectorR -1
				hexC = sectorC 			
				print 'top right'	
			else :
				# We're in the main hex
				hexR = sectorR
				hexC = sectorC
				print 'main'
		return (hexR, hexC)
