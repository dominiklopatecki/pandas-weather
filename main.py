from weather_wadowice import fetch_weather
from excel import append_to_excel
from excel import append_to_csv

import time
while True:
    data = fetch_weather()
    append_to_excel(data)
    append_to_csv(data)
    time.sleep(15)
    print("Pobrano nowe dane")

