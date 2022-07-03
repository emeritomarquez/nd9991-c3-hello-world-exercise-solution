#!/usr/bin/python

import sys

f = open(sys.argv[1], 'r')
lines = f.readlines()
f.close()
rows = []
for line in lines:
    if line =! "[hosts]\n":
        rows.append(line)
print(rows)
g = open(sys.argv[2], 'w+')
for element in rows:
    g.write(element)
g.close()

