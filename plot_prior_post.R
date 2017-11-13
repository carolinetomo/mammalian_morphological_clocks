require(ggplot2)

#args = commandArgs(trailingOnly = T)
#heights = read.table(args[1],h=T)

plt = ggplot(data = heights,aes(x=prior_mean,y=posterior_mean,colour=type)) 
plt = plt+geom_point()+
    xlim(0,50) +
    ylim(0,50)
plt = plt+geom_smooth(method='lm')
plt = plt + geom_errorbarh(aes(xmin = prior_lower,xmax = prior_upper)) +geom_errorbar(aes(ymin=post_lower,ymax=post_upper))
plt = plt+xlab("Prior 95% HPD")
plt = plt+ylab("Posterior 95% HPD")
plt = plt + labs(colour = "Node Type") + theme_bw()+ scale_colour_brewer(palette="Dark2")

#plt + facet_wrap(~type)
