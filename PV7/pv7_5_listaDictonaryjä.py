# lista dictonaryjä, yleisin yhdistelmä!
products = [
    {"name": "Kahvinkeitin", "price": 79},
    {"name": "Astianpesukone", "price": 299},
    {"name": "Arkkupakastin", "price": 199},
    {"name": "Hammasharja", "price": 229}
]

for p in products:
    # puretaan jokainen dictonary osiin yksi kerrallaan
    name = p["name"]
    price = p["price"]

    print(f"{name}, {price}€")