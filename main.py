import scipy.constants
import math
previous_vector = [1, 0, 1]
current_vector = [1, 90, 1]

def golden_ratio(v, j, a, b, k=0):
    if k < 100 and (b - a) > 0.05:
        print(f'(b-a, k):{(b-a, k)}')
        c_k = b - (1/scipy.constants.golden)*(b-a)
        d_k = a + (1/scipy.constants.golden)*(b-a)
        if g_to_f(v, j, c_k) > g_to_f(v, j, d_k):
            k += 1
            return golden_ratio(v, j, a, d_k, k)
        else:
            k += 1
            return golden_ratio(v, j, c_k, b, k)
    else:
        print(f'(a, b, k):{(a,b,k)}')
        print(f'u_wanted:{((a + b)/2)}')
        return ((a + b)/2)

def g(v):
    print(f'g(v):{v[0]+v[2]+v[1]*(math.sin(v[1]))}')
    return v[0]+v[2]+v[1]*(math.sin(v[1]))

def g_to_f(v, k, x):
    v[k] = x
    return g(v)

def dimensions(v):
    global previous_vector, current_vector
    previous_vector = v
    for j in range(len(v)):
        u = golden_ratio(v, j, 0, 3.14)
        print(f'u:{u}')
        v[j] = u
    current_vector = v

def z(k, i = 0):
    delta = g(current_vector) - g(previous_vector)
    print(f'delta:{delta}')
    while i < k and delta > 0.05:
        dimensions(current_vector)
        i += 1
    return g(current_vector)
if __name__ == '__main__':
    print(f'z(50):{z(10)}')
