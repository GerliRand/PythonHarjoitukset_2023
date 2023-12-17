import json

# luetaan cities.json
file_handle = open("cities.json", "r")

content = file_handle.read()
file_handle.close()

# muutetaan data json-formaatista python dataksi
# tämä data tuottaa listan dictionayjä
cities = json.loads(content)

# käydään silmukalla läpi ja tulostetaan kaupunkien tiedot yksi kaupunki kerrallaan
for city in cities:
    print(city["name"])
    print(city["population"])
    print(city["county"])
    print()