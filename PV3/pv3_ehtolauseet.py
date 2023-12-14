# jos haluat syöttä iän
age = input("Syötä ikä:\n")
age = int(age)

month = input("Anna kuukauden numero:\n")
month = int(month)

# ehtolause, onko ikä alle 20?
# jos on, tulostetaan teksti
if age < 20:
    print("OLet alla 20v")
    print("Tulostetaan, jos ikä on alle 20v!!!")
# elif - ehtoja voi olla monta
elif age < 30:
    print("Olet alle 30v")
else:
    print("Ikäsi on jotain muuta")

# täysin erillinen if-lause kokonaisuus, koska month-muuttuja ei litty age-muuttujaan
if month == 7:
    print("Liikkeemme on heinäkuussa suljettu!")
    print("Tavataan taas elokuussa!")

print("Kiitos ohjelman käytöstä!!!")
