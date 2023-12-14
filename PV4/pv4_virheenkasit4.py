# tämä yhdistä kaikkia ehtolauseita sekä virkeenkäsittelyä

# tehdän ohjelma joka tarkisat onko annettu asiakastunnus oikeaas muodossa
# tunnus on aina 10 merkkiä pitkä ja kuudes merkki on alaviiva

try:
    client = input("Syötä asiakastunnus:\n")

    text_length = len(client)

    if text_length != 10:
        print("Tunnus on väärän mittainen, vaaditaan 10 merkkiä.")
    elif client[5] != "_":
        print("Tunnuksesta puuttuu alaviiva oikeasta paikkaa!")
    else:
        print("Tunnus OK!")

        # otetaan osatekstillä tunnuksen alku- ja loppuosa irti
        # oikealla puolella pitäisi olla ainoastaan numeroita
        id = client[0:5]
        order = client[6:10]
        order = int(order)

        print(id)
        print(order)

# ottaa lopuksi viimeistään kiinni, jos joku syöttää asiakastunnuksen loppuosaan kirjaimen
# esim. A6321_567Y
except Exception as e:
    print(f"Virhe: {e}")