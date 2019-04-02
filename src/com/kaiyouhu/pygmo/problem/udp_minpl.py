# !/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: kaiyouhu@gmail.com

# a modified instance of the problem 5.9 in Luksan, L., and Jan Vlcek.
# “Sparse and partially separable test problems for unconstrained
# and equality constrained optimization.” (1999)


import pygmo as pg
import math


class my_minlp:

    # Return function name
    def get_name(self):
        return "Function minpl"

    def get_bounds(self):
        return ([-5] * 6, [5] * 6)

    # Inequality Constraints
    def get_nic(self):
        return 6

    # Integer Dimension
    def get_nix(self):
        return 2

    def fitness(self, x):
        obj = 0
        for i in range(3):
            obj += (x[2 * i - 2] - 3) ** 2 / 1000. - (x[2 * i - 2] - x[2 * i - 1]) + math.exp(20. * (x[2 * i - 2] - x[2 * i - 1]))
        ce1 = 4 * (x[0] - x[1]) ** 2 + x[1] - x[2] ** 2 + x[2] - x[3] ** 2
        ce2 = 8 * x[1] * (x[1] ** 2 - x[0]) - 2 * (1 - x[1]) + 4 * (x[1] - x[2]) ** 2 + x[0] ** 2 + x[2] - x[3] ** 2 + x[3] - x[4] ** 2
        ce3 = 8 * x[2] * (x[2] ** 2 - x[1]) - 2 * (1 - x[2]) + 4 * (x[2] - x[3]) ** 2 + x[1] ** 2 - x[0] + x[3] - x[4] ** 2 + x[0] ** 2 + x[4] - x[5] ** 2
        ce4 = 8 * x[3] * (x[3] ** 2 - x[2]) - 2 * (1 - x[3]) + 4 * (x[3] - x[4]) ** 2 + x[2] ** 2 - x[1] + x[4] - x[5] ** 2 + x[1] ** 2 + x[5] - x[0]
        ci1 = 8 * x[4] * (x[4] ** 2 - x[3]) - 2 * (1 - x[4]) + 4 * (x[4] - x[5]) ** 2 + x[3] ** 2 - x[2] + x[5] + x[2] ** 2 - x[1]
        ci2 = -(8 * x[5] * (x[5] ** 2 - x[4]) - 2 * (1 - x[5]) + x[4] ** 2 - x[3] + x[3] ** 2 - x[4])
        return [obj, ce1, ce2, ce3, ce4, ci1, ci2]


def _gradient(self, x):
    return pg.estimate_gradient_h(lambda x: self.fitness(x), x)


if __name__=="__main__":
    my_minlp.gradient = _gradient
    # We need to reconstruct the problem as we changed its definition (adding the gradient)
    prob = pg.problem(my_minlp())
    prob.c_tol = [1e-8]*6
    prob = pg.problem(my_minlp())
    print(prob)

    # We run 20 instances of the optimization in parallel via a default archipelago setup
    archi = pg.archipelago(n=20, algo=pg.ipopt(), prob=my_minlp(), pop_size=1)
    archi.evolve(2);
    archi.wait()
    # We get the best of the parallel runs
    a = archi.get_champions_f()
    a2 = sorted(archi.get_champions_f(), key=lambda x: x[0])[0]
    best_isl_idx = [(el == a2).all() for el in a].index(True)
    x_best = archi.get_champions_x()[best_isl_idx]
    f_best = archi.get_champions_f()[best_isl_idx]
    print("Best relaxed solution, x: {}".format(x_best))
    print("Best relaxed solution, f: {}".format(f_best))


