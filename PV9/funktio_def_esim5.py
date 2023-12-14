# importtaa funktions.py tiedostosta kaikki (eli * tarkita kaikki)
from functions import *

word = input("Anna jokin sana:\n")

palindrome = check_palidrome(word)

# funktion tuloksen perusteella ilmoitetaan käyttäjälle onko palidromi
if palindrome:
    print("Palindromi")
else:
    print("Ei ole palindromi")