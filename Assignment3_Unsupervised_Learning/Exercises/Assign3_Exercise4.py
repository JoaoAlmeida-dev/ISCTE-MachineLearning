import random
import time

import matplotlib.pyplot as plt
import numpy as np

from Assignment3_Unsupervised_Learning.Logic.Assign3_ex4_Cluster import Cluster
from Assignment3_Unsupervised_Learning.Logic.Assign3_Point import Point
from Assignment3_Unsupervised_Learning.Logic.Assign3_DistanceMatrix import DistanceMatrix


def assign3_exercise4(epsilon: float, pointN=1000):
    figure, axes = plt.subplots()

    cluster_list: [Cluster] = []
    points_lst: [Point] = Point.generate_Points(alpha=0.3, plot=True, pointN=pointN)
    distance_matrix: DistanceMatrix = DistanceMatrix(size=len(points_lst), points_list=points_lst)
    # print(distance_matrix)

    has_unvisited: bool = distance_matrix.hasPointsNotVisited()
    while has_unvisited:
        cluster = Cluster(epsilon=epsilon, distance_matrix=distance_matrix)
        cluster_list.append(cluster)
        has_unvisited = distance_matrix.hasPointsNotVisited()

    for cluster_index in range(len(cluster_list)):
        cluster_color = (random.random(), random.random(), random.random())
        _ofsset = 0.2
        cluster_color_center = (
            min(cluster_color[0] + _ofsset, cluster_color[0]),
            min(cluster_color[1] + _ofsset, cluster_color[1]),
            min(cluster_color[2] + _ofsset, cluster_color[2]),
        )

        for point in cluster_list[cluster_index].getPoints():
            plt.scatter(point.x, point.y, color=cluster_color, alpha=0.5)
            # circle = plt.Circle(xy=(point.x, point.y), radius=epsilon, alpha=0.01,
            #                    color=cluster_color_center)
            # axes.set_aspect(1)
            # axes.add_artist(circle)

        cluster_initial_point = cluster_list[cluster_index].getInitial_Point()
        circle = plt.Circle(xy=(cluster_initial_point.x, cluster_initial_point.y), radius=epsilon, alpha=0.2,
                            color=cluster_color_center)
        axes.set_aspect(1)
        axes.add_artist(circle)

        plt.scatter(cluster_initial_point.x, cluster_initial_point.y, color=cluster_color_center, alpha=1)
        plt.title("DBSCAN com seed="+str(seed)+",epsilon="+str(epsilon)+" e "+str(pointN)+" pontos")

if __name__ == '__main__':
    # https://www.youtube.com/watch?v=_A9Tq6mGtLI
    seed: int = random.randint(0, 10000)
    # seed = 4670
    # seed= 4756
    # seed= 4670
    seed = 9655
    np.random.seed(seed)
    random.seed(seed)

    start = time.perf_counter()
    epsilon: float = 0.2
    print("seed_109=", seed, "epsilon=", epsilon)
    assign3_exercise4(epsilon,pointN=1000)
    stop = time.perf_counter()
    print("time=", stop - start)

    plt.legend()
    plt.show()
