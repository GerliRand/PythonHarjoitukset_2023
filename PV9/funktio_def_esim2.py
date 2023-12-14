from functions import *

# kutsutaan funktiota ja annettaan tiedot
combine_text("Herra", "Hakkarainen", 42)

# get_year palauttaa tietoa return-komenolla
# tarvitaan samalla muuttuja joka ottaa tiedosta kopion
result = get_year()
print(result)

# kutsutaan apufunktiota joka päättele onko nro pariton tai parillinen
value = input("Syötä jonkin numero:\n")
value = int(value)
result = get_even_number_text(value)
print(result)