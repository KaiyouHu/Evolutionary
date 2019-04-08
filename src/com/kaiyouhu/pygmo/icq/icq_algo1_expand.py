# !/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: kaiyouhu@gmail.com

# Algorithm 1 shows the evolutionary algorithm
# used for optimizing diversity in 2018-Evolutionary
# Diversity Optimization Using Multi-Objective Indicators.


import math
import pygmo as pg
import numpy as np
from matplotlib import cm
from matplotlib.patches import Circle
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


class Point(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def point(self):
        return [self.x, self.y, self.z]

    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ', ' + str(self.z) + ')'


def enpoint(pointlist):
    x = pointlist[0]
    y = pointlist[1]
    z = pointlist[2]
    point = Point(x, y, z)
    return point


def spherepoint(point_radius):
    u = point_radius[0] / (180 * 60) * np.pi
    v = point_radius[1] / (180 * 60) * np.pi
    r = 1
    x = r * np.cos(u) * np.sin(v) + 1
    y = r * np.sin(u) * np.sin(v) + 1
    z = r * np.cos(v) + 1
    point = Point(x, y, z)
    return point


# produce a mutation point
def multirand(*args, size=1):
    # u = theta (θ） 正z轴来看自x轴按逆时针方向转到OM所转过的角
    # v = Phi (φ) 有向线段OP与z轴正向的夹角
    randoms = []
    if size == 1:
        u = np.random.randint(args[0][0], args[0][1], 1)[0]
        v = np.random.randint(args[1][0], args[1][1], 1)[0]
        randoms = [u, v]
        return randoms
    else:
        for index in range(size):
            u = np.random.randint(args[0][0], args[0][1], 1)[0]
            v = np.random.randint(args[1][0], args[1][1], 1)[0]
            random = [u, v]
            randoms.append(random)
        return randoms


# produce a mutation point
def mutationpoint(random):
    # u = theta (θ） 正z轴来看自x轴按逆时针方向转到OM所转过的角
    # v = Phi (φ) 有向线段OP与z轴正向的夹角
    u = random[0] / (180 * 60) * np.pi
    v = random[1] / (180 * 60) * np.pi
    r = 1
    x = r * np.cos(u) * np.sin(v) + 1
    y = r * np.sin(u) * np.sin(v) + 1
    z = r * np.cos(v) + 1
    return Point(x, y, z)


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
        pList[j - 1] = spherepoint(random).point()
        pList = pList
    return pList


# def point draw
def drawpoint(plt, point):
    plt.scatter(point.x, point.y, zs=point.z, s=60, color='b', marker='p')
    pass


# def circle point draw
def drawspherepoint(plt, pList):
    # define sphere point
    for point in pList:
        x = point[0]
        y = point[1]
        z = point[2]
        plt.scatter(x, y, zs=z, s=60, color='black', marker='o')
    # define sphere point
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
        temp[i] = spherepoint(random).point()
        lList.append(temp)
    # print(lList)

    hypvalue = []
    for j in range(len(lList)):
        hypvalue.append(pg.hypervolume(lList[j]).compute(ref_point.point()))
    # print(hypvalue)
    return lList, hypvalue


def algosimple():
    # define problem
    # excute the farthest point (1, 1) to (x-1)^2 + (y-1)^2 + (z-1)^2 = 1

    # define refer point
    ref_point = Point(x=1, y=1, z=1)
    # random point from radius and init group
    # randoms = np.random.randint(0, 90 * 60, size=(8, 2))
    randoms = multirand([180 * 60, 270 * 60], [90 * 60, 180 * 60], size=8)
    pList = []
    for point_radius in randoms:
        # point_radius u(θ) v(φ)
        point = spherepoint(point_radius).point()
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
            fig = plt.figure(k)
            k = k + 1
            # i-311
            plt.subplot(311, projection='3d')
            plt.title('Sphere-' + str(i) + '-1', fontsize=14)
            drawpoint(plt, ref_point)
            drawsphere(plt)
            drawspherepoint(plt, pList=pList)

        # hypervolume compute
        hypsinglecompute(pList=pList, ref_point=ref_point.point())
        # hypervolumn compute

        if flag:
            # i - 312
            plt.subplot(312, projection='3d')
            plt.title('Sphere-' + str(i) + '-2', fontsize=14)
            drawsphere(plt)
            drawspherepoint(plt, pList)
            drawpoint(plt, ref_point)
        # mutation point
        # random = np.random.randint(0, 90 * 60, size=(1, 2))
        random = multirand([180 * 60, 270 * 60], [90 * 60, 180 * 60], size=1)
        mutatpoint = mutationpoint(random)
        if flag:
            plt.scatter(mutatpoint.x, mutatpoint.y, zs=mutatpoint.z, s=60, c='black',marker='+')

        # pop + 1 hypervolumn compute
        lList, hypvalue = hypcompute(pList, random, ref_point=ref_point)
        # pop + 1 hypervolumn compute

        # loop until hyper nearly not change

        pList = listmax(pList, hypvalue, random)

        # i - 313
        if flag:
            plt.subplot(313, projection='3d')
            plt.title('Sphere-' + str(i) + '-3', fontsize=14)
            drawsphere(plt)
            drawspherepoint(plt, pList)
            drawpoint(plt, ref_point)

        i = i + 1
        # pop mutation
        fig.tight_layout()
    # loop until hyper nearly not change

    # change each children graph distance
    fig.tight_layout()
    plt.show()

    pass


# draw spherical surface
def drawsphere(plt):
    # plt.figure(figsize=(6, 6), dpi=80)
    # fig = plt.figure(1)
    # ===========
    # first plot
    # ===========
    # plt.plot(1, projection='3d')
    ax = plt.gca()
    ax.scatter(1, 1, 1, c='g')
    # ax.scatter(0.75, 0.75, 0.75, c='black')
    ax.set_xlabel('Y')
    plt.xlim((0, 1))
    ax.set_ylabel('X')
    plt.ylim((0, 1))
    ax.invert_yaxis()
    ax.set_zlabel('Z')  # 坐标轴

    q = 0  # defines upper starting point of the spherical segment
    p = 1  # defines ending point of the spherical segment as ratio
    # u = theta (θ） 正z轴来看自x轴按逆时针方向转到OM所转过的角
    # v = Phi (φ) 有向线段OP与z轴正向的夹角
    u = np.linspace(1 * np.pi, 1.5 * np.pi, 100)
    v = np.linspace(0.5 * np.pi, 1 * p * np.pi, p * 100)
    r = 1
    X = r * np.outer(np.cos(u), np.sin(v)) + 1
    Y = r * np.outer(np.sin(u), np.sin(v)) + 1
    Z = r * np.outer(np.ones(np.size(u)), np.cos(v)) + 1

    surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, color='azure', alpha=0.4)
    # plt.show()
    pass


if __name__ == "__main__":
    # drawsphere()
    algosimple()
    # print(multirand([1, 5], [2, 6], size=1))
    pass

