[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

import thinkstats2
import sys
import numpy as np
import nsfg
import thinkplot
import pprint
import math

df = nsfg.ReadFemPreg()
preg = nsfg.ReadFemPreg()
live = preg[preg.outcome == 1]
firsts = live[live.birthord == 1]
others = live[live.birthord != 1]

first_hist_inlbs = thinkstats2.Hist(firsts.birthwgt_lb)

others_hist_inlbs = thinkstats2.Hist(others.birthwgt_lb)


mean1 = firsts.birthwgt_lb.mean()
meanother = others.birthwgt_lb.mean()

Manually computed Cohnens d...-0.108450242544

In this example the Cohens' d was -0.108450242544
For the pregnancy example, the difference in means is 0.029 standard deviations,
which is small.

I think with a negative Cohen's d, that indicates that the 2nd group in this
case others, meaning all kids after the 1st one, were heavier.

diff = mean1 - meanother

var1 = firsts.birthwgt_lb.var()

var2 = others.birthwgt_lb.var()

n1, n2 = len(firsts.birthwgt_lb), len(others.birthwgt_lb)

pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)

d = diff / math.sqrt(pooled_var)
print d
