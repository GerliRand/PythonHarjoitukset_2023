import json

# luetaan cities.json
file_handle = open("cities.json", "r", encoding="utf-8")

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

# VAIHE 2
# kysytään käyttäjältä uuden kaupungin tiedot
new_city_name = input("Anna uuden kaupungin nimi:\n")
new_city_county = input("Anna uuden kaupungin maakunta:\n")
new_city_population = int(input("Anna uuden kaupungil asukasluku:\n"))

# rakennetaan uuden kaupungin DICTIONARY ylläolevista muuttujista
new_city = {
    "name": new_city_name,
    "population": new_city_population,
    "county": new_city_county
}

# koska cities on Python-lista, silloin voidaan uusi kaupunki lisätä append() -funktiolla
cities.append(new_city)

# VAIHE 3
# muutetaan cities-lista Python datasta JSON-dataksi

# kaikki muutokset on tallennettu cities-listaan
json_data = json.dumps(cities)

# avataan tiedosto ja tallennetaan uusi data vanhan päälle
# HUOM: a (append-moodia) ei voi käyttää JSONin kanssa
file_handle = open("cities.json", "w", encoding="utf-8")
file_handle.write(json_data)
file_handle.close()

print("Uusi kaupunki tallennettu onnistuneesti!")
