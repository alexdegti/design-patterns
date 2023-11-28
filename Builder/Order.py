import Builder

#A class that represents an order manager.
class OrderManager(object):

	#A method that performs initialisation, assigning the builder
	#belonging to the OrderManager object.
	def __init__(self):
		self.builder = Builder.PlayStationAssembler()

	#A method that parses an order input file, and assembles
	#the adequate object's parts according to it.
	def Assemble(self):

		#Keeps track of parts assembled so far, as two parts indicate
		#(in this case) a complete object.
		partsAssembled = 0

		#Opens input file for reading.
		with open("order.txt", "rt") as inputFile:

			line = inputFile.readline().rstrip()

			while line:
				
				#Assembles the adequate part.
				if line == "main unit":
					self.builder.AssembleMainUnit()
				elif line == "controller":
					self.builder.AssembleController()

				partsAssembled += 1

				#Checks whether an object is complete.
				if partsAssembled % 2 == 0:
					print(self.builder.GetPlayStation())

				line = inputFile.readline().rstrip()


