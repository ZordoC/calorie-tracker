import requests


data = requests.get("https://www.thehealthiestchoicebcn.com/choose-your-meals").json()


print(data.keys())
