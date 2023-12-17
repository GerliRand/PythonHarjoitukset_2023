# aukaistaan yhteys tiedostoon -> kirjoitusmoodi (w)
# luo lennosta uuden tiedoston
# encodingin avulla saa ääkköset kuntoon!!!
file_handle = open("muistio.txt", "w", encoding="utf-8")

# kysytään käyttäjältä tallentava teksti
text = input("Anna jotain tekstiä:\n")

# kirjoitetaan tiedostoon käyttäjän antama teksti
file_handle.write(text)