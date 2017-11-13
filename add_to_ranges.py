import sys

fl = open(sys.argv[1],"r")
count = 0
for i in fl:
    if "samplingDates" not in i:
        print i.strip()
        continue
    else:
        sp = i.strip().split("taxon=")[1].split("lower")[0].strip()
        lower = i.strip().split("lower = ")[1].strip().split("upper = ")[0].replace("\"","").strip()
        upper = i.strip().split("lower = ")[1].strip().split("upper = ")[1].replace("\"","")[0:-2]
        newupper = str(float(upper)+10)
        newlower = str(float(lower)+10)
        print "<samplingDates id= \"samplingDate"+str(count)+"\" spec=\"beast.evolution.tree.SamplingDate\" taxon="+sp+" lower = \""+newlower+"\" upper = \""+newupper+"\"/>"
        count += 1

