from abc import ABC, abstractmethod

#An abstract class representing an asset file.
class Asset(ABC):

	#An empty initialisation method.
	def __init__(self):

		self.fileName
		self.fileSize
		self.fleFormat


	#An abstract method that clones an Asset object, and
	#returns the clone.
	@abstractmethod 
	def Clone(self):
		pass



#A class that represents an audio asset file.
class Audio(Asset):

	#A method that performs initialisation.
	def __init__(self, fileName, fileSize, fileFormat, duration, text = None):

		self.fileName = fileName
		self.fileSize = fileSize
		self.fileFormat = fileFormat
		self.duration = duration
		self.text = text


	#A method that clones this Audio object, and returns
	#the clone.
	def Clone(self):
		return Audio(self.fileName, self.fileSize, self.fileFormat, self.duration, self.text)



#A class that represents a video asset file.
class Video(Asset):

	#A method that performs initialisation.
	def __init__(self, fileName, fileSize, fileFormat, duration, resolution):

		self.fileName = fileName
		self.fileSize = fileSize
		self.fileFormat = fileFormat
		self.duration = duration
		self.resolution = resolution


	#A method that clones this Video object, and returns
	#the clone.
	def Clone(self):
		return Video(self.fileName, self.fileSize, self.fileFormat, self.duration, self.resolution)



#A class that represents a character model asset file.
class CharacterModel(Asset):

	#A method that performs initialisation.
	def __init__(self, fileName, fileSize, fileFormat, polygonsCount, texturesCount):

		self.fileName = fileName
		self.fileSize = fileSize
		self.fileFormat = fileFormat
		self.polygonsCount = polygonsCount
		self.texturesCount = texturesCount


	#A method that clones this Video object, and returns
	#the clone.
	def Clone(self):
		return CharacterModel(self.fileName, self.fileSize, self.fileFormat, self.polygonsCount, self.texturesCount)


