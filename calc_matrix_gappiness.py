import sys
from numpy import mean

if len(sys.argv)!= 2:
    print "usage: " + sys.argv[0]+" <alignment>"
    sys.exit(0)


fl = open(sys.argv[1],"r")
first = fl.readline()

nsites = 0
gcount = []
for i in fl:
    gaps = 0
    spls = i.strip().split()
    if nsites == 0:
        for j in spls[1]:
            nsites+=1
    for j in spls[1]:
        if j == "-" or j == "?":
            gaps +=1
    print spls[0]+"\t"+str(gaps/float(nsites))
    gcount.append(gaps/float(nsites))
print gcount
print mean(gcount)

