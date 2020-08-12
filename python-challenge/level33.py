# http://www.pythonchallenge.com/pc/rock/beer.html

# Page source has comment
# If you are blinded by the light,
#   The brightest pixel move other pixels to random places
# remove its power, with its might.
#   Remove the brightes pixel and the next brightest
# Then from the ashes, fair and square,
#   The noise that is left, can be put into a square with another brightest pixel
# another truth at you will glare.
#   Will look like another letter
# Hint is 138 character long, same as width and height of beer2.png

# Link to image beer1.jpg
# Change to beer2.jpg says that no, png
# Download beer2.png

# Title '33 bottles of beer on the wall'
#   Repeat for 33 times

from PIL import Image
import math

# Open image
im = Image.open('./resource/beer2.png')
# Get data
data = list(im.getdata())

out = None
# Repeat 33 times
for i in range(33):
    # Find max pixel value
    maxVal = max(data)
    # Remove brightest pixel
    data = [(x, 255)[x == maxVal] for x in data if x < maxVal - 1]
    print(len(data))
    l = int(math.sqrt(len(data)))
    # Output image with data without the brightest pixel
    out = Image.new('L', (l, l))
    out.putdata(data)
    out.show()
    input()
# xxxxxxxxxxxvine_ga_rwin_e_mo_ld_i_no_slo
# We only focus on letter with a box surrounding them
# Answer: gremlins
