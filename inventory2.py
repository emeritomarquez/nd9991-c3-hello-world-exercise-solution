#!/usr/bin/python

import sys

f = open(sys.argv[1], 'r')
lines = f.readlines()
f.close()
rows = []
for line in lines:
    if line == "[hosts]\n":
        rows.append(line)
    elif line == "34.220.218.90\n":
        pass
    elif line == "35.89.141.187\n":
        pass
    elif line == "52.38.52.160\n":
        pass
    elif line == "54.214.167.163\n":
        pass
    else:
        rows.append(line)

print(rows)
g = open(sys.argv[2], 'w+')
for element in rows:
    g.write(element)
print(g)
g.close()

