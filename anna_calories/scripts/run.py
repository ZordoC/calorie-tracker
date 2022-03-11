from anna_calories.parser.parse import get_weekly_meals, parse_website
from anna_calories.tracker._tracker import Athlete, HealthiestChoiceMeal, Tracker


#parse_website()

weekly_meals = get_weekly_meals(["drunken-noodles", "chicken-jambalaya", "gnocchis-a-la-vodka", "steak-au-poivre"], "High Protein + Low Carb", "Regular")
print(weekly_meals.describe())

meals = []
for row in weekly_meals.iterrows():
    meal = HealthiestChoiceMeal(row[1]['name'],row[1]['calories'], row[1]['carbs'], row[1]['protein'], row[1]['fat'], row[1]['portion'], row[1]['custom'])
    meals.append(meal)


athlete = Athlete('Anna', 27, 'Female', 165, 62, "Active")
daily_cals = athlete.calculate_daily_calories()
tracker = Tracker(athlete, meals, "4000", 0.1)
total = tracker.count_total_meal_calories()
projection = tracker.calories_projection()
print(projection)



if __name__ == "__main__":
    print("hey")
