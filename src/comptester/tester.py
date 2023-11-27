from time import time
import random

from tqdm import tqdm
import matplotlib.pyplot as plt


def test(expr1: str, expr2: str, iters: int, D: int) -> list:
    """Run a test to compare the performance of two expressions.

    Args:
        expr1 (str): The first expression to test.
        expr2 (str): The second expression to test.
        iters (int): The number of times each expression is tested in a sample.
        D (int): The number of samples to collect.

    Returns:
        list: A list containing the test results.
    """

    E = "lambda x: "
    R = range(iters)

    F = []
    G = []
    H = []
    I = []

    k1 = eval(E + expr1)
    k2 = eval(E + expr2)
    k3 = eval(f"{E}x")

    for K in tqdm(range(D)):
        J = time() * 1000
        for _ in R:
            x = random.random() * 4 - 2
            y = k1(x)

        L = time() * 1000
        for _ in R:
            x = random.random() * 4 - 2
            y = k2(x)

        M = time() * 1000
        for _ in R:
            x = random.random() * 4 - 2
            y = k3(x)

        N = time() * 1000

        F.append(L - J)
        G.append(M - L)
        H.append(N - M)
        I.append(K)

    return [I, F, G, H, expr1, expr2]


def tprint(test: list) -> None:
    """Print the test results to the console.

    Args:
        test (list): The test results to print.
    """

    p = test
    A = "\n"

    print(A + p[4])
    for a in p[1]:
        print(a)

    print(A + p[5])
    for a in p[2]:
        print(a)

    print("\ncontrol")
    for a in p[3]:
        print(a)


def plot(test: list) -> None:
    """Plot the test results.

    Args:
        test (list): The test results to plot.
    """

    p = test

    plt.plot(p[0], p[1], label=p[4])
    plt.plot(p[0], p[2], label=p[5])
    plt.plot(p[0], p[3], label="control")

    plt.xlabel("sample")
    plt.ylabel("time")

    plt.legend()
    plt.show()
