# this script will calculate fitch parsimony score and related indices 
import sys
import tree_reader,node
import site_pattern_test_stat as spts



def read_phylip(fl):
    seqdic = {}
    phy = open(fl,"r")
    first = phy.readline()
    for i in phy:
        spls= i.strip().split()
        seqdic[spls[0]] = spls[1]
    return seqdic

def match_traits_tips(tree,seqdic,site):
    for i in tree.leaves():
        i.data = set(seqdic[i.label][site])

def calc_fitch_parsimony(tree):
    debt = 0
    for i in tree.iternodes(order = "postorder"):
        if i.istip:
            continue
        i.data = i.children[0].data & i.children[1].data
        if len(i.data) == 0:
            i.data = i.children[0].data | i.children[1].data
            if "?" in i.data or "-" in i.data:
                i.data = set([j for j in i.data if j != "?" and j != "-"])
            else:
                debt += 1
    return debt

def tree_length(tree,seqdic):
    return sum(site_fitch_scores(tree,seqdic))

def site_fitch_scores(tree,seqdic):
    nsites = len(seqdic.values()[0])
    site_scores = []
    for i in range(0,nsites):
        match_traits_tips(tree,seqdic,i)
        site_debt = calc_fitch_parsimony(tree)
        site_scores.append(site_debt)
    return site_scores

def sitewise_consistency_index(tree,seqdic):
    nsites = len(seqdic.values()[0])
    site_scores = []
    for i in range(0,nsites):
        match_traits_tips(tree,seqdic,i)
        states = "".join(list(set([list(j.data)[0] for j in tree.leaves()])))
        nstates = len(states.replace("-",""))
        site_debt = calc_fitch_parsimony(tree)
        CI = nstates/float(site_debt)
        site_scores.append(CI)
    return site_scores

def consistency_index(tree,seqdic):
    nsites = len(seqdic.values()[0])
    min_changes = []
    sites  = spts.extract_sites(seqdic)
    for i in range(0,nsites):
        states = "".join(list(set(sites[i])))
        nstates = len(states.replace("-",""))
        min_changes.append(nstates-1)
    debt = tree_length(tree,seqdic)    
    min_changes= sum(min_changes)
    CI = min_changes/float(debt)
    return CI

def retention_index(tree,seqdic):
    nsites = len(seqdic.values()[0])
    min_changes = []
    max_changes = []
    for i in range(0,nsites):
        match_traits_tips(tree,seqdic,i)
        states = "".join(list(set([list(j.data)[0] for j in tree.leaves()])))
        nstates = len(states.replace("-",""))
        if nstates == 1:
            #nstates = 2
            continue
        min_changes.append(nstates-1)
        sitepat = "".join([list(j.data)[0] for j in tree.leaves()])
        tax_states = []
        for j in states.replace("-",""):
            tax_states.append(sitepat.count(j))
        max_changes.append(max(tax_states))
    debt = tree_length(tree,seqdic)    
    min_changes= sum(min_changes)
    max_changes = sum(max_changes)
    ri = (max_changes-float(debt))/(max_changes-float(min_changes))
    return ri

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print "usage: "+sys.argv[0]+" <tree> <PHYLIP alignment> <sitewise fitch scores or CIs>"
        sys.exit(0)

    seqdic = read_phylip(sys.argv[2])
    nwk = open(sys.argv[1],"r").readline().strip()
    tree = tree_reader.read_tree_string(nwk)
    if sys.argv[3].lower() == "ci":
        print consistency_index(tree,seqdic)
        sys.exit(0)
    #scores = sitewise_consistency_index(tree,seqdic)
    #print scores
    #sys.exit(0)
    elif "fitch" in sys.argv[3].lower():
        scores= site_fitch_scores(tree,seqdic)
        outfl = open(sys.argv[2]+".fitchscores","w")
        for i in range(0,len(scores)):
            outfl.write(str(i)+"\t"+str(scores[i])+"\n")


