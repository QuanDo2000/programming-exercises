# Level 21 is inside /output/level20.zip
# Extract package.pack in zip to ./resource/

import zlib
import bz2

# Create variable to store logs
result = ''
# Open file to read
with open('./resource/package.pack', 'rb') as f:
    # Read line
    data = f.read()

# Unzip data according to type
# Reverse data if data is in reverse
while True:
    if data.startswith(b'x\x9c'):
        data = zlib.decompress(data)
        result += ' '
    elif data.startswith(b'BZh'):
        data = bz2.decompress(data)
        result += '#'
    elif data.endswith(b'\x9cx'):
        data = data[::-1]
        result += '\n'
    else:
        break
print(data)
# Data prints out 'sgol ruoy ta kool'
# 'look at your logs'
print(result)
# Answer: copper
