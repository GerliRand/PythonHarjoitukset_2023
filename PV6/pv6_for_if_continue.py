# VERSIO 1 ilman Continue komentoa, sisennetyillä if-lauseilla

import os

data = ["ostoslista.txt", "valokuvat.txt", "dokumentti.txt", "olematontiedosto.txt"]

# for-silmukka, käydään jokainen tiedosto listassa läpi
for filename in data:
    # katsotaan onko käsiteltävä tiedosto olemassa
    if os.path.isfile(filename):
        # katsotaan onko käyttöoikeus tähän tiedostoon
        if os.access(filename, os.R_OK):
            # katsotaan ettei tiedosto ole tyhjä
            if os.path.getsize(filename) > 0:
                file = open(filename, 'r')
                print(file.read() + "\n")
                file.close()


# VERSIO 2, CONTINUE-KOMENNOLLA, ns. "preconditions"

data = ["ostoslista.txt", "valokuvat.txt", "dokumentti.txt", "olematontiedosto.txt"]


# huomaa, että ehtolauseet ovat nyt vastakohtia, eli negaatioita.
# tämä siksi, että jos yksikin ehto tuottaa FALSE => skipataan tiedosto kutsumalla continueta
# selkeämpi rakenne
for filename in data:

    # katsotaan onko tiedosto olemassa
    if not os.path.isfile(filename):
        continue

    # katsotaan onko meillä käyttöoikeus tiedostoon
    if not os.access(filename, os.R_OK):
        continue

    # katsotaan ettei tiedosto ole tyhjä
    if not os.path.getsize(filename) > 0:
        continue

    # kaikki ok, luetaan tiedoston sisältö ja tulostetaan!
    file = open(filename, 'r')
    print(file.read() + "\n")
    file.close()
