# käytettään pohjana koodipaja1_korkoakorolle esimerkkiä
# tässä ei käytettää matemaatista kaava

start_money = 15000
yearly_money = 2000

# korkoprosentti, eli 7% korotus -> 1.07
interest = 1.07

total = start_money

# tehdään silmukka, mikä käy kaikki vuodet ja kasvattaa korkoa sitä mukaan
for year in range(10):
    # lisätään joka vuoden alussa 2000e tilille
    total = total + yearly_money

    # lasketaan vuoden korko
    total = total * interest

# koko rahasumma lopuksi, sis. sijoitukset, pyöristettään
total = round(total, 2)

# paljonko tuli voittoa
new_money = total - start_money - (10 * yearly_money)

print(f"Koko rahasumma: {total}€ ja voitto: {new_money}€")