import random
import numpy as np
from matplotlib import pyplot as plt

import Assignment3_Unsupervised_Learning.Logic.Assign3_PointGenerator
from Assignment3_Unsupervised_Learning.Logic.Assign3_PointGenerator import generate_Points
from binarytree import Node

from Assignment3_Unsupervised_Learning.Logic.TreeManager import TreeManager

lens_for_analysis = [3, 6, 8]


def average_point(point_a: [int, int], point_b: [int, int]) -> [int, int]:
    avg_x = (point_a[0] + point_b[0]) / 2
    avg_y = (point_a[1] + point_b[1]) / 2
    avg_point = [avg_x, avg_y]

    if avg_x > max(point_a[0], point_b[0]) or avg_y > max(point_a[1], point_b[1]) or \
            avg_x < min(point_a[0], point_b[0]) or avg_y < min(point_a[1], point_b[1]):
        print(point_a, point_b, avg_point)
    return avg_point


def distance_between(point_a: np.ndarray, point_b: np.ndarray) -> float:
    return np.sqrt((point_a[0] - point_b[0]) ** 2 + (point_a[1] - point_b[1]) ** 2)


def find_closest_two_points(points_lst: list) -> (np.ndarray, np.ndarray):
    point_a: np.ndarray = points_lst[0]
    point_b: np.ndarray = points_lst[1]
    shortest_distance: float = distance_between(point_a, point_b)

    for point1 in points_lst:
        for point2 in points_lst:
            if point1[0] != point2[0] and point1[1] != point2[1]:
                distance = distance_between(point1, point2)
                if distance < shortest_distance:
                    shortest_distance = distance
                    point_a = point1
                    point_b = point2
    return point_a, point_b


def assign3_exercise3(treemanager:TreeManager):

    a, b, c = generate_Points(plot=True, alpha=1, pointN=200)
    points_lst: list = c.T.copy().tolist()
    initial_len = len(points_lst)
    # lens_for_analysis = [(initial_len / 4) * 1 - 1, (initial_len / 4) * 2 - 1, (initial_len / 4) * 3 - 1, ]

    point_for_analysis = [[[], []] for _ in range(len(lens_for_analysis))]
    points_lst_Length = len(points_lst)
    while points_lst_Length > 2:

        point_a, point_b = find_closest_two_points(points_lst)
        point_avg = average_point(point_a, point_b)
        parent1:Node = treemanager.get(point_a)
        parent2:Node = treemanager.get(point_b)
        root:Node = Node(point_avg)
        root.right = parent1
        root.left =parent2

        treemanager.add(parent1)
        treemanager.add(parent2)
        treemanager.add(root)

        try:
            points_lst.remove(point_a)
            points_lst.remove(point_b)
        except:
            print("ERROR:points_lst", points_lst)
            print("ERROR:point_a", point_a[0], point_a[1])
            print("ERROR:point_b", point_b[0], point_b[1])
        points_lst.append(point_avg)
        print("points_lst_Length:", points_lst_Length, "point_a\t", point_a, "point_b\t", point_b, "point_avg\t",
              point_avg)

        points_lst_Length = len(points_lst)
        if points_lst_Length in lens_for_analysis:
            for point in points_lst:
                # x
                point_for_analysis[lens_for_analysis.index(points_lst_Length)][0].append(point[0])
                # y
                point_for_analysis[lens_for_analysis.index(points_lst_Length)][1].append(point[1])

    for i in range(len(point_for_analysis)):
        curr_label: str = "len" + str(lens_for_analysis[i])
        alpha_value: float = -i / (len(lens_for_analysis)) + 1
        # print("alpha_value", alpha_value)
        plt.scatter(point_for_analysis[i][0], point_for_analysis[i][1], label=curr_label, alpha=alpha_value - 0.1,
                    c=Assignment3_Unsupervised_Learning.Logic.Assign3_PointGenerator.GREYSCALE[i])

    plt.scatter(points_lst[0][0], points_lst[0][1], label="lastPointA",
                c=Assignment3_Unsupervised_Learning.Logic.Assign3_PointGenerator.COLORS[0])
    plt.scatter(points_lst[1][0], points_lst[1][1], label="lastPointB",
                c=Assignment3_Unsupervised_Learning.Logic.Assign3_PointGenerator.COLORS[1])
    print("end-points_lst", points_lst)
    plt.legend()
    plt.show()


if __name__ == '__main__':
    seed: int = random.randint(0, 10000)
    seed = 4670
    # good seed 4756
    # good seed 4670
    np.random.seed(seed)
    random.seed(seed)

    treemanager:TreeManager = TreeManager()

    plt.figure(figsize=(10, 10))
    assign3_exercise3(treemanager)
    print("seed", seed)
    treemanager.build()
