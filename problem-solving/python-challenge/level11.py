# http://www.pythonchallenge.com/pc/return/5808.html

from PIL import Image
from io import BytesIO
import requests

# Image from page source
im = Image.open('./resource/cave.jpg')
(w, h) = im.size

# Hint odd, even
# Create 2 new images
even = Image.new('RGB', (w // 2, h // 2))
odd = Image.new('RGB', (w // 2, h // 2))

# Seperate the original image into 2
# Criteria is whether pixel is at odd or even position
for i in range(w):
    for j in range(h):
        p = im.getpixel((i, j))
        if (i + j) % 2 == 1:
            odd.putpixel((i // 2, j // 2), p)
        else:
            even.putpixel((i // 2, j // 2), p)

# Show both images
even.show()
odd.show()
# One image has a word
# Answer: evil
