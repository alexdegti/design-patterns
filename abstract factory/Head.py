from abc import ABC, abstractmethod

#An abstract class that defines the head component of an outfit.
class Head(ABC):

	#An abstract method that defines the data members of
	#the Head object.
	@abstractmethod
	def __init__(self):

		self.itemName
		self.intelligenceStat
		self.magicDefenceStat


	#A method that returns a string representation of the Head object.
	def __str__(self):
		return f"Item name: {self.itemName}, Item stats: intelligence-{self.intelligenceStat}, magic defence-{self.magicDefenceStat}"



#A class that represents a concrete pirate Head object.
class PirateBandana(Head):

	#A method that performs initialisation.
	def __init__(self):

		self.itemName = "pirate bandana"
		self.intelligenceStat = 1
		self.magicDefenceStat = 1



#A class that represents a concrete magician Head object.
class MagicianHat(Head):

	#A method that performs initialisation.
	def __init__(self):

		self.itemName = "magician hat"
		self.intelligenceStat = 3
		self.magicDefenceStat = 3



#A class that represents a concrete knight Head object.
class KnightHelmet(Head):

	#A method that performs initialisation.
	def __init__(self):

		self.itemName = "knight helmet"
		self.intelligenceStat = 2
		self.magicDefenceStat = 1


		