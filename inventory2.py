#!/usr/bin/python

import sys

f = open(sys.argv[1], 'r')
lines = f.readlines()
f.close()
rows = []
for line in lines:
    if line == "[hosts]\n":
        rows.append(line)
    elif line == "54.218.104.198\n":
        pass
    elif line == "52.39.16.59\n":
        pass
    elif line == "54.184.97.199\n":
        pass
    elif line == "54.218.249.122\n":
        pass
     elif line == "54.185.203.154\n":
        pass
    else:
        rows.append(line)

print(rows)
g = open(sys.argv[2], 'w+')
for element in rows:
    g.write(element)
print(g)
g.close()

