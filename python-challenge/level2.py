# http://www.pythonchallenge.com/pc/def/ocr.html

import re

# Text got from page source
raw = open('./resource/level2.txt', 'r').read()

# Find rare characters
# Delete all non characters
text = re.sub(r'[^a-z]', "", raw)
print(text)
# Answer: equality
