require(ggplot2)


sim <- data.frame( x = c(-Inf, Inf), y = 24.223, cutoff = factor(24.223))
geo <- data.frame( x = c(-Inf, Inf), y = 17.84, cutoff = factor(17.84))

plt = ggplot(table,aes(x=num_traits))+
    geom_line(aes(y=clade_age,color=char_states)) + geom_point(aes(y=clade_age,color=char_states))
plt = plt + scale_colour_brewer(palette="Dark2")+theme_bw() 
#    ylim(15,25)
plt = plt + geom_line(aes(x,y),linetype="dotted",sim)
plt = plt + geom_line(aes(x,y),linetype="dotted",geo,colour="red")

