import math

# kaksi tapaa potenssiin korotuksiin (ruut, kuup jne)
# tapa 1
total_1 = math.pow(5, 7)
print(total_1)
# tapa 2 (tämä on pythonin oma ja tulosta vastauksen ilman desimaaleja)
total_2 = 5 ** 7
print(total_2)

# neliöjuuri, eli square root => sqrt
value = 9
root_value = math.sqrt(value)
print(root_value)

# kuution halkaisija / kulmasta kulmaan
side = 20
diameter = side * math.sqrt(3)
