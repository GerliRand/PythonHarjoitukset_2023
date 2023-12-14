# and ja or
number = input("Syötä numero:\n")
number = int(number)

# jos numero on suurempi kuin 0 ja samaan aikaan pienempi kuin 30 (eli välillä 0-30)
# if 0 < number < 30:      <- Pythonin shorthand
if number > 0 and number < 30:
    print("Numero on 0 ja 30 välillä.")



# jos numero on pienempi kuin 0 tai suurempi kuin 30 (edellisen vastakohta)
if number < 0 or number > 30:
    print("Numero on joko alle 0 tai yli 30.")
