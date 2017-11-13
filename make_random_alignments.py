# this replaces the sequences in a BEAST2 XML file with random traits 
from numpy import random
import sys

if len(sys.argv) != 2:
    print "usage: "+sys.argv[0]+" <BEAST2 XML Template>"
    sys.exit(0)

def generate_random_seq(prob,seqlen):
    newseq = ""
    for i in range(0,seqlen):
        r = random.uniform(0,1)
        if r < prob:
            newseq += "0"
        else:
            newseq += "1"
    return newseq

if __name__ == "__main__":
    xml = open(sys.argv[1],"r")
    for i in xml:
        if "sequence id" not in i:
            print i.strip()
            continue
        else:
            spls = i.strip().split("value=")
            seqlen = len(spls[1])-4
            prob = 0.7
            newseq = generate_random_seq(prob,seqlen)
            print spls[0]+" value="+"\""+newseq+"\"/>"#+"\n"
            
