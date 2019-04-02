# !/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: kaiyouhu@gmail.com

import pygmo as pg


def hv_function():
    hv = pg.hypervolume([[1, 0], [0.5, 0.5], [0, 1], [1.5, 0.75]])
    ref_point = [2, 2]
    hv_compute_value = hv.compute(ref_point)
    print("ref_point compute:")
    print(hv_compute_value)

    hv_exclusive_value = hv.exclusive(1, ref_point)
    print("ref_point 1 exclusive:")
    print(hv_exclusive_value)

    hv_exclusive_value = hv.exclusive(0, ref_point)
    print("ref_point 0 exclusive:")
    print(hv_exclusive_value)

    hv_least_contributor_value = hv.least_contributor(ref_point)
    print("ref_point least_contributor:")
    print(hv_least_contributor_value)
    hv_greatest_contributor_value = hv.greatest_contributor(ref_point)
    print("ref_point greatest_contributor:")
    print(hv_greatest_contributor_value)
    hv_contributions_value = hv.contributions(ref_point)
    print("ref_point contributions:")
    print(hv_contributions_value)

    return 0


def hv_pop():
    # ref_point = [2, 2]
    # points = [[1, 2], [0.5, 3], [0.1, 3.1]]
    udp = pg.dtlz(prob_id=1, dim=5, fdim=3)
    pop = pg.population(prob=udp, size=2)
    # hv = pg.hypervolume(pop=pop)
    udp.plot(pop)
    print(pop)


def hv_point_pop():
    ref_point = [2, 2]
    points = [[1, 2], [0.5, 3], [0.1, 3.1]]
    hv = pg.hypervolume(points)

    udp = pg.dtlz(prob_id=1, dim=5, fdim=4)
    pop = pg.population(prob=udp, size=40)
    # hv = pg.hypervolume(pop=pop)
    udp.plot(pop)
    print(pop)


if __name__ == "__main__":
    hv_pop()
