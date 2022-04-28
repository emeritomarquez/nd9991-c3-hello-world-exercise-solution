#!/usr/bin/python

import sys

f = open(sys.argv[1], 'r')
lines = f.readlines()
f.close()
rows = []
for line in lines:
    if line == "[hosts]\n":
        rows.append(line)
    elif line == "18.236.86.94\n":
        pass
    elif line == "54.245.169.221\n":
        pass
    elif line == "54.68.64.242\n":
        pass
    else:
        rows.append(line)
print(rows)
g = open(sys.argv[2], 'w+')
for element in rows:
    g.write(element)
print(g)
g.close()

