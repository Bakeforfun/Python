# Solution to
# http://www.pythonchallenge.com/pc/def/map.html

# ex1
# K = M, O = Q, E = G

from string import maketrans

shift = ord("M") - ord("K")

initial_phrase = """g fmnc wms bgblr rpylqjyrc gr zw fylb.
rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq
glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle.
sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."""

final_phrase = []

# my method
for x in initial_phrase:
    if x.isalpha():
        letter = ((ord(x) - ord('a')) + shift) % 26
        final_phrase.append(chr(letter + ord('a')))
    else:
        final_phrase.append(x)

# solution method
intab = []
outtab = []
for x in xrange(26):
    intab.append(chr(ord('a') + x))
    outtab.append(chr(((ord(intab[x]) - ord('a')) + shift) % 26 + ord('a')))

trantab = maketrans(''.join(intab), ''.join(outtab))

print "Inital phrase:"
print initial_phrase
print "\nFinal phrase:"
print "".join(final_phrase)
print "\nAnswer to exercise:"
print "map".translate(trantab)
