# sidotuu harjoituksen 7.5

import json
import urllib.request
url = "https://edu.frostbit.fi/api/weather/"
req = urllib.request.Request(url)
raw_data = urllib.request.urlopen(req).read().decode("UTF-8")

weather = json.loads(raw_data)

strongest_wind = 0
strongest_wind_city = ""

weakest_wind = 0

for city in weather:
    print(city)     # tulosta kaupinkien tiedot

    # jos tämän kaupunkin tuuli on kovempi kuin strongest_wind
    # silloin pääivitetään strongest_wind + kaupunki nimi