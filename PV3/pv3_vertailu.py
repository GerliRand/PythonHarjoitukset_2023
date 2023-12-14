# kun vertailet numeromuuttujia toisiinsa
# tarkista että molemmat ovat oikeasti numeromuodossa!
# eli joko int() tai float()
number1 = input("Anna jokin numero:\n")
number1 = int(number1)

number2 = 234

# verrataan numeromuuttujia tosiinsa
# jos toinen muuttujista on jäänyt vahingossa tekstimuotoon - tulee bugeja
if number1 > number2:
    print("Käyttäjän antama numero on suurempi")
else:
    print("Toinen numero on suurempi")

