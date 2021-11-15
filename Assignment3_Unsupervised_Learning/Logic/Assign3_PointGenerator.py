import numpy as np
from matplotlib import pyplot as plt

COLORS = ["red", "green", "blue", "yellow", "purple", "cyan"]
GREYSCALE = [
    "#000000",
    "#999999",
    "#cccccc",
]


def generate_Points(plot: bool, alpha: float, pointN: int) -> (np.ndarray, np.ndarray, np.ndarray):
    mean = [3, 3]
    cov = [[1, 0], [0, 1]]
    a = np.random.multivariate_normal(mean, cov, int(pointN / 2)).T
    mean = [-3, -3]
    cov = [[2, 0], [0, 5]]
    b = np.random.multivariate_normal(mean, cov, int(pointN / 2)).T
    mean = [5,-5]
    cov = [[1, 0], [0, 1]]
    b1 = np.random.multivariate_normal(mean, cov, int(pointN / 2)).T
    c = np.concatenate((a, b, b1), axis=1)
    c = c.T
    np.random.shuffle(c)
    c = c.T
    if plot:
        # x = c[0]
        # y = c[1]
        # plt.plot(x, y, 'x')
        plt.scatter(a[0], a[1], marker='+', label="a", alpha=alpha, color=COLORS[0])
        plt.scatter(b[0], b[1], marker='+', label="b", alpha=alpha, color=COLORS[2])
        plt.scatter(b1[0], b1[1], marker='+', label="b1", alpha=alpha, color=COLORS[4])
        # plt.axis('equal')
        # plt.show()
    return a, b, c
