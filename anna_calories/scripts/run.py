from statistics import mean
from typing import List

from anna_calories.domain import Athlete, FoodLogger, HealthiestChoiceMeal
from anna_calories.parser.parse import get_weekly_meals, parse_website

# parse_website()

meals_names = ["drunken-noodles", "chicken-jambalaya", "gnocchis-a-la-vodka", "steak-au-poivre"]
portion = "Regular"
diet = "High Protein + Low Carb"


def create_all_hc_meal(meals_name_list, portion, diet) -> List[HealthiestChoiceMeal]:
    """Ugly function that needs refactoring ASAP"""
    weekly_meals = get_weekly_meals(meals_name_list, diet, portion)

    meals = []
    for row in weekly_meals.iterrows():
        meal = HealthiestChoiceMeal(
            row[1]["name"],
            row[1]["calories"],
            row[1]["carbs"],
            row[1]["protein"],
            row[1]["fat"],
            row[1]["portion"],
            row[1]["custom"],
        )
        meals.append(meal)

    mean_calories = mean([meal.calories for meal in meals])
    mean_protein = mean([meal.protein for meal in meals])
    mean_carbs = mean([meal.carbs for meal in meals])
    mean_fat = mean([meal.fat for meal in meals])

    mean_meal = HealthiestChoiceMeal(
        "average", mean_calories, mean_carbs, mean_protein, mean_fat, portion, diet
    )

    if (
        len(meals_name_list) < 5
    ):  # In case it's missing we calculate the average calories and macros
        for i in range(5 - len(meals)):
            meals.append(mean_meal)
    # We also need to add weekends
    meals.append(mean_meal)
    meals.append(mean_meal)

    # Let's also do dinner for averages.
    for x in range(7):
        meals.append(mean_meal)

    return meals


if __name__ == "__main__":
    meals = create_all_hc_meal(meals_names, portion, diet)
    print(len(meals))
    athlete = Athlete("Anna", 27, "Female", 165, 62, "Active")
    daily_cals = athlete.calculate_daily_calories()
    logger = FoodLogger(athlete, meals, 0.1)
    df = logger.create_dataframe()
    print(df)
