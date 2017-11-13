import sys,os

if len(sys.argv) != 2:
    print "usage: "+sys.argv[0]+" <directory>"
    sys.exit(0)

for j in os.listdir(sys.argv[1]):
    if ".xml" in j and "\.state" not in j:
        cmd = "beast -threads 1 -overwrite "+sys.argv[1]+"/"+j
        os.system(cmd)
        print cmd
        intree = sys.argv[1]+"/"+j.strip().split("_")[0]+".trees"
        outtree = sys.argv[1]+"/"+j.strip().split("_")[0]+".mcc.tre"
        cmd = "treeannotator -heights mean -burnin 20 "+intree+" > "+outtree
        print cmd
        os.system(cmd)
