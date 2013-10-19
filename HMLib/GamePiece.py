import itertools as itt
class GamePiece :
	"""Represents an instance of a game object which resides on a GameBoard"""
	def __init__(self, name) :
		# A unique identifier for this instance
		self.uuid = ""
		# A name for this instance
		self.name = name
	# Game pieces can be seperated into their visual representation and
	# and their game logic representation

	#Visual needs
		# Current display image
	#Game Logic
		# Health, stats, condition, etc
		
	def __repr__(self):
		return self.name
	def isAdjacentTo(self, otherPiece):
		return areAdjacent(self.loc, otherPiece.loc)
		
def areAdjacent(locA, locB):
	#Adjacency matrix
	neighbors = ((1,0),(1,-1),(0,-1),(-1,0),(-1,1),(0,1))
	dif_q = locA[0] - locB[0]
	dif_r = locA[1] - locB[1]
	return dif_q != dif_r and abs(dif_q) <=1 and abs(dif_r) <=1

def sumElm(tupleA, tupleB):
	return tuple(x + y for x, y in itt.izip(tupleA, tupleB))
	
#hashmap implementation of a grid
class map(object):
	def __init__(self, dims):
		self.q_dim,self.r_dim = dims
		self.size = self.q_dim * self.r_dim
		self.map = dict()
	def mapKey(self, loc):
		q,r = loc
		# Bounds Checking
		if 0 <= q < self.q_dim and 0 <= r <= self.r_dim:
			return loc
		else:
			raise BaseException("Not within map bounds")
	def insert(self, piece, loc):
		key = self.mapKey(loc)
		if key in self.map:
			raise BaseException("space occupied")
		else:
			self.map[key] = piece
	def get(self, loc):
		key = self.mapKey(loc)
		if key in self.map:
			return self.map[key]
		else:
			return None
	def remove(self, locA):
		del self.map[self.mapKey(loc)]
	def move(self, locA, locB):
		self.insert(self, self.get(locA), locB) 
		self.remove(locA)
	def areAdjacent(locA, locB):
		#Adjacency matrix
		neighbors = ((1,0),(1,-1),(0,-1),(-1,0),(-1,1),(0,1))
		dif_q = locA[0] - locB[0]
		dif_r = locA[1] - locB[1]
		return dif_q != dif_r and abs(dif_q) <=1 and abs(dif_r) <=1
	def neighbors(self, loc):
		offsets = ((1,0),(1,-1),(0,-1),(-1,0),(-1,1),(0,1))
		neighbors = [self.get(sumElm(loc,offset)) for offset in offsets if self.mapKey(sumElm(loc,offset)) in self.map]
		# neighbors = []
		
		# # For each offset
		# for offset in offsets:
			# print 'Checking location {0}'.format(sumElm(loc, offset))
			# # Figure out if we have anything in the map for that loc
			# piece = self.get(sumElm(loc, offset))
			# if piece != None:
				# neighbors.append(piece)
		return neighbors
			

myMap = map((5,5))
piece1 = GamePiece("Bill at 1,1")
piece2 = GamePiece("Jim at 2,1")
myMap.insert(piece1, (1,1))
myMap.insert(piece2, (2,1))
print myMap.get((1,1))
print myMap.get((2,1))
print myMap.neighbors((1,1))
		
# test adjacency

space = [(x,y) for x in xrange(5) for y in xrange(5)]
target = (3,2)

print "Target location: {0}".format(target)
for point in space:
	if areAdjacent(target, point):
		print "{0} is adjacent".format(point)
	else:
		print "{0} is not adjacent".format(point)