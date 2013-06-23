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
	def __init__(self, hexSideLength, gridColor) :
		self.hex = Hexagon(hexSideLength)
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
			surface.blit(grassTile, (xOffset, yOffset))
			pygame.draw.lines(surface, self.gridColor, True, self.hex.points((xOffset, yOffset)))
			xOffset = xOffset + width

	def drawGrid(self, surface) :
		rows, columns = surface.get_size()
		rows = rows / (self.hex.height() - self.hex.tileOffset()[1])
		columns = columns / self.hex.width()
		for r in range(rows) :
			self.drawRow(surface, columns, r)