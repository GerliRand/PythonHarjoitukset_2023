# kokelmat kokelman sisällä eli lista listassa
book = {
    "name": "My Lady Jane",
    "year": 2016,
    "publisher": {
        "name": "HarperTeen",
        "organization": "HarperCollins Publishers",
        "location": "New York"
        }
    }
# jos halutaan tulostaa arvo
print(book["name"])

# vaihtoehto 1
# tallentaa omaan apumuutujaan
publisher = book["publisher"]
print(publisher["organization"])

# vaihtoehto 2 - TYKKÄÄN TÄSTÄ!
# eli book->publisher->organization
print(book["publisher"]["organization"])
