import requests
import datetime
from tools import wind_speed, celsius_degrees

API_KEY = "912c622485ebcccfe6e75ebb3dc2de10"
city_name = "Wadowice"


def fetch_weather ():
    URL = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}"

    try:
        response = requests.get(URL)
        weather = response.json()

        data = {
            "Odczuwalna": weather["main"]["feels_like"],
            "Ciśnienie": weather["main"]["pressure"],
            "Wilgotność": weather["main"]["humidity"],
            "Zwykla temperatura": celsius_degrees(weather["main"]["temp"]),
            "Opis": weather["weather"][0]["description"],
            "Nazwa": weather["name"],
            "Prędkość wiatru": wind_speed(weather["wind"]["speed"]),
            "Data": datetime.datetime.now()
        }
        return data


    except Exception as err:
        print (err)


