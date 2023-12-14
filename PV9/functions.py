# TÄLLÄ ON OMAT FUNKTIOT
# määritellään funktio nimeltä show_text
# funktio ei tee mitäään ennen kun sitä kutsutaan
def show_text():
    print("Tervetuloa ohjelman käyttäjäksi")
    print("-------------------------------")
    print("Seuraa ohjeita!")
    print()

# funktio joka tulostaa koko nimen ja iän
def combine_text(first, last, age):
    print(f"Tervetuloa: {first} {last}!")
    print(f"Ikäsi on: {age} vuotta.")

# apufunktio, joka palauttaa kuluvan vuoden numerona (voi käyttää datetime)
def get_year():
    year = 2023
    return year

# funktio joka päättelee annetusta numerosta onko kyseessä parillinen vai pariton luku
def get_even_number_text(number):
    if number % 2 == 0:
        return "Parillinen"
    else:
        return "Pariton"

# apufunktio joka kääntää tekstin toisinpäin
def reserve_string(text):
    return text[::-1]