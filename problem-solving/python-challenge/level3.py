# http://www.pythonchallenge.com/pc/def/equality.html

import re

# Text got from page source
raw = open('./resource/level3.txt', 'r').read()

# Find occurences of 1 lowercase surrounded by exactly 3 uppercase on each side.
text = re.findall('[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+', raw)
print(''.join(text))
# Answer: linkedlist
# Shows linkedlist.php, replace that into web page
