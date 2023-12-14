# tekstin korvaaminen

drinks = "kahvi, mehu, tee, cola"
print(drinks)

# korva mehu sanalla fanta
drinks = drinks.replace("mehu", "fanta")
print(drinks)
print()

# toinen tapa, pilku asenetaan rivin vaidolla
new_drinks = drinks.replace(", ", "\n")
print(new_drinks)
print()

# sanan etsiminen tekstistä (käytä tässä viimeistä drink muuttuja)
user_text = input("Mitä juomaa haluat:\n")
if user_text in drinks:
    print("Löytyi!")
else:
    print("Ei löytynyt...")