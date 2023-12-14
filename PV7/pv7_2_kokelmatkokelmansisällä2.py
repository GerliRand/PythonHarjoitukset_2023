# tuotteiden eri kategoriat omissa listoissa
books = ["Da Vinci Code", "Onnellinen minä", "Sijoittajat"]
movies = ["Jurassic Park", "Forrest Gump", "Love me"]

# kaikki verkkokaupan tuotteet
products = [books, movies]

for category in products:
    for item in category:
        print(item)