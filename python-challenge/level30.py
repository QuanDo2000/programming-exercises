# http://www.pythonchallenge.com/pc/ring/yankeedoodle.html
# Page source has comment 'while you look at the csv file'
# Download csv file from web page

from PIL import Image
import math

# Read data from file
with open('./resource/yankeedoodle.csv') as f:
    # Read data from csv file
    data = [x.strip() for x in f.read().split(',')]
    # Get amount of data
    length = len(data)
    # 7367

factors = [x for x in range(2, length // 2) if length % x == 0]
# Get values that are a factors of length of data

# Put values in image
img = Image.new('F', (53, 139))
img.putdata([float(x) for x in data], 256)
# Transpose image for right orientation
img = img.transpose(Image.FLIP_LEFT_RIGHT)
img = img.transpose(Image.ROTATE_90)
# img.show()
# Get formula n = str(x[i])[5] + str(x[i])[5] + str(x[i])[6]

# Temp lists
a = data[0::3]
b = data[1::3]
c = data[2::3]

# Read data according to instruction on image
res = bytes([int(x[0][5] + x[1][5] + x[2][6]) for x in zip(a, b, c)])
print(res[:200])
# Get 'So, you found the hidden message.\nThere is lots of room here
# for a long message, but we only need very little space to say
# "look at grandpa", so the rest is just garbage. ...'
# Answer: grandpa
