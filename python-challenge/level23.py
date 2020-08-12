# http://www.pythonchallenge.com/pc/hex/bonus.html
# There are 3 comments in page source

# First comment
# todo: do you owe someone an apology? now it is a good time to
# tell him that you are sorry. Please show good manners although
# it has nothing to do with this level.

# Second comment
# it can't find it. this is an undocumented module.

# Third comment
# 'va gur snpr bs jung?'

# Import module this
import this
# Prints out text
import codecs

string = 'va gur snpr bs jung?'

# Text is stored in this.s but rotated by 13 characters
# Use codecs to decode text
print()
print(codecs.decode(string, 'rot-13'))
print()
# 'in the face of what?'
# From the text: 'In the face of ambiguity'
# Answer: ambiguity
