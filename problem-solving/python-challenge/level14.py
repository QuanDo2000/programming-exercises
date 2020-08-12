# http://www.pythonchallenge.com/pc/return/italy.html
# Page source has hint
# remember: 100*100 = (100+99+99+98) + (...
# Title of page is 'walk around'
# Image of page is spiral in clockwise direction
from PIL import Image

# Image from page source
im = Image.open('./resource/wire.png')
# Real size is 10000*1
# Use pixels to create a 100 * 100 img

# Map moving direction
delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]
# Var to store output image
out = Image.new('RGB', [100, 100])
x, y, p = -1, 0, 0
# Start d at 200, which is 100 * 2
d = 200

while d / 2 > 0:
    for v in delta:
        steps = d // 2
        for s in range(steps):
            x, y = x + v[0], y + v[1]
            out.putpixel((x, y), im.getpixel((p, 0)))
            p += 1
        d -= 1
# Output image
out.save('./output/level14_out.jpg')
# Image shows a cat
# cat page says 'and its name is uzi. you'll hear from him later.'
# Answer: uzi
