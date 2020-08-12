# http://www.pythonchallenge.com/pc/return/balloons.html
# Title 'can you tell the difference?'
# Page has 2 images with different brightness
# Go to http://www.pythonchallenge.com/pc/return/brightness.html
# Same 2 pics but source code has message 'maybe consider deltas.gz'
# Download file deltas.gz, username: huge, password: file

# File has .gz
import gzip
import difflib

# Inside has 1 text file
# Data has 2 columns
data = gzip.open('./resource/deltas.gz')
d1, d2 = [], []
# Need to decode after reading
# 1st column stops at 53, 2nd columns starts at 56
for line in data:
    d1.append(line[:53].decode() + '\n')
    d2.append(line[56:].decode())

# Compare 2 columns
compare = difflib.Differ().compare(d1, d2)

# Create files to store data
f0 = open('./output/level18_f0.png', 'wb')
f1 = open('./output/level18_f1.png', 'wb')
f2 = open('./output/level18_f2.png', 'wb')


for line in compare:
    # Line index 0 contains compare result => '+' or '-' or ' '
    # Line starts at index 2 => [2:]
    # Remove extra spaces from line => strip().split(' ')
    # Convert each value into hexadecimal => int(o, 16)
    # Finally convert to bytes to write to file
    bs = bytes([int(o, 16) for o in line[2:].strip().split(' ') if o])

    # Write each result into different files
    if line[0] == '+':
        f1.write(bs)
    elif line[0] == '-':
        f2.write(bs)
    else:
        f0.write(bs)

# Close files
f0.close()
f1.close()
f2.close()
# f0 shows '../hex/bin.html'
# f1 shows 'butter'
# f2 shows 'fly'
# Answer: http://www.pythonchallenge.com/pc/hex/bin.html
# Username: butter
# Password: fly
