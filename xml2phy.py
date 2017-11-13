import sys

if len(sys.argv) != 2:
    print "usage: "+sys.argv[0]+" <BEAST XML file>"
    sys.exit(0)

def extract_xml_seqs(fl):
    seq_dic={}
    for i in open(fl,"r"):
        if "sequence id" not in i:
            continue
        lab = i.strip().split("taxon=")[1].split("totalcount")[0].replace("\"","")
        seq = i.strip().split("value=")[1][1:-3]
        seq_dic[lab] = seq
    return seq_dic

def print_phylip(fl):
    seqdic = extract_xml_seqs(sys.argv[1])
    ntax = str(len(seqdic.keys()))
    nchar = str(len(seqdic.values()[0]))
    for i in seqdic.keys():
        print i+"\t"+seqdic[i]

def print_nexus(fl):
    seqdic = extract_xml_seqs(sys.argv[1])
    ntax = str(len(seqdic.keys()))
    nchar = str(len(seqdic.values()[0]))
    print "\#NEXUS\nBEGIN TAXA;"
    print "DIMENSIONS NTAX="+str(ntax)+";\nTAXLABELS"
    print "\n\t".join(seqdic.keys())
    print ";\nEND;\n"
    print "BEGIN CHARACTERS;"
    print "\tDIMENSIONS NCHAR="+str(nchar)+";"
    print "\tFORMAT DATATYPE=STANDARD MISSING=? GAP =- SYMBOLS = \"0123456789\";\n\tMATRIX"
    for i in seqdic.keys():
        print "\t"+i+"\t"+seqdic[i]
    print ";\nEND;"

if __name__ == "__main__":
    print_nexus(sys.argv[1])

