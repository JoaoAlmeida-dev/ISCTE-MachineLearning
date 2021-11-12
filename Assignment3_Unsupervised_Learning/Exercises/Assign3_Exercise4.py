import random

import matplotlib.pyplot as plt
import numpy as np

from Assignment3_Unsupervised_Learning.Logic.Assign3_PointGenerator import generate_Points
from Assignment3_Unsupervised_Learning.Logic.Assign3_ex4_Cluster import Cluster
from Assignment3_Unsupervised_Learning.Logic.Point import Point
from Assignment3_Unsupervised_Learning.Logic.Helpers import distance_between


def point_get_Epsylon_points(point: Point, point_list: [Point], epsilon: float) -> [np.ndarray]:
    _epsilon_points_list: [np.ndarray] = []
    for point_from_list in point_list:
        if distance_between(point_a=point_from_list, point_b=point) < epsilon:
            _epsilon_points_list.append(point_from_list)
    return _epsilon_points_list


def assign3_exercise4(epsilon: float):
    cluster_list: [Cluster] = []
    points_lst: [Point] = Point.generate_Points(alpha=1, plot=False, pointN=1000)

    while len(points_lst) > 0:
        cluster = Cluster.create_cluster(points_lst)
        cluster_list.append(cluster)
        cluster_points = cluster.getPoints()

        points_lst.remove(cluster_points)

    plt.legend()
    plt.show()


if __name__ == '__main__':
    seed: int = random.randint(0, 10000)
    # seed = 4670
    # good seed 4756
    # good seed 4670
    np.random.seed(seed)
    random.seed(seed)
    epsilon = random.random()
    # assign3_exercise4(epsilon)
