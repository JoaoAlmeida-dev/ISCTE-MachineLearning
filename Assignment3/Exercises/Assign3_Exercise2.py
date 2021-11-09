import matplotlib.pyplot as plt
import numpy as np
import random

import Assignment3.Logic.Assign3_PointGenerator
from Assignment3.Logic.Assign3_PointGenerator import generate_Points

alpha = 1


def assign3_exercise2_advanceR(a: np.ndarray, b: np.ndarray, c: np.ndarray):
    points_closer_r1_label1: list = []
    points_closer_r1_label2: list = []
    points_closer_r2_label1: list = []
    points_closer_r2_label2: list = []

    r1List: list = []
    r2List: list = []

    r1 = random.choice(c.T)
    r2 = random.choice(c.T)
    print("r1", r1)
    print("r2", r2)
    while r1[0] == r2[0] and r1[1] == r2[1]:
        r1 = random.choice(c.T)
        r2 = random.choice(c.T)
    print("r1", r1)
    print("r2", r2)
    r1List.append(r1)
    r2List.append(r2)

    iterations = 10
    d1: float = 0.0
    d2: float = 0.0
    n_examples = len(a[0]) + len(b[0])
    print("n_examples", n_examples)
    for i in range(iterations):
        for point in c.T:
            r1Closeness: float = np.sqrt((r1[0] - point[0]) ** 2 + (r1[0] - point[0]) ** 2)
            r2Closeness: float = np.sqrt((r2[0] - point[0]) ** 2 + (r2[0] - point[0]) ** 2)
            if r1Closeness < r2Closeness:
                d1 = d1 + (point - r1)
            else:
                d2 = d2 + (point - r2)

            # print("d1",d1)
            # print("d2",d2)
            if i == (iterations - 1):
                if r1Closeness < r2Closeness:
                    # closer to r1 from a
                    if point in a.T:
                        points_closer_r1_label1.append(point)
                    # closer to r1 from b
                    else:
                        points_closer_r1_label2.append(point)
                else:
                    # closer to r2 from a
                    if point in a.T:
                        points_closer_r2_label1.append(point)
                    # closer to r2 from b
                    else:
                        points_closer_r2_label2.append(point)

        r1 = r1 + (alpha / n_examples) * d1
        r2 = r2 + (alpha / n_examples) * d2
        print(i, "r1", r1, "d1", d1)
        print(i, "r2", r2, "d2", d2)
        r1List.append(r1)
        r2List.append(r2)
    r1_List_NPArray = np.asarray(r1List).T
    r2_List_NPArray = np.asarray(r2List).T

    plt.plot(r1_List_NPArray[0], r1_List_NPArray[1], 'o', label="r1first", color='orange', linewidth=100)
    plt.plot(r1_List_NPArray[0][-1], r1_List_NPArray[1][-1], 'o', label="r1last", color='red', linewidth=100)

    plt.plot(r2_List_NPArray[0], r2_List_NPArray[1], 'o', label="r2first", color='brown', linewidth=100)
    plt.plot(r2_List_NPArray[0][-1], r2_List_NPArray[1][-1], 'o', label="r2last", color='black', linewidth=100)

    return points_closer_r1_label1, points_closer_r1_label2, points_closer_r2_label2, points_closer_r2_label1


def assign3_exercise2_line_a():
    a, b, c = generate_Points(True, 1000)
    assign3_exercise2_advanceR(a, b, c)
    plt.title("assign3_exercise2_line_a")
    plt.legend()


def assign3_exercise2_line_b():
    a, b, c = generate_Points(False, 1000)
    points_closer_r1_label1, points_closer_r1_label2, points_closer_r2_label2, points_closer_r2_label1 = assign3_exercise2_advanceR(
        a, b, c)

    points_closer_r1_label1_NParray = np.asarray(points_closer_r1_label1).T
    points_closer_r1_label2_NParray = np.asarray(points_closer_r1_label2).T
    points_closer_r2_label2_NParray = np.asarray(points_closer_r2_label2).T
    points_closer_r2_label1_NParray = np.asarray(points_closer_r2_label1).T
    # print("points_closer_r1_label1_NParray",points_closer_r1_label1_NParray)
    # print("points_closer_r1_label2_NParray",points_closer_r1_label2_NParray)
    # print("points_closer_r2_label2_NParray",points_closer_r2_label2_NParray)
    # print("points_closer_r2_label1_NParray",points_closer_r2_label1_NParray)

    alpha_value_plotting: float = 0.5
    if points_closer_r1_label1_NParray.size != 0:
        plt.scatter(points_closer_r1_label1_NParray[0], points_closer_r1_label1_NParray[1], marker='+',
                    label="closer_r1_label1",
                    color=Assignment3.Logic.Assign3_PointGenerator.COLORS[0], alpha=alpha_value_plotting)
    if points_closer_r1_label2_NParray.size != 0:
        plt.scatter(points_closer_r1_label2_NParray[0], points_closer_r1_label2_NParray[1], marker='+',
                    label="closer_r1_label2",
                    color=Assignment3.Logic.Assign3_PointGenerator.COLORS[1], alpha=alpha_value_plotting)
    if points_closer_r2_label2_NParray.size != 0:
        plt.scatter(points_closer_r2_label2_NParray[0], points_closer_r2_label2_NParray[1], marker='+',
                    label="closer_r2_label2",
                    color=Assignment3.Logic.Assign3_PointGenerator.COLORS[2], alpha=alpha_value_plotting)
    if points_closer_r2_label1_NParray.size != 0:
        plt.scatter(points_closer_r2_label1_NParray[0], points_closer_r2_label1_NParray[1], marker='+',
                    label="closer_r2_label1",
                    color=Assignment3.Logic.Assign3_PointGenerator.COLORS[3], alpha=alpha_value_plotting)
    plt.title("assign3_exercise2_line_b")
    plt.legend()


if __name__ == '__main__':
    # np.random.seed(1)
    # random.seed(1)
    plt.figure(figsize=(10, 10))
    plt.subplot(121)
    assign3_exercise2_line_a()
    plt.subplot(122)
    assign3_exercise2_line_b()
    plt.show()
