import requests

url = "https://wttr.in/{}"
c = input("Enter city to get weather: ")


def get_weather(city):
    new_url = url.format(city)
    try:
        res = requests.get(new_url)
        print(res.text)
    except:
        print("An error occurred try again")


get_weather(c)
