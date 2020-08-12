# http://www.pythonchallenge.com/pc/return/romance.html
# Page has cookie image
# In the corner has image from level 4, the next nothing level
# Go into developers screen > Application > Cookies
# Cookie name 'info' has value 'you+should+have+followed+busynothing...'

# Part 1
from urllib.request import urlopen, Request  # Part 3: Request
from urllib.parse import unquote_plus, unquote_to_bytes, quote_plus  # Part 3: quote_plus
import re
import bz2
# Part 2
from xmlrpc.client import ServerProxy


"""
# First number of nothing in level 4
num = 12345
info = ''
while True:
    # Open page
    page = urlopen(
        'http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing={}'.format(num))
    # Get data
    raw = page.read().decode('utf-8')
    print(raw)
    # Get cookie from page
    cookie = page.getheader('Set-Cookie')
    # Search for info of cookie
    value = re.search('info=(.*?);', cookie).group(1)
    # Add value of cookie to info
    info += value
    # Find next busynothing
    match = re.search('next busynothing is (\d+)', raw)
    if match == None:
        break
    else:
        # Set new busynothing
        num = match.group(1)

# Translate unquote to bytes, replace + with ' '
res = unquote_to_bytes(info.replace('+', ' '))
print(res)
# Use bz2 to decompress res
print(bz2.decompress(res), end='\n\n')
# Get sentence 'is it the 26th already? call his father and inform him that "the flowers are on their way". he\'ll understand.'
# 'call' => Use phonebook.php in level 13
# His father => Mozart's father
"""

"""
# Part 2
# Using phonebook to call Leopold, Mozart's father
conn = ServerProxy('http://www.pythonchallenge.com/pc/phonebook.php')

print(conn.phone('Leopold'), end='\n\n')
# Get '555-VIOLIN'
# If web page http://www.pythonchallenge.com/pc/return/violin.html
# Get 'no! i mean yes! but ../stuff/violin.php.'
# New page http://www.pythonchallenge.com/pc/stuff/violin.php
"""

# Part 3
url = 'http://www.pythonchallenge.com/pc/stuff/violin.php'
msg = 'the flowers are on their way'
# Send request with message in cookie info
req = Request(url, headers={'Cookie': 'info=' + quote_plus(msg)})
# Find message
print(re.search('<br><br>\s(.*)</font>', urlopen(req).read().decode()).group(1))
# Message 'oh well, don't you dare to forget the balloons.'
# Answers: balloons
