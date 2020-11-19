from datetime import date, datetime


class LunchChoices:

    def __init__(self, recipes, ingredients):
        self.recipes = recipes
        self.ingredients = ingredients
        self.today = date.today()

    def choices(self):
        # seperating expired ingredients from still usable one by using following list comprehension.
        usable_ingredients_dicts = [ingredient for ingredient in self.ingredients["ingredients"]
                                    if datetime.strptime(ingredient["use-by"], '%Y-%m-%d').date() >= self.today]
        usable_ingredients = [item['title']
                              for item in usable_ingredients_dicts]
        usable_recipes = [recipe for recipe in self.recipes["recipes"]
                          if all(item in usable_ingredients for item in recipe["ingredients"])]
        usable_ingredients_with_expired_best_before = [item['title'] for item in usable_ingredients_dicts
                                                       if datetime.strptime(item["best-before"], '%Y-%m-%d').date() < self.today]
        usable_recipes
