print("Aloitetaan!")

# silmukka 0-9
for x in range(10):
    #jos x on tasan 6, katkaistaan silmukka
    if x == 6:
        print("Huono arvo, skipataan!")
        continue

    print(x)

print("Valmis!")
