from abc import ABC, abstractmethod

#An abstract class that represents a Japanese grammar component.
class JapaneseGrammar(ABC):

	#A method that performs initialisation.
	def __init__(self, japaneseString, englishMeaning):

		self.japaneseString = japaneseString
		self.englishMeaning = englishMeaning


	#A method that returns a string representation of a JapaneseGrammar
	#object. 
	def __str__(self):
		return f"{self.japaneseString} ({self.englishMeaning})"

	#An abstract method that accpets a JapaneseGrammarVisitor object.
	@abstractmethod
	def Accept(self, visitor):
		pass



#A class that represents a noun in Japanese.
class Noun(JapaneseGrammar):

	#A method that accepts a concrete JapaneseGrammarVisitor object.
	def Accept(self, visitor):
		visitor.VisitNoun(self)



#A class that represents an ichidan-verb in Japanese.
class IchidanVerb(JapaneseGrammar):

	#A method that accepts a concrete JapaneseGrammarVisitor object.
	def Accept(self, visitor):
		visitor.VisitIchidanVerb(self)



#A class that represents an i-adjective in Japanese.
class IAdjective(JapaneseGrammar):

	#A method that accepts a concrete JapaneseGrammarVisitor object.
	def Accept(self, visitor):
		visitor.VisitIAdjective(self)


