from dataclasses import dataclass


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


class Athlete:
    age: int
    gender: str  # Male/Female
    height: str  # in cm
    weight: int  # in kg
    activity: str  # Light, Moderate, Active, Very Active

    def calculate_bmr(self):
        """Calculate base metabolic rate
        BMR is the calories you burn by just existing
        """
        BMR = 10 * self.weight + 6.25 * self.height - 5 * self.age + 5
        if self.gender == "female":
            return BMR - 166
        return BMR


example = HealthiestChoiceMeal("drunken-noodles", 433, 41, 27, 18, "Small", "None")


@dataclass
class Tracker:
    athlete: Athlete
    meals: list[Meal]
    total_calories: int
    deficit: float  # percentage

    def count_total_lunch_calories(self):
        pass
