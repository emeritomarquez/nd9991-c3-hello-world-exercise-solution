#!/usr/bin/python

import sys

f = open(sys.argv[1], 'r')
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
    elif line == "172.31.32.205\n":
        pass
    elif line == "172.31.29.68\n":
        pass
    elif line == "172.31.25.22\n":
        pass
    elif line == "172.31.28.42\n":
        pass
    elif line == "172.31.1.88\n":
        pass
    elif line == "172.31.4.91\n":
        pass
    elif line == "172.31.13.83\n":
        pass
    elif line == "172.31.20.231\n":
        pass
    else:
        rows.append(line)


print(rows)
g = open(sys.argv[2], 'w+')
for element in rows:
    g.write(element)
print(g)
g.close()

