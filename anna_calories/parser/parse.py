import pandas as pd
import requests
from bs4 import BeautifulSoup

from datetime import date    

TODAY = date.today().isoformat()


BASE_URL = "https://www.thehealthiestchoicebcn.com/"

DISH_CLASS = "text-xl lg:text-2xl font-bold text-white lg:tracking-wider"
URL = "https://www.thehealthiestchoicebcn.com/choose-your-meals"


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
        fp.write("date,name,portion,custom,calories,carbs,protein,fat \n")
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

    for day,dish in week_dishes.items():
        url = build_nutri_url(day, dish)
        dish_macros = get_dish_macros(url, dish)
        create_csv(dish, dish_macros)

parse_website()

print(pd.read_csv("data/drunken-noodles.csv"))