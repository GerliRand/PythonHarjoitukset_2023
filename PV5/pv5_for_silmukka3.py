# tehdään alkuun tyhjä tekstimuuttuja, joka rakennetaan valmiiksi silmukan avulla
# kannatta kokeilla Python Tutorissa!

text = ""

for year in range(2017, 2024):
    text = text + str(year) + "-"

# osateksti, otetaan viimeinen merkki pois
text = text[:-1]

print(text)
