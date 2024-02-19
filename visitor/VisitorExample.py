import JapaneseGrammar as jg
import JapaneseGrammarVisitor as jgv

#A class that represents a visitor example.
class VisitorExample(object):

	#A method that initialises the class with
	#a JapaneseGrammarVisitor object.
	def __init__(self):
		self.visitor = jgv.JapaneseGrammarVisitorConjugateToNegativeTense()

	#A method that iterates over a sequence of concrete
	#JapaneseGrammar objects.
	def Iterate(self, sequence):

		for element in sequence:
			element.Accept(self.visitor)



if __name__ == "__main__":

	visitor = VisitorExample()
	# grammarComponents = [jg.IchidanVerb("to-ke-ru", "To dissolve"), jg.IchidanVerb("tsu-ki-ru", "To use-up"), jg.IchidanVerb("kan-ga-mi-ru", "To be in light of something")]
	# grammarComponents = [jg.Noun("bi-n", "Jar"), jg.Noun("den-ta-ku", "Calculator"), jg.Noun("ko-bu-ne", "Boat")]
	grammarComponents = [jg.IAdjective("e-ra-i", "Remarkable"), jg.IAdjective("a-wa-ta-da-shi-i", "Hectic"), jg.IAdjective("a-ma-i", "Sweet")]

	visitor.Iterate(grammarComponents)