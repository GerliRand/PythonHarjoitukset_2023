# aukaistaan yhteys tiedostoon -> kirjoitusmoodi (w)
# luo lennosta uuden tiedoston
# encodingin avulla saa ääkköset kuntoon!!!
# jos käyttää w sijaan a - niin se ei kirjoittaa yli vaan lisää
file_handle = open("muistio.txt", "a", encoding="utf-8")

# kysytään käyttäjältä tallentava teksti
text = input("Anna jotain tekstiä:\n")

# kirjoitetaan tiedostoon käyttäjän antama teksti
file_handle.write(text + "\n")