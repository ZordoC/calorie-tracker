import pandas as pd
import requests
from bs4 import BeautifulSoup

from ..utils.const import TODAY, BASE_URL, DISH_CLASS, URL


def create_soup(url: str):
    data = requests.get(url).text
    return BeautifulSoup(data, "html.parser")


def get_weekly_dishes(soup) -> list:
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    week_dishes = {
        day: div.text.lower().replace(" ", "-")
        for (day, div) in zip(weekdays, soup.findAll(class_=DISH_CLASS))
    }
    return week_dishes


def build_nutri_urls(week_dishes: dict) -> list:
    urls = [f"{BASE_URL}products/{v}?date={k}" for k, v in week_dishes.items()]
    return urls


def get_dish_macros(url: str, name: str) -> list:
    tmp = create_soup(url)
    data = []
    for x in tmp.findAll(class_="flex border-b text-tiny lg:text-sm"):
        data.append(x.text.rstrip().lstrip().replace("\n\n\n", ","))
    dic = dict(name=data)
    return data


def create_csv(name, dish_macros: list) -> None:
    with open(f"data/{name}.csv", "w") as fp:
        fp.write("date,name,portion,custom,calories,carbs,protein,fat\n")
        for ele in dish_macros:
            fp.write(TODAY + "," + name + "," + ele + "\n")


def build_nutri_url(weekday: str, dish: str) -> list:
    if weekday == "Thursday" and dish == "chicken-jambalaya":
        return f"{BASE_URL}products/pork-sirloin-with-cheese-grits?date=Thursday"

    url = f"{BASE_URL}products/{dish}?date={weekday}"
    return url


def parse_website():
    soup = create_soup(URL)

    week_dishes = get_weekly_dishes(soup)
    # print(week_dishes)

    for day, dish in week_dishes.items():
        url = build_nutri_url(day, dish)
        dish_macros = get_dish_macros(url, dish)
        create_csv(dish, dish_macros)


def get_meal(dish: str, diet: str, portion_size: str) -> pd.DataFrame:
    df = pd.read_csv(f"data/{dish}.csv")
    df = df[df["portion"] == portion_size]
    df = df[df["custom"] == diet]
    return df


df = get_meal("drunken-noodles", "High Protein + Low Carb", "Regular")


def get_weekly_meals(names: list[str], diet: str, portion_size) -> list[pd.DataFrame]:
    tmp = []
    for name in names:
        meal = get_meal(name, diet, portion_size)
        tmp.append(meal)
    return pd.concat(tmp)
