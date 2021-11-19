import random
import time

import numpy as np
from matplotlib import pyplot as plt

import Assignment3_Unsupervised_Learning.Logic.Assign3_PointGenerator
from Assignment3_Unsupervised_Learning.Logic.Assign3_DistanceMatrix import DistanceMatrix
from Assignment3_Unsupervised_Learning.Logic.Assign3_Point import Point
from Assignment3_Unsupervised_Learning.Logic.Assign3_PointGenerator import generate_Points
# from Assignment3_Unsupervised_Learning.Logic.Assign3_TreeManager import TreeManager
from Assignment3_Unsupervised_Learning.Logic.Assign3_TreeManager import Node, TreeManager

lens_for_analysis = [4, 25, 100]


def average_point(point_a: Point, point_b: Point) -> Point:
    avg_x = (point_a.x + point_b.x) / 2
    avg_y = (point_a.y + point_b.y) / 2
    avg_point = Point(avg_x, avg_y, label="avg")

    #    if avg_x > max(point_a.x, point_b.x) or avg_y > max(point_a.y, point_b.y) or \
    #            avg_x < min(point_a.x, point_b.x) or avg_y < min(point_a.y, point_b.y):
    #        print(point_a, point_b, avg_point)
    return avg_point


def assign3_exercise3(treemanager: TreeManager, pointN):
    # def assign3_exercise3():

    points_lst: [Point] = Point.generate_Points(alpha=0.3, plot=True, pointN=pointN)
    distance_matrix: DistanceMatrix = DistanceMatrix(size=len(points_lst), points_list=points_lst)

    # lens_for_analysis = [(initial_len / 4) * 1 - 1, (initial_len / 4) * 2 - 1, (initial_len / 4) * 3 - 1, ]
    point_for_analysis = [[[], []] for _ in range(len(lens_for_analysis))]
    points_lst_Length = distance_matrix.size
    while points_lst_Length > 2:

        point_a, point_b = distance_matrix.get_closest_pair()
        point_avg = average_point(point_a, point_b)
        parent1: Node = treemanager.get(point_a)
        parent2: Node = treemanager.get(point_b)
        root: Node = Node(point_avg)
        root.right = parent1
        root.left = parent2

        # treemanager.add(parent1)
        # treemanager.add(parent2)
        treemanager.add(root)

        distance_matrix.remove_point(point_a)
        distance_matrix.remove_point(point_b)
        distance_matrix.add_point(point_avg)

        print("points_lst_Length:", points_lst_Length, "point_a\t", point_a, "point_b\t", point_b, "point_avg\t",
              point_avg)

        points_lst_Length = distance_matrix.size
        if points_lst_Length in lens_for_analysis:
            for point in distance_matrix.points_list:
                # x
                len_index = lens_for_analysis.index(points_lst_Length)
                point_for_analysis[len_index][0].append(point.x)
                # y
                point_for_analysis[len_index][1].append(point.y)

    for i in range(len(point_for_analysis)):
        curr_label: str = "len" + str(lens_for_analysis[i])
        alpha_value: float = -i / (len(lens_for_analysis)) + 1
        # print("alpha_value", alpha_value)
        plt.scatter(point_for_analysis[i][0], point_for_analysis[i][1], label=curr_label, alpha=alpha_value - 0.01,
                    c=Assignment3_Unsupervised_Learning.Logic.Assign3_PointGenerator.GREYSCALE[i])

    plt.scatter(points_lst[0].x, points_lst[0].y, label="lastPointA", c="green")
    plt.scatter(points_lst[1].x, points_lst[1].y, label="lastPointB", c="purple")
    return points_lst[0] , points_lst[1]


def plot_children(root_b, root_a):
    pointA_children: [Node] = TreeManager.get_all_children(root_node=root_a)
    pointB_children: [Node] = TreeManager.get_all_children(root_node=root_b)

    pointA_children_list_plot: [[float],[float]] = [[],[]]
    pointB_children_list_plot: [[float],[float]] = [[],[]]
    for node in pointA_children:
        pointA_children_list_plot[0].append(node.data.x)
        pointA_children_list_plot[1].append(node.data.y)
    for node in pointB_children:
        pointB_children_list_plot[0].append(node.data.x)
        pointB_children_list_plot[1].append(node.data.y)

    plt.scatter(x=pointA_children_list_plot[0], y=pointA_children_list_plot[1], label="pointA_Children",alpha=0.7)
    plt.scatter(x=pointB_children_list_plot[0], y=pointB_children_list_plot[1], label="pointb_Children",alpha=0.7)
    plt.scatter(root_a.data.x, root_a.data.y, label="pointA")
    plt.scatter(root_b.data.x, root_b.data.y, label="pointB")

    plt.title("Final points and their children")
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    seed: int = random.randint(0, 10000)
    seed = 4670
    # good seed_109 4756
    # good seed_109 4670
    np.random.seed(seed)
    random.seed(seed)

    treemanager: TreeManager = TreeManager()

    plt.figure(figsize=(10, 10))
    start = time.perf_counter()
    lastPointA,lastPointB = assign3_exercise3(treemanager=treemanager, pointN=500)

    print("seed", seed)
    stop = time.perf_counter()
    print("time=", stop - start)

    plt.legend()
    plt.show()

    root_lastPointA= treemanager.get(lastPointA)
    root_lastPointB= treemanager.get(lastPointB)
    plot_children(root_lastPointA,root_lastPointB,)




    treemanager.build()
