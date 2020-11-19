import datetime


class LunchChoices:

    def __init__(self, recipes, ingredients):
        self.recipes = recipes
        self.ingredients = ingredients
        self.today = datetime.now().date()

	def choices():
		
