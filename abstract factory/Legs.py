from abc import ABC, abstractmethod

#An abstract class that defines the torso component of an outfit.
class Legs(ABC):

	#An abstract method that defines the data members of
	#the Legs object.
	@abstractmethod
	def __init__(self):

		self.itemName
		self.speedStat
		self.movementStat


	#A method that returns a string representation of the Legs object.
	def __str__(self):
		return f"Item name: {self.itemName}, Item stats: speed-{self.speedStat}, movement-{self.movementStat}"



#A class that represents a concrete pirate Legs object.
class PirateBoots(Legs):

	#A method that performs initialisation.
	def __init__(self):

		self.itemName = "pirate boots"
		self.speedStat = 4
		self.movementStat = 3



#A class that represents a concrete magician Legs object.
class MagicianSandals(Legs):

	#A method that performs initialisation.
	def __init__(self):

		self.itemName = "magician sandals"
		self.speedStat = 1 
		self.movementStat = 2



#A class that represents a concrete knight Legs object.
class KnightLegsArmour(Legs):

	#A method that performs initialisation.
	def __init__(self):

		self.itemName = "knight legs armour"
		self.speedStat = 2
		self.movementStat = 2


