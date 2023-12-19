from abc import ABC, abstractmethod

#An abstract class that represents a meal object.
class Meal(ABC):
	
	#An empty initialisation method that declares the data members
	#that subclasses contain.
	@abstractmethod
	def __init__(self):

		self.starter
		self.main
		self.desert

	#A method that returns a string representation of a meal object.
	def __str__(self):

		return f"starter: {self.starter}, main: {self.main}, desert: {self.desert}"



#A class that represents a standard meal. 
class StandardMeal(Meal):

	#A method that performs initialisation.
	def __init__(self):

		self.starter = "salad"
		self.main = "sweet fried rice"
		self.desert = "chocolate cake"
		self.tag = "standard meal"



#A class that represents a gluten free meal.
class GlutenFreeMeal(Meal):

	#A method that performs initialisation.
	def __init__(self):

		self.starter = "gluten-free salad"
		self.main = "plain rice"
		self.desert = "gluten-free chocolate bar"
		self.tag = "gluten-free meal"



#A class that represents a low-fat meal.
class LowFatMeal(Meal):

	#A method that performs initialisation.
	def __init__(self):

		self.starter = "carrot"
		self.main = "buckwheat"
		self.desert = "date"
		self.tag = "low-fat meal"



#An abstract class that represents a MealFactory object.
class MealFactory(ABC):

	#An abstract factory method.
	@abstractmethod
	def CreateMeal(self):
		pass



#A class that represents a StandardMeal object factory.
class StandardMealFactory(MealFactory):

	#A factory method.
	def CreateMeal(self):
		return StandardMeal()



#A class that represents a GlutenFreeMeal object factory.
class GlutenFreeMealFactory(MealFactory):

	#A factory method.
	def CreateMeal(self):
		return GlutenFreeMeal()



#A class that represents a LowFatMeal object factory.
class LowFatMealFactory(MealFactory):

	#A factory method.
	def CreateMeal(self):
		return LowFatMeal()


		