require(ggplot2)

plt = ggplot(data = heights,aes(x=prior_upper-prior_lower,y=post_upper-post_lower,colour=type))

 plt = plt + geom_point()+
     geom_smooth(method='lm')
plt = plt+xlab("Prior 95% HPD Interval Width")
plt = plt+ylab("Posterior 95% HPD Interval Width")
   
plt = plt + labs(colour = "Node Type") + theme_bw()+ scale_colour_brewer(palette="Dark2")
     
