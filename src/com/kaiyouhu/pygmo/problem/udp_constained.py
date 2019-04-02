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
        return ([-5] * 6, [5] * 6)

    # Inequality Constraints
    def get_nic(self):
        return 2

    # Equality Constraints
    def get_nec(self):
        return 4

    def gradient(self, x):
        return pg.estimate_gradient_h(lambda x: self.fitness(x), x)

    def fitness(self, x):
        obj = 0
        for i in range(3):
            obj += (x[2 * i - 2] - 3) ** 2 / 1000. - (x[2 * i - 2] - x[2 * i - 1])\
                + math.exp(20. * (x[2 * i - 2] - x[2 * i - 1]))
        ce1 = 4 * (x[0] - x[1]) ** 2 + x[1] - x[2] ** 2 + x[2] - x[3] ** 2
        ce2 = 8 * x[1] * (x[1] ** 2 - x[0]) - 2 * (1 - x[1]) + 4 * (x[1] - x[2]) ** 2\
            + x[0] ** 2 + x[2] - x[3] ** 2 + x[3] - x[4] ** 2
        ce3 = 8 * x[2] * (x[2] ** 2 - x[1]) - 2 * (1 - x[2]) + 4 * (x[2] - x[3]) ** 2\
            + x[1] ** 2 - x[0] + x[3] - x[4] ** 2 + x[0] ** 2 + x[4] - x[5] ** 2
        ce4 = 8 * x[3] * (x[3] ** 2 - x[2]) - 2 * (1 - x[3]) + 4 * (x[3] - x[4]) ** 2 + x[2] ** 2\
            - x[1] + x[4] - x[5] ** 2 + x[1] ** 2 + x[5] - x[0]
        ci1 = 8 * x[4] * (x[4] ** 2 - x[3]) - 2 * (1 - x[4]) + 4 * (x[4] - x[5]) ** 2 + x[3] ** 2\
            - x[2] + x[5] + x[2] ** 2 - x[1]
        ci2 = -(8 * x[5] * (x[5] ** 2 - x[4]) - 2 * (1 - x[5]) + x[4] ** 2 - x[3] + x[3] ** 2 - x[4])
        return [obj, ce1, ce2, ce3, ce4, ci1, ci2]


prob = pg.problem(UdpConstrained())
print(prob)


def method_a():
    algo = pg.algorithm(uda=pg.nlopt('auglag'))
    algo.extract(pg.nlopt).local_optimizer = pg.nlopt('var2')
    algo.set_verbosity(200)  # in this case this correspond to logs each 200 objevals
    pop = pg.population(prob=UdpConstrained(), size=1)
    pop.problem.c_tol = [1E-6] * 6
    pop = algo.evolve(pop)


def method_b():
    algo = pg.algorithm(uda=pg.mbh(pg.nlopt("slsqp"), stop=20, perturb=.2))
    print(algo)
    algo.set_verbosity(1)  # in this case this correspond to logs each 1 call to slsqp
    pop = pg.population(prob=UdpConstrained(), size=1)
    pop.problem.c_tol = [1E-6] * 6
    pop = algo.evolve(pop)


if __name__ == "__main__":
    method_b()
