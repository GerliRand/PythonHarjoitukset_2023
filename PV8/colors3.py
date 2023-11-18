from colorama import Fore, Back, Style

# kysytään käyttäjältä luku
number = input("Anna jokin numero:\n")
number = int(number)

# reagoidaan eri väreillä riippuen siitä onko numero positiivinen tai negatiivinen
if number >= 0:
    print(Fore.BLACK + Back.LIGHTGREEN_EX + "Positiivinen luku")

else:
    print(Fore.BLACK + Back.LIGHTRED_EX + "Negatiivinen luku")