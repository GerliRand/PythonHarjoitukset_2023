text = input("Anna joko numero tai tekstiä:\n")

if text.isnumeric():
    print("Annoit numeron.")
    number = int(text)
    print(number)
else:
    print("Annoit tekstiä!")