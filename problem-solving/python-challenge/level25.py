# http://www.pythonchallenge.com/pc/hex/lake.html
# Has image of a puzzle with 25 pieces => 25 files
# Page source has hint 'can you see the waves' => wav files
# Title is 'imagine how they sound' => make into image

import urllib.request as urlrequest
import wave
from PIL import Image

"""
# Uncomment to download all files
# Add authentication to page request
topUrl = 'http://www.pythonchallenge.com/pc/hex/'
# Add username and password
passMan = urlrequest.HTTPPasswordMgrWithDefaultRealm()
passMan.add_password(None, topUrl, 'butter', 'fly')
# Create handler and opener
handler = urlrequest.HTTPBasicAuthHandler(passMan)
opener = urlrequest.build_opener(handler)

# Get 25 wav files from url
# Must use this way because can't use urlretrieve
url = 'http://www.pythonchallenge.com/pc/hex/lake{}.wav'
for i in range(1, 26):
    # Get page content
    page = opener.open(url.format(i))
    # Write page content to file
    with open('./resource/level25_lake{}.wav'.format(i), 'wb') as f:
        f.write(page.read())
"""

# Read all wavs file
wavs = [wave.open('./resource/level25_lake{}.wav'.format(i))
        for i in range(1, 26)]
# Create new image to store result
result = Image.new('RGB', (300, 300), 0)
# Get amount of frames
num_frames = wavs[0].getnframes()
# Generate small image from each wav file
for i in range(len(wavs)):
    # Get data
    byte = wavs[i].readframes(num_frames)
    # Generate image
    img = Image.frombytes('RGB', (60, 60), byte)
    # Paste all small image into one big image in specific order
    # Fill each line in order from left to right
    result.paste(img, (60 * (i % 5), 60 * (i // 5)))

# Save big image to output file
result.save('./output/level25.png')
# Answer: decent
