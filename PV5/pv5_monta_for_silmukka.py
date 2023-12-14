# tehdään ylätason pääsilmukka
for x in range(3):
    print(f"Pääsilmukka: x = {x}")

    # alisilmukka, ajettaan 3 kertaa, koska pääsilmukka ajetaan 3 kertaa
    # alisilmukka ajaa oman koodinsa 5 kertaa
    for y in range(5):
        print(f"\t\t Alisilmukka: y = {y}")
