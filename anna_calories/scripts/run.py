from anna_calories.parser.parse import get_weekly_meals, parse_website
from anna_calories.tracker._tracker import Athlete, HealthiestChoiceMeal


#parse_website()

weekly_meals = get_weekly_meals(["drunken-noodles", "chicken-jambalaya"], "High Protein + Low Carb", "Regular")

meals = []
for row in weekly_meals.iterrows():
    meal = HealthiestChoiceMeal(row[1]['name'],row[1]['calories'], row[1]['carbs'], row[1]['protein'], row[1]['fat'], row[1]['portion'], row[1]['custom'])
    meals.append(meal)