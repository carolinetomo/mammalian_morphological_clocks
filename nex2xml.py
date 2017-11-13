import sys

def nex2xml(nexus,xml,states,nsites,rep=0):
    nex = open(nexus,"r")
    start = False
    seqd = {}
    seq_len = ""
    for i in nex:
        if "matrix" in i.lower():
            start = True
        elif start == True and ";" not in i:
            spls = i.strip().split()
            lab = spls[0]
            seq = spls[1]
            newseq = spls[1].replace("1","0").replace("2","1").replace("3","2").replace("4","3")
            seqd[lab] = newseq
        elif ";" in i and start == True:
            seq_len = str(len(seq))
            start = False
    nex.close()

    xml = open(xml,"r")
    cur = "".join(nexus.strip().split(".")[0:-2])
    outxml = open(cur+"/"+str(rep)+"_"+cur+".xml","w")
    for i in xml: 
        if "sequence id" not in i and "FilteredAlignment" not in i and "tracelog" not in i and "treelog" not in i:
            outxml.write(i.strip()+"\n")
            #print i.strip()
            continue
        elif "FilteredAlignment" in i:
            spls = i.strip().split("filter=")
            newline = spls[0]+" filter=\"1-"+nsites+"\">"
            outxml.write(newline+"\n")
        elif "sequence id" in i:
            spls = i.strip().split("value=")
            curtip = spls[0].strip().split("taxon=")[1].split("totalcount")[0].replace("\"","").strip()
            newseq = "\""
            newseq += seqd[curtip]
            newseq += "\""
            newseq += "/>\n"
            newstate = "totalcount=\""+states+"\""
            outxml.write(spls[0].replace("totalcount=\"3\"",newstate)+"value="+newseq)
        elif "tracelog" in i:
            newline = i.replace("fileName=\"cetacean.log\"","fileName=\""+cur+"/"+str(rep)+".log\"")
            outxml.write(newline+"\n")
        elif "treelog" in i:
            newline = i.replace("fileName=\"$(tree).trees\"","fileName=\""+cur+"/"+str(rep)+".trees\"")
            outxml.write(newline+"\n")
if __name__ == "__main__":
    if len(sys.argv) != 5:
        print "usage: "+sys.argv[0] + " <NEXUS sequence file> <BEAST2 XML file> <nstates> <nsites>"
        sys.exit(0)

    nex2xml(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])
