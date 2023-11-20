# Pillow moduli esimerkki
from PIL import Image, ImageDraw

# luodaan uusi kuva, koko: 100 x 30
# värit - rgb
img = Image.new('RGB', (500, 300), color=(73, 109, 137))

# alustetaan piirto-objekti
d = ImageDraw.Draw(img)

# piirretään tekstiä
# kordinaadit alkaa aina vasemmasta yläkulmasta
d.text((120, 80), "Hello World", fill=(255, 255, 0))

# piiretään ympyrä
# xy - aloituspiste on kohdassa 100, 100 - oikea alanurkka on kohdassa 200, 200
d.ellipse((100, 100, 200, 200), fill=(192, 102, 217), outline=(0, 0, 0))

# tallennetaan lopputulos tiedostoon (eli luo uuden tiedostoon)
img.save('pil_text.png')
