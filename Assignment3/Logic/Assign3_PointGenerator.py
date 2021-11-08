import numpy as np
from matplotlib import pyplot as plt


def generate_Points(plot: bool) -> (np.ndarray, np.ndarray, np.ndarray):
    mean = [3, 3]
    cov = [[1, 0], [0, 1]]
    a = np.random.multivariate_normal(mean, cov, 500).T
    mean = [-3, -3]
    cov = [[2, 0], [0, 5]]
    b = np.random.multivariate_normal(mean, cov, 500).T
    c = np.concatenate((a, b), axis=1)
    c = c.T
    np.random.shuffle(c)
    c = c.T
    if plot:
        # x = c[0]
        # y = c[1]
        # plt.plot(x, y, 'x')
        plt.scatter(a[0], a[1], marker='1', label="a", alpha=0.5)
        plt.scatter(b[0], b[1], marker='1', label="b", alpha=0.5)
        # plt.axis('equal')
        # plt.show()
    return a, b, c
