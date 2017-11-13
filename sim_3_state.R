#this simulates trinary traits along a single rate
require(NELSI)
require(geiger)
args <- commandArgs(trailingOnly = TRUE)
tree <- read.tree(toString(args[1]))
#mean.rate <- as.numeric(args[3])
#rate.sd <- as.numeric(args[4])

mol.tree = tree
mol.tree$edge.length = mol.tree$edge.length/40
rate = 0.01
q<-matrix(c(-0.4,0.2,0.2,0.2,-0.4,0.2,0.2,0.2,-0.4),3,3)
q<-matrix(c(-0.1,0.05,0.05,0.05,-0.1,0.05,0.05,0.05,-0.1),3,3)
char = sim.char(mol.tree,q,model="discrete",n=1000)
char = data.frame(char)

shuffled = char[,sample(ncol(char))]
write.table(shuffled,sep = "\t", row.names=TRUE,col.names=FALSE,quote=FALSE,file = "single_rate_3_1000.tsv")

shuffled = char[,sample(ncol(char))][,1:500]
write.table(shuffled,sep = "\t", row.names=TRUE,col.names=FALSE,quote=FALSE,file = "single_rate_3_500.tsv")

shuffled = char[,sample(ncol(char))][,1:100]
write.table(shuffled,sep = "\t", row.names=TRUE,col.names=FALSE,quote=FALSE,file = "single_rate_3_100.tsv")

shuffled = char[,sample(ncol(char))][,1:70]
write.table(shuffled,sep = "\t", row.names=TRUE,col.names=FALSE,quote=FALSE,file = "single_rate_3_70.tsv")

shuffled = char[,sample(ncol(char))][,1:30]
write.table(shuffled,sep = "\t", row.names=TRUE,col.names=FALSE,quote=FALSE,file = "single_rate_3_30.tsv")

shuffled = char[,sample(ncol(char))][,1:10]
write.table(shuffled,sep = "\t", row.names=TRUE,col.names=FALSE,quote=FALSE,file = "single_rate_3_10.tsv")

shuffled = char[,sample(ncol(char))][,1:5]
write.table(shuffled,sep = "\t", row.names=TRUE,col.names=FALSE,quote=FALSE,file = "single_rate_3_5.tsv")
