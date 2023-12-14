# luodaan tuotelista
products = ["Pölynimuri", "Kahvinkeitin", "Jääkaappi", "Pakastin"]

# kysytään käyttäjältä järjestysnumero
# Huom. indeksit ovat int -muodossa
choice = input("Monesko tuote näytetään?\n")
choice = int(choice)

# otetaan muuttujaan talteen, kuinka monta tuotetta meillä on
amount = len(products)

# tarkistetaan että käyttäjän antama indeksi on listan rajoissa
# onhan choice pienempi kuin amount ja samaan aikaan joko 0 tai suurempi -> eli nyt 0-3
if choice < amount and choice >= 0:
    # näytetään choice-muuttujan mukainen elementti listasta
    text = products[choice]
    print(text)
else:
    print("Tällä indeksillä ei ole tuotetta.")