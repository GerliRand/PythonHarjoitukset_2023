import json

file_handle = open("app_data.json", "r")
content = file_handle.read()
file_handle.close()

# muutetaan json data python dataksi
city = json.loads(content)

# nyt on python dictionary ja voidaan tulostaa
print(city)
print(city["population"])
