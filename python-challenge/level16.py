# http://www.pythonchallenge.com/pc/return/mozart.html
# Page has image with similar pink stripes

from PIL import Image, ImageChops
import numpy as np

# Get image from source page
image = Image.open('./resource/mozart.gif')
# Shift all pixel at index(195), which is pink
# Shift all to 1 position
shifted = [bytes(np.roll(row, -row.tolist().index(195)).tolist())
           for row in np.array(image)]
# Draw image from shifted data
Image.frombytes(image.mode, image.size, b''.join(shifted)).show()
# Answer: romance
