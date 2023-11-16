from abc import ABC, abstractmethod
import Head
import Torso
import Legs

#An abstract singleton class that defines how a concrete
#OutfitFactory class should behave.
class OutfitFactory(ABC):

	#Overwrites the magic method __new__ in order to turn
	#this class into a singleton.
	def __new__(self):

		if not hasattr(self, "instance"):
			self.instance = super().__new__(self)
		return self.instance


	#An abstract factory method for the Head object.
	@abstractmethod
	def CreateHead(self):
		pass

	#An abstract factory method for the Torso object.
	@abstractmethod
	def CreateTorso(self):
		pass

	#An abstract factory method for the Legs object.
	@abstractmethod
	def CreateLegs(self):
		pass



#A class that represents a concrete pirate outfit factory.
class PirateOutfitFactory(OutfitFactory):

	#A conrete factory method for the Head object.
	def CreateHead(self):
		return Head.PirateBandana()

	#A conrete factory method for the Torso object.
	def CreateTorso(self):
		return Torso.PirateCoat()

	#A conrete factory method for the Legs object.
	def CreateLegs(self):
		return Legs.PirateBoots()



#A class that represents a concrete magician outfit factory.
class MagicianOutfitFactory(OutfitFactory):

	#A conrete factory method for the Head object.
	def CreateHead(self):
		return Head.MagicianHat()

	#A conrete factory method for the Torso object.
	def CreateTorso(self):
		return Torso.MagicianRob()

	#A conrete factory method for the Legs object.
	def CreateLegs(self):
		return Legs.MagicianSandals()



#A class that represents a concrete knight outfit factory.
class KnightOutfitFactory(OutfitFactory):

	#A conrete factory method for the Head object.
	def CreateHead(self):
		return Head.KnightHelmet()

	#A conrete factory method for the Torso object.
	def CreateTorso(self):
		return Torso.KnightTorsoArmour()

	#A conrete factory method for the Legs object.
	def CreateLegs(self):
		return Legs.KnightLegsArmour()


