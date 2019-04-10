# !/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: kaiyouhu@gmail.com


# DTLZ2:
# The search space is continuous, unimodal and the problem is not deceptive.
# dim=2

from platypus import NSGAII, DTLZ2, RandomGenerator
import matplotlib.pyplot as plt
import pygmo as pg
import math


# compute the max hyper volume point
# select the least loss point to replace
def list_max(point_list, hyper_value, mutate_point):
    i = 1
    j = 0
    point_list = point_list
    hyper_max = hyper_value[0]
    while i < len(hyper_value):
        if hyper_max < hyper_value[i]:
            hyper_max = hyper_value[i]
            j = i
        else:
            j = j
        i = i + 1
    if j == 0:
        point_list = point_list
    else:
        point_list[j - 1] = mutate_point
        point_list = point_list
    return point_list, hyper_max


# def point draw
def draw_point(plt, point):
    plt.scatter(point[0], point[1], s=60, color='b', marker='p')
    pass


# def circle point draw
def draw_point_list(plt, point_list):
    # define sphere point
    for point in point_list:
        x = point[0]
        y = point[1]
        plt.scatter(x, y, s=60, color='black', marker='o')
    pass


# pop + 1 hyper volume compute
def hyp_compute(point_list, mutate_point, reference_point):

    point_collection = list()
    point_collection.append(point_list)
    for i in range(len(point_list)):
        temp = point_list.copy()
        temp[i] = mutate_point
        point_collection.append(temp)

    hyper_value = []
    for j in range(len(point_collection)):
        hyper_value.append(pg.hypervolume(point_collection[j]).compute(reference_point))
    return point_collection, hyper_value


# compute the max hyper volume point
# select the least loss point to replace
def list_max(point_list, hyp_value, mutate_point):
    i = 1
    j = 0
    hyper_max = hyp_value[0]
    while i < len(hyp_value):
        if hyper_max < hyp_value[i]:
            hyper_max = hyp_value[i]
            j = i
        else:
            j = j
        i = i + 1
    if j == 0:
        point_list = point_list
    else:
        point_list[j - 1] = mutate_point
        point_list = point_list
    return point_list, hyper_max


# generate mutation point
def generate_point(nobjs, population_size):
    # define the problem definition
    problem = DTLZ2(nobjs=nobjs)
    # instantiate the optimization algorithm
    algorithm = NSGAII(problem, population_size=population_size)
    algorithm.run(1000)
    # mutate_point = RandomGenerator().generate(problem=problem)
    return algorithm.result[0].objectives._data
    pass


def write_pareto(problem, algorithm):

    # optimize the problem using 10,000 function evaluations
    algorithm.run(10000)

    objectives = []
    # print pareto front
    for solution in algorithm.result:
        # solution.objectives is typeof(FixedLengthArray)
        # _data is private data, although it can be visited directly
        # the true way may be as follow
        # objectives.append([solution.objectives.__getitem__(0), solution.objectives.__getitem__(1)])
        objectives.append(solution.objectives._data)
    return objectives


def draw_pareto():
    # define the problem definition
    problem = DTLZ2(nobjs=2)

    # instantiate the optimization algorithm
    algorithm = NSGAII(problem, population_size=20)

    # optimize the problem using 10,000 function evaluations
    algorithm.run(10000)

    # plot the results using matplotlib
    plt.figure(figsize=(6, 6), dpi=80)
    plt.figure()
    plt.subplot(111)
    plt.scatter([s.objectives[1] for s in algorithm.result],
                [s.objectives[0] for s in algorithm.result],
                s=36, color='blue')
    plt.xlim([0, 1.1])
    plt.ylim([0, 1.1])
    plt.xlabel("$f_1(x)$")
    plt.ylabel("$f_2(x)$")

    plt.show()


def main():

    # define refer point
    reference_point = [1.5, 1.5]

    # define the problem definition
    problem = DTLZ2(nobjs=2)

    # instantiate the optimization algorithm
    algorithm = NSGAII(problem, population_size=5)

    point_list = write_pareto(problem, algorithm)
    i = 1
    k = 1
    plt.rcParams.update({'figure.max_open_warning': 0})
    while i <= 3125:  # 1 5 25 625 3125 15625
        if math.log(i, 5).is_integer():
            flag = 1
        else:
            flag = 0
        if flag:
            plt.figure(figsize=(6, 18), dpi=80)
            fig = plt.figure(k)
            k = k + 1
            # i-311
            plt.subplot(311)
            plt.title('dtlz2-' + str(i) + '-1', fontsize=14)
            draw_point(plt, reference_point)
            # drawsphere(plt)
            draw_point_list(plt, point_list=point_list)

        if flag:
            # i - 312
            plt.subplot(312)
            plt.title('dtlz2-' + str(i) + '-2', fontsize=14)
            # drawsphere(plt)
            draw_point_list(plt, point_list)
            draw_point(plt, reference_point)
        # mutation point
        mutate_point = generate_point(nobjs=2, population_size=1)
        if flag:
            plt.scatter(mutate_point[0], mutate_point[1], s=60, c='black', marker='+')

        # pop + 1 hyper volume compute
        point_collection, hyp_value = hyp_compute(point_list, mutate_point, reference_point=reference_point)
        # pop + 1 hyper volume compute

        # loop until hyper nearly not change

        point_list, hyper_max = list_max(point_list, hyp_value, mutate_point)

        # i - 313
        if flag:
            plt.subplot(313)
            plt.title('dtlz2-' + str(i) + '-3', fontsize=14)
            # drawsphere(plt)
            draw_point_list(plt, point_list)
            draw_point(plt, reference_point)
            # print hyp_value
            print('Current order is %d, and the hyper_max is %10f' % (i, hyper_max))

        i = i + 1
        # pop mutation
        fig.tight_layout()
    # loop until hyper nearly not change

    # change each children graph distance
    fig.tight_layout()
    plt.show()
    pass


if __name__ == '__main__':
    main()
    pass


