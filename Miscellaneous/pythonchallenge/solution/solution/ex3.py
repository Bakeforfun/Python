# Solution to
# http://www.pythonchallenge.com/pc/def/equality.html

# ex3

f = open("solution/ex3_source.txt", 'r')
data = ''.join([line.rstrip() for line in open('solution/ex3_source.txt')])
f.close()

res = []
for x in data:
    if x.isupper():
        res.append(1)
    else:
        res.append(0)

answer = []
for x in xrange(9, len(res)):
    s = sum(res[x-9:x])
    if s == 6:
        if res[x-1] == 0:
            if res[x-5] == 0:
                if res[x-9] == 0:
                    print res[x-9:x]
                    print "%s", data[x-9:x]
                    answer.append(data[x-5])

print "".join(answer)
