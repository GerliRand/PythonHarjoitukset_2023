# osateksin esimerkki
text = input("Anna jotain tekstiä:\n")

# tulosta teksin ensimmäisestä merkistä kymmneeseen
subtext1 = text[0:10]
print(subtext1)

# tulosta teksin kuudennesta merkistä viidentoista merkkiin
subtext2 = text[5:15]
print(subtext2)

# tulosta viisi viimeistä merkkiä
subtext3 = text[-5:]
print(subtext3)

# tulosta kaikki merkit viidenen merkin jälkeen
subtext4 = text[5:]
print(subtext4)
