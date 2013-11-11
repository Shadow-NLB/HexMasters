class CollisionException(Exception) :
	def __init__(self, fromLoc, toLoc) :
		self.message = "Collision moving from {0} to {1}. GamePiece already exists at {1}".format(fromLoc, toLoc)

class GameBoard :
	""" Represents the playing field populated by game pieces."""
	def __init__(self, boardSize) :
		# A unique identifier for the board
		self.uuid = ""
	
		# Implement board matrix as a list of lists
		self.boardMatrix = [[None for i in xrange(boardSize[0])] for j in xrange(boardSize[1])]

	def addPiece(self, newPiece, location) :
		""" Add a new piece to the game board """
		self.boardMatrix[location[0]][location[1]] = newPiece
		return None

	def removePiece(self, location) :
		""" Remove an existing piece from the board """
		self.boardMatrix[location[0]][location[1]] = None

	def getPiece(self, location) :
		""" Get a GamePiece at a specified location """
		return self.boardMatrix[location[0]][location[1]]

	def movePiece(self, startLoc, endLoc) :
		""" Move a game piece from startLoc to endLoc

		raises a CollisionException if endLoc is not empty
		"""
		# Collision check
		if (self.boardMatrix[endLoc[0]][endLoc[1]] != None) :
			raise CollisionException(startLoc, endLoc)
		else :
			# Move the game piece
			self.boardMatrix[endLoc[0]][endLoc[1]] = self.boardMatrix[startLoc[0]][startLoc[1]]

			# Empty the old position
			self.boardMatrix[startLoc[0]][startLoc[1]] = None

