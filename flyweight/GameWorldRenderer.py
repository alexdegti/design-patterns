import PatchesOfFlowersFactory as poff
import PatchOfFlowersContext as pofc

#A class that represents a game world renderer,
#functions as a driver class.
class GameWorldRenderer(object):

	#A method that turns this class into a singleton.
	def __new__(self):

		if not hasattr(self, "instance"):
			self.instance = super().__new__(self)

		return self.instance


	#A method that performs initialisation.
	def __init__(self):

		self.patchesOfFlowersFactory = poff.PatchesOfFlowersFactory()

		#The patches of flowers that need to be rendered.
		self.patchesOfFlowersToRender = [("rose", pofc.PatchOfFlowersContext((162, 0, 22), 24, 15)),
										 ("forget-me-not", pofc.PatchOfFlowersContext((222, 0, 35), 59, 28)),
										 ("poppy", pofc.PatchOfFlowersContext((54, 0, 17), 41, 12)),
										 ("hollyhock", pofc.PatchOfFlowersContext((120, 0, 37), 66, 36)),
										 ("chrysanthemum", pofc.PatchOfFlowersContext((63, 0, 21), 88, 14)),
										 ("forget-me-not", pofc.PatchOfFlowersContext((191, 0, 43), 76, 32)),
										 ("daisy", pofc.PatchOfFlowersContext((152, 0, 19), 44, 23)),
										 ("daffodil", pofc.PatchOfFlowersContext((72, 0, 16), 62, 29)),
										 ("rose", pofc.PatchOfFlowersContext((24, 0, 20), 53, 18)),
										 ("daisy", pofc.PatchOfFlowersContext((216, 0, 30), 69, 33)),
										 ("poppy", pofc.PatchOfFlowersContext((94, 0, 27), 56, 20)),
										 ("forget-me-not", pofc.PatchOfFlowersContext((41, 0, 13), 71, 26))]



if __name__ == "__main__":

	gameWorldRenderer = GameWorldRenderer()

	for patchOfFlowers in gameWorldRenderer.patchesOfFlowersToRender:
		gameWorldRenderer.patchesOfFlowersFactory.CreatePatchOfFlowers(patchOfFlowers[0]).RenderPatchOfFlowers(patchOfFlowers[1])