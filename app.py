import json
from pathlib import Path
from flask import Flask, render_template, redirect
from src.lunch import LunchChoices
base_path = Path(__file__)
file_path = (base_path / "../data").resolve()

app = Flask(__name__)

@app.route("/")
def index():
    return redirect("/lunch")

@app.route("/lunch")
def suggest_lunch():
    with open(f'{file_path}/recipes.json') as recipes, open(f'{file_path}/ingredients.json') as ingredients:
        recipes = json.load(recipes)
        ingredients = json.load(ingredients)
        lunchChoices = LunchChoices(recipes, ingredients).choices()
        return render_template("base.html", data=lunchChoices)


if __name__ == '__main__':
    app.run(port=8000)
