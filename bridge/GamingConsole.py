from abc import ABC, abstractmethod

#A class that represents a gaming console.
class GamingConsole(ABC):

	#An abstract method that performs partial initialisation.
	@abstractmethod
	def __init__(self):

		self.tag
		self.volume = 0
		self.brightness = 0
		self.isOn = False


	#A getter method for the volume data member.
	def GetVolume(self):
		return self.volume

	#A setter method for the volume data member.
	def SetVolume(self, volume):
		self.volume = volume

	#A getter method for the brightness data member.
	def GetBrightness(self):
		return self.brightness

	#A setter method for the brightness data member.
	def SetBrightness(self, brightness):
		self.brightness = brightness

	#A getter method for the isOn data member.
	def IsOn(self):
		return self.isOn

	#A method that sets the isOn data member to True if
	#its current value is False.
	def TurnOn(self):
		
		if not self.IsOn():
			self.isOn = True


	#A method that sets the isOn data member to False if
	#its current value is True.
	def TurnOff(self):
		
		if self.IsOn():
			self.isOn = False



#A class that represents a Wii gaming console.
class Wii(GamingConsole):

	#A method that performs initialisation.
	def __init__(self):

		self.tag = "Wii"
		super().__init__()



#A class represents an Xbox 360 gaming console.
class Xbox360(GamingConsole):

	#A method that performs initialisation.
	def __init__(self):

		self.tag = "Xbox 360"
		super().__init__()



#A class represents a PlayStation 3 gaming console.
class PlayStation3(GamingConsole):

	#A method that performs initialisation.
	def __init__(self):

		self.tag = "PlayStation 3"
		super().__init__()


