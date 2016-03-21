# Solution to
# http://www.pythonchallenge.com/pc/def/channel.html

# ex6

import zipfile

my_zip = zipfile.ZipFile("solution\ex6_channel.zip")

nothing = "90052"

comments = []
while True:
    file_name = nothing + ".txt"
    f = my_zip.open(file_name, 'r')
    data = f.read()
    print data
    comments.append(my_zip.getinfo(file_name).comment)
    data = data.split(" ")
    nothing = data[len(data)-1]
    if not nothing.isdigit():
        break

print "".join(comments)
my_zip.close()
