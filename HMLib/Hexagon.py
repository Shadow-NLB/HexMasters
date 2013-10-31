sinThirty = .5
cosThirty = .866
class Hexagon:
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