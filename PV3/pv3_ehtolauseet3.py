age = input("Syötä ikä:\n")
age = int(age)

# pienempi kuin
if age < 30:
    print("Olet alle 30v")

# suurempi kuin
if age > 30:
    print("Olet yli 30v")

# suurempi tai yhtäsuuri, sama pienempi tai yhtäsuuri <=
# if age >= 30:
#     print("Olet yli 30v tai tasan 30v")

# tasaarvo
if age == 30:
    print("Olet tasan 30v")

# negaatio, eli == vastakohta
if age != 30:
    print("Et ole tasan 30v")
