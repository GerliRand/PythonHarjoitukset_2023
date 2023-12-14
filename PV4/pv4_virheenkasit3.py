# jokainen eri virhetyypi pitä ottaa kiini
try:
    number = input("Anna numero:\n")
    number = int(number)

    divided = 100 / number
    print(divided)

# yleiset exceptinoit ei ole ymmerrettäviä käyttäjälle
except Exception as e:
    print(f"Virhe: {e}")