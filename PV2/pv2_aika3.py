from datetime import date, datetime, timedelta

# lasketaan tästä päivästä vuoden loppuun
first = date(2023, 9, 5)
second = date(2023, 12, 31)

delta = second -first
days = delta.days
print(f"Päiviä jäljellä tätä vuotta: {days} kpl")

# esim. jos lainataan kirjastosta uusi kirja, milloin on viimeinen palatuspäivä
today = datetime.now()
today = today + timedelta(21)

print(f"Palautuspäivä kolmen viikon päästä on: {today}")