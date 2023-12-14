from datetime import datetime

# haetaan aikaleima kellonajan kanssa
today = datetime.now()
print(today)

# tulostettaan aika formatissa: PV.KK.VVVV HH:MM:SS
# pelkkä pvm, anna ainostaan ("%d.%m.%Y")
date_text = today.strftime("%d/%m/%Y %H:%M:%S")
print(date_text)
