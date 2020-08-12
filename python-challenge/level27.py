# http://www.pythonchallenge.com/pc/hex/speedboat.html
# Page source has comment 'did you say gif?' next to zigzag.img
# Download zigzag.gif to ./resource/

import keyword
from PIL import Image
import bz2

# Read image zigzag.gif
im = Image.open('./resource/zigzag.gif')
# Get palette of image
# Since R == G == B so only need to get R values
palette = im.getpalette()[::3]
# Make translation table
table = bytes.maketrans(bytes([i for i in range(256)]), bytes(palette))
# Get raw data
raw = im.tobytes()
# Get translated data
trans = raw.translate(table)
# Place all data in a list of tuples
zipped = list(zip(raw[1:], trans[:-1]))
# Sort out all the tuples that contains different data
diff = list(filter(lambda p: p[0] != p[1], zipped))
# Get the index of the different data
indices = [i for i, p in enumerate(zipped) if p[0] != p[1]]

# Create new image
im2 = Image.new('RGB', im.size)
# Fill image with white
colors = [(255, 255, 255)] * len(raw)
# Color the index of different data a different color
for i in indices:
    colors[i] = (0, 0, 0)
# Draw image
im2.putdata(colors)
# Image shows 'not keyword', and 'busy?'

# The different data spells out a compressed zip file
s = [t[0] for t in diff]
# Get the text
text = bz2.decompress(bytes(s))
# Text contains a lot of python keywords and '../ring/bell.html'

# Print out all words which are not keywords in python
print(set([w for w in text.split() if not keyword.iskeyword(w.decode())]))
# Result is 'exec', 'repeat', 'print', 'switch', '../ring/bell.html'
# Since I'm using python 3, 'exec' and 'print' is no longer a keyword
# The only two left is 'repeat' and 'switch'
# Username: repeat
# Password: switch
