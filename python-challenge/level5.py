# http://www.pythonchallenge.com/pc/def/peak.html

import requests
# Pronounce peak hell sounds like pickle
import pickle

# Web page from original page source
page = requests.get('http://www.pythonchallenge.com/pc/def/banner.p')
# Use pickle to read data from page
data = pickle.loads(page.text.encode('utf-8'))
# data is lists of lists of tuples with format (character, length)

# Loop for each list in data and print out character * length
for line in data:
    print(''.join([k * v for k, v in line]))
# Answer: channel
