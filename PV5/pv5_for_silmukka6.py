# kysytään käyttäjältä kierrosten (lukujen) määrä
# HUOM! älä koskaan yritä if-lauseella, paitsi jos vaihtoehtoja on max 3
cycles = input("Montako lukua kysytään?\n")
cycles = int(cycles)

total = 0

# ajetaan silmukka niin monta kertaa kuin käyttäjä halusi
for x in range(cycles):
    number = int(input("Anna numero:\n"))
    total = total + number

print(f"Yhteensä: {total}")