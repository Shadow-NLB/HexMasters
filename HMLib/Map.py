# General Notes
# Using AXIAL coordinates
# relation to cube coordinates
# q = x r = z  :: y = -x-z
#
#

# General purpose functions to convert between coordinate systems

def cuTax_(x,y,z):
	# q=x r=z
	return (x,z)
def cuTax(loc):
	x,y,z = loc
	return cuTax_(x,y,z)
def axTcu_(q,r):
	return (q,-q-r,r)
def axTcu(loc):
	q,r = loc
	return axTcu_(q,r)
	


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
	
	def range(locA, distance):
		'''Lists of locations that are within [distance] from [locaA]'''
      
      # This algorithm is described in cube coordinates
      x,y,z = axTcu(locA)
      results = []
		# For each change in x that is within the distance
		for d_x in xrange(-distance, distance +1 ):
         #For each change in y that is within a moving range
         # HINT: when d_x is at its largest value, the 
         for d_y in xrange(max(-distance, -d_x-distance),min(distance + 1, -d_x+distance)):
            #Calculate d_z
            d_z = -d_x-d_y
            # Actual point is each of the d_'s applied to current loc
            # Convert to q,r and append
            results.append(cuTax_(x + d_x, y + d_y, z + d_z))
      return results
         
            
	
	def distance(locA, locB):
		''' Determines the "straight line" distance between two locations.'''
		#Adjacency matrix
		# Calc the abs difference between q's
		dif_q = locA[0] - locB[0]
		# Calc difference between r's
		dif_r = locA[1] - locB[1]
		# Calc difference between diff's
		dif_dif = dif_q-dif_r
		# Return the largest absolute of the three quantities
		return max(abs(diq_q),abs(dif_r),abs(dif_Dif))
		
	def areAdjacent(locA, locB):
		''' Returns true if two locations are adjacent. Does not check bounds'''
		return distance(locA, locB) <= 1
		
	def neighbors(self, loc):
		''' Returns a tuple of neighboring locations '''
		offsets = ((1,0),(1,-1),(0,-1),(-1,0),(-1,1),(0,1))
		neighbors = [self.get(sumElm(loc,offset)) for offset in offsets if self.mapKey(sumElm(loc,offset)) in self.map]
		return neighbors