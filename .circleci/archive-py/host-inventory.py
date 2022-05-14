#!/usr/bin/env python

f = open('inventory.txt', 'r')
lines = f.readlines()
f.close()
rows = []
for line in lines:
    if line == "[hosts]":
        rows.append(line)
    elif line == "172.31.18.180":
        continue
    elif line == "172.31.4.250":
        continue
    elif line == "172.31.2.246":
        continue
    elif line == "172.31.5.120":
        continue
    elif line == "172.31.13.218":
        continue
    elif line == "172.31.9.5":
        continue
    elif line == "172.31.29.68":
        continue
    else:
        rows.append(line)
print(rows)
g = open('inventory1.txt', 'w+')
g.write(rows)
print(g)
