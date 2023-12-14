print("Ajetaan tilausraportti:")

# pääsilmukka ajaa tilaukset (3 kpl)
for order in range(3):
    print(f"KÄSITELLÄÄN TILAUSTA nro: {order}")

    # alisilmukka käsittelee käsittelyssä olevan Tilauksen sisällä olevat Tuotteet
    # oletuksena, että tilauksessa on tasan 5 tuotetta
    for product in range(5):
        print(f"\t Käsitellään tilauksen {order} tuotetta {product}!")

print("Kiitos ohjelman käytöstä!")