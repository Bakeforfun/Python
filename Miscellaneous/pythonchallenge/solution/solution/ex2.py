# Solution to
# http://www.pythonchallenge.com/pc/def/ocr.html

# ex2

f = open("solution/ex2_source.txt", 'r')

data = f.read()

res = []
for x in data:
    if x.isalpha():
        res.append(x)

print "".join(res)
f.close()
