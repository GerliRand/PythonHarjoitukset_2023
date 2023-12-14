# lista kaupunkeja
cities = ["oulu", "espoo", "vantaa", "tampere", "helsinki", "pori"]

# tehdään kaksi tyhjä listaa (ämpäriä)
long_cities = []
short_cities = []

# käydään kaikki kaupungit läpi ja asetettaan joko lyhyisiin tai pitkiin kaupungin nimiin
for city in cities:
    if len(city) < 6:
        short_cities.append(city)
    else:
        long_cities.append(city)

print(long_cities)
print(short_cities)

