import PatchOfFlowers as pof

#A class that represents a factory for
#PatchOfFlowers objects.
class PatchesOfFlowersFactory(object):

	#A method that turns this class into a singleton.
	def __new__(self):

		if not hasattr(self, "instance"):
			self.instance = super().__new__(self)

		return self.instance


	#A method that performs initialisation.
	def __init__(self):
		self.patchesOfFlowers = {}

	#A static utility method that converts the kind
	#argument into a tuple containing the data members
	#of a PatchOfFlowers object.
	@staticmethod
	def KindToDataMembers(kind):

		output = ()

		if kind == "forget-me-not":
			output = ("forget-me-not", 12)
		elif kind == "daffodil":
			output = ("daffodil", 22)
		elif kind == "hollyhock":
			output = ("hollyhock", 53)
		elif kind == "rose":
			output = ("rose", 35)
		elif kind == "daisy":
			output = ("daisy", 17)
		elif kind == "poppy":
			output = ("poppy", 20)
		elif kind == "chrysanthemum":
			output = ("chrysanthemum", 24)

		return output


    #The factory method for flyweight PatchOfFlowers objects.
	def CreatePatchOfFlowers(self, kind):

		#Checks whether the object already exists.
		patchOfFlowers = self.patchesOfFlowers.get(kind)

		#If the flyweight object does not exist, creates
		#a new instance.
		if patchOfFlowers == None:
			patchOfFlowers = pof.PatchOfFlowers(*PatchesOfFlowersFactory.KindToDataMembers(kind))
			self.patchesOfFlowers.update({kind : patchOfFlowers})

		return patchOfFlowers


