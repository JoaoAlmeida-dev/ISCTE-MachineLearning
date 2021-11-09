import matplotlib.pyplot as plt
import numpy as np
import random

from Assignment3.Logic.Assign3_PointGenerator import generate_Points

alpha = 10E-5


def assign3_exercise1():
    a, b, c = generate_Points(True, 1000)
    r1ListBeggining: list = []
    r2ListBeggining: list = []
    r1ListEndOfPassage: list = []
    r2ListEndOfPassage: list = []

    r1 = random.choice(a.T)
    r2 = random.choice(b.T)
    iterations = 10
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
        r1ListEndOfPassage.append((r1[0], r1[1]))
        r2ListEndOfPassage.append((r2[0], r2[1]))

    plt.scatter(r1ListBeggining[0], r1ListBeggining[1], label="r1ListBeggining")
    plt.scatter(r2ListBeggining[0], r2ListBeggining[1], label="r2ListBeggining")

    plt.scatter(r1ListEndOfPassage[0], r1ListEndOfPassage[1], label="r1ListEndOfPassage")
    plt.scatter(r2ListEndOfPassage[0], r2ListEndOfPassage[1], label="r2ListEndOfPassage")
    plt.legend()
    plt.show()


if __name__ == '__main__':
    np.random.seed(1)
    random.seed(1)
    plt.figure(figsize=(10, 10))
    assign3_exercise1()
