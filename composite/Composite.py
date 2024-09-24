import sys
import Adversary

if __name__ == "__main__":

	encounters = []

	#Assumes that a name of a valid input file
	#was passed as a command line argument.
	with open(sys.argv[1], "rt") as inputFile:

		for line in inputFile.read().split("\n"):

			adversary = line.split()

			#Single enemy.
			if adversary[0] == "SE":
				name, attackPoints = adversary[1].split("_")
				encounters.append(Adversary.SingleEnemy(name, attackPoints))

			#A gang of enemies.
			elif adversary[0] == "GOE":
				gangOfEnemies = []
				for enemy in adversary[1].split(","):
					name, attackPoints = enemy.split("_")
					gangOfEnemies.append(Adversary.SingleEnemy(name, attackPoints))
				encounters.append(Adversary.GangOfEnemies(gangOfEnemies))

			#Opposing factions of enemies.
			else:
				firstFaction, secondFaction = [], []
				for enemy in adversary[1].split(","):
					name, attackPoints = enemy.split("_")
					firstFaction.append(Adversary.SingleEnemy(name, attackPoints))
				for enemy in adversary[2].split(","):
					name, attackPoints = enemy.split("_")
					secondFaction.append(Adversary.SingleEnemy(name, attackPoints))
				encounters.append(Adversary.OpposingFactionsOfEnemies([firstFaction, secondFaction]))

	#The enemies attack the player.
	for encounter in encounters:
		encounter.Attack()