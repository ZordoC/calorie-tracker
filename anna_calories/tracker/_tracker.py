from dataclasses import dataclass
from datetime import datetime
import pandas as pd

# drunken-noodles,Small,None,433,41,27,18


@dataclass
class Meal:
    name: str
    calories: int
    carbs: int
    protein: int
    fat: int


@dataclass
class HealthiestChoiceMeal(Meal):
    """Represents a meal from the healthieschoice food delivery"""

    portion_size: str
    diet: str

@dataclass
class Athlete:
    name: str
    age: int
    gender: str  # Male/Female
    height: str  # in cm
    weight: int  # in kg
    activity: str  # Light, Moderate, Active, Very Active

    def calculate_bmr(self):
        """Calculate base metabolic rate
        BMR is the calories you burn by just existing
        """
        bmr = 10 * self.weight + 6.25 * self.height - 5 * self.age + 5
        if self.gender == "Female":
            return bmr - 166
        return bmr

    def calculate_daily_calories(self):
        calories = 0
        bmr = self.calculate_bmr()
        if  self.activity == 'Very Active':
            calories = bmr + 800
        elif self.activity == 'Active':
            calories = bmr + 600
        elif self.activity == 'Moderate':
            calories = bmr + 400
        elif self.activity == 'Light':
            calories = bmr + 300
        return calories

example = HealthiestChoiceMeal("drunken-noodles", 433, 41, 27, 18, "Small", "None")

@dataclass
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
        for meal in self.meals:
            counter += meal.calories
        return counter

    @property
    def athlete_name(self):
        return self._athlete

    @property
    def total_calories(self):
        return self._total_calories
    
    @property
    def daily_calories(self):
        return self.athlete.calculate_daily_calories()

    def calories_aim(self):
        calories = self._athlete.calculate_daily_calories()
        return calories * 7 * (1 - self.deficit) 

    def add_meal(self, meal: Meal):
        self.total_calores =+ meal.calories
    
    def get_bmr(self):
        return self.athlete.calculate_bmr()

    def store_data(self):
        # "date", "planned_calories", "total_calories"
        self._df["date"] = self._date
        self._df["planned_calories"] = self.planned_calories
        self._df["total_calories"] = self.total_calores
        


