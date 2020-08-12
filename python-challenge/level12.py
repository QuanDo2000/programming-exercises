# http://www.pythonchallenge.com/pc/return/evil.html
# Page source leads to evil1.jpg
# Change that to evil2.jpg, image says 'not jpg, .gfx'
# Try evil3.jpg => image says 'no more evils...'
# Try evil4.jpg => nothing or error
# If Bash => curl -u hugh:file http://www.pythonchallenge.com/pc/return/evil4.jpg
# Get 'Bert is evil! go back!'

# evil2.gfx download from changing to gfx
data = open('./resource/evil2.gfx', 'rb').read()
print(data)
# Original image (evil1.jpg) is showing cards being dealt in 5
for i in range(5):
    # Write out 5 files in bytes => 'wb'
    open('./output/level12_%d.jpg' % i, 'wb').write(data[i::5])
# 5 images spells a word
# Answer: disproportional
