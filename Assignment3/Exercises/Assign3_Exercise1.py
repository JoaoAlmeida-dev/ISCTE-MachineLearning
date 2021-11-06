import matplotlib.pyplot as plt
import numpy as np
import random

alpha = 10E-5


def generate_Points() -> (np.ndarray, np.ndarray, np.ndarray):
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
    # x = c[0]
    # y = c[1]
    # plt.plot(x, y, 'x')
    plt.scatter(a[0], a[1], marker='1', label="a")
    plt.scatter(b[0], b[1], marker='1', label="b")
    # plt.axis('equal')
    # plt.show()
    return a, b, c


def exercise1(a: np.ndarray, b: np.ndarray, c: np.ndarray):
    r1ListBeggining: list = []
    r2ListBeggining: list = []
    r1ListLast: list = []
    r2ListLast: list = []

    r1 = random.choice(a.T)
    r2 = random.choice(b.T)
    iterations = 100
    for i in range(iterations):
        for point in c.T:
            r1Closeness: float = np.sqrt((r1[0] - point[0]) ** 2 + (r1[0] - point[0]) ** 2)
            r2Closeness: float = np.sqrt((r2[0] - point[0]) ** 2 + (r2[0] - point[0]) ** 2)
            # print(point,r1Closeness,r2Closeness)
            if r1Closeness < r2Closeness:
                r1 = (1 - alpha) * r1 + alpha * point
            else:
                r2 = (1 - alpha) * r2 + alpha * point
            if i == 0:
                r1ListBeggining.append((r1[0], r1[1]))
                r2ListBeggining.append((r2[0], r2[1]))
            if i == iterations - 1:
                r1ListLast.append((r1[0], r1[1]))
                r2ListLast.append((r2[0], r2[1]))
    r1ListBegginingArray: np.ndarray = np.asarray(r1ListBeggining).T
    r2ListBegginingArray: np.ndarray = np.asarray(r2ListBeggining).T
    r1ListLastArray: np.ndarray = np.asarray(r1ListLast).T
    r2ListLastArray: np.ndarray = np.asarray(r2ListLast).T

    print(r1ListBegginingArray)
    print(r2ListBegginingArray)
    print(r1ListLastArray)
    print(r2ListLastArray)
    plt.scatter(r1ListBegginingArray[0], r1ListBegginingArray[1], label="beggining")
    plt.scatter(r2ListBegginingArray[0], r2ListBegginingArray[1], label="beggining")

    plt.scatter(r1ListLastArray[0], r1ListLastArray[1], label="end")
    plt.scatter(r2ListLastArray[0], r2ListLastArray[1], label="end")
    plt.legend()
    plt.show()


if __name__ == '__main__':
    random.seed(1)
    points1, points2 , pointsconcat = generate_Points()
    exercise1(points1, points2 , pointsconcat)
