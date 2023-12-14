text = input("Opiskelija tai aikuinen? (o/a):\n")

# muutetaan syötetty teksti pieneksi, eli iso A ja O myös toimi
text = text.lower()

if text == "a":
    print("Aikuinen")
elif text == "o":
    print("Opiskelija")
else:
    print("Väärä valinta...")