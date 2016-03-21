# Solution to
# http://www.pythonchallenge.com/pc/def/linkedlist.php

# ex4

import urllib

url_name = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345"

for x in xrange(1, 400):
    url_request = urllib.urlopen(url_name)
    data = url_request.read()
    print data
    if "html" in data:
        break
    data = data.split(" ")
    nothing = data[len(data)-1]
    url_name = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + nothing
