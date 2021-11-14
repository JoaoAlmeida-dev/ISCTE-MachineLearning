import random

import matplotlib.pyplot as plt
import numpy as np

from Assignment3_Unsupervised_Learning.Logic.Assign3_ex4_Cluster import Cluster
from Assignment3_Unsupervised_Learning.Logic.Assign3_Point import Point
from Assignment3_Unsupervised_Learning.Logic.Assign3_ex4_DistanceMatrix import DistanceMatrix
from Assignment3_Unsupervised_Learning.Logic.Helpers import distance_between, create_empty_matrix


# def point_get_Epsylon_points(point_index: Point, point_list: [Point], epsilon: float) -> [np.ndarray]:
#    _epsilon_points_list: [np.ndarray] = []
#    for point_from_list in point_list:
#        if distance_between(point_a=point_from_list, point_b=point_index) < epsilon:
#            _epsilon_points_list.append(point_from_list)
#    return _epsilon_points_list


def assign3_exercise4(epsilon: float):
    figure, axes = plt.subplots()

    cluster_list: [Cluster] = []
    points_lst: [Point] = Point.generate_Points(alpha=0.3, plot=True, pointN=20)
    distance_matrix: DistanceMatrix = DistanceMatrix(size=len(points_lst), points_list=points_lst)
    print(distance_matrix)
    # while len(points_lst) > 0:
    has_unvisited: bool = distance_matrix.hasPointsNotVisited()
    counter = 0
    while has_unvisited and counter < 2:
        cluster = Cluster(epsilon=epsilon, distance_matrix=distance_matrix)
        cluster_list.append(cluster)
        has_unvisited = distance_matrix.hasPointsNotVisited()
        counter += 1

    for cluster_index in range(len(cluster_list)):
        cluster_color = (random.random(), random.random(), random.random())

        for point in cluster_list[cluster_index].getPoints():
            plt.scatter(point.x, point.y, c=cluster_color, alpha=0.5)

        cluster_initial_point = cluster_list[cluster_index].getInitial_Point()
        circle = plt.Circle(xy=(cluster_initial_point.x, cluster_initial_point.y), radius=epsilon, alpha=0.2,
                            color="orange")
        axes.set_aspect(1)
        axes.add_artist(circle)

        plt.scatter(cluster_initial_point.x, cluster_initial_point.y, c="green", alpha=1)
    plt.legend()
    plt.show()


if __name__ == '__main__':
    seed: int = random.randint(0, 10000)
    # seed = 4670
    # good seed 4756
    #seed= 4670
    np.random.seed(seed)
    random.seed(seed)
    epsilon: float = random.random()
    epsilon = 2
    assign3_exercise4(epsilon)
