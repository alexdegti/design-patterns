from GamingConsole import PlayStation3

#A class that represents a controller.
class Controller(object):

	#A method that performs initialisation.
	def __init__(self):
		self.gamingConsole = PlayStation3()

	#A method that increases the volume by 1 if the
	#maximal volume value hasn't been reached yet. (maximal
	#volume value equals 100)
	def IncreaseVolume(self):

		currentVolume = self.gamingConsole.GetVolume()

		if currentVolume < 100:
			self.gamingConsole.SetVolume(currentVolume + 1)


	#A method that decreases the volume by 1 if its
	#current value is greater than 0.
	def DecreaseVolume(self):

		currentVolume = self.gamingConsole.GetVolume()

		if currentVolume > 0:
			self.gamingConsole.SetVolume(currentVolume - 1)


	#A method that mutes the volume.
	def Mute(self):
		self.gamingConsole.SetVolume(0)

	#A method that increases the brightness by 1 if the 
	#maximal brightness value hasn't been reached yet. (maximal
	#brightness value is 100)
	def IncreaseBrightness(self):
		
		currentBrightness = self.gamingConsole.GetBrightness()

		if currentBrightness < 100:
			self.gamingConsole.SetBrightness(currentBrightness + 1)

	
	#A method that decreases the brightness by 1 if its
	#current value is greater than 0.
	def DecreaseBrightness(self):
		
		currentBrightness = self.gamingConsole.GetBrightness()

		if currentBrightness > 0:
			self.gamingConsole.SetBrightness(currentBrightness - 1)


	#A method that dims the screen's brightness.
	def DimScreen(self):
		self.gamingConsole.SetBrightness(20)

	#A method that turns on the gamaing console data member.
	def TurnOn(self):
		self.gamingConsole.TurnOn()

	#A method that turns off the gaming console data member.
	def TurnOff(self):
		self.gamingConsole.TurnOff()


