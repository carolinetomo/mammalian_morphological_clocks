import sys,os

if len(sys.argv) != 2:
    print "usage: "+sys.argv[0]+" <directory prefix>"
    sys.exit(0)

for i in os.listdir("./"):
    if sys.argv[1] in i:
        for j in os.listdir(i):
            if sys.argv[1] in j and "\.state" not in j:
                cmd = "beast -threads 3 -overwrite "+i+"/"+j
                os.system(cmd)
                print cmd
                intree = i+"/"+j.strip().split("_")[0]+".trees"
                outtree = i+"/"+j.strip().split("_")[0]+".mcc.tre"
                cmd = "treeannotator -heights mean -burnin 20 "+intree+" > "+outtree
                print cmd
                os.system(cmd)
