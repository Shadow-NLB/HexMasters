
class Swordsmen :
	maxHP = 10
	defense = 3
	attack = 2
	move = 1

class UnitStats :
	currentHP = 0

class GamePiece :
	"""Represents an instance of a game object which resides on a GameBoard"""
	def __init__(self) :
		# A unique identifier for this instance
		self.uuid = ""
		# A name for this instance
		self.name = ""
	# Game pieces can be seperated into their visual representation and
	# and their game logic representation

	#Visual needs
		# Current display image
	#Game Logic
		# Health, stats, condition, etc

class UnitPiece(GamePiece) :
	def __init__(self, statClass, color):
		self.stats = UnitStats()
		self.color = color
	

		

