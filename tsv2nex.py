import sys

def format_nexus(filename):
    newfl = open(filename+".nex","w")
    oldfl = open(filename,"r")
    newfl.write("#NEXUS"+"\n"+"Begin data;"+"\n"+"Dimensions ntax=23 nchar=20;\n" +"Format datatype=standard missing = ?;"+"\n"+"Matrix"+"\n")
    for j in oldfl:
        spls = j.strip().split()
        seq = "".join(spls[1:])
        line = "\t".join([spls[0],seq])+"\n"
        newfl.write(line)
    newfl.write(";"+"\n"+"end;")#+"\n"+"Begin MrBayes;\n\tLset Rates = Equal;\n\tprset applyto=(1) brlenspr=clock:uniform;\n\tmcmc ngen=1000000 samplefreq=100 printfreq=10000 nchains=1 nruns=1;\n\tsump;\n\tsumt burnin = 200;\n\tquit;\nend;")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "usage: "+sys.argv[0]+" <.tsv file>"
        sys.exit(0)
    fl = sys.argv[1]
    format_nexus(fl)
