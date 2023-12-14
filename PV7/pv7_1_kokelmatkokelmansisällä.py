# kokelmat kokelman sisällä, esim. lista
temp_day_1 = [13.5, 16.4, 11.6, 11.3]
temp_day_2 = [12.1, 15.2, 11.9, 10.4]
temp_day_3 = [15.3, 17.6, 12.5, 11.6]

teperatures = [temp_day_1, temp_day_2, temp_day_3]

# temperatures on lista, eli tarvitaan for-silmukka
for day in teperatures:
    print("Uusi päivä:")
    for temp in day:        # pitää tehdä tuplasti for-silmukka jotta tulostais allekkain eikä listana
        print(temp)