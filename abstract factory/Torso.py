from abc import ABC, abstractmethod

#An abstract class that defines the torso component of an outfit.
class Torso(ABC):

	#An abstract method that defines the data members of
	#the Torso object.
	@abstractmethod
	def __init__(self):

		self.itemName
		self.healthPointsStat
		self.defenceStat


	#A method that returns a string representation of the Torso object.
	def __str__(self):
		return f"Item name: {self.itemName}, Item stats: health points-{self.healthPointsStat}, defence-{self.defenceStat}"



#A class that represents a concrete pirate Torso object.
class PirateCoat(Torso):

	#A method that performs initialisation.
	def __init__(self):

		self.itemName = "pirate coat"
		self.healthPointsStat = 20
		self.defenceStat = 2

		

#A class that represents a concrete magician Torso object.
class MagicianRob(Torso):

	#A method that performs initialisation.
	def __init__(self):

		self.itemName = "magician rob"
		self.healthPointsStat = 5 
		self.defenceStat = 1



#A class that represents a concrete knight Torso object.
class KnightTorsoArmour(Torso):

	#A method that performs initialisation.
	def __init__(self):

		self.itemName = "knight torso armour"
		self.healthPointsStat = 40
		self.defenceStat = 3


