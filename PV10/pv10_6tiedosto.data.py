import json

# python dictionary - phone
phone = {
    "name": "Nokia 3310",
    "release_year": 2000,
    "battery": "1000mAh",
    "camera": False,
    "weight": 133
}

# python data muutetaan json-formattiin (eli tekstiksi)
# HUOM: python data ei voi suoraan tallentaa
content = json.dumps(phone)

# tallennetaan json tiedostona
file_handle = open("nokiaphone.json", "w")
file_handle.write(content)
file_handle.close()

print("Kiitos puhelimen tallentamisesta!")