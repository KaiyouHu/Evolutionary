# !/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: kaiyouhu@gmail.com

# the problem 5.9 in Luksan, L., and Jan Vlcek.
# “Sparse and partially separable test problems for
# unconstrained and equality constrained optimization.” (1999)

import pygmo as pg
import math


class UdpConstrained:
    # def __init__(self, dim):
    #     self.dim = dim
    def get_bounds(self):
        return ([0, 0], [6, 16])

    # Return numbers of objectives
    def get_nobj(self):
        return 2

    # Inequality Constraints
    def get_nic(self):
        return 1

    # Equality Constraints
    def get_nec(self):
        return 1

    def gradient(self, x):
        return pg.estimate_gradient_h(lambda x: self.fitness(x), x)

    def fitness(self, x):
        obj1 = x[0] + x[1]
        obj2 = - (80 * x[0] + 100 * x[1])
        ce1 = 4 * x[0] + 2 * x[1] - 48
        ci1 = 4 * x[0] + 5 * x[1] - 80
        return [obj1, obj2, ce1, ci1]

    # Return function name
    def get_name(self):
        return "UdpConstrained icode function"

prob = pg.problem(UdpConstrained())
print(prob)


def method_a():
    algo = pg.algorithm(uda=pg.nlopt('auglag'))
    algo.extract(pg.nlopt).local_optimizer = pg.nlopt('var2')
    algo.set_verbosity(200)  # in this case this correspond to logs each 200 objevals
    pop = pg.population(prob=UdpConstrained(), size=1)
    pop.problem.c_tol = [1E-6] * 2
    pop = algo.evolve(pop)


def method_b():
    algo = pg.algorithm(uda=pg.mbh(pg.nlopt("slsqp"), stop=20, perturb=.2))
    print(algo)
    algo.set_verbosity(1)  # in this case this correspond to logs each 1 call to slsqp
    pop = pg.population(prob=UdpConstrained(), size=1)
    pop.problem.c_tol = [1E-6] * 2
    pop = algo.evolve(pop)


def method_c():
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


if __name__ == "__main__":
    method_c()
    # pass
