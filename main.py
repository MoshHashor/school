import pandas
import numpy as np
import scipy.constants
import math

# print(scipy.constants.golden)
# break_point= 1
# global break_point

def golden_ratio(v, j, a, b, k=0):
    if k >= 100:
        print('stop')
    if b - a <= 0.05:
        result = np.array([a, b, k])
        print(result)
        return result
    c_k = b - (1/scipy.constants.golden)*(b-a)
    d_k = a + (1/scipy.constants.golden)*(b-a)
    if g_to_f(v, j, c_k) > g_to_f(v, j, d_k):
        k += 1
        golden_ratio(v, j, a, d_k, k)
    else:
        k += 1
        golden_ratio(v, j, c_k, b, k)

def g(v):
    print(v[0]+v[1]*(math.sin(v[1])))
    return v[0]+v[1]*(math.sin(v[1]))

def g_to_f(v, k, x):
    v[k] = x
    return g(v)

def dimensions(v=[1, 1]):
    for j in range(len(v)):
        u = golden_ratio(v, j, 0, 3.14)
        print(u)
        v[j] = (u[0]+u[1])/2

print(dimensions([5,0]))
