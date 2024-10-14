from abc import ABC, abstractmethod
from random import random

#An abstract class represnting a player attack.
class Attack(ABC):

	#An empty initialisation method that declares the
	#data members of an Attack object.
	def __init__(self):

		self.weapon
		self.damage


	#An abstract attack method for the player.
	@abstractmethod
	def Attack(self):
		return f"The player attacks with {self.weapon}, and causes {self.damage} damage!"



#A class that represents a slash attack.
class Slash(Attack):

	#A method that performs initialisation.
	def __init__(self):

		self.weapon = "Heavenly Sword"
		self.damage = 11


	#A method that attacks an enemy.
	def Attack(self):
		return super().Attack()

		

#A class that represents a spell attack.
class Spell(Attack):

	#A method that performs initialisation.
	def __init__(self):

		self.weapon = "Wooden Staff"
		self.damage = 8


	#A method that attacks an enemy.
	def Attack(self):
		return super().Attack()



#An abstract class that represents an attack
#decorator.
class AttackDecorator(Attack):

	#A method that performs initialisation.
	def __init__(self, attack):
		self.attack = attack



#A method that decorates an Attack object by
#adding a fire element to it. Might inflict a burn
#status effect upon the enemy.
class FireElement(AttackDecorator):

	#A method that perform initialisation.
	def __init__(self, attack):
		super().__init__(attack)

	#A method that attacks an enemy.
	def Attack(self):
		
		output = self.attack.Attack() + f"\t The attack was imbued with a fire element!"

		if random() > 0.8:
			output = self.attack.Attack() + f"\t The added fire element inflicts burn on the enemy!"

		return output



#A method that decorates an Attack object by 
#increasing the damage data member.
class IncreasedDamage(AttackDecorator):

	#A method that perform initialisation.
	def __init__(self, attack):
		super().__init__(attack)

	#A method that attacks an enemy.	
	def Attack(self):

		if hasattr(self.attack, "damage"):
			self.attack.damage += 4
		else:
			self.attack.attack.damage += 4

		return self.attack.Attack()


