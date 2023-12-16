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

# apufunktio joka laskee tunneista päivien lukumäärän
def hours_to_days(hours):
    result = hours // 24
    return result

# apufunktio joka kääntää tekstin toisinpäin
def reserve_string(text):
    return text[::-1]

# apufuntio joka tarkistaa onko annettu teksti palindromi vai ei
def check_palidrome(text):
    # kutsutaan toista omaa funktiota
    reversed_text = reserve_string(text)

    if text == reversed_text:
        return True
    else:
        return False

# apufunktio joka tarkista onko tilauskoodi syötetty oikeassa formaatissa
def check_order(code):
    result = True
    # jos koodi ei ole tasan 10 merkkiä => False
    if len(code) != 10:
        result = False
    # jos koodin ensimmäinen kirjain ei ole T => False
    if code[0] != "T":
        result = False

    return result

# apufunktio mikä tulostaa listan allekkain
def show_list(data):
    # tulosta sisältö silmukalla
    for word in data:
        print(word)

# apufunktio joka laskee listan numeroista keskiarvon
def get_list_average(numbers):
    total = sum(numbers)
    amount = len(numbers)
    result = total / amount
    result = round(result, 2)
    return result
