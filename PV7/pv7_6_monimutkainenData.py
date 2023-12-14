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

# yhdistetään hotellit
hotels = [hotel_1, hotel_2]

# tulosta datan paremassa muodossa
vd.var_dump(hotels)

# tulostetaan hotellien nimet käyttämällä for-silmukka
for hotel in hotels:
    print(hotel["name"])

    # print(hotel["services"])    # tapa 1 - raaka muoto, eli huono tapa

    # for service in hotel["services"]:     # tapa 2 - toinen for-silmukka
    #     print(service)

    services = "\n".join(hotel["services"])     # liimataan yhteen join(), ei käytettää for-silmukka, hyvä tapa!
    print(services)

    if "restaurant" in services:
        print("Hotellissa on ravintola")

    if "sauna" in services:
        print("Hotellissa on sauna")

    print()
# haetaan toisen hotellin luokitus
print(hotels[1]["rating"])
