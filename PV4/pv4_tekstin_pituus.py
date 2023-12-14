text = input("Kirjoita jonkin lause:\n")

# tulostetaan tekstin pituus
text_length = len(text)
print(f"Tekstissä merkkejä: {text_length}")

# lasketaan pienet a-kirjaimet (huom. pienet ja isot kirjaimet on erikseen)
a_letters = text.count("a")
print(f"Tekstissä on pieniä a-kirjaimia: {a_letters}")
print()

# tarkistetaan tekstin pituus
if text_length > 30:
    print("Pitkä lause!")
else:
    print("Lyhyt lause.")

# tarkistus, onko teksti tai ei
if text_length == 0:
    print("Teksti on tyhjä!")
else:
    print("Tässä on tekstiä")