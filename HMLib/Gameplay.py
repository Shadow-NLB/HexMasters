import random
import time

random.seed(time.localtime())

def rollAttack (numDice) :
	""" Rolls [numDice] dice and returns number of hits """
	hits = 0
	for i in xrange(numDice) :
		roll = random.randint(0,5)
		if (roll < 3) :
			hits += 1

	return hits

def rollDefense (numDice) :
	""" Rolls [numDice] dice and returns number of blocks """
	blocks = 0
	for i in xrange(numDice) :
		roll = random.randint(0,5)
		if (roll == 5) :
			blocks += 1

	return blocks

def Combat(attacker, defender) :
	# Roll attack
	hits = rollAttack(attacker.stats.attack)

	# roll defense
	blocks = rollDefense(defender.stats.defense)

	defender.currentHP = defender.currentHP - (hits - blocks)

def Turn(player) :

	# Reset player action points
	player.actionPoints = battle.maxActionPoints
	
	# Player action loop
	while (player.actionPoints > 0) :
		#Get player input
		player.actionPoints -= 1
	# Decrement counters
	# Increment mana

	

