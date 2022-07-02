#!/usr/bin/python

import sys

f = open(sys.argv[1], 'r')
lines = f.readlines()
f.close()
rows = []
for line in lines:
    if line == "[hosts]\n":
        rows.append(line)
    elif line == "35.87.95.234\n":
        pass
    elif line == "18.237.5.140\n":
        pass
    elif line == "35.85.58.241\n":
        pass
    elif line == "54.190.110.174\n":
        pass
    else:
        rows.append(line)


print(rows)
g = open(sys.argv[2], 'w+')
for element in rows:
    g.write(element)
print(g)
g.close()

