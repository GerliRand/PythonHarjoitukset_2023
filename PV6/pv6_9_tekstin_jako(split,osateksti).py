code = "TILAUS12354_A13654_2023"

# split-in avulla jaetaan osiin, tämä on oikea tapa!
parts = code.split("_")
first = parts[0]
second = parts[1]
year = parts[2]

# perinteisisti osatekstillä
# Huom. toimii ainoastaan silloin kuin tiedot pysyy samaana
# first = code[0:11]
# second = code[12:18]
# year = code[-4:]

print(first)
print(second)
print(year)

