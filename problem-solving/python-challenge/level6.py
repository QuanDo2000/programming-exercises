# http://www.pythonchallenge.com/pc/def/channel.html

# Hint zip file from source page, next to <html>
import zipfile
import re

# Zip file got from changing the web page to ...channel.zip
f = zipfile.ZipFile('./resource/channel.zip')
# Number from readme.txt file in zip
num = 90052
# Create list to save comments
comments = []
# Loop through all files in sequence
while True:
    # Get file content
    content = f.read(str(num) + '.txt').decode('utf-8')
    # Get comments from each file read
    comments.append(f.getinfo(str(num) + '.txt').comment.decode('utf-8'))
    print(content)
    # Find next nothing in content
    match = re.search('nothing is (\d+)', content)
    if match == None:
        break
    num = match.group(1)
    # Final content is 'Collect the comments'

# Comment is list of characters
# Join comments to get answer
print(''.join(comments))
# Image spells hockey
# Page says: it's in the air. look at the letters.
# The word hockey in image is made up of characters.
# Answer: oxygen
