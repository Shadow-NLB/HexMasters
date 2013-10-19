# Tags
T_Infantry, T_Cavalry, T_Archer, T_Ranged, T_Human = [x for x in xrange(5)]

class Unit(object):
	''' Defines the basic Unit Object
	
	This class will be the base class for all classes of unit'''
	
	attackBuffs = [] # A list of functions to call in order to determine the appropriate attack score based on context
	defenseBuffs = [] # A list of functions to call in order to determine the appropriate attack score based on context
	maxHP = 1 # A max HP for units of a given class
	tags = set([]) # A set of tags which are used to identify units of special types.
	baseAttack = 1 # A base attack score which will be modified by buffs during combat
	baseDefense = 1 # A base defense score which will be modifierd by buffs during combat
	MP = 1 # The number of spaces a unit may move in one turn
	range = 1 # The range of a unit's attack

	def __init__(self):
		''' Define some example properties that are true for ALL units'''
		self.hp = maxHP
		self.tags = tags
	def attack(self, battleState):
		netAttack = baseAttack
		for buff in self.attackBuffs:
			netAttack = buff(netAttack, battleState)
		return netAttack
	def defend(self, battleState):
		netDefense = baseDefense
		for buff in self.defenseBuffs:
			netDefense = buff(netDefense, battleState)
		return netDefense
	
# I could resolve all types to a series of tag values. This flat structure is simple to implement.
# Concerns: Will need to make many "is this a ___ type"

class Swordsmen(Unit):
	#Specify Class Defaults here
	maxHP = 6
	baseAttack = 2
	baseDefense = 3
	tags=[T_Infantry, T_Human]
	def __init__(self):
		super(Swordsmen, self).__init__(self)
		
class Axmen(Unit):
	#Specify Class Defaults here
	maxHP = 6
	baseAttack = 3
	baseDefense = 2
	tags=[T_Infantry, T_Human]
	def __init__(self):
		super(Axmen, self).__init__(self)

class Longbowmen(Unit):
	maxHP = 5
	baseAttack = 2
	baseDefense = 1
	range = 2
	tags=[T_Infantry, T_Archer]
	def __init__(self):
		super(Longbowmen, self).__init__(self)
		
class LightCavalry(Unit):
	maxHP = 4
	baseAttack = 4
	baseDefense = 4
	MP = 2
	tags=[T_Cavalry]
	
#
# Define BUFFS
# Buffs require both unit and tag definitions
#
def att_p1v_T_Infantry(baseAttack, battleState):
	if T_Infantry in battleState.defender.tags
        return baseAttack + 1
    else:
		return baseAttack
		
# Attach buffs to classes
Axmen.attackBuffs.add(att_p1v_T_Infantry)
LightCavalry.attackBuffs.add(att_p1v_T_Infantry)

