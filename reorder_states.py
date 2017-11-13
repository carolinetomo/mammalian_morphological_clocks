import sys

if len(sys.argv) != 5:
    print "usage: " +sys.argv[0]+" <NEXUS-formatted input file> <# of taxa> <# of sites> <phylip or nexus output>"
    sys.exit(0)

fl = open(sys.argv[1],"r")
start = False
print sys.argv[2]+"\t"+sys.argv[3]
for i in fl:
    if start == False and "matrix" not in i.lower():
        if "nex" in sys.argv[4]:
            print i.strip()
        continue
    elif "matrix" in i.lower():
        if "nex" in sys.argv[4]:
            print i.strip()
        start = True
    elif start == True and ";" not in i:
        spls = i.strip().split()
        newseq = spls[1].replace("1","0").replace("2","1").replace("3","2").replace("4","3")
        print spls[0]+"\t"+newseq
    elif start == True and ";" in i:
        if "nex" in sys.argv[4]:
            print i.strip()
        start = False

