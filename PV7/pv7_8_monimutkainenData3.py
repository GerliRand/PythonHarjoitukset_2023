# TEST_HOTELLIT
# monimutkaisemmat hotellit 2kpl
import var_dump as vd

test_hotel_1 = {
    "name": "Wilderness Inn",
    "rating": 4.7,
    "wifi": True,
    "breakfast": {
        "free": True,
        "start": "6:30",
        "end": "10:00"
    },
    "services": [
        {"name": "sauna", "open": "17:00", "close": "22:30"},
        {"name": "meeting_room", "open": "7:30", "close": "20:00"},
        {"name": "restaurant", "open": "12:00", "close": "21:00"},
    ],
    "price_level": 5,
    "other_info": "nature, good services"
}

test_hotel_2 = {
    "name": "North Ice Hostel",
    "rating": 3.5,
    "wifi": True,
    "breakfast": {
        "free": False,
        "start": "-",
        "end": "-"
    },
    "services": [
        {"name": "sauna", "open": "19:00", "close": "22:00"},
        {"name": "room_service", "open": "12:00", "close": "00:00"},

    ],
    "price_level": 2,
    "other_info": "affordable, city centre"
}

# yhdistetään ja korvataan aiempi hotellilista uudella hotellilla
hotels = [test_hotel_1, test_hotel_2]
test_hotel = hotels[0]      # ei tarvitse!

# katsotaan miltä näyttää
# vd.var_dump(test_hotel)

# haetaan hotellin palvelut omaan muuttujaansa
# katsotaan miltä näyttää
test_services = test_hotel["services"]
vd.var_dump(test_services)

for hotel in hotels:
    print(hotel["name"])

    for service in hotel["services"]:
        print(f"{service['name']}, {service['open']} - {service['close']}")
    print()