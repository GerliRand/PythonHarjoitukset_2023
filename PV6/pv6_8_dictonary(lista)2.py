measurements = {
    "temperature": 3.5,
    "humidity": 0.85,
    "wind": 3.5
}

numbers = list(measurements.values())   # tehdän tiedoista lista
print(numbers)

# keskiarvon määritelmä = lukujen summa / lukujen määrä
total = sum(numbers)
amount = len(numbers)

# lasketaan keskiarvo ja pyöristetään
average = total / amount
average = round(average, 1)
print(average)