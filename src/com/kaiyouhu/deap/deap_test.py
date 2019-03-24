# !/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: kaiyouhu
# 导入deap测试

import random
from deap import base, creator, tools
IND_SIZE = 10

creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()
toolbox.register("attribute", random.random)
toolbox.register("individual", tools.initRepeat, creator.Individual,
                 toolbox.attribute, n=IND_SIZE)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)