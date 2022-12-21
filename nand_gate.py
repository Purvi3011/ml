# -*- coding: utf-8 -*-
"""NAND_GATE.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1eqHwmD1NwyY1bFDeHbSCt1zzYHJGDD77
"""

import numpy as np
import pandas as pd

x1 = [0,1]
x2 = [[0,0],[0,1],[1,0],[1,1]]

gates = {}
gates['X'] = x2

"""**FUNCTIONS**"""

def activation(y_hat):
    if(y_hat>=0):
        return 1
    else:
        return 0

def perceptron(x,w,b):
    y = []
    for x_hat in x:
        # print(x_hat)
        xw = np.dot(x_hat,w) + b
        # print(xw)
        y.append(activation(xw))
    return y

"""**NOT GATE**"""

def NOT(x):
    w = [-1]
    b = 0
    # print(x)
    return perceptron(x,w,b)

not_ = NOT(x1)
print('NOT', not_)

"""**NAND GATE**"""

def NAND(x):
    w = [1,1]
    b = -2
    # print(x)
    return NOT(perceptron(x,w,b))

nand = NAND(x2)
gates['NAND'] = nand
print('NAND', nand)

all_w = [[0,0],[0,1],[1,0],[1,1]]
all_b = [-2, -1, 0, 1, 2]

for w in all_w:
    for b in all_b:
        temp = perceptron(x2,w,b)
        if temp == nand:
            print(w, b, temp)

data = pd.DataFrame(gates)
print(data)
