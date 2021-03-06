PREORDER = 0; POSTORDER = 1
BRANCHLENGTH = 0; INTERNODES = 1

#trying to deprecate this.
class Node:
    def __init__(self):
        self.data = {}
        self.isroot = False
        self.istip = False
        self.label = None
        self.length = 0
        self.old_length = 0
        self.parent = None
        self.children = []
        self.nchildren = 0
        self.comment = None
        #self.charst = 0.
        #self.sigsq = 0.
        #self.rate_class = 0
        self.height = None
        self.number = 0
        self.occurrences = None
        self.num_occurrences = None

    def get_newick_repr(self,showbl=False,show_rate=False):
        ret = ""
        for i in range(len(self.children)):
            if i == 0:
                ret += "("
            ret += self.children[i].get_newick_repr(showbl,show_rate)
            if i == len(self.children)-1:
                ret += ")"
            else:
                ret += ","
        if self.label != None:
            ret += self.label
        if showbl == True:
            ret += ":" + str(self.length)
        if show_rate ==True:
            ret += ":" + str(self.sigsq)
        return ret

    def add_child(self, child):
        assert child not in self.children
        self.children.append(child)
        child.parent = self
        self.nchildren += 1

    def remove_child(self, child):
        assert child in self.children
        self.children.remove(child)
        child.parent = None
        self.nchildren -= 1
    
    def prune_from_node(self):
        for i in self.descendants("POSTORDER"):
            if len(self.children) == 0:
                self.prune()

    def leaves(self):
        return [ n for n in self.iternodes() if n.istip ]

    def iternodes(self, order=PREORDER, v=None):
        if order == PREORDER:
            yield self
        #print [i.label for i in self.children] 
        for child in self.children:
            for d in child.iternodes(order):
                yield d
        if order == POSTORDER:
            yield self
    """
    def postorder_nodes(self):
        [yield d for d in child.postorder_nodes() for child in self.children]
        yield self
    """
    def descendants(self, order=PREORDER, v=None):
        if v is None:
            v = []
        #assert order in ("PREORDER", "POSTORDER")
        for child in self.children:
            if order == PREORDER:
                v.append(child)
            else:
                v.insert(0, child)
            if child.children:
                child.descendants(order, v)
        return v

    def find_descendant(self, label):
        if label == self.label:
            return self
        else:
            for child in self.children:
                n = child.find_descendant(label)
                if n:
                    return n
        return None

    def prune(self):
        p = self.parent
        if p:
            p.remove_child(self)
        return p

    def graft(self, node):
        parent = self.parent
        parent.remove_child(self)
        n = Node()
        n.add_child(self)
        n.add_child(node)
        parent.add_child(n)

    def leaf_distances(self, store=None, measure=BRANCHLENGTH):
        if store is None:
            store = {}
        leaf2len = {}
        if self.children:
            for child in self.children:
                if measure == BRANCHLENGTH:
                    assert child.length is not None
                    dist = child.length
                elif measure == INTERNODES:
                    dist = 1
                else:
                    raise "InvalidMeasure"
                child.leaf_distances(store, measure)
                if child.istip:
                    leaf2len[child.label] = dist
                else:
                    for k, v in store[child].items():
                        leaf2len[k] = v + dist
        else:
            leaf2len[self] = {self.label: 0}
        store[self] = leaf2len
        return store

    def rootpath(self):
        n = self
        while 1:
            yield n
            if n.parent:
                n = n.parent
            else:
                break

    def tip_labels(self):
        labs = []
        for i in self.leaves():
            labs.append(i.label)
        return labs

    def nnodes(self, type="internal"):
        n = 0
        if type == "internal":
            for i in self.iternodes():
                if i.istip or i == self:
                    continue
                n += 1
        elif type == "all":
            for i in self.iternodes():
                n+=1
        elif type == "tips":
            for i in self.iternodes():
                if i.istip:
                    n+=1
        return n




    """
    # this returns all possible NNIs for a single bifurcating node with bifurcating children
    # tree should probably be deep copied before using this
    """
    def nni_set(self): 
        if len(self.children) != 2 or len(self.descendants()) < 3:
            print "this only works on bifurcating selfs that parent multiple subtrees (ie. does not lead to only terminal edges)"
            return None
        
        subtrees = []

        for child in self.children:
            if child.istip == False:
                assert len(child.children) == 2
                for sub in child.children:
                    subtrees.append(sub)

        subtrees += [i for i in self.children if i.istip] #add terminal subtree child --> 'c' in (a,b),c)) 
        assert len(subtrees) == 3 or len(subtrees) == 4

        nni_trees = []
        for c1 in subtrees:
            for c2 in subtrees:
                p1 = c1.parent
                p2 = c2.parent
                if c1 == c2 or p1 == p2: #can't swap subtrees with same parent 
                    continue

                p1.remove_child(c1)
                p1.add_child(c2)
                p2.remove_child(c2)
                p2.add_child(c1)

                c1.parent = p2  #swap subtrees
                c2.parent = p1
                nni_trees.append(self.get_newick_repr())

        nni_trees = list(set(nni_trees)) #remove duplicates
        #print len(nni_trees)
        return nni_trees



def reroot(oldroot, newroot):
    oldroot.isroot = False
    newroot.isroot = True
    v = []
    n = newroot
    while 1:
        v.append(n)
        if not n.parent: break
        n = n.parent
    #print [ x.label for x in v ]
    v.reverse()
    for i, cp in enumerate(v[:-1]):
        node = v[i+1]
        # node is current node; cp is current parent
        #print node.label, cp.label
        cp.remove_child(node)
        node.add_child(cp)
        cp.length = node.length
    return newroot


def getMRCATraverseFromPath(path1, curn2):
    mrca = None
    #find first match between this node and the first one
    parent = curn2
    x = True;
    while x == True:
        for i in range(len(path1)):
            if parent == path1[i]:
                mrca = parent
                x = False
                break
        parent = parent.parent
    return mrca   










