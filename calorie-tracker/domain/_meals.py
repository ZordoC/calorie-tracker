from dataclasses import dataclass


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
