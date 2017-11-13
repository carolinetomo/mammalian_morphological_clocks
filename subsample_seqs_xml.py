import sys

if len(sys.argv) !=3:
    print "usage: "+sys.argv[0] + " <BEAST2 XML file> <sites to keep>"
    sys.exit(0)

def subsample_ambiguous(oldseq,nsites):
    newseq = ""
    count = 0
    ambig = False
    for i in oldseq: 
        if count == nsites:
            return newseq
        if i != "{" and ambig == False:
            newseq += i 
            count += 1
        elif i == "{":
            ambig_site = i
            ambig = True
        elif ambig == True and i != "}": 
            ambig_site += i
        elif ambig == True and i == "}":
            ambig_site += i
            newseq += ambig_site
            ambig = False
            count += 1

xml = open(sys.argv[1],"r")
cutoff = int(sys.argv[2])
for i in xml:
    if "sequence id" not in i:
        print i.strip()
        continue
    else:
        spls = i.strip().split("value=")
        old_seq = spls[1][0:-2].replace("\"","")
        newseq = "\""
        #newseq += subsample_ambiguous(old_seq, 100)
        newseq += old_seq[0:cutoff]
        newseq += "\""
        newseq += "/>\n"
        print spls[0].strip().replace("totalcount=\"2\"","totalcount=\"2\"")+" value="+newseq.strip()
