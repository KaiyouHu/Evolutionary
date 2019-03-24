# !/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: kaiyouhu

import pygmo as pg


def main():
    hv = pg.hypervolume([[1, 0], [0.5, 0.5], [0, 1], [1.5, 0.75]])
    ref_point = [2, 2]
    hv_value = hv.compute(ref_point)
    print(hv_value)
    return 0


if __name__ == "__main__":
    main()