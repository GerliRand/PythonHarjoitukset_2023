humidity = 92
temperature = 15
raining = False

# jos kosteus on yli 80%, silloin raining on True
if humidity > 80:
    raining = True

# jos lämpötila on alla 0, niin ei ole vesisadetta
if temperature < 0:
    raining = False

if raining:
    print("Sataa vettä!")
else:
    print("Ei sada!")
