# !/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: kaiyouhu@gmail.com

# Algorithm 1 shows the evolutionary algorithm
# used for optimizing diversity in 2018-Evolutionary
# Diversity Optimization Using Multi-Objective Indicators.


import math
import pygmo as pg
import numpy as np
from matplotlib.patches import Circle
import matplotlib.pyplot as plt


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def point(self):
        return [self.x, self.y]

    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'


def enpoint(pointlist):
    x = pointlist[0]
    y = pointlist[1]
    point = Point(x, y)
    return point


def cirpoint(point_x):
    angle = point_x / (60 * 180) * np.pi
    x = 1 - np.cos(angle)
    y = 1 - np.sin(angle)
    point = Point(x, y)
    return point


# produce a mutation point
def mutationpoint(random):
    angle = random[0] / (60 * 180) * np.pi
    x = 1 - np.cos(angle)
    y = 1 - np.sin(angle)
    return Point(x, y)


# compute the max hypervolume point
# select the least loss point to replace
def listmax(pList, hypvalue, random):
    i = 1
    j = 0
    pList = pList
    hypermax = hypvalue[0]
    while i < len(hypvalue):
        if hypermax < hypvalue[i]:
            hypermax = hypvalue[i]
            j = i
        else:
            j = j
        i = i + 1
    if j == 0:
        pList = pList
    else:
        pList[j - 1] = cirpoint(random[0]).point()
        pList = pList
    return pList


# def point draw
def drawpoint(plt, point):
    plt.plot(point.x, point.y, 'bs')
    pass
# def point draw

# def circle draw
def drawcircle(plt):
    # define circle
    x = np.linspace(0, 1, 50)
    y = 1 - np.sqrt(1 - (x - 1) * (x - 1))
    plt.plot(x, y, label='circle')
    plt.xlabel('X', fontsize=14)
    plt.ylabel('Y', fontsize=14)
    # define circle


#def circle point draw
def drawcirclepoint(plt, pList):
    # define circle point
    for point in pList:
        # angle = point_x / (60 * 180) * np.pi
        x = point[0]
        y = point[1]
        # print('x = %f and y = %f'%(x, y))
        plt.plot(x, y, 'g^')
    # define circle point
    pass


# pop hypervolumn compute
def hypsinglecompute(pList, ref_point):
    hv = pg.hypervolume(pList)
    hypvalue = hv.compute(ref_point)
    return hypvalue


# pop + 1 hypervolumn compute
def hypcompute(pList, random, ref_point):
    pList0 = pList
    lList = []
    lList.append(pList0)
    for i in range(len(pList)):
        temp = pList.copy()
        temp[i] = cirpoint(random[0]).point()
        lList.append(temp)
    # print(lList)

    hypvalue = []
    for j in range(len(lList)):
        hypvalue.append(pg.hypervolume(lList[j]).compute(ref_point.point()))
    # print(hypvalue)
    return lList, hypvalue


def algosimple():
    # define problem
    # excute the farthest point (1, 1) to (x-1)^2 + (y-1)^2 = 1

    # define refer point
    ref_point = Point(1, 1)
    # random point from radius and init group
    randoms = np.random.randint(0, 90 * 60, 8)
    pList = []
    for point_x in randoms:
        point = cirpoint(point_x).point()
        # print(point)
        pList.append(point)

    i = 1
    k = 1
    plt.rcParams.update({'figure.max_open_warning': 0})
    while i < 2000:
        flag = 0
        if math.log(i, 5).is_integer():
            flag = 1
        else:
            flag = 0
        if flag:
            plt.figure(figsize=(6, 18), dpi=80)
            plt.figure(k)
            k = k + 1
            # i-311
            plt.subplot(311)
            plt.title('Cycle-' + str(i) + '-1', fontsize=14)
            drawpoint(plt, ref_point)
            drawcircle(plt)
            drawcirclepoint(plt, pList=pList)

        # hypervolume compute
        hypsinglecompute(pList=pList, ref_point=ref_point.point())
        # hypervolumn compute

        if flag:
            # i - 312
            plt.subplot(312)
            plt.title('Cycle-' + str(i) + '-2', fontsize=14)
            drawcircle(plt)
            drawcirclepoint(plt, pList)
            drawpoint(plt, ref_point)
        # mutation point
        random = np.random.randint(0, 90 * 60, 1)
        mutatpoint = mutationpoint(random)
        if flag:
            plt.plot(mutatpoint.x, mutatpoint.y, 'bs')

        # pop + 1 hypervolumn compute
        lList, hypvalue = hypcompute(pList, random, ref_point=ref_point)
        # pop + 1 hypervolumn compute

        # loop until hyper nearly not change

        pList = listmax(pList, hypvalue, random)

        # i - 313
        if flag:
            plt.subplot(313)
            plt.title('Cycle-' + str(i) + '-3', fontsize=14)
            drawcircle(plt)
            drawcirclepoint(plt, pList)
            drawpoint(plt, ref_point)

        i = i + 1
        # pop mutation
        # plt.tight_layout()
    # loop until hyper nearly not change

    # change each children graph distance

    plt.show()

    pass


def algocon():
    pass


def drawcir1():
    x = np.linspace(0, 1, 50)
    y = np.sqrt(1 - x * x)
    plt.plot(x, y, label='circle')
    plt.xlabel('X', fontsize=14)
    plt.ylabel('Y', fontsize=14)
    plt.title('x^2+y^2=1', fontsize=14)
    plt.show()


def drawcir2():
    fig = plt.figure()
    ax = fig.add_subplot(111)
    cir1 = Circle(xy=(0.0, 0.0), radius=1, alpha=0.5)
    ax.add_patch(cir1)
    x, y = 0, 0
    ax.plot(x, y, 'ro')

    plt.axis('scaled')
    plt.axis('equal')
    plt.show()


def drawcir3():
    plt.figure(figsize=(8, 8), dpi=80)
    plt.figure(1)
    plt.subplot(211)
    plt.plot(1, 1, 'bs')

    plt.subplot(212)
    plt.plot(1, 1, 'bs')
    plt.tight_layout()

    plt.figure(2)
    plt.subplot(221)
    plt.plot(1, 1, 'bs')

    plt.subplot(224)
    plt.plot(1, 1, 'bs')
    plt.tight_layout()
    plt.show()
    pass


if __name__ == "__main__":
    # drawcir3()
    algosimple()
    pass

