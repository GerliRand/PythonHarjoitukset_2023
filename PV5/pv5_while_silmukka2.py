# tehdään apumuuttuja, joka pitää kirjaa siitä pidetäänkö ohjelmaa enää käynnissä

running = True

# ohjelman pääsilmukka, joka pitää ohjelman käynnissä niin kauan kuin käyttäjä haluaa
while running:
    print("Ohjelma on käynnissä!")

    # kysytään käyttäjältä numero
    number = input("Anna numero: \n")
    number = int(number)

    # tuplataan käyttäjän numeroa
    total = number * 2
    print(f"Numero tuplattuna: {total}")


    choice = input("Haluatko jatkaa ohjelman käyttöä? (k/e):\n")
    # pakotettaan pieneksi kirjaimiksi, eli iso E ja K toimi myös
    if choice.lower() == 'e':
        running = False

# tämä ajetaan vasta kun while-silmukkaa lopettaa toiminnan
print("Kiitos ohjelman käytöstä!")

