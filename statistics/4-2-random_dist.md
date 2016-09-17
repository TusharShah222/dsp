[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

from scipy.stats import uniform

import matplotlib.pyplot as plt

import thinkstats2

import thinkplot

rv = uniform()

r = uniform.rvs(size=1000)

print r

pmf = thinkstats2.Pmf(r, label='PMF')

cdf = thinkstats2.Cdf(r, label='CDF')

thinkplot.PrePlot(2)

thinkplot.Pmfs([pmf, cdf])

thinkplot.Cdfs([pmf, cdf])

thinkplot.Show(xlabel='random values', ylabel='frequencies')

The distribution of 1000 random numbers seems to be uniform.
The CDF is approximately a straight line, which means that the distribution is uniform.

