# !/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: kaiyouhu@gmail.com

import pygmo as pg


class UdpFunction:
    def __init__(self, dim):
        self.dim = dim

    def fitness(self, x):
        return [sum(x * x)]

    def get_bounds(self):
        return ([-1] * self.dim, [1] * self.dim)

    def get_name(self):
        return "Udp Function!"


algo = pg.algorithm(pg.bee_colony(gen = 20, limit = 20))
prob = pg.problem(UdpFunction(3))
pop = pg.population(prob, 10)
pop =algo.evolve(pop)
print(prob)
print(pop.champion_f)
print(pop.champion_x)
