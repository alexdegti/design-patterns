#A class that represents the contexet of the flyweight
#class PatchOfFlowers.
class PatchOfFlowersContext(object):

	#A method that performs initialisation.
	def __init__(self, patchsCentreCoordinates, density, radius):

		self.patchsCentreCoordinates = patchsCentreCoordinates
		self.density = density
		self.radius = radius


