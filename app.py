import json
from flask import Flask, render_template
from src.lunch import LunchChoices

app = Flask(__name__)


@app.route('/lunch')
def suggest_lunch():
    with open('data/recipes.json') as recipes, open('data/ingredients.json') as ingredients:
        recipes = json.load(recipes)
        ingredients = json.load(ingredients)
        lunchChoices = LunchChoices(recipes, ingredients).choices()
        return render_template("base.html", data=lunchChoices)


if __name__ == '__main__':
    app.run()
