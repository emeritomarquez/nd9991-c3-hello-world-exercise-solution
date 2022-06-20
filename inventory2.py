#!/usr/bin/python


import sys

f = open(sys.argv[1], 'r')
lines = f.readlines()
f.close()
rows = []
for line in lines:
    if line == "[hosts]\n":
        rows.append(line)
    elif line == "35.87.96.184\n":
        pass
    elif line == "54.69.86.178\n":
        pass
    elif line == "54.186.184.223\n":
        pass
    elif line == "34.221.45.78\n":
        pass
    else:
        rows.append(line)

print(rows)
g = open(sys.argv[2], 'w+')
for element in rows:
    g.write(element)
print(g)
g.close()

