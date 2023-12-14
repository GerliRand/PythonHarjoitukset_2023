running = True

# ajetaan ohjelmaa niin kauan kuin käyttäjä haluaa
while running:
    # kysy nro käyttäjältä
    print("Ohjelma loppuu painamalla pelkästään Enteriä!")
    number = input("Syötä numero:\n")


    print()

    # jos teksti ei ole tyhjä, tulostetaan lista numeroita
    if number != "":
        print("Tulostetaan seuraavat 3 numeroa:")

        # tulostetaan seuraavat kolme numeroa käyttäjän numeron jälkeen
        number = int(number)    # tämä pitää olla tässä, muuten Enter ei lopeta ohjelma
        for x in range(3):
            print(f"=> {number + x + 1}")

    else:
        # muussa tapauksessa lopetetaan ohjelma
        running = False

    print()

print("Kiitos ohjelman käytöstä!")