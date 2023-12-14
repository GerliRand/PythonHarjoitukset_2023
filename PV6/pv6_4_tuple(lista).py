# Tuplessa sisältöä ei voi muutta jälkikäteen
# Tehdään tuple, jossa on viikonpäivät
# voi laittaa allekkain tai vierekkäin
weekdays = ("Maanantai",
            "Tiistai",
            "Keskiviikko",
            "Torstai",
            "Perjantai",
            "Lauantai",
            "Sunnuntai")

# kysytään käyttäjältä viikonpäivä indeksi
choice = input("Kuinka mones viikonpäivä?\n")
choice = int(choice) - 1    # otetaan yksi pois, koska indeksi lukeminen aika nollasta (nyt antamalla 3 -> Keskiviikko)

# print(weekdays[choice])
# tai
text = weekdays[choice]
print(text)
