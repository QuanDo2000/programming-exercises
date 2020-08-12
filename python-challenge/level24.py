# http://www.pythonchallenge.com/pc/hex/ambiguity.html
# Has image of a maze
# Title 'from top to bottom'

from PIL import Image

# Open maze.png from web page
maze = Image.open('./resource/maze.png')
# Possible movement directions
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
# Value of white pixel
white = (255, 255, 255, 255)
w, h = maze.size

# Print out first row
# for i in range(w):
#     print(maze.getpixel((i, 0)))
# Almost all is white pixels, except 1 at (w - 2, 0)

# Print out last row
# for i in range(w):
#     print(maze.getpixel((i, h-1)))
# Almost all white pixel, except 1 at (1, h - 1)

# If print out inner pixels
# All non-white points will have format (x, 0, 0, 255)
# Find all x from the shortest path through maze
# Put all x into file

nextMap = {}

entrance = (w - 2, 0)
dest = (1, h - 1)

# Start queue from destination
queue = [dest]
# Loop until end of queue
while queue:
    # Remove from queue
    pos = queue.pop()
    # If current position is entrance, break
    if pos == entrance:
        break
    # Check viability in each direction and add in queue if viable
    for d in directions:
        tmp = (pos[0] + d[0], pos[1] + d[1])
        if not tmp in nextMap and 0 <= tmp[0] < w and 0 <= tmp[1] < h and maze.getpixel(tmp) != white:
            nextMap[tmp] = pos
            queue.append(tmp)

# Search for shortest path
path = []
while pos != dest:
    path.append(maze.getpixel(pos)[0])
    pos = nextMap[pos]

# Skip the 0s in the path list
print(path[1::2])
# Output to level24_maze.zip
open('./output/level24_maze.zip', 'wb').write(bytes(path[1::2]))
# In zip file there is a picture maze.jpg
# In picture has a word
# Answer: lake
