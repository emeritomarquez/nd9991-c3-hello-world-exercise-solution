#!/usr/bin/python

import sys

f = open(sys.argv[1], 'r')
lines = f.readlines()
f.close()
rows = []
for line in lines:
    if line == "[hosts]\n":
        rows.append(line)
#Windows AWS Work Machine
    elif line == "172.31.18.180\n":
        pass
#Ubuntu    
    elif line == "172.31.4.250\n":
        pass
#app01 prometheus
    elif line == "172.31.2.246\n":
        pass
#lb01
    elif line == "172.31.5.120\n":
        pass
#app02 prometheus node exporter-pip-ansible
    elif line == "172.31.13.218\n":
        pass
#nodejs-server-port-3000
    elif line == "172.31.9.5\n":
        pass
#Kali Linux
    elif line == "172.31.32.205\n":
        pass
#amazon-linux2
    elif line == "172.31.29.68\n":
        pass
#linux-ec2-ansible-test
    elif line == "172.31.25.22\n":
        pass
#ansible-test
    elif line == "172.31.28.42\n":
        pass
#Ubuntu 22.04
    elif line == "172.31.1.88\n":
        pass
#RedHat-Ansible
    elif line == "172.31.4.91\n":
        pass
#Ubuntu18.04.6-ansible
    elif line == "172.31.13.83\n":
        pass
    else:
        rows.append(line)


print(rows)
g = open(sys.argv[2], 'w+')
for element in rows:
    g.write(element)
print(g)
g.close()

