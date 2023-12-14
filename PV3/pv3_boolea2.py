# Boolean-muuttuja esimerkki

# TEHTÄVÄNANTO:
# Tehdään ohjelma, joka päättelee muuttujista, onko ulkona HYVÄ tai HUONO sää
# Huono sää: jos lämpötila on alle +10 c
# Huono sää: jos kosteusprosentti on yli 80%
# Huono sää: jos tuulennopeus on yli 2.5 m/s
# Huono sää: jos ulkona on pimeää
# Tässä tapauksessa ulkona on pimeää, jos klo 20-24 tai 0-7

good_weather = True

# nämä muuttujat voidaan kysyä käyttäjältä (input-in avulla), tässä annettu valmiiksi
temperature = 15
humidity = 32
wind_speed = 1.4
time = 18

# apu-muuttujat, eli milloin aurinko laske ja milloin nouse
sun_down = 20
sun_rise = 7

# yhdellä if lausella menee usein sotkuiseksi, eimerkki:
#if temperature < 10 or humidity > 80 or wind_speed > 2.5 or (time > sun_down ...):

if temperature < 10:
    good_weather = False
if humidity > 80:
    good_weather = False
if wind_speed > 2.5:
    good_weather = False
if time > sun_down or time < sun_rise:
    good_weather = False


if good_weather:
    print("Hyvä sää.")
else:
    print("Huono sää!")