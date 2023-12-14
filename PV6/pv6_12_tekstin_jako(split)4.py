# esimerkki, jos on kaksi erotinmerkkiä (-) tunnisteessa

code = "JOTAIN133-20456-123456-123A"

# tämä tilanne on haastava, koska datan sisällä on käytössä sama merkki
# kuin merkki mitä käytettään erottimena

# tapa1: erotellaan ensin kaikki ja sitten liimataan viimeiset kaksi yhteen (123456 ja 123A)
# hyvä erotin olisi tolppa |

parts = code.split("-")
print(parts)

first = parts[0]
second = parts[1]
security_number = parts[2] + "-" + parts[3]    # liimataan yhteen

print(first)
print(second)
print(security_number)