import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import sys

if len(sys.argv) != 2:
    print "usage: "+sys.argv[0]+" <table with heights and HPD ranges>"
    sys.exit(0)


def plot_mean_heights(heights):
    ax = sns.lmplot(x="prior_mean",y="posterior_mean",data=heights)
    plt.show()
    sys.exit(0)

if __name__ == "__main__":
    heights = pd.read_table(sys.argv[1])
    plot_mean_heights(heights)
