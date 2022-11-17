import pandas
import numpy as np
import scipy.constants
import math

# The target of the code below is to find (by using numerical methods) an optimal vector (or close to optimal) to a given function (g)
# we first insert a random vector to dimensions function and this function find the best value for each dimension by using the golden ratio function.


# The function below gets a vector and returns a scalar
def g(v):
    print(v[0]+v[1]*(math.sin(v[1])))
    return v[0]+v[1]*(math.sin(v[1]))

# The function below gets a vector, an index and a scalar. The function enters the value x in cell k and returns g of the updated vector 
def g_to_f(v, k, x):
    v[k] = x
    return g(v)

# The function below gets a vector, index - for locating the exact cell in the vector, left border, right border, 
# and another index - for allowing to iterate in the function.
# The function 
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
        
# the function gets a vector and for every cell in the vector it performes golden_ration function on it
def dimensions(v=[1, 1]):
    for j in range(len(v)):
        u = golden_ratio(v, j, 0, 3.14)
        print(u)
        v[j] = (u[0]+u[1])/2

print(dimensions([5,0]))
