# Pillow moduli esimerkki
from PIL import Image, ImageDraw

# luodaan uusi kuva, koko: 100 x 30
img = Image.new('RGB', (100, 40), color=(73, 109, 137))

# alustetaan piirto-objekti
d = ImageDraw.Draw(img)

# piirretään tekstiä
# kordinaadit alkaa aina vasemmasta yläkulmasta
d.text((10, 10), "Hello World", fill=(255, 255, 0))

# tallennetaan lopputulos tiedostoon (eli luo uuden tiedostoon)
img.save('pil_text.png')
