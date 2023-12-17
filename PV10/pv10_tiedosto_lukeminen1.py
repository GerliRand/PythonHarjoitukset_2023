# aukaistaan yhteys tiedostoon
file_handle = open("weekdays.txt", "r")

# luetaan tiedoston sisältö muuttujaan
# tietotyyppi on string
content = file_handle.read()

# muista aina sulkea tiedosto!
file_handle.close()

print(content)


