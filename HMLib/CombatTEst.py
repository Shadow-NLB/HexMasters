# Testing out a general way to have conditional bonuses
# The most general solution will be to have some kind of "battle state" object which gets passed into these functions
# The battle state object will generalize the conditions which can be used to determine a buff

class BattleState(object):
	def __init__(self, attacker, defender, terrainInfo)
		self.attacker = attacker
		self.defender = defender

# The simplest kind of conditional game mechanism is buffs
# The contract for these functions is simple,
# They only take the current battle state and the current value of the property they affect
# Its true I could make the buff return a numer to add, but this way it the most general
# Buffs can do whatever math they want
# Adam might actually be able to grasp this if I give him very tight instructions

class UnitClass(object):
	def __init__(self):
		self.baseAttack = 0
		self.augments = []
	def getAttackScore(self, enemyUnit):
		attack = self.baseAttack
		for augment in self.augments:
			attack = augment(attack, enemyUnit)
		return attack
			
	
class PikemanClass(UnitClass):
	def __init__(self):
		super(PikemanClass, self).__init__()
		self.baseAttack = 3
		self.augments = [pikesBuff]
		
class CavalryClass(UnitClass):
	def __init__(self):
		self.baseAttack = 4

#Example
def p1AttVsCav(baseAttack, battleState):
	if isinstance(battleState.defender, CavalryClass):
		return baseAttack + 1;
	else
		return baseAttack;