# !/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: kaiyouhu@gmail.com


from pygmo import *
from matplotlib import pyplot as plt


udp = zdt(prob_id=1)
pop = population(prob=udp, size=10, seed=3453412)
ndf, dl, dc, ndl = fast_non_dominated_sorting(pop.get_f())
pop = population(udp, 100)
ax = plot_non_dominated_fronts(pop.get_f())
plt.ylim([0, 6])
plt.title("ZDT1: random initial population")
algo = algorithm(moead(gen=250))
pop = algo.evolve(pop)
ax = plot_non_dominated_fronts(pop.get_f())
plt.title("ZDT1: ... and the evolved population")
ndf, dl, dc, ndl = fast_non_dominated_sorting(pop.get_f())
plt.show()