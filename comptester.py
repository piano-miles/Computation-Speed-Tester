import random
import time

import matplotlib.pyplot as plt
from tqdm import tqdm


def test(A, B, C, D):
    E = 'lambda x: '

    F = []
    G = []
    H = []
    I = []

    k1 = eval(E+A)
    k2 = eval(E+B)
    k3 = eval(E+'x')

    for K in tqdm(range(D)):
        J = time.time()*1000
        for j in range(C):
            x = random.random()*4-2
            y = k1(x)

        L = time.time()*1000
        for j in range(C):
            x = random.random()*4-2
            y = k2(x)

        M = time.time()*1000
        for j in range(C):
            x = random.random()*4-2
            y = k3(x)

        N = time.time()*1000

        F.append(L-J)
        G.append(M-L)
        H.append(N-M)
        I.append(K)

    return [I, F, G, H, A, B]


def tprint(p):
    A = '\n'
    
    print(A+p[4])
    for a in p[1]:
        print(a)
        
    print(A+p[5])
    for a in p[2]:
        print(a)
        
    print('\ncontrol')
    for a in p[3]:
        print(a)


def plot(p):
    plt.plot(p[0], p[1], label=p[4])
    plt.plot(p[0], p[2], label=p[5])
    plt.plot(p[0], p[3], label='control')
    
    plt.xlabel('sample')
    plt.ylabel('time')
    
    plt.legend()
    plt.show()
