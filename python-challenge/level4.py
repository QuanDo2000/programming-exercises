# http://www.pythonchallenge.com/pc/def/linkedlist.php

import re
import requests

# URL of the image on web page
url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={}'
# First nothing number shown
number = 12345
# Loop through nothings
while True:
    # Get page content
    page = requests.get(url.format(number))
    # Search for next nothing
    match = re.search('the next nothing is (\d+)', page.text)
    if match != None:
        number = int(match.group(1))
    else:
        print(page.text)
        # User input at pages where there is no number
        cont = input('Continue? y/n ')
        if cont.lower() == 'n':
            break
        else:
            number /= 2
    print(page.text)

print(page.text)
# Answer: peak.html
