# Solution to
# http://www.pythonchallenge.com/pc/def/peak.html

# ex5

import pickle

f = open("solution/ex5_banner.p", 'r')
data = pickle.load(f)
f.close()

res = []
for num_x, val_x in enumerate(data):
    for num_y, val_y in enumerate(data[num_x]):
        for z in xrange(val_y[1]):
            res.append(val_y[0])
    res.append("\n")

print "".join(res)
