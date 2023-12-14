import json
import urllib.request

url = "https://edu.frostbit.fi/api/weather/"
req = urllib.request.Request(url)
raw_data = urllib.request.urlopen(req).read().decode("UTF-8")

weather = json.loads(raw_data)

strongest_wind = 0
strong_wind_city = ""

for city in weather:
    wind_speed = city.get("WindSpeedMS")

    if wind_speed is not None and wind_speed > strongest_wind:
        strongest_wind = wind_speed
        strong_wind_city = city.get("name", "N/A")

print("Kaupunki, jossa on eniten tuulta:")
print("Kaupunki:", strong_wind_city)
print("Tuulen nopeus:", strongest_wind, "m/s")