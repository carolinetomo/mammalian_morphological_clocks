import sys

if len(sys.argv) != 2:
    print "usage: "+sys.argv[0]+" <tab-separated geologic range file>"
    sys.exit(0)

fl = open(sys.argv[1],"r")

samp = ""
tax = ""
count = 0
tax += "\t\t<taxonset id = \"GeoTax\" spec = \"TaxonSet\">\n"
for i in fl:
    spls = i.strip().split("\t")
    sp = spls[0]
    upper = spls[1]
    lower = spls[2]
    samp += "\t\t<samplingDates id= \"samplingDate"+str(count)+"\" spec=\"beast.evolution.tree.SamplingDate\" taxon=\""+sp+"\" lower = \""+lower+"\" upper = \""+ upper+ "\"/>\n"
    #samp += "\t\t<taxon id =\""+sp+"\" spec = \"Taxon\"/>\n\t\t</samplingDates>\n"
    tax += "\t\t\t<taxon id = \""+sp+"\" spec = \"Taxon\"/>\n"
    count += 1

tax += "\t\t</taxonset>\n"

print "\t<operator id=\"SampledNodeDateRandomWalker.0\" spec=\"SampledNodeDateRandomWalker\" tree=\"@Tree.t:hominin\" weight=\"10.0\" windowSize=\"1.0\">"
print tax
print samp

