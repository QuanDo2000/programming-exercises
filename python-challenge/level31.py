# http://www.pythonchallenge.com/pc/ring/grandpa.html
# Picture of a rock
# Search google get 'kohsamui' in 'thailand'
# Username: kohsamui
# Password: thailand
# Image of mandelbrot set
# Info left="0.34" top="0.57" width="0.036" height="0.027"
# iterations="128"

from PIL import Image

# Open image downloaded from web page
img = Image.open('./resource/mandelbrot.gif')

# Store values
left = 0.34
top = 0.57
width = 0.036
height = 0.027
iterations = 128
# Get image size
w, h = img.size
# Get step
xstep = width / w
ystep = height / h

# Var to store result
result = []

# Mandelbrot loop with reversed y direction
for y in range(h - 1, -1, -1):
    for x in range(w):
        c = complex(left + x * xstep, top + y * ystep)
        z = 0 + 0j
        for i in range(iterations):
            z = z * z + c
            if abs(z) > 2:
                break
        result.append(i)

# Copy to img2
img2 = img.copy()
img2.putdata(list(result))
# img2.show()

# Get all diferences between 2 imgs
diff = [(a - b) for a, b in zip(img.getdata(), img2.getdata()) if a != b]
length = len(diff)
# Get factors of the length of differences
factors = [x for x in range(2, length // 2) if length % x == 0]
# print(factors)
# [23, 73]

# Create new image with dimension as factors
plot = Image.new('L', (23, 73))
plot.putdata([(i < 16) and 255 or 0 for i in diff])
plot.resize((230, 730)).show()
# Image shows arecibo message
# Answer: arecibo
