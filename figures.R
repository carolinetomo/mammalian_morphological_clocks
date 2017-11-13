setwd("~/Dropbox/bayes/whales/two_node_sims/")
require(ggplot2)
require(plyr)
fl <- read.csv("replicated_node_age_sampling_deep.tab",sep="\t")

means <- ddply(fl,~char_states+num_traits+nrates,summarise,mean_age=mean(clade_age))

ggplot(aes(y = clade_age, x = factor(num_traits), fill = char_states), data = fl) + 
  geom_boxplot()+
  xlab("Matrix Size")+
  ylab("Mean node age") +
  labs(fill="Data Type") +
  theme_bw() +
  scale_fill_brewer(palette = "Accent")

ggplot(aes(y 
           = clade_age, x = factor(num_traits), fill = nrates), data = fl) + 
  geom_violin(draw_quantiles=0.5) + 
  geom_hline(yintercept=24.223,linetype="dotted",colour = "red") +
  geom_hline(yintercept=17.84,linetype="dotted",colour = "red") +
  facet_wrap(~char_states) +
  xlab("Matrix Size")+
  ylab("Topological Error") +
  labs(fill="Data Type") +
  theme_bw() + 
  scale_fill_brewer(palette = "Accent")

#plot for deep node
ggplot(aes(y = clade_age, x = factor(num_traits), fill = char_states), data = fl) + 
  geom_violin(draw_quantiles=0.5) + 
  geom_hline(yintercept=41.8932,linetype="dotted",colour = "red") +
  geom_hline(yintercept=34.6095,linetype="dotted",colour = "red") +
  facet_wrap(~nrates) +
  xlab("Matrix Size")+
  ylab("Topological Error") +
  labs(fill="Data Type") +
  theme_bw() + 
  scale_fill_brewer(palette = "Accent")

#deep node with opposite colour/facet_wrap arrangement
ggplot(aes(y = clade_age, x = factor(num_traits), fill = nrates), data = fl) + 
  geom_violin(draw_quantiles=0.5) + 
  geom_hline(yintercept=41.8932,linetype="dotted",colour = "red") +
  geom_hline(yintercept=34.6095,linetype="dotted",colour = "red") +
  facet_wrap(~char_states) +
  xlab("Matrix Size")+
  ylab("Posterior mean age") +
  labs(fill="Number of rates") +
  theme_bw() + 
  scale_fill_brewer(palette = "Accent")

#read in other file
fl <- read.csv("replicated_node_age_sampling_kogia.tab",sep="\t")

#plot for Kogia node
ggplot(aes(y = clade_age, x = factor(num_traits), fill = char_states), data = fl) + 
    geom_violin(draw_quantiles=0.5) + 
    geom_hline(yintercept=14.119,linetype="dotted",colour = "red") +
    geom_hline(yintercept=2.8545,linetype="dotted",colour = "red") +
    facet_wrap(~nrates) +
    xlab("Matrix Size")+
    ylab("Topological Error") +
    labs(fill="Data Type") +
    theme_bw() + 
    scale_fill_brewer(palette = "Accent")

#reverse facet_wrap and colour like before
ggplot(aes(y = clade_age, x = factor(num_traits), fill = nrates), data = fl) + 
  geom_violin(draw_quantiles=0.5) + 
  geom_hline(yintercept=14.119,linetype="dotted",colour = "red") +
  geom_hline(yintercept=2.8545,linetype="dotted",colour = "red") +
  facet_wrap(~char_states) +
  xlab("Matrix Size")+
  ylab("Posterior mean age") +
  labs(fill="Number of rates") +
  theme_bw() + 
  scale_fill_brewer(palette = "Accent")








ggplot(aes(y = upper, x = factor(num_traits), fill = char_states), data = fl) + 
  geom_violin(draw_quantiles=0.5) + 
  geom_hline(yintercept=24.223,linetype="dotted",colour = "red") +
  geom_hline(yintercept=17.84,linetype="dotted",colour = "red") +
  facet_wrap(~nrates) +
  xlab("Matrix Size")+
  ylab("Topological Error") +
  labs(fill="Data Type") +
  theme_bw() + 
  scale_fill_brewer(palette = "Accent")

ggplot(aes(y = lower, x = factor(num_traits), fill = char_states), data = fl) + 
  geom_violin(draw_quantiles=0.5) + 
  geom_hline(yintercept=24.223,linetype="dotted",colour = "red") +
  geom_hline(yintercept=17.84,linetype="dotted",colour = "red") +
  facet_wrap(~nrates) +
  xlab("Matrix Size")+
  ylab("Posterior mean age") +
  labs(fill="Data Type") +
  theme_bw() + 
  scale_fill_brewer(palette = "Accent")

ggplot(aes(y = upper-lower, x = factor(num_traits), fill = char_states), data = fl) + 
  geom_violin(draw_quantiles=0.5) + 
  facet_wrap(~nrates) +
  xlab("Matrix Size")+
  ylab("Topological Error") +
  labs(fill="Data Type") +
  theme_bw() + 
  scale_fill_brewer(palette = "Accent")


