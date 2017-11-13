import sys

fl = open(sys.argv[1],"r")
count = 0
for i in fl:
    if "samplingDates" not in i:
        print i.strip()
        continue
    else:
        sp = i.strip().split("taxon=")[1].split("lower")[0].strip()
        print "<samplingDates id= \"samplingDate"+str(count)+"\" spec=\"beast.evolution.tree.SamplingDate\" taxon="+sp+" lower = \"0\" upper = \"150\"/>"
        count += 1

