#this simulates binary traits along discrete rate categories
require(NELSI)
require(geiger)
args <- commandArgs(trailingOnly = TRUE)
tree <- read.tree(toString(args[1]))
#mean.rate <- as.numeric(args[3])
#rate.sd <- as.numeric(args[4])

mol.tree = tree
mol.tree$edge.length = mol.tree$edge.length/18
rate = 0.6
q<-list(rbind(c(-rate, rate), c(rate, -rate)))
char = sim.char(mol.tree,q,model="discrete",n=200)
char = data.frame(char)


rate = 0.5
q<-list(rbind(c(-rate, rate), c(rate, -rate)))
char = merge(char,data.frame(sim.char(mol.tree,q,model="discrete",n=200)),by="row.names")
colnames(char)=c(1:ncol(char))
rownames(char) = char[,1]
char=char[,-1]

rate = 0.25
q<-list(rbind(c(-rate, rate), c(rate, -rate)))
char = merge(char,data.frame(sim.char(mol.tree,q,model="discrete",n=200)),by="row.names")
colnames(char)=c(1:ncol(char))
rownames(char) = char[,1]
char=char[,-1]

rate = 0.9
q<-list(rbind(c(-rate, rate), c(rate, -rate)))
char = merge(char,data.frame(sim.char(mol.tree,q,model="discrete",n=200)),by="row.names")
colnames(char)=c(1:ncol(char))
rownames(char) = char[,1]
char=char[,-1]

rate = 0.1
q<-list(rbind(c(-rate, rate), c(rate, -rate)))
char = merge(char,data.frame(sim.char(mol.tree,q,model="discrete",n=200)),by="row.names")
colnames(char)=c(1:ncol(char))
rownames(char) = char[,1]
char=char[,-1]

shuffled = char[,sample(ncol(char))]
write.table(shuffled,sep = "\t", row.names=TRUE,col.names=FALSE,quote=FALSE,file = "multi_rate_bin_1000.tsv")

shuffled = char[,sample(ncol(char))][,1:500]
write.table(shuffled,sep = "\t", row.names=TRUE,col.names=FALSE,quote=FALSE,file = "multi_rate_bin_500.tsv")

shuffled = char[,sample(ncol(char))][,1:100]
write.table(shuffled,sep = "\t", row.names=TRUE,col.names=FALSE,quote=FALSE,file = "multi_rate_bin_100.tsv")

shuffled = char[,sample(ncol(char))][,1:70]
write.table(shuffled,sep = "\t", row.names=TRUE,col.names=FALSE,quote=FALSE,file = "multi_rate_bin_70.tsv")

shuffled = char[,sample(ncol(char))][,1:30]
write.table(shuffled,sep = "\t", row.names=TRUE,col.names=FALSE,quote=FALSE,file = "multi_rate_bin_30.tsv")

shuffled = char[,sample(ncol(char))][,1:10]
write.table(shuffled,sep = "\t", row.names=TRUE,col.names=FALSE,quote=FALSE,file = "multi_rate_bin_10.tsv")

shuffled = char[,sample(ncol(char))][,1:5]
write.table(shuffled,sep = "\t", row.names=TRUE,col.names=FALSE,quote=FALSE,file = "multi_rate_bin_5.tsv")
