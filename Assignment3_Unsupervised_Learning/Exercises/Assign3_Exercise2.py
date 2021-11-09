import math

import matplotlib.pyplot as plt
import numpy as np
import random

from matplotlib import patches
from matplotlib.lines import Line2D

import Assignment3_Unsupervised_Learning.Logic.Assign3_PointGenerator
from Assignment3_Unsupervised_Learning.Logic.Assign3_PointGenerator import generate_Points

r_plot_symbol = 'o'

alpha = 10E-2
r_color_list=['orange','red','brown','black']
r_label=["r1first" ,"r1last" , "r2first","r2last"]

def assign3_exercise2_advanceR(a: np.ndarray, b: np.ndarray, c: np.ndarray):
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
    print("r1", r1)
    print("r2", r2)
    while r1[0] == r2[0] and r1[1] == r2[1]:
        r1 = random.choice(c)
        r2 = random.choice(c)
    print("r1", r1)
    print("r2", r2)
    r1List.append(r1)
    r2List.append(r2)

    iterations = 100
    d1: np.ndarray = np.zeros(2)
    d2: np.ndarray = np.zeros(2)
    n_examples = len(c)
    print("n_examples", n_examples)
    for i in range(iterations):
        for point in c:
            r1Closeness: float = np.sqrt((r1[0] - point[0]) ** 2 + (r1[1] - point[1]) ** 2)
            r2Closeness: float = np.sqrt((r2[0] - point[0]) ** 2 + (r2[1] - point[1]) ** 2)
            if r1Closeness < r2Closeness:
                d1 = d1 + (point - r1)
            else:
                d2 = d2 + (point - r2)

            # print("d1",d1)
            # print("d2",d2)
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

        print(i, "r1", r1, "d1", d1)
        print(i, "r2", r2, "d2", d2)
        r1List.append(r1)
        r2List.append(r2)
    r1_List_NPArray = np.asarray(r1List).T
    r2_List_NPArray = np.asarray(r2List).T

    plt.plot(r1_List_NPArray[0], r1_List_NPArray[1], r_plot_symbol, label=r_label, color=r_color_list[0], linewidth=100)
    plt.plot(r1_List_NPArray[0][-1], r1_List_NPArray[1][-1], r_plot_symbol, label=r_label, color=r_color_list[1], linewidth=100)

    plt.plot(r2_List_NPArray[0], r2_List_NPArray[1], r_plot_symbol, label=r_label, color=r_color_list[1], linewidth=100)
    plt.plot(r2_List_NPArray[0][-1], r2_List_NPArray[1][-1], r_plot_symbol, label=r_label, color=r_color_list[1], linewidth=100)

    return [points_closer_r1_label1, points_closer_r1_label2, points_closer_r2_label2, points_closer_r2_label1]


def assign3_exercise2_line_a():
    a, b, c = generate_Points(plot=True,alpha=1,pointN= 1000)
    assign3_exercise2_advanceR(a, b, c)
    plt.title("assign3_exercise2_line_a")
    plt.legend()


def assign3_exercise2_line_b():
    a, b, c = generate_Points(plot=False,alpha=1,pointN= 1000)
    points: list = assign3_exercise2_advanceR(a, b, c)

    alpha_value_plotting: float = 0.5
    labels = ["closer_r1_label1", "closer_r1_label2", "closer_r2_label2", "closer_r2_label1"]
    points_closer_label_NParray = [np.asarray(i).T for i in points]
    for i in range(len(points_closer_label_NParray)):
        if points_closer_label_NParray[i].size != 0:
            plt.scatter(points_closer_label_NParray[i][0], points_closer_label_NParray[i][1], marker='+',
                        color=Assignment3_Unsupervised_Learning.Logic.Assign3_PointGenerator.COLORS[i],
                        label=labels[i],
                        alpha=alpha_value_plotting)

#    plt.title("assign3_exercise2_line_b")
    patch_0 = patches.Patch(color=Assignment3_Unsupervised_Learning.Logic.Assign3_PointGenerator.COLORS[0], label=labels[0])
    patch_1 = patches.Patch(color=Assignment3_Unsupervised_Learning.Logic.Assign3_PointGenerator.COLORS[1], label=labels[1])
    patch_2 = patches.Patch(color=Assignment3_Unsupervised_Learning.Logic.Assign3_PointGenerator.COLORS[2], label=labels[2])
    patch_3 = patches.Patch(color=Assignment3_Unsupervised_Learning.Logic.Assign3_PointGenerator.COLORS[3], label=labels[3])

    plt.legend(handles=[patch_0, patch_1,patch_2,patch_3])
    #plt.legend(prop={'size': 6})


if __name__ == '__main__':
    # np.random.seed(1)
    # random.seed(1)
    plt.figure(figsize=(10, 10))
    plt.subplot(121)
    assign3_exercise2_line_a()
    plt.subplot(122)
    EXPERIENTS = 9
    for i in range(EXPERIENTS):
        gridside:int = int(math.sqrt(EXPERIENTS))
        plt.subplot(gridside,gridside,i+1)
        assign3_exercise2_line_b()

    plt.show()
