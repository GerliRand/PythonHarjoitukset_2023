# eli jos koodin tulee toistoa, pitäisi käyttää silmukkaa
total = 0

# ei näin!!!
# number1 = int(input("Anna numero: \n"))
# total = total + number1
# number1 = int(input("Anna numero: \n"))
# total = total + number1
# number1 = int(input("Anna numero: \n"))
# total = total + number1
# number1 = int(input("Anna numero: \n"))
# total = total + number1
# number1 = int(input("Anna numero: \n"))
# total = total + number1

# kysytään käyttäjältä numero 5 kertaa ja lisätään total-muuttujaan
# liitetään numerot yhteen
for x in range(5):
    number = int(input("Anna numero: \n"))
    total = total + number

print(total)

