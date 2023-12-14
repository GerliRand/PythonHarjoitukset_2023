age = 26
city = "Espoo"
student = True

# and - sanan vuoksi kaikkien ehtojen pitää täyttyä
# esim. jos muuttujaan olisi annettu Vantaa - tämä silloin ei toimi
# kolme muuttuja verrattaan harvoin, kaksi on yleinen
if age >= 18 and city == "Espoo" and student == True:
    print("Aikuinen espoolainen opiskelija.")
    if city == "Espoo":
        print("Aikuisten tervisehuolto osoiteessa: Lintukuja 12 A")
    if city == "Vantaa":
        print("Aikuisten tervisehuolto osoiteessa: Mikonkatu 43 B")

if age >= 18:
    print("Aikuisia koskevat terveydenhuollon ohjeet.")
else:
    print("Alaikäisten terveydenhuollon ohjeet.")
