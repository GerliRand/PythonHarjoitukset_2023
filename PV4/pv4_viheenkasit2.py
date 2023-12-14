# jokainen eri virhetyypi pitä ottaa kiini

try:
    number = input("Anna numero:\n")
    number = int(number)

    # tämä tuottaa ZeroDivisionErrorin jos nr on 0
    divided = 100 / number
    print(divided)

except ValueError:
    print("Syötit tekstä. Käynnistä ohjelma uudelleen.")

except ZeroDivisionError:
    print("Nollalla ei saa jakaa! Syötä muu numero.")
