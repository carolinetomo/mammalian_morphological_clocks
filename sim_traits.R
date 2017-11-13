#This simulates binary characters under a single rate
require(NELSI)
require(geiger)
args <- commandArgs(trailingOnly = TRUE)
tree <- read.tree(toString(args[1]))
#mean.rate <- as.numeric(args[3])
#rate.sd <- as.numeric(args[4])

mol.tree = tree
mol.tree$edge.length = mol.tree$edge.length/18
rate = 0.2
q<-list(rbind(c(-rate, rate), c(rate, -rate)))
char = sim.char(mol.tree,q,model="discrete",n=1000)
char = data.frame(char)
outfl = paste(toString(args[1]),".tsv",sep="") 

shuffled = char[,sample(ncol(char))]
write.table(shuffled,sep = "\t", row.names=TRUE,col.names=FALSE,quote=FALSE,file = "single_rate_bin_1000.tsv")

shuffled = char[,sample(ncol(char))][,1:500]
write.table(shuffled,sep = "\t", row.names=TRUE,col.names=FALSE,quote=FALSE,file = "single_rate_bin_500.tsv")

shuffled = char[,sample(ncol(char))][,1:100]
write.table(shuffled,sep = "\t", row.names=TRUE,col.names=FALSE,quote=FALSE,file = "single_rate_bin_100.tsv")

shuffled = char[,sample(ncol(char))][,1:70]
write.table(shuffled,sep = "\t", row.names=TRUE,col.names=FALSE,quote=FALSE,file = "single_rate_bin_70.tsv")

shuffled = char[,sample(ncol(char))][,1:30]
write.table(shuffled,sep = "\t", row.names=TRUE,col.names=FALSE,quote=FALSE,file = "single_rate_bin_30.tsv")

shuffled = char[,sample(ncol(char))][,1:10]
write.table(shuffled,sep = "\t", row.names=TRUE,col.names=FALSE,quote=FALSE,file = "single_rate_bin_10.tsv")

shuffled = char[,sample(ncol(char))][,1:5]
write.table(shuffled,sep = "\t", row.names=TRUE,col.names=FALSE,quote=FALSE,file = "single_rate_bin_5.tsv")

