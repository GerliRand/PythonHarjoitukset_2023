# importtaa funktions.py tiedostosta kaikki (eli * tarkita kaikki)
from functions import *

user_value = input("Anna tuntien lukumäärä:\n")
user_value = int(user_value)

# lasketaan päivien määrä omalla apufunktiolla
days = hours_to_days(user_value)
print(days)