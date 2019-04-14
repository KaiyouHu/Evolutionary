# !/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: kaiyouhu@gmail.com


from pygmo import *
import pygmo as pg
import matplotlib.pyplot as plt


# user define problem
# y = f(x1, x2) = x1^2 + x2^2
# -10 <= x1, x2 <= 10
# evolve the min value of y
class UDProblem:

    def get_bounds(self):
        return [-10] * 2, [10] * 2

    # Return numbers of objectives
    def get_nobj(self):
        return 1

    def gradient(self, x):
        return pg.estimate_gradient_h(lambda x: self.fitness(x), x)

    def fitness(self, x):
        obj1 = x[0]*x[0] + x[1]*x[1]
        return [obj1]

    # Return function name
    def get_name(self):
        return "UDProblem"


def draw_pso():
    
    algo = algorithm(pso(gen=500))
    algo.set_verbosity(50)
    prob = problem(UDProblem())  # rosenbrock(10)
    pop = population(prob, 20)
    # print(pop)
    pop = algo.evolve(pop)
    pass


if __name__ == '__main__':
    draw_pso()
    # prob = problem(UDProblem())
    # pop = population(prob,  size=20)
    # # print(prob)
    # print(pop)
    pass
