# hyvä esimerkki - missä listat ovat erittäin näppäriä

# lista arvosanoista:
grades = [5, 8, 9, 10, 6, 8, 8]

# keskiarvo määritelmä = lukujen summa / lukujen määrä
total = sum(grades)
amount = len(grades)

# lasketaan keskiarvo ja pyöristetään
average = total / amount
average = round(average, 1)
print(average)