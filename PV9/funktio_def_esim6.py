# importtaa funktions.py tiedostosta kaikki (eli * tarkita kaikki)
from functions import *

# kokeillaan omaa tilauskoodin validointifunktiota
test = "T6739-6584"
result = check_order(test)

# tarkistetaan lopputulos
if result:
    print("Tilauskoodi ok")
else:
    print("Väärä tilauskoodi")