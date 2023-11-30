from abc import ABC, abstractmethod

#An abstract class that represents a video games console.
class Console(ABC):

	#An empty initialisation method that declares the data members
	#that subclasses might contain.
	def __init__(self):

		self.mainUnit
		self.controller
		self.screen


	#A dummy abstract method that keeps the Console class abstract.
	@abstractmethod
	def AbstractMethod(self):
		pass



#A subclass of the Console class, that represents A PlayStation
#video games console. 
class PlayStation(Console):

	#A method that performs initialisation.
	def __init__(self, mainUnit, controller):
		
		self.mainUnit = mainUnit
		self.controller = controller


	#A method that returns a string representing the PlayStation object.
	def __str__(self):
		return f"console components: {(self.mainUnit, self.controller)}"

	#A dummy method.
	def AbstractMethod(self):
		pass



#A subclass of the Console class, that represents An Xbox
#video games console.
class Xbox(Console):

	#A method that performs initialisation.
	def __init__(self, mainUnit, controller):
		
		self.mainUnit = mainUnit
		self.controller = controller
		

	#A method that returns a string representing the Xbox object.
	def __str__(self):
		return f"console components: {(self.mainUnit, self.controller)}"

	#A dummy method.
	def AbstractMethod(self):
		pass



#A subclass of the Console class, that represents A Switch
#video games console.
class Switch(Console):

	#A method that performs initialisation.
	def __init__(self, mainUnit, controller, screen):
		
		self.mainUnit = mainUnit
		self.controller = controller
		self.screen = screen


	#A method that returns a string representing the Switch object.
	def __str__(self):
		return f"console components: {(self.mainUnit, self.controller, self.screen)}"
	
	#A dummy method.
	def AbstractMethod(self):
		pass


