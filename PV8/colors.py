from colorama import Fore, Back, Style

print(Fore.BLUE + "Eri väristä tekstiä!")
print(Back.LIGHTWHITE_EX + "Eri taustaväri :)")
print("Edelleen teksti on sininen ja taustaväri on valkoinen!")

# palautettaan kaikki normaaliksi
print(Style.RESET_ALL)
print("Nyt ollaan takaisin normaalissa tilassa!")
