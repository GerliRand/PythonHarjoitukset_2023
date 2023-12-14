# sama loogikka kuin edelisessä 2

print("Aloitettaan ohjelma!")

# viisi henkilö silmukassa
for person in range(5):
    print(f"Henkilön {person + 1} vuoro puhua!")   # person + 1 taí range(1, 6)

    # jokaisen henkilön pitää sanoa vuorollaan numerot 1-4
    for number in range(4):
        print(f"\t Henkilö {person + 1} sanoo numeron {number + 1}!")

print("Kaikki ovat puhuneet")
