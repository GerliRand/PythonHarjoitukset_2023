import math

# piin arvon saadan helposti math-moduulin kautta
# käyttää tätä viikkotehtävissä
print(math.pi)

# lasketaan ympyrän ympärysmitta = 2 * pi * säde
# radius (säde) = esim. 13
radius = input("Anna säde kokonaisluvuna: ")
radius = int(radius)
border = 2 * math.pi * radius
# pyöristettään vastaus
border = round(border, 2)
print(f"Ympärysmitta: {border}cm")     #tulosta: Ympärysmitta: 81.68cm

