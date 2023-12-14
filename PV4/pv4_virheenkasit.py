# otetaan mahdollinen virhetilanne kiinni
# kysyttään numero, mutta jos annettaan esim. sana, niin ohjelma ilmoita eikä kaatu
try:
    number = input("Anna numero:\n")
    number = int(number)
    number = number * 2
    print(number)
except ValueError:
    print("Syötit tekstä. Käynnistä ohjelma uudelleen.")

