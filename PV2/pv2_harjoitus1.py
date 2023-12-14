# pyydetään käyttäjältä säästöt
# Huom: data tulee tekstinä, vaikka siinä olisi numeroita - eli pitää muutta numeroiksi!
# desimaaliluku -> float() ja kokonaisluku -> int()

savings = input("Kuinka paljon sinulla on säästöjä?\n")
savings = float(savings)

# toinen vaihtoehto tehdä
salary = float(input("Kuinka paljon sait tässä kuussa palkka?\n"))

# lisättään korko 5%
increase = 1.05

total = (savings + salary) * increase
print(f"Raha yhteensä, sisältäen korko: {total} €")
