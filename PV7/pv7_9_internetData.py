import urllib.request
import json

import var_dump as vd
# get internet data
url = 'https://edu.frostbit.fi/api/events'
req = urllib.request.Request(url)
raw_data = urllib.request.urlopen(req).read().decode("UTF-8")

# kääntää raaka datan pythonin muotoon
data = json.loads(raw_data)
# vd.var_dump(data)

single_event = data[0]      # voit tulosta ja ottaa siitä copsyn avuksi (alla näkyy)
vd.var_dump(single_event)

# jokainen tapahtuma data-listassa (lista dictonaryjä)
# yksi dictonay -> yksi tapahtuma
for event in data:
    categories = ", ".join(event["categories"])     # etsitään categories ja lisätään perkkäin ja yht ,

    print(event["name"])        # tulostetaan kaikkien tapahtumien nimet

    # tehdään apumuuttujat jotta saataisi osite tiedot
    street_address = event["address"]["street_address"]
    postal_code = event["address"]["postal_code"]

    print(f"{postal_code} {street_address}")
    # tulostetaan kategoriat jos niitä on, muuten ilmoitetaan ettei ole kategorioita 
    if categories != "":
        print(categories)
    else:
        print("- EI KATEGORIOITA -")
    print()


#0 dict(4)
    # ['name'] => str(13) "Alcinan saari"
    # ['date'] => str(8) "3.2.2024"
    # ['categories'] => list(1)
    #     [0] => str(8) "musiikki"
    # ['address'] => dict(2)
    #     ['street_address'] => str(16) "Helsinginkatu 58"
    #     ['postal_code'] => str(5) "00260"
