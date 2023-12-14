# mitä tehdään silloin kuin käytetään kahte eri välimerkkiä
# miten käytettään split():ä
code = "TILAUS12354_A13654*2023"

# halkaistaan ensin koko koodi alaviivalla
# lopputuloksena:
# 0 => TILAUS12354
# 1 => A13654*2023
parts = code.split("_")
# ensimmäinen elementti on ok, pistetään talteen
first = parts[0]

# indeksi 1 => tässä on jäljellä vielä *:llä jaottelu
subcode = parts[1]
# pilkotaan jäljellä oleva koodi *:n perusteella
subparts = subcode.split("*")

# tallennetaan omiin muuttujiin
second = subparts[0]
year = subparts[1]

print(first)
print(second)
print(year)