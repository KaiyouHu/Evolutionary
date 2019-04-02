# !/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: kaiyouhu@gmail.com

# a test function for multi - objective optimization being introduced
# in Schaffer, J.David (1984).Some experiments
# in machine learning using vector evaluated genetic algorithms
# (artificial intelligence, optimization, adaptation, pattern recognition) (PhD).Vanderbilt University


import pygmo as pg


class Schaffer:

    # Define objectives
    def fitness(self, x):
        f1 = x[0] ** 2
        f2 = (x[0] - 2) ** 2
        return [f1, f2]

    # Return number of objectives
    def get_nobj(self):
        return 2

    # Return bounds of decision variables
    def get_bounds(self):
        return ([0] * 1, [2] * 1)

    # Return function name
    def get_name(self):
        return "Schaffer function N.1"

prob = pg.problem(Schaffer())
print(prob)

# create population
pop = pg.population(prob, size=20)
# select algorithm
algo = pg.algorithm(pg.nsga2(gen=40))
# run optimization
pop = algo.evolve(pop)
# extract results
fits, vectors = pop.get_f(), pop.get_x()
# extract and print non-dominated fronts
ndf, dl, dc, ndr = pg.fast_non_dominated_sorting(fits)
print(fits)
print(vectors)
