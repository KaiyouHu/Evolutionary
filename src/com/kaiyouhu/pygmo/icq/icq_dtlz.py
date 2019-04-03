# !/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: kaiyouhu@gmail.com


import pygmo as pg
import matplotlib.pyplot as plt


def draw_dtlz(prob_id, dim=5, fdim=3, alph=0.5, individual_size=20):
    udp = pg.dtlz(prob_id=prob_id, dim=dim, fdim=fdim)
    pop = pg.population(udp, individual_size)
    udp.plot(pop)  # doctest: +SKIP
    pass


if __name__ == "__main__":
    for index in range(5):
        draw_dtlz(prob_id=(index + 1))
    pass