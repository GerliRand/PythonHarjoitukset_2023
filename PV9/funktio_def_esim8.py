# importtaa funktions.py tiedostosta kaikki (eli * tarkita kaikki)
from functions import *

numbers = [5, 8, 5, 4, 9, 10, 10, 9]
grades = [1, 5, 4, 1, 1, 5, 5, 3, 4]
temperatures = [-5.5, -4, 2, 11, 4.2, 18.2, 22.8]

# lasketaan numeroiden keskiarvo
avg_numbers = get_list_average(numbers)
print(avg_numbers)

# lasketaan arvosanojen keskiarvo
avg_grades = get_list_average(grades)
print(avg_grades)

# lasketaan lämpötiljojen keskiarvo
avg_temperatures = get_list_average(temperatures)
print(avg_temperatures)