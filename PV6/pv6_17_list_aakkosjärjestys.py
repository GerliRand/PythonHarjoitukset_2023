berries = ["Mustikka", "hilla", "Karpalo", "Mansikka"]
print(berries)

# lista aakkosjärjestykseen
berries.sort()
print(berries)

# opettaja suosittele tätä!
berries = sorted(berries)
print(berries)

# jos halutaan, että kirjankoko ei haitta, silloin näin!!!
berries.sort(key=lambda v: v.upper())
print(berries)