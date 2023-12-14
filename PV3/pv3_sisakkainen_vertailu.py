status = input("Opiskelija vai aikuinen? (o/a)\n")
price = input("Lipun alkuperäinen hinta:\n")
price = float(price)        # rahan kanssa käytettään - float (desimaali)

# opiskelijat saa 50% alennusta
# aikuset maksavat täyden hinnan + palvelumaksu 2.5€
# paitsi jos lipun hinta on yli 100€, silloin ei ole palvelumaksu

if status == "o":
    price = price * 0.5

elif status == "a":
    #palvelumaksu lisätään ainoastaan silloin kuin hinta on alle 100€
    if price < 100:
        price = price + 2.5

print(f"Lopullinen hinta: {price} €")