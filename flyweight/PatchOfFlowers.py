#A flyweight class that represents different flower patches
#to be rendered in the game's world.
class PatchOfFlowers(object):

	#A method that performs initialisation.
	def __init__(self, texture, height):

		self.texture = texture
		self.height = height


	#A method that renders this PatchOfFlowers object.
	def RenderPatchOfFlowers(self, patchOfFlowersContext):

		print(f"Rendering a patch of {self.texture} at location {patchOfFlowersContext.patchsCentreCoordinates}. radius: {patchOfFlowersContext.radius} density: {patchOfFlowersContext.density} height: {self.height}")


