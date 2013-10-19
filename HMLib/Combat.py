import random

class BattleState(object):
	''' Represents the state of the battle'''
	def __init__(self, attacker, defender, terrainInfo):
		self.attacker = attacker
		self.defender = defender

def roll(numberDice):
    return [random.randint(0,5) for x in xrange(numberDice)]

def rollHits(numberDice):
	total = 0
	for die in roll(numberDice):
		total += 1 if die < 3 else 0
	return total
	
def rollBlocks(numberDice):
	total = 0
	for die in roll(numberDice):
		total += 1 if die == 1 else 0
	return total
	
def combat(battleState):
	''' This is the main repeatable sequence of events for combat'''
	# Roll the attack dice
	attacker = battleState.attacker
	defender = battleState.defender
	totalHits = rollHits(attacker.attack(battleState))
	# Roll the defense dice
	totalBlocks = rollBlocks(defender.defense(battleState))
	# Calculate net hits
	netHits = totalHits - totalBlocks
	# Subtract from defenders hp
	defender.hp -= netHits
	print 'Defender defeated!' if defender.hp <= 0 else 'Defender HP={0}'.format(defender.hp)