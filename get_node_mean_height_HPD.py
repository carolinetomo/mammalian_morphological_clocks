# this script processes simulation results for mean heights and HPDS of tested nodes
import tree_reader,extract_HPD
import sys,os

def mrca(c1,c2,tree):
    n1 = [i for i in tree.leaves() if i.label == c1][0]
    n2 = [i for i in tree.leaves() if i.label == c2][0]
    for i in tree.iternodes(order = "preorder"):
        leaves = i.leaves()
        if n1 in leaves and n2 not in leaves:
            return i.parent
        
def get_height(node):
    if node.istip:
        return 0.0
    else:
        return max([float(get_height(i))+float(i.length) for i in node.children])   

def read_nexus(treefl):
    start_t = False
    nm_dic = {} 
    for i in open(treefl,"r"):
        if "Translate" in i.strip():
            start_t = True
        elif start_t== True and ";" not in i: 
            spls = i.strip().replace(",","").split()
            nm_dic[spls[0]]=spls[1]
        elif start_t == True and ";" in i:
            start_t = False
        elif "tree TREE1" in i:
            spls = i.strip().split("TREE1 =")
            nwk = spls[1].strip()
    tree = tree_reader.read_tree_string(nwk)
    for node in tree.iternodes():
        if node.istip:
            newlabel = nm_dic[node.label]
            node.label = newlabel 
    return tree

if __name__ == "__main__":
    if len(sys.argv) != 2: 
        print "usage: "+sys.argv[0] + " <directory containing subdirectories>"
        sys.exit(0)
    print "char_states"+"\t"+"nrates"+"\t"+"num_traits"+"\t"+"clade_age"+"\t"+"upper"+"\t"+"lower"
    for i in os.listdir(sys.argv[1]):
        if "_rate_" in i and ".state" not in i:
            spls = i.strip().split("_")
            nstates = spls[2]
            sitewise = spls[0]
            nchar = spls[3]
            for j in os.listdir(i):
                if j.strip().split(".")[-1] == "tre":
                    tree = read_nexus(i+"/"+j)
                    #for node in tree.iternodes():
                    #    if "Aetiocetus_cotylalveus" in [k.label for k in node.leaves()] and "Janjucetus_hunderi" in [k.label for k in node.leaves()] and "Agorophius_pygmaeus" not in [k.label for k in node.leaves()]:
                        #if "Kogia_breviceps" in [l.label for l in node.children]:
                    node = mrca("Aetiocetus_cotylalveus","Janjucetus_hunderi",tree)
                    #node = mrca("Kogia_breviceps","Physeter_catodon",tree)
                    height = get_height(node) 
                    note_spls = node.note.split("height_95%_HPD=")
                    range_spls = note_spls[1].strip().split(",")
                    upper = range_spls[1].replace("}","")
                    lower = range_spls[0].replace("{","")
                    print nstates+"\t"+sitewise+"\t"+nchar+"\t"+str(height)+"\t"+upper+"\t"+lower 




