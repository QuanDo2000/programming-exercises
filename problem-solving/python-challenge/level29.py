# http://www.pythonchallenge.com/pc/ring/guido.html
# Title 'silence!'
# Source page has empty lines with varying lengths

from urllib.request import Request, urlopen
import bz2
import base64

# Make request to page
req = Request('http://www.pythonchallenge.com/pc/ring/guido.html')
# Add authorization
req.add_header('Authorization', 'Basic {}'.format(
    base64.b64encode(b'repeat:switch').decode()))
# Get only the blank lines => [12::]
raw = urlopen(req).read().splitlines()[12:]
# Convert length into int and int into char
data = bytes([len(i) for i in raw])
# Decompress data to get content
print(bz2.decompress(data))
# Get 'Isn't it clear? I am yankeedoodle!'
# Answer: 'yankeedoodle'
