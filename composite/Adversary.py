from abc import ABC, abstractmethod
from random import random

#An abstract class that represents an adversary the
#player might face in battle.
class Adversary(ABC):

	#An abstract method that returns a string representation
	#of an adversary.
	@abstractmethod
	def __str__(self):
		pass

	#An abstract method that attacks the player.
	@abstractmethod
	def Attack(self):
		pass



#A class that represents a single enemy the player
#faces.
class SingleEnemy(Adversary):

	#A method that performs initialisation.
	def __init__(self, name, attackPoints):

		self.name = name
		self.attackPoints = attackPoints


	#A method that returns a string representation of a
	#single enemy.
	def __str__(self):
		return f"Single enemy:\n\tname-{self.name}, attack points-{self.attackPoints}"

	#A method that attacks the player.
	def Attack(self):
		print(f"{self.name} attacks the player, and causes {self.attackPoints} damage!")



#A class that represents a gang of enemies the player
#faces.
class GangOfEnemies(Adversary):

	#A method that performs initialisation.
	#enemiesList is a list of Adversary objects.
	def __init__(self, enemiesList):
		self.enemiesList = enemiesList

	#A method that returns a string representation of a 
	#gang of enemies.
	def __str__(self):

		stringRepresentation = "Gang of enemies:\n"

		for enemy in self.enemiesList:
			stringRepresentation += f"\tname-{enemy.name}, attack points-{enemy.attackPoints}\n"

		return stringRepresentation[: len(stringRepresentation) - 1]


	#A method that attacks the player.
	def Attack(self):

		for enemy in self.enemiesList:
			enemy.Attack()



#A class that represents opposing factions the player
#faces.
class OpposingFactionsOfEnemies(Adversary):

	#A method that performs initialisation.
	#listOfEnemiesFactions is a list containing two lists
	#of Adversary objects.
	def __init__(self, listOfEnemiesFactions):
		self.listOfEnemiesFactions = listOfEnemiesFactions

	#A method that returns a string representation of
	#opposing factions of enemies.
	def __str__(self):
		
		stringRepresentation = "Opposing factions of enemies:\nFirst faction enemies:\n"

		for enemy in self.listOfEnemiesFactions[0]:
			stringRepresentation += f"\tname-{enemy.name}, attack points-{enemy.attackPoints}\n"

		stringRepresentation += "Second faction enemies\n"

		for enemy in self.listOfEnemiesFactions[1]:
			stringRepresentation += f"\tname-{enemy.name}, attack points-{enemy.attackPoints}\n"

		return stringRepresentation[: len(stringRepresentation) - 1]


	#A method that attacks the player.
	def Attack(self):

		for enemiesFaction in self.listOfEnemiesFactions:
			for enemy in enemiesFaction:
				#The enemy might attack a different monster with
				#a probability of 0.3.
				if random() > 0.7:
					print(f"{enemy.name} attacks a monster from the other faction, and causes {enemy.attackPoints} damage!")
				else:
					enemy.Attack()
    				

