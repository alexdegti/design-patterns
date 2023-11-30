from abc import ABC, abstractmethod
import Console

#An abstract class that represents a Console object builder.
class ConsoleAssembler(ABC):

	#A dummy abstract method that keeps the ConsoleAssmebler class abstract.
	@abstractmethod
	def AbstractMethod(self):
		pass

	#An empty method that assembles the mainUnit part of a Console object.
	def AssembleMainUnit(self):
		pass

	#An empty method that assembles the controller part of a Console object.
	def AssembleController(self):
		pass

	#An empty method that assembles the controller part of a Console object.
	def AssembleScreen(self):
		pass


#A concrete class that represents a PlayStation object builder.
class PlayStationAssembler(ConsoleAssembler):

	#A dummy abstract method.
	def AbstractMethod(self):
		pass

	#A method that builds the mainUnit part.
	def AssembleMainUnit(self):
		self.mainUnit = "PlayStation main unit"

	#A method that builds the controller part.
	def AssembleController(self):
		self.controller = "PlayStation controller"

	#A getter method for the complete PlayStation object.
	def GetPlayStation(self):
		return Console.PlayStation(self.mainUnit, self.controller)



#A concrete class that represents an Xbox object builder.
class XboxAssembler(ConsoleAssembler):

	#A dummy abstract method.
	def AbstractMethod(self):
		pass

	#A method that builds the mainUnit part.
	def AssembleMainUnit(self):
		self.mainUnit = "Xbox main unit"

	#A method that builds the controller part.
	def AssembleController(self):
		self.controller = "Xbox controller"

	#A getter method for the complete Xbox object.
	def GetXbox(self):
		return Console.Xbox(self.mainUnit, self.controller)



#A concrete class that represents a Switch object builder.
class SwitchAssembler(ConsoleAssembler):

	#A dummy abstract method.
	def AbstractMethod(self):
		pass
	
	#A method that builds the mainUnit part.
	def AssembleMainUnit(self):
		self.mainUnit = "Switch main unit"

	#A method that builds the controller part.
	def AssembleController(self):
		self.controller = "Switch controller"

	#A method that builds the screen part.
	def AssembleConsoleScreen(self):
		self.screen = "Switch screen"

	#A getter method for the complete Switch object.
	def GetSwitch(self):
		return Console.Switch(self.mainUnit, self.controller, self.screen)


		