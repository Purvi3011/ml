# -*- coding: utf-8 -*-
"""ADAM.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1j7AtVlsjagn_hG0kgAV6xzjGaP-xCqtI
"""

import numpy as np
import pandas as pd
from sklearn import datasets
import matplotlib.pyplot as plt

def sigmoid(Y_in):
    return 1 / (1 + np.exp(-Y_in))

def find_Yhat(X, w, b):
    # IF LIST OF LIST / LIST OF TUPLE IS USED, THEN INDIVIDUAL LIST/TUPLE SHOULD BE HANDLED DIFFERENTLY
    if type(X) in [type([1]), type((1,2))]:
        Y_in = np.dot(X, w) + b
    else:
        Y_in = X * w + b

    return sigmoid(Y_in)

def delta_w(X, Y_true, Y_pred):
  return -2 * (Y_true - Y_pred) * Y_pred * (1 - Y_pred) * X

def delta_b(Y_true, Y_pred):
  return -2 * (Y_true - Y_pred) * Y_pred * (1 - Y_pred)

X = [0.5, 2.5]
Y = [0.2, 0.9]

n_epochs = 300
df = pd.DataFrame([(x, y) for x, y in zip(X, Y)], columns = ['X', 'Y'])
df.head()



"""### **ADAM**

*UPDATE WEIGHTS AFTER EACH ROWS WITH CHANGING LEARNING RATE GRADUALLY OVER TIME WITH WEIGHTS*
"""

def adam(X, Y, noofepochs = 300, b1 = 0.5, b2 = 0.5):
    w = -2; alpha = 1; b = -2;
    e = 0.01
    mw, mb, vw, vb = 0, 0, 0, 0

    # LIST FOR ALL EPOCHS
    error_mega_list = []
    weights_mega_list = []
    bias_mega_list = []
        
    for i in range(noofepochs):
        # LIST FOR EACH EPOCH
        error_list = []
        for x, y in zip(X, Y):
            Y_hat = find_Yhat(x, w, b)
            error_list.append((y - Y_hat) ** 2)

            dw = delta_w(x, y, Y_hat)
            db = delta_b(y, Y_hat)

            mw = b1 * mw + (1 - b1) * dw
            mb = b1 * mb + (1 - b1) * db
            
            vw = b2 * vw + (1 - b2) * (dw ** 2)
            vb = b2 * vb + (1 - b2) * (db ** 2)

            w += (-alpha / (vw + e)**0.5) * mw
            b += (-alpha / (vb + e)**0.5) * mb


        error_mega_list.append(error_list)
        weights_mega_list.append(w)
        bias_mega_list.append(b)
        
    return error_mega_list, weights_mega_list, bias_mega_list

errors_adam, weights_adam, biases_adam = adam(X, Y, n_epochs)

print(round(np.mean(errors_adam[-1]),5))
print(round(weights_adam[-1],3))
print(round(biases_adam[-1],3))

plt.title("WEIGHT VS EPOCHS")
epoch_range = [i for i in range(n_epochs)]
weight_range = [w for w in weights_adam]
plt.plot(epoch_range, weight_range)
plt.xlabel('EPOCHS ')
plt.ylabel('WEIGHT')
plt.show()

