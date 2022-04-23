#!/usr/bin/python

import sys

f = open(sys.argv[2], 'r')
lines = f.readlines()
f.close()
rows = []
for line in lines:
    if line == "[hosts]\n":
        rows.append(line)
    elif line == "172.31.18.180\n":
        pass
    elif line == "172.31.4.250\n":
        pass
    elif line == "172.31.2.246\n":
        pass
    elif line == "172.31.5.120\n":
        pass
    elif line == "172.31.13.218\n":
        pass
    elif line == "172.31.9.5\n":
        pass
    elif line == "172.31.29.68\n":
        pass
    else:
        rows.append(line)
print(rows)
g = open(sys.argv[3], 'w+')
for element in rows:
    g.write(element)
print(g)
g.close()

