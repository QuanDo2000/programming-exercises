# http://www.pythonchallenge.com/pc/def/oxygen.html

from PIL import Image
import requests
from io import BytesIO
import re

# Get image from page
img = Image.open(BytesIO(requests.get(
    'http://www.pythonchallenge.com/pc/def/oxygen.png').content))

# Get pixels in middle row, row with black, white boxes
row = [img.getpixel((x, img.height / 2)) for x in range(img.width)]
# Get only boxes that are grayscale => r == g == b
# Boxes are 7 pixels wide => [::7]
row = [r for r, g, b, a in row[::7] if r == g == b]
# Each pixel index in row can be translate into a character
# Get a sentence 'smart guy, you made it. the next level is [105, 110, 116, 101, 103, 114, 105, 116, 121]'
# Get all numbers in sentence and translate into character again
nums = map(int, re.findall('\d+', ''.join(map(chr, row))))
print(''.join(map(chr, nums)))
# Answer: integrity
