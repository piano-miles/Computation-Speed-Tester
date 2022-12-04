import random
from tqdm import tqdm
import time
import matplotlib.pyplot as plt

t1 = []
t2 = []
t3 = []
t0 = []

test1 = 'x*x*x' # Multiplication
test2 = 'x**3' # Power
test3 = 'x' # Control

for K in tqdm(range(100)):
    s1 = time.time()*1000

    for j in range(100000):
        x = random.random()*4-2
        y = eval(test1)

    s2 = time.time()*1000

    for j in range(100000):
        x = random.random()*4-2
        y = eval(test2)

    s3 = time.time()*1000

    for j in range(100000):
        x = random.random()*4-2
        y = eval(test3)

    s4 = time.time()*1000

    t1.append(s2-s1)
    t2.append(s3-s2)
    t3.append(s4-s3)
    t0.append(K)

print('\n'+test1)
for a in t1:
    print(a)

print('\n'+test2)
for a in t2:
    print(a)

print('\ncontrol')
for a in t3:
    print(a)

plt.plot(t0, t1, label=test1)
plt.plot(t0, t2, label=test2)
plt.plot(t0, t3, label='control')
plt.xlabel("sample")
plt.ylabel("time")
plt.legend()
plt.show()
