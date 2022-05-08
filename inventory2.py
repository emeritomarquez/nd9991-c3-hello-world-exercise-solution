#!/usr/bin/python

import sys

f = open(sys.argv[1], 'r')
lines = f.readlines()
f.close()
rows = []
for line in lines:
    if line == "[hosts]\n":
        rows.append(line)
    elif line == "54.245.26.167\n":
        pass
    elif line == "34.219.10.77\n":
        pass
    elif line == "54.245.198.249\n":
        pass
    elif line == "52.13.23.182\n":
        pass
    elif line == "34.210.122.108\n":
        pass
    else:
        rows.append(line)

print(rows)
g = open(sys.argv[2], 'w+')
for element in rows:
    g.write(element)
print(g)
g.close()

