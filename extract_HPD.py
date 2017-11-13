#this script will read in treeannotator2 MCC trees and output mean heights and HPDs
import tree_reader
import sys

def label_internal_nodes(tree):
    c = 0
    for i in tree.iternodes():
        if i.istip == False:
            i.label = "i"+str(c)
            c+=1

def extract_newick_from_nexus(treefl):
    for i in open(treefl,"r"):
        if "tree TREE1" in i:
            spls = i.strip().split("TREE1 =")
            nwk = spls[1].strip()
            return nwk

def get_HPD(prior,posterior):
    nwk = extract_newick_from_nexus(prior)
    prior_tree = tree_reader.read_tree_string(nwk)
    label_internal_nodes(prior_tree)
    nwk = extract_newick_from_nexus(posterior)
    posterior_tree = tree_reader.read_tree_string(nwk)
    label_internal_nodes(posterior_tree)
    print "node_label\tprior_mean\tprior_upper\tprior_lower\tposterior_mean\tpost_upper\tpost_lower\ttype"
    heights = {}
    for i in prior_tree.iternodes():
        spls = i.note.split("height_95%_HPD=")
        mean = spls[0].split("&height=")[1].replace(",","")
        spls1 = spls[1].split(",")
        upper = spls1[1].strip("}")
        lower = spls1[0].strip("{")
        heights[i.label] = [mean,upper,lower]
    for i in posterior_tree.iternodes():
        spls = i.note.split("height_95%_HPD=")
        mean = spls[0].split("&height=")[1].replace(",","")
        spls1 = spls[1].split(",")
        upper = spls1[1].strip("}")
        lower = spls1[0].strip("{")
        if "i" in i.label:
            ntype = "internal"
        else:
            ntype = "tip"
        l = [mean,upper,lower,ntype]
        for j in l:
            heights[i.label].append(j)
    for i in heights.keys():
        print i+"\t"+"\t".join(heights[i])

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print "usage: "+sys.argv[0]+" <PRIOR treefl> <POSTERIOR treefl>"
        sys.exit(0)
    prior = sys.argv[1]
    posterior = sys.argv[2]
    get_HPD(prior,posterior)
