from datetime import date, datetime


class LunchChoices:

    def __init__(self, recipes, ingredients):
        self.recipes = recipes
        self.ingredients = ingredients
        self.today = date.today()

    def choices(self):
        usable_ingredients = set()
        best_before_expired_ingridiens = set()
        for ingredient in self.ingredients["ingredients"]:
            if datetime.strptime(ingredient["use-by"], '%Y-%m-%d').date() >= self.today:
                usable_ingredients.add(ingredient['title'])
                if datetime.strptime(ingredient["best-before"], '%Y-%m-%d').date() < self.today:
                    best_before_expired_ingridiens.add(ingredient['title'])
        usable_recipes = [recipe for recipe in self.recipes["recipes"]
                          if set(recipe["ingredients"]).issubset(usable_ingredients)]
        usable_recipes.sort(key=lambda recipe: best_before_expired_ingridiens.intersection(
            set(recipe["ingredients"])))
        return usable_recipes
