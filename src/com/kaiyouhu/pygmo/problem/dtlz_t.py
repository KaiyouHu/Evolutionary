# !/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: kaiyouhu


import pygmo as pg


def dtlz_p1():
    udp = pg.dtlz(prob_id=1, dim=5, fdim=3)
    pop = pg.population(udp, 40)
    hv = pg.hypervolume(pop)
    udp.plot(pop)  # doctest: +SKIP


def dtlz_p2():
    udp = pg.dtlz(prob_id=2, fdim=3, dim=5)
    pop = pg.population(udp, 40)
    udp.plot(pop)  # doctest: +SKIP


def dtlz_p3():
    udp = pg.dtlz(prob_id=3, fdim=3, dim=5)
    pop = pg.population(udp, 40)
    udp.plot(pop)  # doctest: +SKIP


def dtlz_p4():
    udp = pg.dtlz(prob_id=4, fdim=3, dim=5)
    pop = pg.population(udp, 40)
    udp.plot(pop)  # doctest: +SKIP


def dtlz_p5():
    udp = pg.dtlz(prob_id=5, fdim=3, dim=5)
    pop = pg.population(udp, 40)
    udp.plot(pop)  # doctest: +SKIP


def dtlz_p6():
    udp = pg.dtlz(prob_id=6, fdim=3, dim=5)
    pop = pg.population(udp, 40)
    udp.plot(pop)  # doctest: +SKIP


if __name__ == "__main__":
    dtlz_p4()
