# http://www.pythonchallenge.com/pc/hex/copper.html
# Page source says 'or maybe white.gif would be more bright'

from PIL import Image, ImageDraw

# white.gif downloaded from http://www.pythonchallenge.com/pc/hex/white.gif
# white.gif is almost all black, with 1 pixel with (8, 8, 8)
# Only 1 pixel has different color
# The pixel is moving in the white.gif
# Need to emulate the joystick
img = Image.open('./resource/white.gif')
# Variable to store new image
new = Image.new('RGB', (500, 200))
draw = ImageDraw.Draw(new)
# Set first point to start at the edge of image
cx, cy = 0, 100
# Read all frames in white.gif
for frame in range(img.n_frames):
    # Get frame
    img.seek(frame)
    # getbbox() get black box boundary
    left, upper, right, lower = img.getbbox()

    # Calculates the position of the non-black pixel
    # Set movement direction accordingly
    dx = left - 100
    dy = upper - 100

    # If black pixel is reset to original position
    # Move cursor 50 pixels to the right for more space
    if dx == dy == 0:
        cx += 50
        cy = 100
    # Move cursor according to dx, dy
    cx += dx
    cy += dy
    # Draw point at cursor
    draw.point([cx, cy])

# Show image
new.show()
# Answer: bonus
