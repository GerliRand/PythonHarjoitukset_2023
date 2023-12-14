# työkalu var_dump  -> tulosta datan paremassa muodossa
import var_dump as vd

# luodaan hotelli no. 1
hotel_1 = {
    "name": "Snow Line Hotels",
    "rating": 4.3,
    "wifi": True,
    "free_breakfast": True,
    "services": ["sauna", "meetings", "restaurant", "parking", "safaris"],
    "price_level": 4
}

# luodaan hotelli no. 2
hotel_2 = {
    "name": "North Ice Hostel",
    "rating": 3.5,
    "wifi": True,
    "free_breakfast": False,
    "services": ["sauna", "parking"],
    "price_level": 2
}

# tehdään tyjä lista
sauna_hotels = []

# yhdistetään hotellit
hotels = [hotel_1, hotel_2]

# tulostetaan hotellien nimet käyttämällä for-silmukka
for hotel in hotels:
    print(hotel["name"])

    # tulostetaan - missä hotellissa on ravintola
    for service in hotel["services"]:
        if service == "restaurant":
            print("Hotellissa on ravintola")

        # missä hotellissa on sauna, tulosta listana (sen muoto voi muokata .join(), katso exercise 7.4 tai 7.1)
        if service == "sauna":
            sauna_hotels.append(hotel["name"])

            # saunaH = ", ".join(sauna_hotels)

    print()

print(sauna_hotels)
