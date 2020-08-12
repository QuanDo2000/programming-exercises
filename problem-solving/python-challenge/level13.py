# http://www.pythonchallenge.com/pc/return/disproportional.html

import xmlrpc.client

# phonebook.php from page source
# Page is an XML so use xmlrpc.client
conn = xmlrpc.client.ServerProxy(
    'http://www.pythonchallenge.com/pc/phonebook.php')
# Bert from evil4.jpg in last level
print(conn.phone('Bert'))
# Phone Bert got '555-ITALY'
# Answer: italy
