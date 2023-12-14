# oletetaan että tämän syksyn alennuskoodi on WINTER23
# kysytään käyttäjältä alennuskoodi
sales_code = input("Anna alennuskoodi:\n")
current_code = "WINTER23"

# tekstiä verrataan joko == tai !=
if sales_code == current_code:
    print("Olet oikeutettu alennukseen!")
else:
    print("Normaali hinta.")