# http://www.pythonchallenge.com/pc/ring/bell.html
# Picture of jungle
# Description 'RING-RING-RING say it out loud'
# Go to http://www.pythonchallenge.com/pc/ring/green.html
# Content 'yes! green!'

from PIL import Image

# Open image downloaded from web page
im = Image.open('./resource/bell.png')

# Get green values
green = list(im.split()[1].getdata())
# Green values has light and dark alternating

# Get difference every two values
diff = [abs(a - b) for a, b in zip(green[0::2], green[1::2])]
# Most of green values has light and dark different by 42

# Filter out only the non 42 values
filtered = list(filter(lambda x: x != 42, diff))

# Print out different values as decoded bytes
print(bytes(filtered).decode())
# 'whodunnit().split()[0] ?'
# Python developer: 'Guido van Rossum'
# Answer: guido
