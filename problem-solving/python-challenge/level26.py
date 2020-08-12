# http://www.pythonchallenge.com/pc/hex/decent.html
# Has description under image 'Hurry up, I'm missing the boat'
# Title 'be a man - apologize'
# Page source has comment 'you've got his email'

# Send email apologizing to leopold.moz@pythonchallenge.com
# Response
# Never mind that.
# Have you found my broken zip?
# md5: bbb8b499a0eef99b52c7f13f4e78c24b
# Can you believe what one mistake can lead to?

import hashlib

# Store md5 hash code
md5code = 'bbb8b499a0eef99b52c7f13f4e78c24b'
# Read corrupted zip data
data = open('./output/level24_maze/mybroken.zip', 'rb').read()

# Find the one CRC error
# Trying all one-byte substitution
# If matches md5 hash then return result in new zip file
for i in range(len(data)):
    for j in range(256):
        newData = data[:i] + bytes([j]) + data[i+1:]
        if hashlib.md5(newData).hexdigest() == md5code:
            open('./output/repaired.zip', 'wb').write(newData)

# Zip file has image with word 'speed'
# Remember description in web page 'Hurry up, I'm missing the boat'
# Answer: speedboat
