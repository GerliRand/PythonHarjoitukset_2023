choice = input("Oletko opiskelija vai aikuinen? (a/o)\n")

if choice == "o":
    print("Tämä koodi käsittelee opiskelijakohtaisen koodin.")
    print("Esim. lasketaan jokin lipun hinta yms.")
elif choice == "a":
    print("Tähän sitten aikuisten laskentalogiikka")
else:
    print("Valinta ei tunnistettu. Käynnistä ohjelma uudelleen.")