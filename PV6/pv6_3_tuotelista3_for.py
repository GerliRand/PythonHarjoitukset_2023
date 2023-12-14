# luodaan tuotelista
products = ["Pölynimuri", "Kahvinkeitin", "Jääkaappi", "Pakastin"]

#for-silmukka, joka käy jokaisen products-listan tuotteen vuorollaan läpi
for p in products:
    print(p)

print("Kiitos ohjelman käytöstä!")


# NUMEROITU LISTA - opettaja ei suosittele, koska voi tulla ongelmia
amount = len(products)

for index in range(amount):
    p = products[index]
    print(f"{index + 1}. {p}")      # lisätään idexille + 1, muuten alkaa numerosta 0
