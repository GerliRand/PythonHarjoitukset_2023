# kolmas paramtri on nimeltään step (koodissa 2)
# tämä kasvattaa vuotta +2 (oletuksena on aina +1)
# eli tulostaa: 2000, 2002, 2004, ... 2018
for year in range(2000, 2020, 2):
    print(year)

print()

# periteinen tapa
# käytettään if / else
# tulosa: Parillinen! Kierros 0 ; Pariton Kierros 1 ; Parillinen! Kirreos 2 ...
print("Aloitetaan!")
for x in range (10):
    if x % 2 == 0:
        print(f"Parillinen! Kierros {x}")

    else:
        print(f"Pariton. Kierros {x}")

print("Valmis!")
