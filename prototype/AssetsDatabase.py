import Asset

#A class that represents an assets database.
class AssetsDatabase(object):

	#A method that turns this class into a singleton.
	def __new__(self):

		if not hasattr(self, "instance"):
			self.instance = super().__new__(self)
			
		return self.instance


	#A method that performs initialisation.
	def __init__(self):
		self.database = {"audio" : Asset.Audio("default", "86 MB", "WAV", "0:30"),
						 "video" : Asset.Video("default", "543 MB", "MP4", "5:36", "1920 x 1080"),
						 "character model" : Asset.CharacterModel("default", "121 MB", "FXB", "20005", "4")}


	#A method that validates the asset type passed as argument
	#to the MakeClone method.
	def IsAssetTypeValid(self, assetType): 
		return assetType == "audio" or assetType == "video" or assetType == "character model" 

	#A method that creates a clone of an Asset object,
	#in accordance with the assetType argument.
	#Raises a ValueError if the argument invalid.
	def MakeClone(self, assetType):
		if not self.IsAssetTypeValid(assetType):
			raise ValueError(f"Given type [{assetType}] is not part of the database.")

		return self.database.get(assetType).Clone()



#The driver part of the program.
if __name__ == "__main__":

	assetsDatabase = AssetsDatabase()

	firstAudioFile = assetsDatabase.MakeClone("audio")
	secondAudioFile = assetsDatabase.MakeClone("audio")

	#Confirms that the two clonned Audio objects are indeed distinct.
	print(f"first file memory address: {id(firstAudioFile)}, second file memory address: {id(secondAudioFile)}")


