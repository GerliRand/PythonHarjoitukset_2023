# yksinkertainen kirje / paketti hintalaskurin pohja
choice = input("Kirje vai paketti? (k/p)\n")
weight = input("Paino?\n")
weight = int(weight)

if choice == "k":
    print("Kirjeen hinta on 50snt + 8snt per 100g.\n")

    # jos on iso kirje, tarkistetaan mahtuuko postiluukusta
    if weight > 500:
        big_letter = input("Mahtuuko kirje postiluukusta? Vastaa kyllä tai ei (k/e)\n")

        # jos kirje ei mahdu postiluukusta, niin lisämaksu
        if big_letter == "e":
            print("HUOM! Ison kirjeen lisämaksu on 2€")

elif choice == "p":
    print("Paketin hinta on 2€ + 20snt per 100g.")

print("Kiitos laskurin käytöstä!")