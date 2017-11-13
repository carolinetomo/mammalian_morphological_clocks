import sys,os
import tsv2nex,nex2xml

if len(sys.argv) != 5:
    print "usage: " + sys.argv[0] + " <R script for simulation> <TREE for sims> <BEAST 2 XML template> <# states>"
    sys.exit(0)

reps = 20 

for i in range(0,reps):
    cmd = "Rscript "+ sys.argv[1]+" "+sys.argv[2]
    os.system(cmd)
    for j in os.listdir("./"):
        if j.strip().split(".")[-1]=="tsv":
            nsites=j.strip().split("_")[-1].strip().split(".")[0]
            tsv2nex.format_nexus(j)
            nex2xml.nex2xml(j+".nex",sys.argv[3],sys.argv[4],nsites,str(i))
    cmd = "rm *.tsv*"
    os.system(cmd)

