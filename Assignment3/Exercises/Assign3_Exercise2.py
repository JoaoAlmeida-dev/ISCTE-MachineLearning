import matplotlib.pyplot as plt
import numpy as np
import random

alpha = 10E-5
color1 = 'b'
color2 = 'r'
color3 = 'g'
color4 = 'c'


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
    # plt.scatter(a[0], a[1], marker='1', label="a")
    # plt.scatter(b[0], b[1], marker='1', label="b")
    # plt.axis('equal')
    # plt.show()
    return a, b, c


def exercise2(a: np.ndarray, b: np.ndarray, c: np.ndarray):
    points_closer_r1_label1: list = []
    points_closer_r1_label2: list = []
    points_closer_r2_label1: list = []
    points_closer_r2_label2: list = []

    r1List: list = []
    r2List: list = []

    r1 = random.choice(a.T)
    r2 = random.choice(b.T)
    r1List.append(r1)
    r2List.append(r2)

    iterations = 100
    d1: float = 0.0
    d2: float = 0.0
    n_examples = 1000
    for i in range(iterations):
        for point in c.T:
            r1Closeness: float = np.sqrt((r1[0] - point[0]) ** 2 + (r1[0] - point[0]) ** 2)
            r2Closeness: float = np.sqrt((r2[0] - point[0]) ** 2 + (r2[0] - point[0]) ** 2)
            d1 = d1 + (point - r1)
            d2 = d2 + (point - r2)
            if r1Closeness < r2Closeness:
                # closer to r1
                if point in a.T:
                    points_closer_r1_label1.append(point)
                else:
                    points_closer_r1_label2.append(point)
            else:
                # closer to r2
                if point in a.T:
                    points_closer_r2_label1.append(point)
                else:
                    points_closer_r2_label2.append(point)

        r1 = r1 + (alpha / n_examples) * d1
        r2 = r2 + (alpha / n_examples) * d2
        r1List.append(r1)
        r2List.append(r2)
    r1_List_NPArray = np.asarray(r1List).T
    r2_List_NPArray = np.asarray(r2List).T

    plt.plot(r1_List_NPArray[0][0], r1_List_NPArray[1][0],'*', label="r1first", color='orange')
    plt.plot(r2_List_NPArray[0][0], r2_List_NPArray[1][0],'*', label="r2first", color='grey')
    plt.plot(r1_List_NPArray[0][-1], r1_List_NPArray[1][-1],'*', label="r1last", color='red')
    plt.plot(r2_List_NPArray[0][-1], r2_List_NPArray[1][-1],'*', label="r2last", color='black')

    points_closer_r1_label1_NParray = np.asarray(points_closer_r1_label1).T
    points_closer_r1_label2_NParray = np.asarray(points_closer_r1_label2).T
    points_closer_r2_label2_NParray = np.asarray(points_closer_r2_label2).T
    points_closer_r2_label1_NParray = np.asarray(points_closer_r2_label1).T
    print("points_closer_r1_label1_NParray",points_closer_r1_label1_NParray)
    print("points_closer_r1_label2_NParray",points_closer_r1_label2_NParray)
    print("points_closer_r2_label2_NParray",points_closer_r2_label2_NParray)
    print("points_closer_r2_label1_NParray",points_closer_r2_label1_NParray)


    if points_closer_r1_label1_NParray.size != 0:
        plt.scatter(points_closer_r1_label1_NParray[0], points_closer_r1_label1_NParray[1],label="closer_r1_label1", color=color1)
    if points_closer_r1_label2_NParray.size != 0:
        plt.scatter(points_closer_r1_label2_NParray[0], points_closer_r1_label2_NParray[1],label="closer_r1_label2", color=color2)
    if points_closer_r2_label2_NParray.size != 0:
        plt.scatter(points_closer_r2_label2_NParray[0], points_closer_r2_label2_NParray[1],label="closer_r2_label2", color=color3)
    if points_closer_r2_label1_NParray.size != 0:
        plt.scatter(points_closer_r2_label1_NParray[0], points_closer_r2_label1_NParray[1],label="closer_r2_label1", color=color4)

    plt.legend()
    plt.show()


if __name__ == '__main__':
    random.seed(1)
    points1, points2, pointsconcat = generate_Points()
    exercise2(points1, points2, pointsconcat)
