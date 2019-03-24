# !/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: kaiyouhu

from deap.tools.indicator import hypervolume as hv
import numpy as np


def main():
    xarray = [1, 3, 2]
    numset = np.asarray(xarray)
    hv(numset)
    print(" 0 ")
    # print(yarray)
    print(" 1 ")
    return xarray


if __name__ == "__main__":
    main()