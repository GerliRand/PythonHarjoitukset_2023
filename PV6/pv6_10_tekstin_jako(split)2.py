codes = ["TILAUS12354_A13654_2023", "TILAUS6584545_B565_2022"]

# käydään lista läpi silmukassa
for code in codes:
    # jaetaan koodi osiin splitillä
    parts = code.split("_")
    first = parts[0]
    second = parts[1]
    year = parts[2]

    print(first)
    print(second)
    print(year)
    print()