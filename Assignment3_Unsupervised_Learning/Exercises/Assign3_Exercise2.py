import math
import time

import matplotlib.pyplot as plt
import numpy as np
import random

from matplotlib import patches
from matplotlib.lines import Line2D

import Assignment3_Unsupervised_Learning.Logic.Assign3_PointGenerator
from Assignment3_Unsupervised_Learning.Logic.Assign3_PointGenerator import generate_Points_as_arrays

r_plot_symbol = 'o'

r_color_list = ['orange', 'green', 'brown', 'black']
r_label = ["r1first", "r1last", "r2first", "r2last"]

line_b_c_labels = ["closer_r1_label1", "closer_r1_label2", "closer_r2_label2", "closer_r2_label1"]
r1_color = "purple"
r1_end_color = "black"
r2_color = "green"
r2_end_color = "grey"
exercise2_legendPatches = [
    Line2D([0], [0], color='w', marker='o', markerfacecolor=r1_color, markersize=10, label="r1"),
    Line2D([0], [0], color='w', marker='o', markerfacecolor=r1_end_color, markersize=10, label="r1_end"),
    Line2D([0], [0], color='w', marker='o', markerfacecolor=r2_color, markersize=10, label="r2"),
    Line2D([0], [0], color='w', marker='o', markerfacecolor=r2_end_color, markersize=10, label="r2_end"),
    patches.Patch(color=Assignment3_Unsupervised_Learning.Logic.Assign3_PointGenerator.COLORS[0],
                  label=line_b_c_labels[0]),
    patches.Patch(color=Assignment3_Unsupervised_Learning.Logic.Assign3_PointGenerator.COLORS[1],
                  label=line_b_c_labels[1]),
    patches.Patch(color=Assignment3_Unsupervised_Learning.Logic.Assign3_PointGenerator.COLORS[2],
                  label=line_b_c_labels[2]),
    patches.Patch(color=Assignment3_Unsupervised_Learning.Logic.Assign3_PointGenerator.COLORS[3],
                  label=line_b_c_labels[3]),
]


def decode_positives_matrix(a, b, point, points_closer_r1_label1, points_closer_r1_label2, points_closer_r2_label1,
                            points_closer_r2_label2, r1Closeness, r2Closeness):
    if r1Closeness < r2Closeness:
        # point from a, closer to r1
        if point in a:
            points_closer_r1_label1.append(point)
        # point from b, closer to r1
        elif point in b:
            points_closer_r1_label2.append(point)
    else:
        # point from a, closer to r2
        if point in a:
            points_closer_r2_label1.append(point)
        # point from b, closer to r2
        elif point in b:
            points_closer_r2_label2.append(point)


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
                decode_positives_matrix(a, b, point, points_closer_r1_label1, points_closer_r1_label2,
                                        points_closer_r2_label1, points_closer_r2_label2, r1Closeness, r2Closeness)

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
        plt.plot(r1_List_NPArray[0], r1_List_NPArray[1], r_plot_symbol, label="r1", color=r1_color)
        plt.plot(r1_List_NPArray[0][-1], r1_List_NPArray[1][-1], r_plot_symbol, label="r1End", color=r1_end_color)

        plt.plot(r2_List_NPArray[0], r2_List_NPArray[1], r_plot_symbol, label="r2", color=r2_color)
        plt.plot(r2_List_NPArray[0][-1], r2_List_NPArray[1][-1], r_plot_symbol, label="r2End", color=r2_end_color)

    return [points_closer_r1_label1, points_closer_r1_label2, points_closer_r2_label2, points_closer_r2_label1]


def assign3_exercise2_line_a(exercise_seed, exercise_alpha, pointN=1000):
    a, b, c = generate_Points_as_arrays(plot=True, alpha=0.5, pointN=pointN)
    assign3_exercise2_advanceR(a, b, c, plot=True)

    plt.title("seed=" + str(exercise_seed) + " alpha=" + str(exercise_alpha))
    plt.legend()


def assign3_exercise2_line_b(exercise_seed, exercise_alpha, labels: [str]):
    a, b, c = generate_Points_as_arrays(plot=False, alpha=0.5, pointN=1000)
    points: list = assign3_exercise2_advanceR(a, b, c, plot=True)

    alpha_value_plotting: float = 0.5
    points_closer_label_NParray = [np.asarray(i).T for i in points]
    for i in range(len(points_closer_label_NParray)):
        if points_closer_label_NParray[i].size != 0:
            plt.scatter(points_closer_label_NParray[i][0], points_closer_label_NParray[i][1], marker='+',
                        color=Assignment3_Unsupervised_Learning.Logic.Assign3_PointGenerator.COLORS[i],
                        label=labels[i],
                        alpha=alpha_value_plotting)


def run_exercise2_line_a(exercise_seed, exercise_alpha, ):
    start = time.perf_counter()

    assign3_exercise2_line_a(exercise_seed=exercise_seed, exercise_alpha=exercise_alpha, pointN=1000)

    stop = time.perf_counter()
    print("time=", stop - start)
    plt.tight_layout()
    plt.legend()
    plt.show()


def run_exercise2_line_b(exercise_seed, exercise_alpha, ):
    assign3_exercise2_line_b(exercise_seed=exercise_seed, exercise_alpha=exercise_alpha, labels=line_b_c_labels)
    plt.title("seed=" + str(exercise_seed) + " alpha=" + str(exercise_alpha))
    plt.legend(handles=exercise2_legendPatches)
    plt.tight_layout()
    plt.show()


def run_exercise2_line_c(exercise_seed, exercise_alpha):
    EXPERIENTS = 9
    gridside: int = int(math.sqrt(EXPERIENTS))
    fig = plt.figure()
    for i in range(EXPERIENTS):
        plt.subplot(gridside, gridside, i + 1)
        assign3_exercise2_line_b(exercise_seed=exercise_seed, exercise_alpha=exercise_alpha, labels=line_b_c_labels)
    fig.legend(handles=exercise2_legendPatches, loc="lower center", ncol=4, )
    fig.suptitle("seed=" + str(exercise_seed) + " alpha=" + str(exercise_alpha))

    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    alpha = 10E-3

    seed = random.randint(0, 1000)
    # seed_109 = 356
    # seed_109 = 456
    seed = 771
    np.random.seed(seed)
    random.seed(seed)

    run_exercise2_line_a(exercise_seed=seed, exercise_alpha=alpha)
    run_exercise2_line_b(exercise_seed=seed, exercise_alpha=alpha)
    run_exercise2_line_c(exercise_seed=seed, exercise_alpha=alpha)
