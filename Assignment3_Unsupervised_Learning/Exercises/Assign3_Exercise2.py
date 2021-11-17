import math
import time

import matplotlib.pyplot as plt
import numpy as np
import random

from matplotlib import patches
from matplotlib.lines import Line2D

import Assignment3_Unsupervised_Learning.Logic.Assign3_PointGenerator
from Assignment3_Unsupervised_Learning.Logic.Assign3_PointGenerator import generate_Points

r_plot_symbol = 'o'

alpha = 10E-2
r_color_list = ['orange', 'green', 'brown', 'black']
r_label = ["r1first", "r1last", "r2first", "r2last"]


def assign3_exercise2_advanceR(a: np.ndarray, b: np.ndarray, c: np.ndarray, plot: bool):
    a = a.T
    b = b.T
    c = c.T
    points_closer_r1_label1: list = []
    points_closer_r1_label2: list = []
    points_closer_r2_label1: list = []
    points_closer_r2_label2: list = []

    r1List: list = []
    r2List: list = []

    r1 = random.choice(c)
    r2 = random.choice(c)
    while r1[0] == r2[0] and r1[1] == r2[1]:
        r1 = random.choice(c)
        r2 = random.choice(c)

    r1List.append(r1)
    r2List.append(r2)

    iterations = 10
    d1: np.ndarray = np.zeros(2)
    d2: np.ndarray = np.zeros(2)
    n_examples = len(c)
    for i in range(iterations):
        for point in c:
            r1Closeness: float = ((r1[0] - point[0]) ** 2 + (r1[1] - point[1]) ** 2) ** 0.5
            r2Closeness: float = ((r2[0] - point[0]) ** 2 + (r2[1] - point[1]) ** 2) ** 0.5
            if r1Closeness < r2Closeness:
                d1 = d1 + (point - r1)
            else:
                d2 = d2 + (point - r2)
            if i == (iterations - 1):
                if r1Closeness < r2Closeness:
                    # closer to r1 from a
                    if point in a:
                        points_closer_r1_label1.append(point)
                    # closer to r1 from b
                    elif point in b:
                        points_closer_r1_label2.append(point)
                else:
                    # closer to r2 from a
                    if point in a:
                        points_closer_r2_label1.append(point)
                    # closer to r2 from b
                    elif point in b:
                        points_closer_r2_label2.append(point)

        r1 = r1 + (alpha / n_examples) * d1
        r2 = r2 + (alpha / n_examples) * d2
        d1 = np.zeros(2)
        d2 = np.zeros(2)

        # print(i, "r1", r1, "d1", d1)
        # print(i, "r2", r2, "d2", d2)
        r1List.append(r1)
        r2List.append(r2)
    r1_List_NPArray = np.asarray(r1List).T
    r2_List_NPArray = np.asarray(r2List).T
    if plot:
        plt.plot(r1_List_NPArray[0], r1_List_NPArray[1], r_plot_symbol, label="r1", color="purple")
        plt.plot(r1_List_NPArray[0][-1], r1_List_NPArray[1][-1], r_plot_symbol, label="r1End", color="black")

        plt.plot(r2_List_NPArray[0], r2_List_NPArray[1], r_plot_symbol, label="r2", color="green")
        plt.plot(r2_List_NPArray[0][-1], r2_List_NPArray[1][-1], r_plot_symbol, label="r2End", color="grey")

    return [points_closer_r1_label1, points_closer_r1_label2, points_closer_r2_label2, points_closer_r2_label1]


def assign3_exercise2_line_a(exercise_seed, exercise_alpha, pointN=1000):
    a, b, c = generate_Points(plot=True, alpha=0.5, pointN=pointN)
    assign3_exercise2_advanceR(a, b, c, plot=True)

    plt.title("seed=" + str(exercise_seed) + " alpha=" + str(exercise_alpha))
    plt.legend()


def assign3_exercise2_line_b(labels:[str]):
    a, b, c = generate_Points(plot=False, alpha=0.5, pointN=1000)
    points: list = assign3_exercise2_advanceR(a, b, c, plot=True)

    alpha_value_plotting: float = 0.5
    points_closer_label_NParray = [np.asarray(i).T for i in points]
    for i in range(len(points_closer_label_NParray)):
        if points_closer_label_NParray[i].size != 0:
            plt.scatter(points_closer_label_NParray[i][0], points_closer_label_NParray[i][1], marker='+',
                        color=Assignment3_Unsupervised_Learning.Logic.Assign3_PointGenerator.COLORS[i],
                        label=labels[i],
                        alpha=alpha_value_plotting)

    #    plt.title("assign3_exercise2_line_b")



def run_exercise2_line_a():
    start = time.perf_counter()

    assign3_exercise2_line_a(exercise_seed=seed, exercise_alpha=alpha, pointN=1000)

    stop = time.perf_counter()
    print("time=", stop - start)
    plt.tight_layout()
    plt.legend()
    plt.show()


def run_exercise2_line_b():
    labels = ["closer_r1_label1", "closer_r1_label2", "closer_r2_label2", "closer_r2_label1"]

    assign3_exercise2_line_b(labels)

    patch_0 = patches.Patch(color=Assignment3_Unsupervised_Learning.Logic.Assign3_PointGenerator.COLORS[0],
                            label=labels[0])
    patch_1 = patches.Patch(color=Assignment3_Unsupervised_Learning.Logic.Assign3_PointGenerator.COLORS[1],
                            label=labels[1])
    patch_2 = patches.Patch(color=Assignment3_Unsupervised_Learning.Logic.Assign3_PointGenerator.COLORS[2],
                            label=labels[2])
    patch_3 = patches.Patch(color=Assignment3_Unsupervised_Learning.Logic.Assign3_PointGenerator.COLORS[3],
                            label=labels[3])

    plt.legend(handles=[patch_0, patch_1, patch_2, patch_3])
    plt.tight_layout()
    plt.show()


def run_exercise2_line_c():
    labels = ["closer_r1_label1", "closer_r1_label2", "closer_r2_label2", "closer_r2_label1"]

    patch_0 = patches.Patch(color=Assignment3_Unsupervised_Learning.Logic.Assign3_PointGenerator.COLORS[0],
                            label=labels[0])
    patch_1 = patches.Patch(color=Assignment3_Unsupervised_Learning.Logic.Assign3_PointGenerator.COLORS[1],
                            label=labels[1])
    patch_2 = patches.Patch(color=Assignment3_Unsupervised_Learning.Logic.Assign3_PointGenerator.COLORS[2],
                            label=labels[2])
    patch_3 = patches.Patch(color=Assignment3_Unsupervised_Learning.Logic.Assign3_PointGenerator.COLORS[3],
                            label=labels[3])
    EXPERIENTS = 9
    for i in range(EXPERIENTS):
        gridside: int = int(math.sqrt(EXPERIENTS))
        plt.subplot(gridside, gridside, i + 1)
        plt.legend(handles=[patch_0, patch_1, patch_2, patch_3])
        assign3_exercise2_line_b(labels)

    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    seed = random.randint(0, 1000)
    # seed = 356
    # seed = 456
    seed = 254
    np.random.seed(seed)
    random.seed(seed)

    #run_exercise2_line_a()
    run_exercise2_line_b()
    run_exercise2_line_c()
