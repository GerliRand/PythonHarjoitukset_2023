from colorama import Fore, Back, Style

print(Fore.BLUE + "Eri väristä tekstiä!")
print("Lisää tekstiä, vieläkin sama väri!")
print(Fore.RED + Back.LIGHTBLACK_EX + "Vaihdetaan tausta ja tekstin väri samalla!")
print("Vieläkin on punainen teksti ja harmaa tausta.")

# palautettaan kaikki normaaliksi
print(Style.RESET_ALL)
print("Nyt ollaan takaisin normaalissa tilassa!")