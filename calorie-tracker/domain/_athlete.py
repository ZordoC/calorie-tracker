from dataclasses import dataclass


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
        if self.activity == "Very Active":
            calories = bmr + 800
        elif self.activity == "Active":
            calories = bmr + 600
        elif self.activity == "Moderate":
            calories = bmr + 400
        elif self.activity == "Light":
            calories = bmr + 300
        return calories
