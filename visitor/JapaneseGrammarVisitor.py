from abc import ABC, abstractmethod

#An abstract class that represents a Japanese grammar visitor.
class JapaneseGrammarVisitor(ABC):

	#An abstract method that visits a Noun object.
	@abstractmethod
	def VisitNoun(self, noun):
		pass

	#An abstract method that visits an IchidanVerb object.
	@abstractmethod
	def VisitIchidanVerb(self, ichidanVerb):
		pass

	#An abstract method that visits an IAdjective object.
	@abstractmethod
	def VisitIAdjective(self, iAdjective):
		pass



#A class that represents a concrete visitor that prints a JapaneseGrammar
#object.
class JapaneseGrammarVisitorPrint(JapaneseGrammarVisitor):

	#A method that prints a Noun object.
	def VisitNoun(self, noun):
		print(noun)

	#A method that prints an IchidanVerb object.
	def VisitIchidanVerb(self, ichidanVerb):
		print(ichidanVerb)

	#A method that prints an IAdjective object.
	def VisitIAdjective(self, iAdjective):
		print(iAdjective)



#A class that represents a concrete visitor that conjugates a JapaneseGrammar
#object to the past tense.
class JapaneseGrammarVisitorConjugateToPastTense(JapaneseGrammarVisitor):

	#A method that conjugates a Noun object to the past tense.
	def VisitNoun(self, noun):
		print(f"{noun.japaneseString} ({noun.englishMeaning}) --> {noun.japaneseString}-da-tta")

	#A method that conjugates an IchidanVerb object to the past tense.
	def VisitIchidanVerb(self, ichidanVerb):
		print(f"{ichidanVerb.japaneseString} ({ichidanVerb.englishMeaning}) --> {ichidanVerb.japaneseString[: len(ichidanVerb.japaneseString) - 3]}-ta")

	#A method that conjugates an IAdjective object to the past tense.
	def VisitIAdjective(self, iAdjective):
		print(f"{iAdjective.japaneseString} ({iAdjective.englishMeaning}) --> {iAdjective.japaneseString[: len(iAdjective.japaneseString) - 2]}-ka-tta")



#A class that represents a concrete visitor that conjugates a JapaneseGrammar
#object to the negative tense.
class JapaneseGrammarVisitorConjugateToNegativeTense(JapaneseGrammarVisitor):

	#A method that conjugates a Noun object to the negative tense.
	def VisitNoun(self, noun):
		print(f"{noun.japaneseString} ({noun.englishMeaning}) --> {noun.japaneseString}-ja-nai")

	#A method that conjugates an IchidanVerb object to the negative tense.
	def VisitIchidanVerb(self, ichidanVerb):
		print(f"{ichidanVerb.japaneseString} ({ichidanVerb.englishMeaning}) --> {ichidanVerb.japaneseString[: len(ichidanVerb.japaneseString) - 3]}-nai")

	#A method that conjugates an IAdjective object to the negative tense.
	def VisitIAdjective(self, iAdjective):
		print(f"{iAdjective.japaneseString} ({iAdjective.englishMeaning}) --> {iAdjective.japaneseString[: len(iAdjective.japaneseString) - 2]}-ku-nai")


		