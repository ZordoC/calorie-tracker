from dataclasses import dataclass
from datetime import datetime

import pandas as pd

from ._athlete import Athlete
from ._meals import Meal

# drunken-noodles,Small,None,433,41,27,18


class FoodLogger:
    def __init__(self, athlete: Athlete, meals: list[Meal], deficit: float):
        self._df = pd.DataFrame(columns=["date", "planned_calories", "total_calories"])
        self._athlete = athlete
        self._meals = meals
        self._deficit = deficit
        self._date = datetime.now()

    @property
    def planned_calories(self):
        counter = 0
        for meal in self._meals:
            counter += meal.calories
        return counter

    @property
    def athlete_name(self):
        return self._athlete

    @property
    def daily_calories(self):
        return self.athlete.calculate_daily_calories()

    @property
    def calories_goal(self):
        calories = self._athlete.calculate_daily_calories()
        return calories * 7 * (1 - self._deficit)

    def add_meal(self, meal: Meal):
        self.total_calores = +meal.calories

    def get_bmr(self):
        return self.athlete.calculate_bmr()

    def create_dataframe(self):
        # "date", "planned_calories", "total_calories"
        data = {}
        data["date"] = [self._date]
        data["planned_calories"] = [self.planned_calories]
        data["calorie_goal"] = [self.calories_goal]
        return pd.DataFrame(data)
