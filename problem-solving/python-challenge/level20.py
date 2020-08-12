# http://www.pythonchallenge.com/pc/hex/idiot2.html

import urllib.request as urlreq
import base64
import re

# Make connection to web page
request = urlreq.Request('http://www.pythonchallenge.com/pc/hex/unreal.jpg')
# Add in credentials username:password
cred = base64.b64encode(b'butter:fly')
# Add credentials to request header
request.add_header('Authorization', 'Basic {}'.format(cred.decode()))
print(request.headers)
# {'Authorization': 'Basic YnV0dGVyOmZseQ=='}

# Get response from page
response = urlreq.urlopen(request)
print(response.headers)
# Content-Type: image/jpeg
# Content-Range: bytes 0-30202/2123456789
# Connection: close
# Transfer-Encoding: chunked
# Date: Fri, 20 Sep 2019 19:30:58 GMT
# Server: lighttpd/1.4.35

# Huge file of length 2123456789
# Ranage from 0-30202

# Compile regex pattern
pattern = re.compile('bytes (\d+)-(\d+)/(\d+)')

while True:
    try:
        # Get content-range from header
        contentRange = response.headers['content-range']
        # Get byte start, end and length
        (start, end, length) = pattern.search(contentRange).groups()
        # Set new range in header
        request.headers['Range'] = 'bytes={}-'.format(int(end) + 1)
        # Make request to web page again
        response = urlreq.urlopen(request)
        # Print message from page
        print(response.read().decode())
        print(response.headers)
    except:
        break
# Result
# (30203-30236) Why don't you respect my privacy?
# (30237-30283) we can go on in this way for really long time.
# (30284-30294) stop this!
# (30295-30312) invader! invader!
# (30313-30346) ok, invader. you are inside now.

# Get content after the length
request.headers['Range'] = 'bytes={}-'.format(int(length) + 1)
response = urlreq.urlopen(request)
print(response.read().decode())
print(response.headers)
# (2123456744 - 2123456788)
# Get message 'esrever ni emankcin wen ruoy si drowssap eht'
# Reversed becomes 'the password is your new nickname in reverse'
# Nickname is 'invader' => 'redavni'

# Now reverse the search
request.headers['Range'] = 'bytes={}-'.format(2123456743)
response = urlreq.urlopen(request)
print(response.read().decode())
print(response.headers)
# (2123456712-2123456743)
# 'and it is hiding at 1152983631.'

# Get content at byte range 1152983631
request.headers['Range'] = 'bytes={}-'.format(1152983631)
response = urlreq.urlopen(request)

# Save content to zip file
with open('./output/level21.zip', 'wb') as f:
    f.write(response.read())

# readme.txt
# Yes! This is really level 21 in here.
# And yes, After you solve it, you'll be in level 22!
# Now for the level:
# * We used to play this game when we were kids
# * When I had no idea what to do, I looked backwards.
