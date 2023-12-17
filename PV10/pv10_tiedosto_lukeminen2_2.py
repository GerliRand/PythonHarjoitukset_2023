# aukaistaan yhteys tiedostoon
file_handle = open("weekdays.txt", "r")

# luetaan tiedoston sisältö muuttujaan
content = file_handle.read()

# muista aina sulkea tiedosto!
file_handle.close()

# muutetaan content -> listaksi
# JOS TIEDOSTO SAATAAN LISTA MUOTOON - KAIKKI OPITTU PÄTEE!!!
lines = content.split("\n")
print(lines)

# tulostetaan nyt lista allekkain
for line in lines:
    print(line)
print()

# haetaan rivien määrä len funktiolla
amount = len(lines)
# tulostetaan numeroitu lista (materiaaleissa: toistolauseet sivu 62)
for index in range(amount):
    line = lines[index]
    print(f"{index + 1}. {line}")