# luodaan tuotelista
products = ["Pölynimuri", "Kahvinkeitin", "Jääkaappi", "Pakastin", "Hammasharja", "Kirjahylly"]

# pyydetään käyttäjältä monesko tuote muutetaan
choice = input("Monesko tuote muutetaan?\n")
choice = int(choice)

# pyydetään käyttäjältä uuden tuotteen nimi
new_product = input("Anna korvaavan tuotteen nimi?\n")

# vaihdetaan käyttäjän indeksi mukainen tuote uudeksi tuotteeksi
products[choice] = new_product

print(products)