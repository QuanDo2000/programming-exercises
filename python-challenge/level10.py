# http://www.pythonchallenge.com/pc/return/bull.html
# Page says 'len(a[30]) = ?'
# Page source has sequence.txt
# a = [1, 11, 21, 1211, 111221,
# Look-and-say sequence

import re

# First number in sequence
x = '1'
# Loop for 30 times cause len(30)
for _ in range(30):
    # findall returns a tuple with (number, length - 1)
    # (\d) to search number, (\1*) is for the first group repeated
    # so next number is length, number
    x = ''.join([str(len(i + j)) + i for i, j in re.findall(r'(\d)(\1*)', x)])
    print(x)

print(len(x))
# Answer: 5808
