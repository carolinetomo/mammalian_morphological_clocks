#this simulates trinary characters along discrete rate categories
require(NELSI)
require(geiger)
args <- commandArgs(trailingOnly = TRUE)
tree <- read.tree(toString(args[1]))
#mean.rate <- as.numeric(args[3])
#rate.sd <- as.numeric(args[4])

mol.tree = tree
mol.tree$edge.length = mol.tree$edge.length/40
#rate = 0.01
q<-matrix(c(-0.6,0.3,0.3,0.3,-0.6,0.3,0.3,0.3,-0.6),3,3)
char = sim.char(mol.tree,q,model="discrete",n=200)
char = data.frame(char)

q<-matrix(c(-0.8,0.4,0.4,0.4,-0.8,0.4,0.4,0.4,-0.8),3,3)
char = merge(char,data.frame(sim.char(mol.tree,q,model="discrete",n=200)),by="row.names")
colnames(char)=c(1:ncol(char))
rownames(char) = char[,1]
char=char[,-1]

q<-matrix(c(-1.0,0.5,0.5,0.5,-1.0,0.5,0.5,0.5,-1.0),3,3)
char = merge(char,data.frame(sim.char(mol.tree,q,model="discrete",n=200)),by="row.names")
colnames(char)=c(1:ncol(char))
rownames(char) = char[,1]
char=char[,-1]

q<-matrix(c(-1.5,0.75,0.75,0.75,-1.5,0.75,0.75,0.75,-1.5),3,3)
char = merge(char,data.frame(sim.char(mol.tree,q,model="discrete",n=200)),by="row.names")
colnames(char)=c(1:ncol(char))
rownames(char) = char[,1]
char=char[,-1]

q<-matrix(c(-1.8,0.9,0.9,0.9,-1.8,0.9,0.9,0.9,-1.8),3,3)
char = merge(char,data.frame(sim.char(mol.tree,q,model="discrete",n=200)),by="row.names")
colnames(char)=c(1:ncol(char))
rownames(char) = char[,1]
char=char[,-1]

shuffled = char[,sample(ncol(char))]
write.table(shuffled,sep = "\t", row.names=TRUE,col.names=FALSE,quote=FALSE,file = "multi_rate_3_1000.tsv")

shuffled = char[,sample(ncol(char))][,1:500]
write.table(shuffled,sep = "\t", row.names=TRUE,col.names=FALSE,quote=FALSE,file = "multi_rate_3_500.tsv")

shuffled = char[,sample(ncol(char))][,1:100]
write.table(shuffled,sep = "\t", row.names=TRUE,col.names=FALSE,quote=FALSE,file = "multi_rate_3_100.tsv")

shuffled = char[,sample(ncol(char))][,1:70]
write.table(shuffled,sep = "\t", row.names=TRUE,col.names=FALSE,quote=FALSE,file = "multi_rate_3_70.tsv")

shuffled = char[,sample(ncol(char))][,1:30]
write.table(shuffled,sep = "\t", row.names=TRUE,col.names=FALSE,quote=FALSE,file = "multi_rate_3_30.tsv")

shuffled = char[,sample(ncol(char))][,1:10]
write.table(shuffled,sep = "\t", row.names=TRUE,col.names=FALSE,quote=FALSE,file = "multi_rate_3_10.tsv")

shuffled = char[,sample(ncol(char))][,1:5]
write.table(shuffled,sep = "\t", row.names=TRUE,col.names=FALSE,quote=FALSE,file = "multi_rate_3_5.tsv")

