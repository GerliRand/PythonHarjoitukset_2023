# aukaistaan yhteys tiedostoon
file_handle = open("weekdays.txt", "r")

# tehdään juokseva rivinumero
counter = 0

# luetaan tiedoston sisältöä rivi kerrallaan niin kauan kuin on data
# eli jos tiedostossa on 100 rivi niin koodi ajetaan 100 kertaa
while True:
    line = file_handle.readline()

    counter = counter + 1   # kasvatetaan laskurimuuttujaa
    print(f"{counter}. {line}")

    # jos rivit loppuvat tiedostosta -> silloin break
    # tulostu kuitenkin yksi ylimääräinen rivinumero
    if not line:
        break

# muista aina sulkea tiedosto!
file_handle.close()