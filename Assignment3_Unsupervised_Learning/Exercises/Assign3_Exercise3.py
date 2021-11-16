import random
import time

import numpy as np
from matplotlib import pyplot as plt

import Assignment3_Unsupervised_Learning.Logic.Assign3_PointGenerator
from Assignment3_Unsupervised_Learning.Logic.Assign3_DistanceMatrix import DistanceMatrix
from Assignment3_Unsupervised_Learning.Logic.Assign3_Point import Point
from Assignment3_Unsupervised_Learning.Logic.Assign3_PointGenerator import generate_Points
#from Assignment3_Unsupervised_Learning.Logic.Assign3_TreeManager import TreeManager

lens_for_analysis = [4, 8, 10]


def average_point(point_a: Point, point_b: Point) -> Point:
    avg_x = (point_a.x + point_b.x) / 2
    avg_y = (point_a.y + point_b.y) / 2
    avg_point = Point(avg_x, avg_y)

    if avg_x > max(point_a.x, point_b.x) or avg_y > max(point_a.y, point_b.y) or \
            avg_x < min(point_a.x, point_b.x) or avg_y < min(point_a.y, point_b.y):
        print(point_a, point_b, avg_point)
    return avg_point


#def assign3_exercise3(treemanager:TreeManager):
def assign3_exercise3():

    a, b, c = generate_Points(plot=True, alpha=1, pointN=200)
    #points_lst: list = c.T.copy().tolist()
    points_lst: [Point] = Point.generate_Points(alpha=0.3, plot=True, pointN=1000)
    distance_matrix: DistanceMatrix = DistanceMatrix(size=len(points_lst), points_list=points_lst)

    # lens_for_analysis = [(initial_len / 4) * 1 - 1, (initial_len / 4) * 2 - 1, (initial_len / 4) * 3 - 1, ]
    point_for_analysis = [[[], []] for _ in range(len(lens_for_analysis))]
    points_lst_Length = distance_matrix.size
    while points_lst_Length > 2:

        point_a, point_b = distance_matrix.get_closest_pair()
        point_avg = average_point(point_a, point_b)
        #parent1:Node = treemanager.get(point_a)
        #parent2:Node = treemanager.get(point_b)
        #root:Node = Node(point_avg)
        #root.right = parent1
        #root.left =parent2

        #treemanager.add(parent1)
        #treemanager.add(parent2)
        #treemanager.add(root)

        distance_matrix.remove_point(point_a)
        distance_matrix.remove_point(point_b)

        distance_matrix.add_point(point_avg)

        print("points_lst_Length:", points_lst_Length, "point_a\t", point_a, "point_b\t", point_b, "point_avg\t",point_avg)

        points_lst_Length = distance_matrix.size
        if points_lst_Length in lens_for_analysis:
            for point in distance_matrix.points_list:
                # x
                point_for_analysis[lens_for_analysis.index(points_lst_Length)][0].append(point.x)
                # y
                point_for_analysis[lens_for_analysis.index(points_lst_Length)][1].append(point.y)

    for i in range(len(point_for_analysis)):
        curr_label: str = "len" + str(lens_for_analysis[i])
        alpha_value: float = -i / (len(lens_for_analysis)) + 1
        # print("alpha_value", alpha_value)
        plt.scatter(point_for_analysis[i][0], point_for_analysis[i][1], label=curr_label, alpha=alpha_value - 0.1,
                    c=Assignment3_Unsupervised_Learning.Logic.Assign3_PointGenerator.GREYSCALE[i])

    #plt.scatter(points_lst[0][0], points_lst[0][1], label="lastPointA",
    #            c=Assignment3_Unsupervised_Learning.Logic.Assign3_PointGenerator.COLORS[0])
    #plt.scatter(points_lst[1][0], points_lst[1][1], label="lastPointB",
    #            c=Assignment3_Unsupervised_Learning.Logic.Assign3_PointGenerator.COLORS[1])
    print("end-points_lst", points_lst)



if __name__ == '__main__':
    seed: int = random.randint(0, 10000)
    seed = 4670
    # good seed 4756
    # good seed 4670
    np.random.seed(seed)
    random.seed(seed)

    #treemanager:TreeManager = TreeManager()

    plt.figure(figsize=(10, 10))
    start = time.perf_counter()
    #assign3_exercise3(treemanager)
    assign3_exercise3()
    print("seed", seed)
    stop = time.perf_counter()
    print("time=",stop-start)
    plt.legend()
    plt.show()
    #treemanager.build()
