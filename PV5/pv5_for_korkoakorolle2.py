# Versio 2

# kuinka monta vuotta kestää, että pääsemme sijoituksilla tiettyyn voittoon?

start_money = 15000     # raha alussa
yearly_money = 2000     # näin paljon laitettaan joka vuosi

target_savings = 40000  # tavoite

interest = 1.07         # intress

# apumuuttujat silmukkaa varten
total = start_money
winnings = 0

# vuodet 1-30
for year in range(1, 31):
    total = total + yearly_money

    # korkoa korolle
    total = total * interest

    # kuinka paljon voittoa tähän vuoteen mennessä
    winnings = total - start_money - (year * yearly_money)

    # tarkistetaan ollanko jo tavoitteessa, jos ollaan, niin break - koska ei tarvitse enää jatkaa laskemista
    if winnings >= target_savings:
        print(f"Tavoitteeseen päästiin vuonna: {year}")
        break

# jos kävi niin, ettei päästy tavoitteeseen, ilmoitetaan käyttäjälle
if winnings < target_savings:
    print("Tavoite ei onnistu tällä aikavälillä ja sijoituksilla!")